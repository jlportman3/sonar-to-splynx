#!/usr/bin/env python3
"""Verify Sonar GraphQL backup against live Sonar data.

Compares per-collection record counts between the Postgres backup and the
live Sonar GraphQL API. Optionally runs in parallel.
"""

from __future__ import annotations

import argparse
import os
import sys
import threading
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Set

from concurrent.futures import ThreadPoolExecutor, as_completed

from dotenv import load_dotenv
from psycopg import connect

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.apis.sonar_client import SonarGraphQLClient
from src.backup.sonar_graphql_backup import GraphQLSchema
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger

load_dotenv()

logger = get_logger("verify_backup")


@dataclass
class CollectionCheck:
    name: str
    backup_count: int
    sonar_count: Optional[int]
    matched: Optional[bool]
    note: Optional[str] = None


class BackupVerifier:
    def __init__(
        self,
        database_url: str,
        collections: Optional[Set[str]] = None,
        threads: int = 4,
        request_timeout: float = 20.0,
    ) -> None:
        self.database_url = database_url
        self.collections_filter = collections
        self.thread_count = max(1, threads)
        self.client = SonarGraphQLClient(config, request_timeout=request_timeout)
        schema_data = self.client.get_schema_info()
        self.schema = GraphQLSchema(schema_data)
        self._collection_map = {
            cf.name: cf for cf in self.schema.discover_collection_fields()
        }
        self._db_local = threading.local()

    def _get_db_conn(self):
        conn = getattr(self._db_local, "conn", None)
        if conn is None:
            conn = connect(self.database_url)
            conn.autocommit = True
            self._db_local.conn = conn
        return conn

    def close(self) -> None:
        conn = getattr(self._db_local, "conn", None)
        if conn is not None:
            try:
                conn.close()
            except Exception:  # pragma: no cover
                pass

    def fetch_backup_tables(self) -> Dict[str, str]:
        conn = self._get_db_conn()
        with conn.cursor() as cur:
            cur.execute("SELECT query_name, table_name FROM backup_tables")
            rows = cur.fetchall()
        table_map = {row[0]: row[1] for row in rows}
        if self.collections_filter:
            table_map = {
                name: table
                for name, table in table_map.items()
                if name in self.collections_filter
            }
        return table_map

    def count_backup_rows(self, table_name: str) -> int:
        conn = self._get_db_conn()
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {table_name}")
            (count,) = cur.fetchone()
        return int(count)

    def build_count_query(self, collection_name: str) -> Optional[str]:
        collection = self._collection_map.get(collection_name)
        if not collection:
            return None
        parts: List[str] = ["query Verify {", f"  {collection_name}"]
        arg_clause = []
        if collection.supports_paginator:
            arg_clause.append("paginator: { page: 1, records_per_page: 1 }")
        if arg_clause:
            parts[-1] += "(" + ", ".join(arg_clause) + ")"
        parts.append("  {")
        emitted_field = False
        if collection.total_count_field_name:
            parts.append(f"    {collection.total_count_field_name}")
            emitted_field = True
        if collection.has_page_info:
            parts.append(f"    {collection.page_info_field_name} {{")
            parts.append("      total_count")
            parts.append("    }")
            emitted_field = True
        if not emitted_field:
            return None
        parts.append("  }")
        parts.append("}")
        return "\n".join(parts)

    def fetch_sonar_count(self, collection_name: str) -> Optional[int]:
        query = self.build_count_query(collection_name)
        if not query:
            return None
        response = self.client.execute_query(query)
        if not response.success or not response.data:
            logger.warning(
                "Sonar query failed for %s: %s",
                collection_name,
                response.errors,
            )
            return None
        container = response.data.get(collection_name) or {}
        collection = self._collection_map.get(collection_name)
        if not collection:
            return None
        if collection.total_count_field_name and collection.total_count_field_name in container:
            return int(container[collection.total_count_field_name])
        page_info = container.get(collection.page_info_field_name) or {}
        if "total_count" in page_info:
            return int(page_info["total_count"])
        return None

    def verify_collection(self, collection_name: str, table_name: str) -> CollectionCheck:
        backup_count = self.count_backup_rows(table_name)
        sonar_count = self.fetch_sonar_count(collection_name)
        matched: Optional[bool] = None
        note: Optional[str] = None
        if sonar_count is not None:
            matched = backup_count == sonar_count
            if not matched:
                note = f"Count mismatch: backup={backup_count} sonar={sonar_count}"
        else:
            note = "Sonar count unavailable"
        return CollectionCheck(
            name=collection_name,
            backup_count=backup_count,
            sonar_count=sonar_count,
            matched=matched,
            note=note,
        )

    def run(self) -> List[CollectionCheck]:
        table_map = self.fetch_backup_tables()
        checks: List[CollectionCheck] = []
        if not table_map:
            logger.warning("No backup tables found to verify")
            return checks

        def worker(item):
            name, table = item
            try:
                return self.verify_collection(name, table)
            except Exception as exc:  # pragma: no cover - logging only
                logger.exception("Verification failed for %s: %s", name, exc)
                return CollectionCheck(
                    name=name,
                    backup_count=0,
                    sonar_count=None,
                    matched=False,
                    note=str(exc),
                )

        items = list(table_map.items())
        if self.thread_count > 1 and len(items) > 1:
            with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
                futures = {executor.submit(worker, item): item[0] for item in items}
                for future in as_completed(futures):
                    checks.append(future.result())
        else:
            for item in items:
                checks.append(worker(item))
        return sorted(checks, key=lambda c: c.name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify Sonar GraphQL backup against live data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--database-url",
        default=os.getenv("BACKUP_DATABASE_URL"),
        help="PostgreSQL connection URL (defaults to BACKUP_DATABASE_URL)",
    )
    parser.add_argument(
        "--collections",
        help="Comma-separated list of collection names to verify",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=4,
        help="Number of concurrent verification workers",
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

    database_url = args.database_url
    if not database_url:
        raise ValueError("Database URL not provided (use --database-url or BACKUP_DATABASE_URL)")

    collections = None
    if args.collections:
        collections = {name.strip() for name in args.collections.split(",") if name.strip()}

    verifier = BackupVerifier(
        database_url=database_url,
        collections=collections,
        threads=args.threads,
    )

    try:
        results = verifier.run()
    finally:
        verifier.close()

    if not results:
        logger.warning("No collections verified")
        return

    matched = [r for r in results if r.matched]
    mismatched = [r for r in results if r.matched is False]
    unknown = [r for r in results if r.matched is None]

    for result in results:
        status = "MATCH" if result.matched else ("DIFF" if result.matched is False else "UNKNOWN")
        sonar_info = result.sonar_count if result.sonar_count is not None else "?"
        note = f" - {result.note}" if result.note else ""
        logger.info(
            f"{status:7s} {result.name:40s} backup={result.backup_count} sonar={sonar_info}{note}"
        )

    logger.info(
        "Summary: matched=%s mismatched=%s unknown=%s total=%s",
        len(matched),
        len(mismatched),
        len(unknown),
        len(results),
    )

    if mismatched:
        logger.error("Backup verification detected mismatches")
        sys.exit(1)


if __name__ == "__main__":
    main()
