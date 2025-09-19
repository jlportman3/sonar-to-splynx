#!/usr/bin/env python3
"""CLI tool to back up Sonar GraphQL data into PostgreSQL."""

import argparse
import os
import sys
from typing import Optional, Set

# Ensure project modules are on path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(CURRENT_DIR, "src"))

from src.apis.sonar_client import SonarGraphQLClient
from src.backup.sonar_graphql_backup import SonarGraphQLBackup
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger


def _validate_sonar_config() -> None:
    if not config.sonar_url:
        raise ValueError("SONAR_URL is required in the environment")
    has_token = bool(config.sonar_token or config.sonar_api_key)
    has_user_pass = bool(config.sonar_username and config.sonar_password)
    if not (has_token or has_user_pass):
        raise ValueError("Sonar authentication is required (SONAR_API_KEY or SONAR_USERNAME/SONAR_PASSWORD)")


def _parse_set(value: Optional[str]) -> Optional[Set[str]]:
    if not value:
        return None
    items = [item.strip() for item in value.split(",") if item.strip()]
    return set(items) if items else None


def _resolve_database_url(explicit_url: Optional[str]) -> str:
    """Resolve the Postgres connection string from CLI args or environment variables."""
    if explicit_url:
        return explicit_url

    env_url = os.getenv("BACKUP_DATABASE_URL")
    if env_url:
        return env_url

    host = os.getenv("BACKUP_DB_HOST")
    port = os.getenv("BACKUP_DB_PORT")
    name = os.getenv("BACKUP_DB_NAME")
    user = os.getenv("BACKUP_DB_USER")
    password = os.getenv("BACKUP_DB_PASSWORD")

    if all([host, port, name, user, password]):
        return f"postgresql://{user}:{password}@{host}:{port}/{name}"

    raise ValueError(
        "PostgreSQL connection string is required. Provide --database-url, BACKUP_DATABASE_URL, "
        "or BACKUP_DB_* environment variables."
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Full backup of Sonar GraphQL entities into PostgreSQL",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--database-url",
        default=os.getenv("BACKUP_DATABASE_URL"),
        help="PostgreSQL connection URL (defaults to BACKUP_DATABASE_URL environment variable)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=1000,
        help="Number of records to request per GraphQL page",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=0,
        help="Maximum depth for nested object selection when building GraphQL queries",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        help="Limit the number of records fetched per collection (useful for smoke tests)",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=30.0,
        help="Timeout (in seconds) for each GraphQL HTTP request",
    )
    parser.add_argument(
        "--rate-limit-delay",
        type=float,
        default=5.0,
        help="Seconds to wait before retrying when the API signals rate limiting",
    )
    parser.add_argument(
        "--rate-limit-retries",
        type=int,
        default=5,
        help="Maximum consecutive rate-limit retries per collection",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=1,
        help="Number of collections to back up concurrently",
    )
    parser.add_argument(
        "--include",
        help="Comma-separated list of root query names to include (others skipped)",
    )
    parser.add_argument(
        "--exclude",
        help="Comma-separated list of root query names to skip",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging verbosity",
    )

    args = parser.parse_args()

    setup_logger(args.log_level)
    logger = get_logger("graphql_backup")

    _validate_sonar_config()

    include = _parse_set(args.include)
    exclude = _parse_set(args.exclude)

    database_url = _resolve_database_url(args.database_url)

    logger.info("Initializing Sonar GraphQL backup")
    logger.info(
        "Existing pagination progress will be reused; run make backup-clean to reset."
    )

    client = SonarGraphQLClient(config, request_timeout=args.request_timeout)
    backup = SonarGraphQLBackup(
        client=client,
        database_url=database_url,
        page_size=args.page_size,
        max_depth=args.max_depth,
        sample_size=args.sample_size,
        request_timeout=args.request_timeout,
        rate_limit_delay=args.rate_limit_delay,
        rate_limit_retries=args.rate_limit_retries,
        include=include,
        exclude=exclude,
        thread_pool_size=args.threads,
    )
    backup.run()


if __name__ == "__main__":
    main()
