#!/usr/bin/env python3
"""Incremental Sonar GraphQL backup.

For each collection already captured in the backup database, compare the stored
row count with the live Sonar total. When the totals differ, only the new rows
are downloaded and appended. Collections with matching counts are skipped.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from dotenv import load_dotenv

from psycopg import connect
from psycopg.rows import dict_row

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.apis.sonar_client import SonarGraphQLClient
from src.backup.sonar_graphql_backup import (
    CollectionField,
    GraphQLSchema,
    PostgresBackupWriter,
    SelectionBuilder,
    SonarGraphQLBackup,
)
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger


logger = get_logger("incremental_backup")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Incremental Sonar GraphQL backup (only new records)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--database-url",
        default=os.getenv("BACKUP_DATABASE_URL"),
        help="PostgreSQL connection URL (defaults to BACKUP_DATABASE_URL)",
    )
    parser.add_argument(
        "--collections",
        help="Comma separated list of collections to check (defaults to all)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=500,
        help="Page size to use for incremental downloads",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=0,
        help="Maximum depth for nested selections",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=30.0,
        help="Sonar GraphQL request timeout (seconds)",
    )
    return parser.parse_args()


class IncrementalBackup:
    def __init__(
        self,
        database_url: str,
        include_collections: Optional[Iterable[str]] = None,
        page_size: int = 500,
        max_depth: int = 0,
        request_timeout: float = 30.0,
    ) -> None:
        if not database_url:
            raise ValueError("Database URL is required")
        self.database_url = database_url
        self.page_size = max(1, page_size)
        self.client = SonarGraphQLClient(config, request_timeout=request_timeout)
        schema_data = self.client.get_schema_info()
        self.schema = GraphQLSchema(schema_data)
        self.selection_builder = SelectionBuilder(self.schema, max_depth=max_depth)
        self.writer = PostgresBackupWriter(database_url)
        self.include = {name.strip() for name in include_collections or [] if name.strip()}
        self._collections_map: Dict[str, CollectionField] = {
            cf.name: cf for cf in self.schema.discover_collection_fields()
        }
        self._progress_total = 0
        self._progress_current = 0
        self._progress_collection: Optional[str] = None
        self._progress_last_len = 0

    # ------------------------------ database helpers ---------------------

    def _fetch_backup_tables(self) -> Dict[str, str]:
        with connect(self.database_url) as conn, conn.cursor() as cur:
            cur.execute("SELECT query_name, table_name FROM backup_tables")
            rows = cur.fetchall()
        table_map = {row[0]: row[1] for row in rows}
        if self.include:
            table_map = {
                name: table for name, table in table_map.items() if name in self.include
            }
        return table_map

    def _count_backup_rows(self, table_name: str) -> int:
        with connect(self.database_url) as conn, conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {table_name}")
            (count,) = cur.fetchone()
        return int(count)

    # ------------------------------ sonar helpers -----------------------

    def _build_count_query(self, collection: CollectionField) -> Optional[str]:
        parts: List[str] = ["query CollectionCount {", f"  {collection.name}"]
        args: List[str] = []
        if collection.supports_paginator:
            args.append("paginator: { page: 1, records_per_page: 1 }")
        if collection.supports_limit:
            args.append("limit: 1")
        if args:
            parts[-1] += "(" + ", ".join(args) + ")"
        parts.append("  {")
        emitted = False
        if collection.total_count_field_name:
            parts.append(f"    {collection.total_count_field_name}")
            emitted = True
        if collection.has_page_info:
            parts.append(f"    {collection.page_info_field_name} {{")
            parts.append("      total_count")
            parts.append("      records_per_page")
            parts.append("    }")
            emitted = True
        parts.append("  }")
        parts.append("}")
        return "\n".join(parts) if emitted else None

    def _fetch_sonar_count(self, collection: CollectionField) -> Tuple[Optional[int], Optional[int]]:
        query = self._build_count_query(collection)
        if not query:
            return None, None
        response = self.client.execute_query(query)
        if not response.success or not response.data:
            logger.warning(f"Unable to fetch count for {collection.name}: {response.errors}")
            return None, None
        container = response.data.get(collection.name) or {}
        if collection.total_count_field_name and collection.total_count_field_name in container:
            total = int(container[collection.total_count_field_name])
        else:
            page_info = container.get(collection.page_info_field_name) or {}
            total = int(page_info.get("total_count")) if "total_count" in page_info else None
        per_page = None
        page_info = container.get(collection.page_info_field_name) or {}
        if "records_per_page" in page_info and page_info["records_per_page"] is not None:
            per_page = int(page_info["records_per_page"])
        return total, per_page

    def _build_selection(self, collection: CollectionField) -> str:
        return self.selection_builder.build(collection.entity_type["name"])

    def _build_paginated_query(
        self,
        collection: CollectionField,
        selection: str,
        include_page_info: bool = True,
        use_offset: bool = False,
    ) -> str:
        formatted = selection.replace("\n", "\n      ")
        container_lines = [
            f"    {collection.entities_field_name} {{",
            f"      {formatted}",
            "    }",
        ]
        if include_page_info and collection.has_page_info:
            container_lines.append(f"    {collection.page_info_field_name} {{")
            for field in ["page", "total_pages", "total_count", "records_per_page"]:
                container_lines.append(f"      {field}")
            container_lines.append("    }")
        if include_page_info and collection.has_total_count:
            container_lines.append(f"    {collection.total_count_field_name}")
        args_header: List[str] = []
        args_call: List[str] = []
        if collection.supports_paginator and not use_offset:
            args_header.extend(["$page: Int!", "$per_page: Int!"])
            args_call.append("paginator: { page: $page, records_per_page: $per_page }")
        if use_offset and collection.supports_limit:
            args_header.extend(["$limit: Int!", "$offset: Int!"])
            args_call.append("limit: $limit")
            if collection.supports_offset:
                args_call.append("offset: $offset")
        query_header = "query Incremental"
        if args_header:
            query_header += "(" + ", ".join(args_header) + ")"
        if args_call:
            call_fragment = "(" + ", ".join(args_call) + ")"
        else:
            call_fragment = ""
        lines = [query_header + " {", f"  {collection.name}{call_fragment} {{"]
        lines.extend(container_lines)
        lines.append("  }")
        lines.append("}")
        return "\n".join(lines)

    def _execute_incremental_query(
        self,
        collection: CollectionField,
        query: str,
        variables: Optional[Dict[str, int]] = None,
    ) -> List[Dict[str, Any]]:
        response = self.client.execute_query(query, variables)
        if not response.success or not response.data:
            raise RuntimeError(f"Collection {collection.name} query failed: {response.errors}")
        container = response.data.get(collection.name) or {}
        entities = container.get(collection.entities_field_name) or []
        return entities

    def _determine_page_size(self, remaining: int, hint: Optional[int] = None) -> int:
        if remaining <= 0:
            return 0
        size = self.page_size
        if hint and hint > 1:
            size = min(size, hint)
        size = max(10, size)
        return min(size, remaining)

    def _start_progress(self, collection: str, total: int) -> None:
        self._progress_total = max(0, total)
        self._progress_current = 0
        self._progress_collection = collection
        self._progress_last_len = 0
        if self._progress_total <= 0:
            return
        self._update_progress(increment=0)

    def _update_progress(self, increment: int) -> None:
        if self._progress_total <= 0 or not self._progress_collection:
            return
        self._progress_current = min(
            self._progress_total, self._progress_current + max(0, increment)
        )
        ratio = (self._progress_current / self._progress_total) if self._progress_total else 1.0
        bar_length = 30
        filled_length = int(bar_length * ratio)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        line = (
            f"{self._progress_collection}: |{bar}| "
            f"{self._progress_current}/{self._progress_total} ({ratio * 100:.1f}%)"
        )
        padding = max(0, self._progress_last_len - len(line))
        sys.stdout.write(f"\r{line}{' ' * padding}")
        sys.stdout.flush()
        self._progress_last_len = len(line)

    def _finish_progress(self) -> None:
        if self._progress_total > 0:
            sys.stdout.write("\n")
            sys.stdout.flush()
        self._progress_total = 0
        self._progress_current = 0
        self._progress_collection = None
        self._progress_last_len = 0

    def _fetch_with_offset(
        self,
        collection: CollectionField,
        selection: str,
        start_offset: int,
        target_total: int,
        page_size: int,
    ) -> List[Dict[str, Any]]:
        remaining = max(0, target_total - start_offset)
        if remaining == 0:
            return []
        query = self._build_paginated_query(collection, selection, use_offset=True)
        fetched: List[Dict[str, Any]] = []
        offset = start_offset
        while offset < target_total:
            limit = min(page_size, target_total - offset)
            entities = self._execute_incremental_query(
                collection,
                query,
                {"limit": limit, "offset": offset},
            )
            if not entities:
                break
            fetched.extend(entities)
            self._update_progress(len(entities))
            offset += len(entities)
        return fetched

    def _fetch_with_paginator(
        self,
        collection: CollectionField,
        selection: str,
        start_index: int,
        target_total: int,
        page_size: int,
    ) -> List[Dict[str, Any]]:
        query = self._build_paginated_query(collection, selection, include_page_info=False)
        fetched: List[Dict[str, Any]] = []
        page = max(1, (start_index // page_size) + 1)
        # Ensure we don't miss entries within the partially filled page
        expected_total = target_total
        while len(fetched) + start_index < expected_total:
            entities = self._execute_incremental_query(
                collection,
                query,
                {"page": page, "per_page": page_size},
            )
            if not entities:
                break
            fetched.extend(entities)
            self._update_progress(len(entities))
            page += 1
        return fetched

    def run(self) -> None:
        tables = self._fetch_backup_tables()
        if not self.include:
            log_tables = [name for name in tables if "log" in name.lower()]
            if log_tables:
                logger.info(
                    "Skipping %s log collection(s); use --collections to include them",
                    len(log_tables),
                )
                for name in log_tables:
                    tables.pop(name, None)
        if not tables:
            logger.warning("No backup tables found. Run the full backup first.")
            return
        run_id, _ = self.writer.start_run()
        logger.info(f"Incremental backup run {run_id} started")
        try:
            for collection_name, table in sorted(tables.items()):
                collection = self._collections_map.get(collection_name)
                if not collection:
                    logger.debug(f"Collection {collection_name} not present in schema; skipping")
                    continue
                backup_count = self._count_backup_rows(table)
                sonar_total, per_page = self._fetch_sonar_count(collection)
                if sonar_total is None:
                    logger.info(f"{collection_name}: unable to determine Sonar count; skipping")
                    continue
                if sonar_total <= backup_count:
                    logger.info(f"{collection_name}: counts match ({backup_count}); nothing to do")
                    continue
                delta = sonar_total - backup_count
                logger.info(
                    f"{collection_name}: detected {delta} new record(s) "
                    f"(backup={backup_count}, sonar={sonar_total})"
                )
                selection = self._build_selection(collection)
                entities: List[Dict[str, Any]] = []
                if collection.supports_offset or collection.supports_limit:
                    page_size = self._determine_page_size(delta)
                    self._start_progress(collection_name, delta)
                    try:
                        entities = self._fetch_with_offset(
                            collection,
                            selection,
                            backup_count,
                            sonar_total,
                            page_size,
                        )
                    finally:
                        self._finish_progress()
                elif collection.supports_paginator:
                    # fall back to paginator
                    effective_page_size = self._determine_page_size(delta, per_page)
                    self._start_progress(collection_name, delta)
                    try:
                        entities = self._fetch_with_paginator(
                            collection,
                            selection,
                            backup_count,
                            sonar_total,
                            effective_page_size,
                        )
                    finally:
                        self._finish_progress()
                else:
                    logger.warning(f"{collection_name}: pagination unsupported; re-running full collection")
                    backup_tool = SonarGraphQLBackup(
                        database_url=self.database_url,
                        client=self.client,
                        page_size=self.page_size,
                        include={collection_name},
                        max_depth=0,
                        sample_size=None,
                    )
                    backup_tool.run()
                    continue

                if not entities:
                    logger.info(f"{collection_name}: no entities fetched (possible transient issue)")
                    continue
                table_name = self.writer.ensure_table(collection_name)
                written = self.writer.write_entities(table_name, entities)
                logger.info(f"{collection_name}: appended {written} record(s)")
                duration = 0.0
                self.writer.record_table_stats(collection_name, run_id, written, duration)
                self.writer.mark_table_run(collection_name, run_id)
            self.writer.complete_run(run_id)
            logger.info(f"Incremental backup run {run_id} completed")
        finally:
            self.writer.close()


def main() -> None:
    args = parse_args()
    setup_logger("INFO")
    load_dotenv(Path(".env"))
    collections = args.collections.split(",") if args.collections else None
    job = IncrementalBackup(
        database_url=args.database_url,
        include_collections=collections,
        page_size=args.page_size,
        max_depth=args.max_depth,
        request_timeout=args.request_timeout,
    )
    job.run()


if __name__ == "__main__":
    main()
