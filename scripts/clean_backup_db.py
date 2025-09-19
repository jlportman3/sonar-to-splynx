#!/usr/bin/env python3
"""Drop GraphQL backup tables and truncate metadata in the Postgres storage."""

import os
from typing import Dict, List

from dotenv import load_dotenv
from psycopg import connect, sql

load_dotenv()

BACKUP_DATABASE_URL = os.getenv("BACKUP_DATABASE_URL")
DB_PARAMS: Dict[str, str] = {
    "host": os.getenv("BACKUP_DB_HOST", ""),
    "port": os.getenv("BACKUP_DB_PORT", ""),
    "dbname": os.getenv("BACKUP_DB_NAME", ""),
    "user": os.getenv("BACKUP_DB_USER", ""),
    "password": os.getenv("BACKUP_DB_PASSWORD", ""),
}


def resolve_connection_kwargs() -> Dict[str, str]:
    """Build kwargs for psycopg.connect based on env configuration."""
    if BACKUP_DATABASE_URL:
        return {"conninfo": BACKUP_DATABASE_URL}

    if all(DB_PARAMS.values()):
        return DB_PARAMS

    raise ValueError(
        "Missing Postgres connection details. Set BACKUP_DATABASE_URL or BACKUP_DB_* variables."
    )


def fetch_backup_tables(conn_kwargs: Dict[str, str]) -> List[str]:
    with connect(**conn_kwargs) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT table_name FROM backup_tables")
            return [row[0] for row in cur.fetchall()]


def drop_backup_tables(conn_kwargs: Dict[str, str], tables: List[str]) -> None:
    if not tables:
        return
    with connect(**conn_kwargs) as conn:
        with conn.cursor() as cur:
            for table_name in tables:
                cur.execute(
                    sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
                        sql.Identifier(table_name)
                    )
                )


def truncate_metadata(conn_kwargs: Dict[str, str]) -> None:
    with connect(**conn_kwargs) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS backup_progress (
                    query_name TEXT PRIMARY KEY,
                    next_page INT NOT NULL,
                    per_page INT NOT NULL,
                    updated_at TIMESTAMPTZ NOT NULL,
                    run_id TEXT
                )
                """
            )
            cur.execute(
                "TRUNCATE TABLE backup_runs, backup_tables, backup_table_stats, backup_progress RESTART IDENTITY CASCADE"
            )


def main() -> None:
    conn_kwargs = resolve_connection_kwargs()
    table_names = fetch_backup_tables(conn_kwargs)
    drop_backup_tables(conn_kwargs, table_names)
    truncate_metadata(conn_kwargs)
    print(f"Dropped {len(table_names)} table(s) and truncated metadata tables.")


if __name__ == "__main__":
    main()
