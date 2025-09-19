#!/usr/bin/env python3
"""Populate Splynx company information from the Sonar backup snapshot."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

from dotenv import load_dotenv
from psycopg import connect

BACKUP_TABLE = "graphql_backup__companies"
TARGET_TABLE = "finance_template_values"


def load_env() -> None:
    load_dotenv(Path(".env"))


def fetch_sonar_company() -> Dict[str, str]:
    url = os.getenv("BACKUP_DATABASE_URL")
    if not url:
        raise SystemExit("BACKUP_DATABASE_URL is not set")

    with connect(url) as conn, conn.cursor() as cur:
        cur.execute(f"SELECT data FROM {BACKUP_TABLE} LIMIT 1")
        row = cur.fetchone()
        if not row:
            raise SystemExit("No company record found in Sonar backup")
        return row[0]


def run_mysql_query(sql: str) -> List[List[str]]:
    user = os.getenv("SPLYNX_DB_USER")
    password = os.getenv("SPLYNX_DB_PASSWORD")
    if not user or not password:
        raise SystemExit("SPLYNX_DB_USER/PASSWORD must be set in .env")

    database = os.getenv("SPLYNX_DB_NAME", "splynx")
    socket = os.getenv("SPLYNX_DB_SOCKET")
    host = os.getenv("SPLYNX_DB_HOST", "localhost")
    port = os.getenv("SPLYNX_DB_PORT", "3306")

    command = ["mysql", "-u", user, "--batch", "--skip-column-names", "-e", sql, database]
    if socket:
        command.extend(["-S", socket])
    else:
        command.extend(["-h", host, "-P", str(port)])

    env = os.environ.copy()
    env["MYSQL_PWD"] = password

    result = subprocess.run(command, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise RuntimeError(f"MySQL query failed: {result.stderr.strip()}\nSQL: {sql}")

    rows: List[List[str]] = []
    for line in result.stdout.strip().splitlines():
        if not line:
            continue
        rows.append(line.split("\t"))
    return rows


def get_company_ids() -> List[int]:
    rows = run_mysql_query(f"SELECT id FROM {TARGET_TABLE};")
    if not rows:
        # Splynx creates id=0 by default even if table empty; ensure we have at least [0]
        return [0]
    return [int(row[0]) for row in rows]


def fetch_existing_row(row_id: int) -> Optional[Dict[str, str]]:
    columns = [
        "company_name",
        "street_1",
        "street_2",
        "zip",
        "city",
        "country",
        "iso_country",
        "email",
        "phone",
        "company_id",
        "company_vat",
        "bank_account",
        "bank_name",
        "bank_address",
        "splynx_url",
    ]
    rows = run_mysql_query(
        f"SELECT {', '.join(columns)} FROM {TARGET_TABLE} WHERE id={row_id};"
    )
    if not rows:
        return None
    values = rows[0]
    return dict(zip(columns, values))


def update_company_row(company: Dict[str, str], row_id: int) -> None:
    existing = fetch_existing_row(row_id) or {}
    field_map = {
        "company_name": company.get("name") or existing.get("company_name", ""),
        "street_1": company.get("street_1") or existing.get("street_1", ""),
        "street_2": company.get("street_2") or existing.get("street_2", ""),
        "zip": company.get("zip") or existing.get("zip", ""),
        "city": company.get("city") or existing.get("city", ""),
        "country": company.get("country") or existing.get("country", ""),
        "iso_country": company.get("country") or existing.get("iso_country", "US"),
        "email": company.get("support_email") or existing.get("email", ""),
        "phone": company.get("phone_number") or existing.get("phone", ""),
        "company_id": company.get("company_id") or existing.get("company_id", ""),
        "company_vat": company.get("tax_identification") or existing.get("company_vat", ""),
        "bank_account": company.get("bank_account") or existing.get("bank_account", ""),
        "bank_name": company.get("bank_name") or existing.get("bank_name", ""),
        "bank_address": company.get("bank_address") or existing.get("bank_address", ""),
        "splynx_url": company.get("customer_portal_url") or existing.get("splynx_url", ""),
    }

    assignments_parts = []
    for column, value in field_map.items():
        sanitized = (value or "").replace("'", "''")
        assignments_parts.append(f"{column}='{sanitized}'")
    assignments = ", ".join(assignments_parts)
    sql = f"UPDATE {TARGET_TABLE} SET {assignments} WHERE id={row_id};"
    run_mysql_query(sql)


def main() -> None:
    load_env()
    company = fetch_sonar_company()
    ids = get_company_ids()
    for row_id in ids:
        update_company_row(company, row_id)
    print(f"Updated {len(ids)} company record(s) in Splynx.")


if __name__ == "__main__":
    main()
