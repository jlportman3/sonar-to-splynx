
"""Database utilities for SQLite."""

import sqlite3
from typing import List, Dict, Any

from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_db_connection(db_name: str = "sonar_data.db") -> sqlite3.Connection:
    """Creates a connection to the SQLite database."""
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(conn: sqlite3.Connection, table_name: str, fields: Dict[str, str]) -> None:
    """Creates a table in the database."""
    # Sanitize table name
    table_name = "".join(c for c in table_name if c.isalnum() or c == '_')

    columns = ", ".join([f'"{key}" {value}' for key, value in fields.items()])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    logger.debug(f"Executing SQL: {create_table_sql}")
    conn.execute(create_table_sql)

def insert_data(conn: sqlite3.Connection, table_name: str, data: List[Dict[str, Any]]) -> None:
    """Inserts data into a table."""
    if not data:
        return

    # Sanitize table name
    table_name = "".join(c for c in table_name if c.isalnum() or c == '_')

    placeholders = ", ".join([":" + key for key in data[0].keys()])
    columns = ", ".join([f'"{key}"' for key in data[0].keys()])
    insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    logger.debug(f"Executing SQL: {insert_sql}")
    conn.executemany(insert_sql, data)
    conn.commit()
