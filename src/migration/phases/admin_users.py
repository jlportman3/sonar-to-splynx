"""Import Sonar administrators into Splynx and assign roles."""

from __future__ import annotations

import json
import os
import secrets
import string
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from dotenv import load_dotenv
from psycopg import connect
from psycopg.rows import dict_row

from src.apis.splynx_client import SplynxAPIClient, SplynxConfig
from src.config.settings import config
from src.migration.utils.user_filters import normalize_login, should_skip_user
from src.utils.logger import get_logger

logger = get_logger("admin_user_import")

_CONFIG_PATH = Path("config/role_map.json")
_REPORT_DIR = Path("reports/splynx")
_BACKUP_USERS_TABLE = "graphql_backup__users"
_BACKUP_ROLES_TABLE = "graphql_backup__roles"


@dataclass
class ImportResult:
    created: List[Dict[str, str]]
    skipped: List[Tuple[str, str]]
    failed: List[Tuple[str, str]]


def _load_role_overrides() -> Dict[str, str]:
    if not _CONFIG_PATH.exists():
        return {}
    try:
        with _CONFIG_PATH.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        return {key.lower(): value for key, value in data.items() if isinstance(value, str)}
    except json.JSONDecodeError as exc:
        logger.warning(f"Failed to parse %s: %s", _CONFIG_PATH, exc)
        return {}


def _slugify_role(name: Optional[str]) -> str:
    value = (name or "").strip().lower()
    slug = "".join(ch if ch.isalnum() else "_" for ch in value)
    slug = slug.strip("_")
    return slug or "role"


def _generate_password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + "!@$%*?"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def _resolve_role_mapping(backup_url: str) -> Dict[str, str]:
    overrides = _load_role_overrides()
    mapping: Dict[str, str] = {}
    with connect(backup_url, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT data->>'id' AS id, data->>'name' AS name FROM {_BACKUP_ROLES_TABLE}"
            )
            for row in cur.fetchall():
                role_id = row["id"]
                role_name = row["name"] or "role"
                slug = _slugify_role(role_name)
                mapped = overrides.get(slug, slug)
                mapping[role_id] = mapped
    return mapping


def _fetch_sonar_users(backup_url: str) -> List[Dict[str, str]]:
    with connect(backup_url, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT data FROM {_BACKUP_USERS_TABLE}")
            return [row["data"] if "data" in row else row[0] for row in cur.fetchall()]


def _build_splynx_client() -> SplynxAPIClient:
    if not config.splynx_url or not (config.splynx_api_key or config.splynx_username):
        raise RuntimeError("Splynx credentials are not configured in the environment")
    api_key = config.splynx_api_key or config.splynx_username
    api_secret = config.splynx_password or config.splynx_api_key or config.splynx_password
    splynx_cfg = SplynxConfig(
        base_url=config.splynx_url,
        api_key=api_key,
        api_secret=api_secret,
    )
    return SplynxAPIClient(splynx_cfg)


def _existing_admin_logins(client: SplynxAPIClient) -> Dict[str, Dict[str, str]]:
    response = client.list_administrators()
    if not response.get("success"):
        logger.warning("Unable to fetch existing administrators: %s", response.get("error"))
        return {}
    data = response.get("data") or []
    return {
        normalize_login(admin.get("login", "")): admin for admin in data if admin.get("login")
    }


def _determine_role_slug(user: Dict[str, any], role_map: Dict[str, str]) -> Optional[str]:
    if user.get("super_admin"):
        return "super-administrator"
    role_id = user.get("role_id")
    if role_id and role_id in role_map:
        return role_map[role_id]
    return None


def _prepare_payload(user: Dict[str, any], role_slug: str) -> Dict[str, any]:
    username = (user.get("username") or user.get("email_address") or "").strip()
    email = (user.get("email_address") or f"{username}@example.com").strip()
    name = user.get("name") or user.get("public_name") or username
    password = _generate_password()
    payload = {
        "login": username,
        "name": name,
        "email": email,
        "role_name": role_slug,
        "partner_id": 0,
        "password": password,
    }
    if user.get("language"):
        payload["language"] = user["language"]
    if user.get("mobile_number"):
        payload["phone"] = user["mobile_number"]
    return payload


def _write_report(created: List[Dict[str, str]]) -> Optional[Path]:
    if not created:
        return None
    _REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    report_path = _REPORT_DIR / f"imported_admins_{stamp}.csv"
    headers = ["login", "email", "role", "temporary_password"]
    lines = ["login,email,role,temporary_password"]
    for entry in created:
        lines.append(
            ",".join(
                entry.get(field, "").replace(",", " ") for field in headers
            )
        )
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def import_sonar_administrators() -> ImportResult:
    """Create Splynx administrators for Sonar users and assign mapped roles."""
    load_dotenv(Path(".env"))
    backup_url = os.getenv("BACKUP_DATABASE_URL")
    if not backup_url:
        raise RuntimeError("BACKUP_DATABASE_URL must be set to import administrators")

    role_map = _resolve_role_mapping(backup_url)
    logger.info("Resolved %s Sonar role(s) to Splynx slugs", len(role_map))

    sonar_users = _fetch_sonar_users(backup_url)
    logger.info("Fetched %s Sonar user record(s) from backup", len(sonar_users))

    client = _build_splynx_client()
    existing = _existing_admin_logins(client)
    logger.info("Found %s existing Splynx administrator(s)", len(existing))

    created: List[Dict[str, str]] = []
    skipped: List[Tuple[str, str]] = []
    failed: List[Tuple[str, str]] = []

    for user in sonar_users:
        username = user.get("username") or ""
        login = normalize_login(username)
        if not login:
            skipped.append((user.get("name") or "(unknown)", "missing username"))
            continue
        if not user.get("enabled", True):
            skipped.append((login, "user disabled"))
            continue
        if should_skip_user(username, existing.keys()):
            skipped.append((login, "already exists or filtered"))
            continue

        role_slug = _determine_role_slug(user, role_map)
        if not role_slug:
            skipped.append((login, "no mapped role"))
            continue

        payload = _prepare_payload(user, role_slug)
        response = client.create_administrator(payload)
        if response.get("success"):
            admin_id = response.get("data", {}).get("id")
            logger.info(
                "Created Splynx administrator %s with role %s (id=%s)",
                payload["login"],
                role_slug,
                admin_id,
            )
            existing[normalize_login(payload["login"])] = {"id": admin_id}
            created.append(
                {
                    "login": payload["login"],
                    "email": payload["email"],
                    "role": role_slug,
                    "temporary_password": payload["password"],
                }
            )
        else:
            error_text = json.dumps(response.get("error")) if response.get("error") else "unknown error"
            logger.error(
                "Failed to create administrator %s: %s", payload["login"], error_text
            )
            failed.append((payload["login"], error_text))

    report_path = _write_report(created)
    if report_path:
        logger.info("Wrote administrator import report to %s", report_path)

    logger.info(
        "Administrator import summary: created=%s, skipped=%s, failed=%s",
        len(created),
        len(skipped),
        len(failed),
    )

    return ImportResult(created=created, skipped=skipped, failed=failed)


__all__ = ["import_sonar_administrators", "ImportResult"]
