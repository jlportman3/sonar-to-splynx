#!/usr/bin/env python3
"""Report Sonar GraphQL entity counts by collection."""

from __future__ import annotations

import math
from typing import Dict, Any, Tuple, List

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.apis.sonar_client import SonarGraphQLClient
from src.backup.sonar_graphql_backup import GraphQLSchema
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger

COUNT_PAGE_SIZE = 1000  # Sonar allows up to 1000 records per page


def main() -> None:
    setup_logger("INFO")
    logger = get_logger("sonar_counts")

    client = SonarGraphQLClient(config)
    schema_data = client.get_schema_info()
    schema = GraphQLSchema(schema_data)
    collections = schema.discover_collection_fields()
    logger.info(f"Discovered {len(collections)} collection queries")

    results: List[Tuple[str, int | None]] = []
    for collection in sorted(collections, key=lambda c: c.name):
        count = fetch_collection_count(client, collection, logger)
        results.append((collection.name, count))

    print("\nSonar Entity Counts")
    print("-------------------")
    width = max(len(name) for name, _ in results) + 2
    for name, count in results:
        count_str = str(count) if isinstance(count, int) else "n/a"
        print(f"{name.ljust(width)}{count_str}")


def fetch_collection_count(client: SonarGraphQLClient, collection, logger) -> int | None:
    """Attempt to read total_count via page_info; fall back to manual counting."""
    if collection.supports_paginator and collection.has_page_info:
        query = build_collection_query(collection, include_page_info=True, include_entities=False)
        response = client.execute_query(query, {"page": 1, "per_page": 1})
        if response.success and response.data:
            container = response.data.get(collection.name)
            if container:
                page_info = container.get(collection.page_info_field_name) or {}
                total = page_info.get("total_count")
                if isinstance(total, int):
                    return total
        else:
            if response.errors:
                logger.debug(
                    f"total_count lookup failed for {collection.name}: {response.errors}"
                )

    # Fallback: page through entities counting manually
    per_page = COUNT_PAGE_SIZE if collection.supports_paginator else None
    page = 1
    total = 0
    while True:
        variables: Dict[str, Any] | None = None
        if collection.supports_paginator:
            variables = {"page": page, "per_page": per_page}
        query = build_collection_query(collection, include_page_info=False, include_entities=True)
        response = client.execute_query(query, variables)
        if not response.success or not response.data:
            logger.warning(
                f"Count query failed for {collection.name} (page {page}): {response.errors}"
            )
            if response.errors:
                for error in response.errors:
                    logger.debug(f"  error detail: {error}")
            return None
        container = response.data.get(collection.name)
        if not container:
            logger.warning(f"{collection.name} returned no container on page {page}")
            return None
        entities = container.get(collection.entities_field_name, [])
        batch_count = len(entities)
        total += batch_count
        if not collection.supports_paginator:
            break
        if batch_count < (per_page or 0):
            break
        page += 1
    return total


def build_collection_query(collection, include_page_info: bool, include_entities: bool) -> str:
    args_def = []
    args_call = []
    if collection.supports_paginator:
        args_def.extend(["$page: Int!", "$per_page: Int!"])
        args_call.append("paginator: { page: $page, records_per_page: $per_page }")
    elif collection.supports_limit:
        args_def.extend(["$limit: Int!", "$offset: Int!"])
        args_call.append("limit: $limit")
        if collection.supports_offset:
            args_call.append("offset: $offset")

    args_clause = f"({', '.join(args_def)})" if args_def else ""
    call_clause = f"({', '.join(args_call)})" if args_call else ""

    body_lines = []
    if include_entities:
        body_lines.append(
            "    " + collection.entities_field_name + " { __typename }"
        )
    if include_page_info and collection.has_page_info:
        pi_field = collection.page_info_field_name
        body_lines.append(
            "    "
            + pi_field
            + " { total_count total_pages page records_per_page }"
        )
    if include_page_info and collection.has_total_count and not collection.has_page_info:
        body_lines.append(
            "    " + collection.total_count_field_name
        )

    body = "\n".join(body_lines) if body_lines else "    __typename"
    query = (
        f"query Count_{collection.name}{args_clause} {{\n"
        f"  {collection.name}{call_clause} {{\n"
        f"{body}\n"
        "  }\n"
        "}"
    )
    return query


if __name__ == "__main__":
    main()
