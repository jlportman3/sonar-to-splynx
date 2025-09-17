#!/usr/bin/env python3
"""Smoke test the Sonar GraphQL API by fetching a single record for key entities."""

from __future__ import annotations

import sys
from typing import Dict, Any

from src.apis.sonar_client import SonarGraphQLClient
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger

logger = get_logger("graphql_smoke_test")

COLLECTION_QUERIES: Dict[str, Dict[str, Any]] = {
    "accounts": {
        "query": """
            query AccountsSmoke {
              accounts {
                entities {
                  id
                  name
                }
                page_info {
                  total_count
                  page
                  records_per_page
                }
              }
            }
        """,
        "fields": ("id", "name"),
    },
    "services": {
        "query": """
            query ServicesSmoke {
              services {
                entities {
                  id
                  name
                  type
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "name", "type"),
    },
    "invoices": {
        "query": """
            query InvoicesSmoke {
              invoices {
                entities {
                  id
                  date
                  due_date
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "date", "due_date"),
    },
    "payments": {
        "query": """
            query PaymentsSmoke {
              payments {
                entities {
                  id
                  amount
                  description
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "amount", "description"),
    },
    "inventory_items": {
        "query": """
            query InventoryItemsSmoke {
              inventory_items {
                entities {
                  id
                  overall_status
                  deployment_type_id
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "overall_status", "deployment_type_id"),
    },
    "ip_assignments": {
        "query": """
            query IpAssignmentsSmoke {
              ip_assignments {
                entities {
                  id
                  description
                  subnet_id
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "description", "subnet_id"),
    },
    "tickets": {
        "query": """
            query TicketsSmoke {
              tickets {
                entities {
                  id
                  subject
                  status
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "subject", "status"),
    },
    "users": {
        "query": """
            query UsersSmoke {
              users {
                entities {
                  id
                  name
                  email_address
                }
                page_info {
                  total_count
                  page
                }
              }
            }
        """,
        "fields": ("id", "name", "email_address"),
    },
}


def run_smoke_test() -> bool:
    client = SonarGraphQLClient(config)
    success = True

    for collection, definition in COLLECTION_QUERIES.items():
        query = definition["query"].strip()
        logger.info(f"Querying {collection}")
        response = client.execute_query(query)

        if not response.success:
            logger.error(f"{collection} query failed: {response.errors}")
            success = False
            continue

        data = response.data or {}
        payload = data.get(collection)
        if not payload:
            logger.error(f"{collection} query returned no payload")
            success = False
            continue

        entities = payload.get("entities", [])
        page_info = payload.get("page_info") or {}
        if page_info:
            logger.info(
                f"{collection} page info: total={page_info.get('total_count')} page={page_info.get('page')}"
            )
        if not entities:
            logger.warning(f"{collection} query returned zero entities")
            continue

        first = entities[0]
        summary = {field: first.get(field) for field in definition["fields"]}
        logger.info(f"{collection} sample: {summary}")

    return success


def main() -> None:
    setup_logger("INFO")

    try:
        if not run_smoke_test():
            sys.exit(1)
    except Exception as exc:  # pragma: no cover - safety net for CLI usage
        logger.exception(f"GraphQL smoke test failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
