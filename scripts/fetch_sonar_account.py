#!/usr/bin/env python3
"""Fetch and display Sonar account details via GraphQL."""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, List

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.apis.sonar_client import SonarGraphQLClient
from src.config.settings import config
from src.utils.logger import setup_logger

QUERY = """
query AccountById($id: Int64Bit!, $recordsPerPage: Int!) {
  accounts(id: $id, paginator: { page: 1, records_per_page: $recordsPerPage }) {
    entities {
      id
      sonar_unique_id
      name
      is_delinquent
      activation_date
      next_bill_date
      next_recurring_charge_amount
      account_status { id name }
      account_type { id name }
      addresses {
        entities {
          id
          type
          line1
          city
          subdivision
          zip
        }
      }
      contacts {
        entities {
          id
          name
          email_address
          primary
        }
      }
    }
    page_info {
      page
      total_pages
      total_count
      records_per_page
    }
  }
}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Sonar account details")
    parser.add_argument("account_ids", nargs="+", type=int, help="Account IDs to fetch")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print raw JSON response instead of formatted output",
    )
    return parser.parse_args()


def format_account(account: Dict[str, Any]) -> str:
    lines: List[str] = []
    status = account.get("account_status") or {}
    acc_type = account.get("account_type") or {}
    lines.append(f"Account {account.get('id')} — {account.get('name', 'Unknown')}")
    lines.append(
        "  Status: {status} (#{status_id}) | Type: {type} (#{type_id})".format(
            status=status.get("name", "n/a"),
            status_id=status.get("id", "?"),
            type=acc_type.get("name", "n/a"),
            type_id=acc_type.get("id", "?"),
        )
    )
    lines.append(
        "  Activation: {activation} | Next bill: {bill_date} | Next charge: {charge}".format(
            activation=account.get("activation_date") or "n/a",
            bill_date=account.get("next_bill_date") or "n/a",
            charge=account.get("next_recurring_charge_amount") or "n/a",
        )
    )
    lines.append(f"  Delinquent: {account.get('is_delinquent')}")

    addresses = (account.get("addresses") or {}).get("entities", [])
    if addresses:
        lines.append("  Addresses:")
        for addr in addresses:
            lines.append(
                "    - #{id} {line1}, {city}, {subdivision} {zip} ({atype})".format(
                    id=addr.get("id"),
                    line1=addr.get("line1", ""),
                    city=addr.get("city", ""),
                    subdivision=addr.get("subdivision", ""),
                    zip=addr.get("zip", ""),
                    atype=addr.get("type", ""),
                )
            )
    else:
        lines.append("  Addresses: none")

    contacts = (account.get("contacts") or {}).get("entities", [])
    if contacts:
        lines.append("  Contacts:")
        for contact in contacts:
            lines.append(
                "    - #{id} {name} <{email}> primary={primary}".format(
                    id=contact.get("id"),
                    name=contact.get("name", ""),
                    email=contact.get("email_address", ""),
                    primary=contact.get("primary"),
                )
            )
    else:
        lines.append("  Contacts: none")

    return "\n".join(lines)


def fetch_account(client: SonarGraphQLClient, account_id: int) -> Dict[str, Any]:
    variables = {"id": account_id, "recordsPerPage": 1}
    response = client.execute_query(QUERY, variables)
    if not response.success or not response.data:
        raise RuntimeError(f"GraphQL query failed for account {account_id}: {response.errors or 'no data'}")

    payload = response.data.get("accounts") or {}
    entities = payload.get("entities") or []
    if not entities:
        raise LookupError(f"Account {account_id} not found")
    return entities[0]


def main() -> None:
    args = parse_args()
    setup_logger(config.log_level)

    client = SonarGraphQLClient(config)
    fetched: List[Dict[str, Any]] = []

    for account_id in args.account_ids:
        try:
            account = fetch_account(client, account_id)
        except LookupError as exc:
            print(exc)
            continue
        except RuntimeError as exc:
            print(exc)
            continue

        fetched.append(account)
        if not args.json:
            print(format_account(account))
            print()

    if args.json:
        print(json.dumps(fetched, indent=2))

    if not fetched and not args.json:
        print("No matching accounts returned")


if __name__ == "__main__":
    main()
