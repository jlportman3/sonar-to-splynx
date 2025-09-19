"""Transform Sonar role and permission data into normalized entities."""

from __future__ import annotations

import re
from typing import Dict, Iterable, List, Tuple

from src.models.normalized_schema import (
    EntityType,
    NormalizedPermission,
    NormalizedRole,
    NormalizedRolePermission,
    MigrationStatus,
)

_slug_pattern = re.compile(r"[^a-z0-9]+")


def _slugify(value: str) -> str:
    value = (value or "").strip().lower()
    value = _slug_pattern.sub("_", value)
    return value.strip("_")


class RoleTransformer:
    """Convert raw Sonar role/permission records into normalized models."""

    def __init__(self, source_system: str = "sonar") -> None:
        self.source_system = source_system

    def transform(
        self,
        roles: Iterable[Dict],
        permissions: Iterable[Dict],
        permission_categories: Iterable[Dict],
        role_permissions: Iterable[Dict],
    ) -> Tuple[List[NormalizedRole], List[NormalizedPermission], List[NormalizedRolePermission]]:
        category_map = {
            str(category.get("id")): category.get("name", "uncategorized")
            for category in permission_categories
        }

        permission_entities: Dict[str, NormalizedPermission] = {}
        for record in permissions:
            permission_id = str(record.get("id"))
            if not permission_id:
                continue
            code = _slugify(record.get("name", permission_id))
            permission = NormalizedPermission(
                source_id=permission_id,
                entity_type=EntityType.PERMISSION,
                source_system=self.source_system,
                data={
                    'code': code,
                    'category': category_map.get(str(record.get("permission_category_id")), "uncategorized"),
                    'description': record.get("description") or "",
                    'is_active': bool(record.get("active", True)),
                    'additional_attributes': {
                        'raw_name': record.get("name"),
                    },
                },
            )
            permission.metadata['raw'] = record
            permission_entities[permission_id] = permission

        role_entities: Dict[str, NormalizedRole] = {}
        for record in roles:
            role_id = str(record.get("id"))
            if not role_id:
                continue
            role = NormalizedRole(
                source_id=role_id,
                entity_type=EntityType.ROLE,
                source_system=self.source_system,
                data={
                    'name': record.get("name", ""),
                    'description': record.get("description") or "",
                    'scope': record.get("scope") or "global",
                    'is_system': bool(record.get("system", False)),
                    'additional_attributes': {
                        'category': record.get("category"),
                    },
                },
            )
            role.metadata['raw'] = record
            role_entities[role_id] = role

        role_permission_entities: List[NormalizedRolePermission] = []
        for record in role_permissions:
            role_id = str(record.get("role_id"))
            permission_id = str(record.get("permission_id"))
            if role_id not in role_entities or permission_id not in permission_entities:
                continue
            bridge = NormalizedRolePermission(
                source_id=f"{role_id}:{permission_id}:{record.get('id')}",
                entity_type=EntityType.ROLE_PERMISSION,
                source_system=self.source_system,
                data={
                    'role_id': role_id,
                    'permission_id': permission_id,
                    'granted_at': record.get("created_at"),
                    'granted_by': str(record.get("created_by_user_id")) if record.get("created_by_user_id") else None,
                    'inherited_from': str(record.get("inherited_role_id")) if record.get("inherited_role_id") else None,
                    'additional_attributes': {},
                },
            )
            bridge.metadata['raw'] = record
            bridge.migration_status = MigrationStatus.TRANSFORMED
            role_permission_entities.append(bridge)

            role_entities[role_id].add_relationship(permission_id, "permission")
            permission_entities[permission_id].add_relationship(role_id, "role")

        for entity in role_entities.values():
            entity.migration_status = MigrationStatus.TRANSFORMED
        for entity in permission_entities.values():
            entity.migration_status = MigrationStatus.TRANSFORMED

        return (
            list(role_entities.values()),
            list(permission_entities.values()),
            role_permission_entities,
        )
