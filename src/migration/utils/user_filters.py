"""Utility helpers for deciding which users to migrate."""

from __future__ import annotations

from typing import Iterable

from src.utils.logger import get_logger

logger = get_logger("user_filters")


def normalize_login(login: str) -> str:
    """Lowercase trimmed login identifier."""
    return (login or "").strip().lower()


def should_skip_user(login: str, existing_splynx_logins: Iterable[str]) -> bool:
    """Return True if the Sonar user should not be migrated."""
    normalized_login = normalize_login(login)
    if not normalized_login:
        logger.warning("Skipping user with empty login")
        return True

    if normalized_login == "admin":
        logger.info("Skipping Sonar 'admin' account by policy")
        return True

    normalized_existing = {normalize_login(value) for value in existing_splynx_logins}
    if normalized_login in normalized_existing:
        logger.info("Skipping user %s; already present in Splynx", login)
        return True

    return False


__all__ = ["should_skip_user", "normalize_login"]
