#!/usr/bin/env python3
"""CLI tool to back up Sonar GraphQL data into SQLite."""

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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Full backup of Sonar GraphQL entities into SQLite",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--output",
        default="sonar_graphql_backup.sqlite",
        help="Path to the SQLite database that will store the backup",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=200,
        help="Number of records to request per GraphQL page",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=2,
        help="Maximum depth for nested object selection when building GraphQL queries",
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

    logger.info("Initializing Sonar GraphQL backup (output=%s)", args.output)

    client = SonarGraphQLClient(config)
    backup = SonarGraphQLBackup(
        client=client,
        output_path=args.output,
        page_size=args.page_size,
        max_depth=args.max_depth,
        include=include,
        exclude=exclude,
    )
    backup.run()


if __name__ == "__main__":
    main()
