"""Extract Sonar security roles and permissions from the GraphQL backup."""

from __future__ import annotations

from typing import Dict, List, Optional

from psycopg import connect

_QUERY_NAMES = {
    "roles": "roles",
    "permissions": "permissions",
    "permission_categories": "permission_categories",
    "role_permissions": "role_permissions",
}


class SonarSecurityExtractor:
    """Reads roles/permissions from the backup Postgres database."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.conn = connect(database_url)
        self.conn.autocommit = True
        self._table_cache: Dict[str, str] = {}

    def close(self) -> None:
        try:
            self.conn.close()
        except Exception:  # pragma: no cover - defensive close
            pass

    def _lookup_table(self, query_name: str) -> Optional[str]:
        if query_name in self._table_cache:
            return self._table_cache[query_name]
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT table_name FROM backup_tables WHERE query_name = %s",
                (query_name,),
            )
            row = cur.fetchone()
        if row:
            table_name = row[0]
        else:
            table_name = f"graphql_backup__{query_name}"
        self._table_cache[query_name] = table_name
        return table_name

    def _fetch_collection(self, query_name: str) -> List[Dict]:
        table_name = self._lookup_table(query_name)
        if not table_name:
            return []
        with self.conn.cursor() as cur:
            try:
                cur.execute(f"SELECT data FROM {table_name}")
            except Exception:
                return []
            rows = cur.fetchall()
        return [row[0] for row in rows if row and isinstance(row[0], dict)]

    def fetch_roles(self) -> List[Dict]:
        return self._fetch_collection(_QUERY_NAMES["roles"])

    def fetch_permissions(self) -> List[Dict]:
        return self._fetch_collection(_QUERY_NAMES["permissions"])

    def fetch_permission_categories(self) -> List[Dict]:
        return self._fetch_collection(_QUERY_NAMES["permission_categories"])

    def fetch_role_permissions(self) -> List[Dict]:
        return self._fetch_collection(_QUERY_NAMES["role_permissions"])

