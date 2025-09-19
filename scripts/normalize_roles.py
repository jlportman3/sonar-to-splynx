#!/usr/bin/env python3
"""Generate normalized Sonar roles/permissions ready for Splynx import."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime

from dotenv import load_dotenv

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.extractors.sonar_security_extractor import SonarSecurityExtractor
from src.transformers.role_transformer import RoleTransformer
from src.utils.logger import setup_logger, get_logger

load_dotenv()

logger = get_logger("normalize_roles")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize Sonar roles and permissions",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--database-url",
        default=os.getenv("BACKUP_DATABASE_URL"),
        help="Postgres connection string holding the GraphQL backup",
    )
    parser.add_argument(
        "--output",
        help="Output file for normalized JSON (defaults to stdout)",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    setup_logger(args.log_level)

    if not args.database_url:
        raise ValueError("Database URL not provided. Use --database-url or BACKUP_DATABASE_URL")

    extractor = SonarSecurityExtractor(args.database_url)
    transformer = RoleTransformer()

    try:
        roles = extractor.fetch_roles()
        permissions = extractor.fetch_permissions()
        categories = extractor.fetch_permission_categories()
        mappings = extractor.fetch_role_permissions()
        logger.info(
            "Fetched %s roles, %s permissions, %s categories, %s assignments",
            len(roles),
            len(permissions),
            len(categories),
            len(mappings),
        )

        normalized_roles, normalized_permissions, normalized_role_permissions = transformer.transform(
            roles=roles,
            permissions=permissions,
            permission_categories=categories,
            role_permissions=mappings,
        )

        payload = {
            'generated_at': datetime.utcnow().isoformat(),
            'roles': [entity.to_dict() for entity in normalized_roles],
            'permissions': [entity.to_dict() for entity in normalized_permissions],
            'role_permissions': [entity.to_dict() for entity in normalized_role_permissions],
        }

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as handle:
                json.dump(payload, handle, indent=2)
            logger.info("Wrote normalized roles to %s", args.output)
        else:
            json.dump(payload, sys.stdout, indent=2)
            sys.stdout.write("\n")
    finally:
        extractor.close()


if __name__ == "__main__":
    main()

