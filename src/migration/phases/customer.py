"""Customer phase migrations: ensure user import rules are respected."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv
from psycopg import connect

from src.migration.utils.user_filters import should_skip_user
from src.utils.logger import get_logger

logger = get_logger("customer_phase")

_SONAR_USERS_TABLE = "graphql_backup__users"


def load_env() -> None:
    load_dotenv(Path(".env"))


def _connect_backup():
    url = os.getenv("BACKUP_DATABASE_URL")
    if not url:
        raise RuntimeError("BACKUP_DATABASE_URL is not set")
    return connect(url)


def fetch_sonar_users() -> List[Dict[str, str]]:
    with _connect_backup() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT data FROM {_SONAR_USERS_TABLE}")
        return [row[0] for row in cur.fetchall()]


def fetch_splynx_admin_logins() -> List[str]:
    import subprocess

    user = os.getenv("SPLYNX_DB_USER")
    password = os.getenv("SPLYNX_DB_PASSWORD")
    database = os.getenv("SPLYNX_DB_NAME", "splynx")
    socket = os.getenv("SPLYNX_DB_SOCKET")
    host = os.getenv("SPLYNX_DB_HOST", "localhost")
    port = os.getenv("SPLYNX_DB_PORT", "3306")

    if not user or not password:
        raise RuntimeError("SPLYNX_DB_USER and SPLYNX_DB_PASSWORD must be set for user migration")

    command = ["mysql", "-u", user, f"-p{password}", "--batch", "--skip-column-names", "-e", "SELECT login FROM admins;"]
    if socket:
        command.extend(["-S", socket])
    else:
        command.extend(["-h", host, "-P", str(port)])
    command.append(database)

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to read Splynx admins: {result.stderr.strip()}")

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def run_customer_phase() -> None:
    """Dry-run customer user migration, applying skip rules."""
    load_env()
    sonar_users = fetch_sonar_users()
    existing_logins = fetch_splynx_admin_logins()

    skipped = 0
    candidates = []
    for record in sonar_users:
        login = record.get("login") or record.get("username")
        if should_skip_user(login, existing_logins):
            skipped += 1
            continue
        candidates.append(login)

    logger.info("Evaluated %s Sonar user(s)", len(sonar_users))
    logger.info("Existing Splynx admin logins: %s", existing_logins)
    logger.info("Skipped %s user(s) due to conflict or policy", skipped)
    logger.info("%s user(s) remain eligible for migration (creation not yet implemented)", len(candidates))
    if candidates:
        logger.debug("Eligible logins: %s", candidates)


__all__ = ["run_customer_phase"]
