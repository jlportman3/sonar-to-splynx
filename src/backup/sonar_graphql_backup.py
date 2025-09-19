"""Utilities for backing up Sonar GraphQL data into PostgreSQL."""

from __future__ import annotations

import json
import hashlib
import uuid
import textwrap
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import urlsplit, urlunsplit
import threading

from psycopg import connect, sql
from psycopg.types.json import Json

from src.apis.sonar_client import SonarGraphQLClient
from src.config.settings import config
from src.utils.logger import get_logger

logger = get_logger(__name__)

_DEFAULT_SCALARS = {"String", "Boolean", "Int", "Float", "ID"}
_OPTIONAL_ARG_WHITELIST = {"limit", "offset", "after", "before", "first", "last", "cursor"}
_BACKUP_TABLE_PREFIX = "graphql_backup__"


def _sanitize_table_name(name: str) -> str:
    """Sanitize a name so it is safe to use as a PostgreSQL table."""
    safe = [c if c.isalnum() or c == "_" else "_" for c in name]
    sanitized = "".join(safe).strip("_")
    return sanitized or "unnamed"


def _redact_database_url(url: str) -> str:
    """Mask credentials in a connection string before logging."""
    try:
        parts = urlsplit(url)
    except ValueError:
        return url

    netloc = parts.netloc
    if not netloc or "@" not in netloc:
        return url

    userinfo, host = netloc.split("@", 1)
    if ":" in userinfo:
        username = userinfo.split(":", 1)[0]
        masked_userinfo = f"{username}:***"
    else:
        masked_userinfo = userinfo

    masked_netloc = f"{masked_userinfo}@{host}"
    return urlunsplit((parts.scheme, masked_netloc, parts.path, parts.query, parts.fragment))


def _format_table_name(query_name: str) -> str:
    """Return the physical table name for a given GraphQL query."""
    sanitized = _sanitize_table_name(query_name)
    return f"{_BACKUP_TABLE_PREFIX}{sanitized}"


class GraphQLSchema:
    """Helper around a GraphQL introspection schema."""

    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema
        raw_types = schema.get("__schema", {}).get("types", [])
        self.type_map: Dict[str, Dict[str, Any]] = {
            t["name"]: t for t in raw_types if t.get("name")
        }
        query_type_name = schema.get("__schema", {}).get("queryType", {}).get("name")
        if not query_type_name or query_type_name not in self.type_map:
            raise ValueError("Unable to determine GraphQL query type from schema")
        self.query_type = self.type_map[query_type_name]

        # Collect scalar and enum names (treat custom scalars as scalars for backup)
        self.scalar_types: Set[str] = {
            t["name"]
            for t in raw_types
            if t.get("kind") == "SCALAR" and t.get("name")
        } | _DEFAULT_SCALARS
        self.enum_types: Set[str] = {
            t["name"]
            for t in raw_types
            if t.get("kind") == "ENUM" and t.get("name")
        }

    # ------------------------------------------------------------------
    # Introspection helpers

    def get_type(self, name: Optional[str]) -> Optional[Dict[str, Any]]:
        if not name:
            return None
        return self.type_map.get(name)

    def is_scalar(self, type_name: str) -> bool:
        return type_name in self.scalar_types

    def is_enum(self, type_name: str) -> bool:
        return type_name in self.enum_types

    def resolve_named_type(self, type_ref: Dict[str, Any]) -> Tuple[Optional[Dict[str, Any]], bool]:
        """Resolve a field type into its named type and whether it is a list."""
        is_list = False
        current = type_ref
        while current:
            kind = current.get("kind")
            if kind == "NON_NULL":
                current = current.get("ofType")
                continue
            if kind == "LIST":
                is_list = True
                current = current.get("ofType")
                continue
            break
        if current and current.get("name"):
            named = self.get_type(current["name"])
        else:
            named = None
        return named, is_list

    def is_type_non_null(self, type_ref: Dict[str, Any]) -> bool:
        return type_ref.get("kind") == "NON_NULL"

    def field_has_required_args(self, field: Dict[str, Any]) -> bool:
        for arg in field.get("args", []):
            arg_type = arg.get("type", {})
            default_val = arg.get("defaultValue")
            arg_name = arg.get("name")
            if self.is_type_non_null(arg_type) and default_val is None:
                if arg_name not in _OPTIONAL_ARG_WHITELIST:
                    return True
        return False

    # ------------------------------------------------------------------
    # Discovery helpers

    def discover_collection_fields(self) -> List["CollectionField"]:
        """Discover root query fields that look like list/collection queries."""
        collections: List[CollectionField] = []
        for field in self.query_type.get("fields", []):
            field_name = field.get("name")
            args = field.get("args", [])
            arg_names = {arg.get("name") for arg in args}
            # Heuristic: require a limit-style argument
            if not ({"limit", "first", "paginator"} & arg_names):
                continue
            # Skip fields needing unknown required args
            has_unsupported_required = False
            for arg in args:
                arg_name = arg.get("name")
                arg_type = arg.get("type", {})
                default_val = arg.get("defaultValue")
                if self.is_type_non_null(arg_type) and default_val is None:
                    if arg_name not in {"limit", "offset", "first", "after", "paginator"}:
                        has_unsupported_required = True
                        break
            if has_unsupported_required:
                continue

            return_type, _ = self.resolve_named_type(field.get("type", {}))
            if not return_type:
                continue
            entities_field = None
            page_info_field = None
            total_count_field = None
            for sub_field in return_type.get("fields", []):
                if sub_field.get("name") == "entities":
                    entities_field = sub_field
                elif sub_field.get("name") in {"page_info", "pageInfo"}:
                    page_info_field = sub_field
                elif sub_field.get("name") in {"total_count", "totalCount"}:
                    total_count_field = sub_field
            if not entities_field:
                continue
            entity_type, _ = self.resolve_named_type(entities_field.get("type", {}))
            if not entity_type:
                continue
            page_info_field_name = page_info_field.get("name") if page_info_field else None
            page_info_next_field_name = None
            page_info_cursor_field_name = None
            if page_info_field:
                page_info_type, _ = self.resolve_named_type(page_info_field.get("type", {}))
                if page_info_type:
                    for pf in page_info_type.get("fields", []):
                        pf_name = pf.get("name")
                        if pf_name in {"has_next_page", "hasNextPage"}:
                            page_info_next_field_name = pf_name
                        elif pf_name in {"end_cursor", "endCursor"}:
                            page_info_cursor_field_name = pf_name
            supports_paginator = any(arg.get("name") == "paginator" for arg in args)
            collections.append(
                CollectionField(
                    name=field_name,
                    arguments=args,
                    container_type=return_type,
                    entity_type=entity_type,
                    entities_field_name=entities_field.get("name"),
                    page_info_field_name=page_info_field_name,
                    page_info_next_field_name=page_info_next_field_name,
                    page_info_cursor_field_name=page_info_cursor_field_name,
                    total_count_field_name=total_count_field.get("name") if total_count_field else None,
                    supports_paginator=supports_paginator,
                )
            )
        return collections


@dataclass
class CollectionField:
    """Information about a root query collection field."""

    name: str
    arguments: List[Dict[str, Any]]
    container_type: Dict[str, Any]
    entity_type: Dict[str, Any]
    entities_field_name: str
    page_info_field_name: Optional[str]
    page_info_next_field_name: Optional[str]
    page_info_cursor_field_name: Optional[str]
    total_count_field_name: Optional[str]
    supports_paginator: bool

    @property
    def supports_offset(self) -> bool:
        return any(arg.get("name") == "offset" for arg in self.arguments)

    @property
    def supports_limit(self) -> bool:
        return any(arg.get("name") in {"limit", "first"} for arg in self.arguments)

    @property
    def has_page_info(self) -> bool:
        return self.page_info_field_name is not None

    @property
    def has_total_count(self) -> bool:
        return self.total_count_field_name is not None


class SelectionBuilder:
    """Builds selection sets for a GraphQL type based on introspection."""

    def __init__(self, schema: GraphQLSchema, max_depth: int = 0):
        self.schema = schema
        self.max_depth = max_depth

    def build(self, type_name: str) -> str:
        visited: Set[str] = set()
        selection = self._build_for_type(type_name, depth=0, visited=visited)
        lines = ["__typename"] if selection else ["__typename"]
        if selection:
            lines.extend(selection)
        return "\n".join(lines)

    def _build_for_type(self, type_name: str, depth: int, visited: Set[str]) -> List[str]:
        type_def = self.schema.get_type(type_name)
        if not type_def:
            return []
        visited.add(type_name)
        lines: List[str] = []
        for field in type_def.get("fields", []):
            field_name = field.get("name")
            if not field_name:
                continue
            if self.schema.field_has_required_args(field):
                continue
            field_type, is_list = self.schema.resolve_named_type(field.get("type", {}))
            if not field_type:
                continue
            kind = field_type.get("kind")
            field_type_name = field_type.get("name")
            if kind in {"SCALAR"} or self.schema.is_scalar(field_type_name):
                lines.append(field_name)
            elif kind == "ENUM" or self.schema.is_enum(field_type_name):
                lines.append(field_name)
            elif kind in {"OBJECT", "INTERFACE"}:
                if depth >= self.max_depth:
                    continue
                if field_type_name in visited:
                    continue
                nested = self._build_for_type(field_type_name, depth + 1, visited)
                if nested:
                    nested_block = textwrap.indent("\n".join(nested), "  ")
                    lines.append(f"{field_name} {{\n{nested_block}\n}}")
            elif kind == "UNION":
                # Include typename for union; field-specific handling could be added later.
                lines.append(f"{field_name} {{ __typename }}")
            else:
                # Fallback for other kinds (INPUT_OBJECT etc.)
                continue
        visited.discard(type_name)
        return lines


class PostgresBackupWriter:
    """Persist GraphQL entities into a PostgreSQL database."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.conn = connect(database_url)
        self.conn.autocommit = True
        self._init_metadata()

    def close(self) -> None:
        try:
            self.conn.close()
        except Exception:  # pragma: no cover - best effort close
            pass

    def _init_metadata(self) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS backup_runs (
                    id TEXT PRIMARY KEY,
                    started_at TIMESTAMPTZ NOT NULL,
                    completed_at TIMESTAMPTZ,
                    status TEXT NOT NULL,
                    notes TEXT
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS backup_tables (
                    query_name TEXT PRIMARY KEY,
                    table_name TEXT NOT NULL,
                    last_run_id TEXT,
                    FOREIGN KEY(last_run_id) REFERENCES backup_runs(id)
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS backup_table_stats (
                    run_id TEXT NOT NULL,
                    query_name TEXT NOT NULL,
                    records BIGINT NOT NULL,
                    duration_seconds DOUBLE PRECISION,
                    PRIMARY KEY (run_id, query_name),
                    FOREIGN KEY(run_id) REFERENCES backup_runs(id)
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS backup_progress (
                    query_name TEXT PRIMARY KEY,
                    next_page INT NOT NULL,
                    per_page INT NOT NULL,
                    updated_at TIMESTAMPTZ NOT NULL,
                    run_id TEXT,
                    FOREIGN KEY(run_id) REFERENCES backup_runs(id)
                )
                """
            )

    def get_running_run(self) -> Optional[str]:
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM backup_runs WHERE status = %s ORDER BY started_at DESC LIMIT 1",
                ("running",),
            )
            row = cur.fetchone()
        return row[0] if row else None

    def get_completed_queries(self, run_id: str) -> Set[str]:
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT query_name FROM backup_table_stats WHERE run_id = %s",
                (run_id,),
            )
            rows = cur.fetchall()
        return {row[0] for row in rows}

    def start_run(self) -> Tuple[str, bool]:
        existing = self.get_running_run()
        if existing:
            logger.info("Resuming previous backup run %s", existing)
            return existing, True

        run_id = str(uuid.uuid4())
        started_at = datetime.utcnow()
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO backup_runs (id, started_at, status) VALUES (%s, %s, %s)",
                (run_id, started_at, "running"),
            )
        return run_id, False

    def complete_run(self, run_id: str, status: str = "completed", notes: Optional[str] = None) -> None:
        completed_at = datetime.utcnow()
        with self.conn.cursor() as cur:
            cur.execute(
                "UPDATE backup_runs SET completed_at = %s, status = %s, notes = %s WHERE id = %s",
                (completed_at, status, notes, run_id),
            )

    def ensure_table(self, query_name: str) -> str:
        table_name = _format_table_name(query_name)
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO backup_tables (query_name, table_name) VALUES (%s, %s)"
                " ON CONFLICT (query_name) DO NOTHING",
                (query_name, table_name),
            )
            cur.execute(
                sql.SQL(
                    """
                    CREATE TABLE IF NOT EXISTS {table} (
                        id TEXT PRIMARY KEY,
                        data JSONB NOT NULL,
                        fetched_at TIMESTAMPTZ NOT NULL
                    )
                    """
                ).format(table=sql.Identifier(table_name))
            )
        return table_name

    def write_entities(self, table_name: str, entities: Iterable[Dict[str, Any]]) -> int:
        now = datetime.utcnow()
        rows = []
        for entity in entities:
            entity_id = entity.get("id")
            if entity_id is None:
                json_blob = json.dumps(entity, sort_keys=True)
                entity_id = hashlib.sha256(json_blob.encode("utf-8")).hexdigest()
            rows.append((str(entity_id), Json(entity), now))
        if not rows:
            return 0
        with self.conn.cursor() as cur:
            cur.executemany(
                sql.SQL(
                    """
                    INSERT INTO {table} (id, data, fetched_at)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (id) DO UPDATE
                    SET data = EXCLUDED.data,
                        fetched_at = EXCLUDED.fetched_at
                    """
                ).format(table=sql.Identifier(table_name)),
                rows,
            )
        return len(rows)

    def mark_table_run(self, query_name: str, run_id: str) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                "UPDATE backup_tables SET last_run_id = %s WHERE query_name = %s",
                (run_id, query_name),
            )

    def record_table_stats(self, query_name: str, run_id: str, records: int, duration_seconds: float) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO backup_table_stats (run_id, query_name, records, duration_seconds)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (run_id, query_name)
                DO UPDATE SET records = EXCLUDED.records, duration_seconds = EXCLUDED.duration_seconds
                """,
                (run_id, query_name, records, duration_seconds),
            )

    def get_progress(self, query_name: str) -> Optional[Dict[str, Any]]:
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT next_page, per_page FROM backup_progress WHERE query_name = %s",
                (query_name,),
            )
            row = cur.fetchone()
        if not row:
            return None
        return {"next_page": row[0], "per_page": row[1]}

    def update_progress(self, query_name: str, next_page: int, per_page: int, run_id: str) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO backup_progress (query_name, next_page, per_page, updated_at, run_id)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (query_name)
                DO UPDATE SET next_page = EXCLUDED.next_page,
                              per_page = EXCLUDED.per_page,
                              updated_at = EXCLUDED.updated_at,
                              run_id = EXCLUDED.run_id
                """,
                (query_name, next_page, per_page, datetime.utcnow(), run_id),
            )

    def clear_progress(self, query_name: str) -> None:
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM backup_progress WHERE query_name = %s", (query_name,))


class SonarGraphQLBackup:
    """Coordinates full GraphQL backup into PostgreSQL."""

    def __init__(
        self,
        client: Optional[SonarGraphQLClient] = None,
        database_url: Optional[str] = None,
        page_size: int = 200,
        max_depth: int = 0,
        sample_size: Optional[int] = None,
        request_timeout: float = 30.0,
        rate_limit_delay: float = 5.0,
        rate_limit_retries: int = 5,
        include: Optional[Set[str]] = None,
        exclude: Optional[Set[str]] = None,
        thread_pool_size: int = 1,
    ) -> None:
        self.request_timeout = request_timeout
        if client is None:
            self.client = SonarGraphQLClient(config, request_timeout=request_timeout)
        else:
            self.client = client
            if hasattr(self.client, "request_timeout"):
                self.client.request_timeout = request_timeout
        if not database_url:
            raise ValueError("database_url must be provided for PostgreSQL backups")
        self.database_url = database_url
        self.database_label = _redact_database_url(database_url)
        self.page_size = page_size
        self.max_depth = max_depth
        self.sample_size = sample_size
        self.rate_limit_delay = rate_limit_delay
        self.rate_limit_retries = max(1, rate_limit_retries)
        self.include = include
        self.exclude = exclude or set()
        self.thread_pool_size = max(1, thread_pool_size)
        self.schema: Optional[GraphQLSchema] = None
        self.primary_writer = PostgresBackupWriter(database_url)
        self._thread_local: threading.local = threading.local()
        self._worker_writers: Set[PostgresBackupWriter] = set()
        self._worker_writers_lock = threading.Lock()

    def load_schema(self) -> None:
        logger.info("Fetching GraphQL schema via introspection...")
        schema_data = self.client.get_schema_info()
        self.schema = GraphQLSchema(schema_data)
        logger.info(f"GraphQL schema loaded: {len(self.schema.type_map)} types")

    def _get_worker_writer(self) -> PostgresBackupWriter:
        if self.thread_pool_size == 1:
            return self.primary_writer
        writer = getattr(self._thread_local, "writer", None)
        if writer is None:
            writer = PostgresBackupWriter(self.database_url)
            self._thread_local.writer = writer
            with self._worker_writers_lock:
                self._worker_writers.add(writer)
        return writer

    def _close_worker_writers(self) -> None:
        writers: List[PostgresBackupWriter] = []
        with self._worker_writers_lock:
            writers.extend(self._worker_writers)
            self._worker_writers.clear()
        for writer in writers:
            writer.close()
        self.primary_writer.close()


    def run(self) -> None:
        if not self.schema:
            self.load_schema()
        assert self.schema is not None
        selection_builder = SelectionBuilder(self.schema, max_depth=self.max_depth)
        collection_fields = self.schema.discover_collection_fields()
        logger.info(f"Discovered {len(collection_fields)} collection queries")

        if self.include:
            collection_fields = [cf for cf in collection_fields if cf.name in self.include]
        if self.exclude:
            collection_fields = [cf for cf in collection_fields if cf.name not in self.exclude]
        if not self.include:
            skipped_logs = [cf.name for cf in collection_fields if "log" in cf.name.lower()]
            if skipped_logs:
                logger.info(
                    "Skipping %s log collection(s); use --include to back them up", len(skipped_logs)
                )
                collection_fields = [cf for cf in collection_fields if cf.name not in skipped_logs]

        run_id, resuming_run = self.primary_writer.start_run()
        logger.info(
            "Backup run {} started (writing to {})",
            run_id,
            self.database_label,
        )

        completed_queries: Set[str] = set()
        if resuming_run:
            completed_queries = self.primary_writer.get_completed_queries(run_id)
            if completed_queries:
                logger.info(
                    f"Skipping {len(completed_queries)} previously completed collection(s)"
                )

        collections_to_process: List[CollectionField] = []
        for collection in collection_fields:
            if collection.name in completed_queries:
                logger.info(
                    f"Skipping {collection.name}; already completed in run {run_id}"
                )
                continue
            collections_to_process.append(collection)

        try:
            if self.thread_pool_size > 1 and collections_to_process:
                logger.info(
                    "Backing up %s collections with thread pool size %s",
                    len(collections_to_process),
                    self.thread_pool_size,
                )
                with ThreadPoolExecutor(max_workers=self.thread_pool_size) as executor:
                    futures = [
                        executor.submit(
                            self._backup_collection,
                            collection,
                            selection_builder,
                            run_id,
                        )
                        for collection in collections_to_process
                    ]
                    for future in as_completed(futures):
                        future.result()
            else:
                for collection in collections_to_process:
                    self._backup_collection(collection, selection_builder, run_id)
            self.primary_writer.complete_run(run_id, status="completed")
            logger.info(f"Backup run {run_id} completed")
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.exception(f"GraphQL backup failed: {exc}")
            self.primary_writer.complete_run(run_id, status="failed", notes=str(exc))
            raise
        finally:
            if self.thread_pool_size > 1:
                self._close_worker_writers()

    def _backup_collection(
        self,
        collection: CollectionField,
        selection_builder: SelectionBuilder,
        run_id: str,
    ) -> None:
        query_name = collection.name
        logger.info(f"Backing up query '{query_name}'")
        selection = selection_builder.build(collection.entity_type["name"])
        query_alias = f"backup_{query_name}"
        writer = self._get_worker_writer()

        query_with_page_info = self._build_collection_query(
            collection, query_alias, selection, include_page_info=True
        )
        query_without_page_info = self._build_collection_query(
            collection, query_alias, selection, include_page_info=False
        )

        total_downloaded = 0
        table_name: Optional[str] = None
        started_at = datetime.utcnow()
        per_page = self.page_size
        if self.sample_size is not None:
            per_page = min(per_page, max(1, self.sample_size))
        current_page = 1
        resume_progress: Optional[Dict[str, Any]] = None
        if collection.supports_paginator:
            resume_progress = writer.get_progress(query_name)
            if resume_progress:
                current_page = max(1, int(resume_progress.get("next_page", 1)))
                stored_per_page = int(resume_progress.get("per_page", per_page))
                if stored_per_page > 0:
                    per_page = stored_per_page
                logger.info(
                    f"Resuming {query_name} at page {current_page} (per_page={per_page})"
                )
        use_page_info = collection.has_page_info
        rate_limit_attempts = 0
        successfully_completed = False
        while True:
            variables = {}
            if collection.supports_paginator:
                variables = {"page": current_page, "per_page": per_page}

            query_to_run = (
                query_with_page_info if use_page_info else query_without_page_info
            )

            response = self.client.execute_query(query_to_run, variables or None)
            if not response.success:
                if _is_rate_limit_error(response.errors):
                    rate_limit_attempts += 1
                    if rate_limit_attempts > self.rate_limit_retries:
                        logger.error(
                            "Query %s hit rate limits %s times; aborting",
                            query_name,
                            rate_limit_attempts,
                        )
                        break
                    logger.warning(
                        "Query %s rate limited (attempt %s/%s); sleeping %.1fs",
                        query_name,
                        rate_limit_attempts,
                        self.rate_limit_retries,
                        self.rate_limit_delay,
                    )
                    time.sleep(self.rate_limit_delay)
                    continue
                if use_page_info and self._should_retry_without_page_info(response.errors):
                    logger.warning(
                        "Query %s failed due to page_info aggregation; retrying without page_info",
                        query_name,
                    )
                    use_page_info = False
                    continue
                logger.error(
                    "Query %s failed after retries: %s",
                    query_name,
                    response.errors,
                )
                break

            rate_limit_attempts = 0

            if not response.data:
                logger.error("Query %s returned no data payload", query_name)
                break
            container = response.data.get(query_name)
            if not container:
                logger.warning(f"Query {query_name} response missing container")
                break
            entities = container.get(collection.entities_field_name, [])
            if not entities:
                logger.info(
                    f"No more entities for {query_name} (downloaded {total_downloaded} total)"
                )
                successfully_completed = True
                break
            if total_downloaded == 0:
                table_name = writer.ensure_table(query_name)
            assert table_name is not None
            written = writer.write_entities(table_name, entities)
            total_downloaded += written
            logger.info(
                f"Stored {written} entities from {query_name} (cumulative {total_downloaded})"
            )

            if collection.supports_paginator:
                writer.update_progress(query_name, current_page + 1, per_page, run_id)

            if self.sample_size is not None and total_downloaded >= self.sample_size:
                logger.info(
                    "Reached sample size %s for %s; stopping early",
                    self.sample_size,
                    query_name,
                )
                successfully_completed = True
                break

            if use_page_info and collection.has_page_info:
                page_info = container.get(collection.page_info_field_name) or {}
                logger.debug(
                    f"Page info for {query_name}: {{'page': {page_info.get('page')}, 'total_pages': {page_info.get('total_pages')}, 'records_per_page': {page_info.get('records_per_page')}, 'total_count': {page_info.get('total_count')}}}"
                )
                if collection.supports_paginator:
                    total_pages = page_info.get("total_pages")
                    records_per_page = page_info.get("records_per_page")
                    if isinstance(records_per_page, int) and records_per_page > 0:
                        per_page = records_per_page
                    if isinstance(total_pages, int) and total_pages > 0:
                        if current_page >= total_pages:
                            successfully_completed = True
                            break
                    elif written < per_page:
                        successfully_completed = True
                        break
                    current_page += 1
                    continue
            elif collection.supports_paginator:
                if written < per_page:
                    successfully_completed = True
                    break
                current_page += 1
                continue

            # Non-paginated paths exit after first batch
            successfully_completed = True
            break

        logger.info(f"Finished backing up {query_name} ({total_downloaded} records)")
        duration = (datetime.utcnow() - started_at).total_seconds()
        writer.record_table_stats(query_name, run_id, total_downloaded, duration)
        if successfully_completed:
            if collection.supports_paginator:
                writer.clear_progress(query_name)
            writer.mark_table_run(query_name, run_id)
        else:
            logger.warning(
                "Backup for %s exited early; progress stored for resume",
                query_name,
            )

    def _build_collection_query(
        self,
        collection: CollectionField,
        query_alias: str,
        selection: str,
        include_page_info: bool,
    ) -> str:
        formatted_selection = selection.replace("\n", "\n      ")
        arg_definitions: List[str] = []
        arg_calls: List[str] = []
        if collection.supports_paginator:
            arg_definitions.extend(["$page: Int!", "$per_page: Int!"])
            arg_calls.append("paginator: { page: $page, records_per_page: $per_page }")

        args_clause = ", ".join(arg_definitions)
        query_header = f"query {query_alias}"
        if args_clause:
            query_header += f"({args_clause})"

        container_lines = [
            f"    {collection.entities_field_name} {{",
            f"      {formatted_selection}",
            "    }",
        ]
        if include_page_info and collection.has_page_info:
            pi_lines = [f"    {collection.page_info_field_name} {{"]
            for field_name in ["page", "total_pages", "total_count", "records_per_page"]:
                pi_lines.append(f"      {field_name}")
            if collection.page_info_next_field_name:
                pi_lines.append(f"      {collection.page_info_next_field_name}")
            if collection.page_info_cursor_field_name:
                pi_lines.append(f"      {collection.page_info_cursor_field_name}")
            pi_lines.append("    }")
            container_lines.extend(pi_lines)
        if include_page_info and collection.has_total_count:
            container_lines.append(f"    {collection.total_count_field_name}")

        args_invocation = ", ".join(arg_calls)
        if args_invocation:
            return (
                f"{query_header} {{\n"
                f"  {collection.name}({args_invocation}) {{\n"
                + "\n".join(container_lines)
                + "\n  }\n}"
            )
        return (
            f"{query_header} {{\n"
            f"  {collection.name} {{\n"
            + "\n".join(container_lines)
            + "\n  }\n}"
        )

    @staticmethod
    def _should_retry_without_page_info(errors: Optional[List[Dict[str, Any]]]) -> bool:
        if not errors:
            return False
        for error in errors:
            message = (error or {}).get("message", "").lower()
            if "aggregat" in message or "does not exist" in message:
                return True
        return False


__all__ = [
    "SonarGraphQLBackup",
    "GraphQLSchema",
    "SelectionBuilder",
    "PostgresBackupWriter",
]


def _is_rate_limit_error(errors: Optional[List[Dict[str, Any]]]) -> bool:
    if not errors:
        return False
    for error in errors:
        message = str((error or {}).get("message", "")).lower()
        if "rate limit" in message or "too many" in message or "429" in message:
            return True
    return False
