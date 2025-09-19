#!/usr/bin/env python3
"""Copy Sonar customer custom-field definitions (and values) into Splynx."""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv
from psycopg import connect

BACKUP_FIELDS_TABLE = "graphql_backup__custom_fields"
BACKUP_DATA_TABLE = "graphql_backup__custom_field_data"
SONAR_ENTITY = "Account"

FIELDS_TABLE = "customers_fields"
VALUES_TABLE = "customers_values"

FIELD_COLUMNS = [
    "name",
    "module",
    "category",
    "title",
    "type",
    "position",
    "default_value",
    "min_length",
    "max_length",
    "select_values",
    "decimals",
    "relation_module",
    "addon",
    "addon_uri",
    "addon_input_type",
    "deleted",
    "show_in_list",
    "is_required",
    "is_unique",
    "is_add",
    "searchable",
    "readonly",
    "hidden",
    "disabled",
]

DEFAULT_FIELD_VALUES = {
    "category": "0",
    "default_value": "",
    "min_length": "",
    "max_length": "",
    "select_values": "",
    "decimals": "2",
    "relation_module": "",
    "addon": "",
    "addon_uri": "",
    "addon_input_type": "",
    "deleted": "0",
    "show_in_list": "0",
    "is_add": "1",
    "searchable": "0",
    "readonly": "0",
    "hidden": "0",
    "disabled": "0",
}

TYPE_MAP = {
    "TEXT": "string",
}


def load_env() -> None:
    load_dotenv(Path(".env"))


def fetch_sonar_fields() -> List[Dict[str, str]]:
    url = os.getenv("BACKUP_DATABASE_URL")
    if not url:
        raise SystemExit("BACKUP_DATABASE_URL is not set")

    fields: List[Dict[str, str]] = []
    with connect(url) as conn, conn.cursor() as cur:
        cur.execute(
            f"SELECT data FROM {BACKUP_FIELDS_TABLE} WHERE data ->> 'entity_type' = %s",
            (SONAR_ENTITY,),
        )
        for (row,) in cur.fetchall():
            fields.append(row)
    return fields


def fetch_sonar_values(field_id: str) -> List[Dict[str, str]]:
    url = os.getenv("BACKUP_DATABASE_URL")
    values: List[Dict[str, str]] = []
    with connect(url) as conn, conn.cursor() as cur:
        cur.execute(
            f"SELECT data FROM {BACKUP_DATA_TABLE} WHERE data ->> 'custom_field_id' = %s",
            (field_id,),
        )
        for (row,) in cur.fetchall():
            values.append(row)
    return values


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


def get_existing_field_names() -> Dict[str, Dict[str, str]]:
    rows = run_mysql_query(f"SELECT name, title FROM {FIELDS_TABLE};")
    return {row[0]: {"title": row[1]} for row in rows}


def next_position() -> int:
    rows = run_mysql_query(f"SELECT COALESCE(MAX(position),0) FROM {FIELDS_TABLE};")
    return int(rows[0][0]) + 1 if rows else 1


def slugify(name: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_").lower()
    return slug or "custom_field"


def map_field_type(sonar_type: str) -> str:
    mapped = TYPE_MAP.get(sonar_type.upper())
    if not mapped:
        raise SystemExit(f"Unsupported Sonar custom field type: {sonar_type}")
    return mapped


def insert_definition(field: Dict[str, str], position: int) -> str:
    name = slugify(field.get("name", ""))
    splynx_type = map_field_type(field.get("type", "TEXT"))
    is_required = "1" if field.get("required") else "0"
    is_unique = "1" if field.get("unique") else "0"

    values = {
        "name": name,
        "module": "customers",
        "title": field.get("name", name.title()),
        "type": splynx_type,
        "position": str(position),
        "is_required": is_required,
        "is_unique": is_unique,
    }
    values.update(DEFAULT_FIELD_VALUES)

    assignments = []
    for column in FIELD_COLUMNS:
        val = values.get(column, DEFAULT_FIELD_VALUES.get(column, "")) or ""
        assignments.append("'%s'" % val.replace("'", "''"))

    sql = (
        f"INSERT INTO {FIELDS_TABLE} ({', '.join(FIELD_COLUMNS)}) "
        f"VALUES ({', '.join(assignments)});"
    )
    run_mysql_query(sql)
    return name


def insert_values(field_name: str, sonar_values: List[Dict[str, str]]) -> None:
    if not sonar_values:
        return
    rows = []
    for item in sonar_values:
        customer_id = item.get("customfielddataable_id")
        value = item.get("value", "")
        if not customer_id:
            continue
        sanitized = value.replace("'", "''")
        rows.append(
            (
                int(customer_id),
                field_name,
                sanitized,
            )
        )
    if not rows:
        return

    formatted_rows = []
    for customer_id, name, value in rows:
        escaped_name = name.replace("'", "''")
        escaped_value = value.replace("'", "''")
        formatted_rows.append(f"({customer_id}, '{escaped_name}', '{escaped_value}')")
    values_clause = ", ".join(formatted_rows)
    sql = (
        f"INSERT INTO {VALUES_TABLE} (id, name, value) VALUES "
        + values_clause
        + " ON DUPLICATE KEY UPDATE value=VALUES(value);"
    )
    run_mysql_query(sql)


def main() -> None:
    load_env()
    sonar_fields = fetch_sonar_fields()
    existing = get_existing_field_names()
    position = next_position()

    inserted = 0
    for field in sonar_fields:
        name = slugify(field.get("name", ""))
        if name not in existing:
            insert_definition(field, position)
            position += 1
            inserted += 1
        values = fetch_sonar_values(field.get("id"))
        insert_values(name, values)

    print(f"Processed {len(sonar_fields)} custom field(s); added {inserted} new definition(s).")


if __name__ == "__main__":
    main()
