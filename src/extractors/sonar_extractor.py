
"""Data extractor for Sonar API."""

from typing import List, Dict, Any

from src.apis.sonar_rest_client import SonarRestClient
from src.config.settings import config
from src.utils.logger import get_logger
from src.utils.database import get_db_connection, create_table, insert_data

logger = get_logger(__name__)

class SonarExtractor:
    """Extracts data from the Sonar API."""

    def __init__(self, db_name: str = "sonar_data.db") -> None:
        """Initializes the SonarExtractor."""
        self.client = SonarRestClient(config)
        self.conn = get_db_connection(db_name)

    def _get_fields_from_data(self, data: List[Dict[str, Any]]) -> Dict[str, str]:
        """Infers field types from data."""
        if not data:
            return {}

        fields = {}
        for key, value in data[0].items():
            if isinstance(value, int):
                fields[key] = "INTEGER"
            elif isinstance(value, float):
                fields[key] = "REAL"
            elif isinstance(value, bool):
                fields[key] = "INTEGER"
            else:
                fields[key] = "TEXT"
        return fields

    def _save_to_sqlite(self, table_name: str, data: List[Dict[str, Any]]) -> None:
        """Saves data to a SQLite table."""
        if not data:
            logger.warning(f"No data to save for table {table_name}")
            return

        fields = self._get_fields_from_data(data)
        create_table(self.conn, table_name, fields)
        insert_data(self.conn, table_name, data)
        logger.info(f"Saved {len(data)} records to table {table_name}.")

    def extract_accounts(self) -> None:
        """Extracts all accounts from the Sonar REST API and saves them to SQLite."""
        logger.info("Extracting accounts from Sonar...")
        accounts = self.client.get_all_paginated_data("accounts")
        if accounts:
            self._save_to_sqlite("accounts", accounts)

    def extract_tickets(self) -> None:
        """Extracts all tickets from the Sonar REST API and saves them to SQLite."""
        logger.info("Extracting tickets from Sonar...")
        tickets = self.client.get_all_paginated_data("tickets")
        if tickets:
            self._save_to_sqlite("tickets", tickets)

    def extract_users(self) -> None:
        """Extracts all users from the Sonar REST API and saves them to SQLite."""
        logger.info("Extracting users from Sonar...")
        users = self.client.get_all_paginated_data("users")
        if users:
            self._save_to_sqlite("users", users)

    def extract_all_data(self) -> None:
        """Extracts all available data from the Sonar REST API and saves it to SQLite."""
        logger.info("Starting Sonar data extraction...")
        self.extract_accounts()
        self.extract_tickets()
        self.extract_users()
        logger.info("Sonar data extraction complete.")
