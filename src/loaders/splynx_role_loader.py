"""Splynx loader for security roles and permissions (stub implementation)."""

from __future__ import annotations

from typing import Iterable, List

from src.apis.splynx_client import SplynxAPIClient
from src.models.normalized_schema import (
    NormalizedPermission,
    NormalizedRole,
    NormalizedRolePermission,
)
from src.utils.logger import get_logger

logger = get_logger("splynx_role_loader")


class SplynxRoleLoader:
    """Synchronize normalized roles and permissions into Splynx.

    Current implementation focuses on diff reporting; API write methods are
    intentionally stubbed until final mapping is approved.
    """

    def __init__(self, client: SplynxAPIClient) -> None:
        self.client = client

    def plan_changes(
        self,
        roles: Iterable[NormalizedRole],
        permissions: Iterable[NormalizedPermission],
        assignments: Iterable[NormalizedRolePermission],
    ) -> None:
        """Log the intended changes without applying them."""
        role_list: List[NormalizedRole] = list(roles)
        permission_list: List[NormalizedPermission] = list(permissions)
        assignment_list: List[NormalizedRolePermission] = list(assignments)

        logger.info(
            "Planned synchronization: roles=%s permissions=%s assignments=%s",
            len(role_list),
            len(permission_list),
            len(assignment_list),
        )
        for role in role_list:
            logger.debug("Role %s -> %s", role.source_id, role.data)
        for permission in permission_list:
            logger.debug("Permission %s -> %s", permission.source_id, permission.data)
        for mapping in assignment_list:
            logger.debug("RolePermission %s -> %s", mapping.source_id, mapping.data)

    def apply(self, *args, **kwargs) -> None:
        """Placeholder for future implementation."""
        raise NotImplementedError("Splynx role loader not yet implemented")

