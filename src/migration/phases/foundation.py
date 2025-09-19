"""Foundation phase migrations: company info, custom fields, roles/permissions."""

from __future__ import annotations

import json
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

from dotenv import load_dotenv
from psycopg import connect

from src.extractors.sonar_security_extractor import SonarSecurityExtractor
from src.models.normalized_schema import (
    NormalizedPermission,
    NormalizedRole,
    NormalizedRolePermission,
)
from src.transformers.role_transformer import RoleTransformer
from src.apis.splynx_client import SplynxAPIClient, SplynxConfig
from src.config.settings import config
from src.utils.logger import get_logger

logger = get_logger("foundation_phase")

# ---------------------------------------------------------------------------
# Shared utilities


def load_env() -> None:
    load_dotenv(Path(".env"))


def _get_splynx_client() -> SplynxAPIClient:
    if not config.splynx_url:
        raise RuntimeError("SPLYNX_URL must be configured to update permissions")
    api_key = config.splynx_api_key or config.splynx_username
    api_secret = config.splynx_password or config.splynx_api_key
    if not api_key or not api_secret:
        raise RuntimeError("Splynx API credentials are not fully configured")
    splynx_cfg = SplynxConfig(
        base_url=config.splynx_url,
        api_key=api_key,
        api_secret=api_secret,
    )
    return SplynxAPIClient(splynx_cfg)


# ---------------------------------------------------------------------------
# Company migration helpers

_COMPANY_BACKUP_TABLE = "graphql_backup__companies"
_COMPANY_TARGET_TABLE = "finance_template_values"


def _connect_backup() -> Tuple[str, str]:
    url = os.getenv("BACKUP_DATABASE_URL")
    if not url:
        raise RuntimeError("BACKUP_DATABASE_URL is not set")
    return url, os.getenv("BACKUP_DB_NAME", "sonar_backup")


def _fetch_sonar_company() -> Dict[str, str]:
    url, _ = _connect_backup()
    with connect(url) as conn, conn.cursor() as cur:
        cur.execute(f"SELECT data FROM {_COMPANY_BACKUP_TABLE} LIMIT 1")
        row = cur.fetchone()
        if not row:
            raise RuntimeError("No company record found in Sonar backup")
        return row[0]


def _run_mysql_query(sql: str) -> List[List[str]]:
    user = os.getenv("SPLYNX_DB_USER")
    password = os.getenv("SPLYNX_DB_PASSWORD")
    if not user or not password:
        raise RuntimeError("SPLYNX_DB_USER/PASSWORD must be set in .env")

    database = os.getenv("SPLYNX_DB_NAME", "splynx")
    socket = os.getenv("SPLYNX_DB_SOCKET")
    host = os.getenv("SPLYNX_DB_HOST", "localhost")
    port = os.getenv("SPLYNX_DB_PORT", "3306")

    command = ["mysql", "-u", user, "--batch", "--skip-column-names", "-e", sql, database]
    if socket:
        command.extend(["-S", socket])
    else:
        command.extend(["-h", host, "-P", str(port)])

    env = os.environ.copy()
    env["MYSQL_PWD"] = password

    result = subprocess.run(command, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise RuntimeError(f"MySQL query failed: {result.stderr.strip()}\nSQL: {sql}")

    rows: List[List[str]] = []
    for line in result.stdout.strip().splitlines():
        if not line:
            continue
        rows.append(line.split("\t"))
    return rows


def _get_company_ids() -> List[int]:
    rows = _run_mysql_query(f"SELECT id FROM {_COMPANY_TARGET_TABLE};")
    if not rows:
        return [0]
    return [int(row[0]) for row in rows]


def _fetch_existing_company(row_id: int) -> Optional[Dict[str, str]]:
    columns = [
        "company_name",
        "street_1",
        "street_2",
        "zip",
        "city",
        "country",
        "iso_country",
        "email",
        "phone",
        "company_id",
        "company_vat",
        "bank_account",
        "bank_name",
        "bank_address",
        "splynx_url",
    ]
    rows = _run_mysql_query(
        f"SELECT {', '.join(columns)} FROM {_COMPANY_TARGET_TABLE} WHERE id={row_id};"
    )
    if not rows:
        return None
    values = rows[0]
    return dict(zip(columns, values))


def _update_company_row(company: Dict[str, str], row_id: int) -> None:
    existing = _fetch_existing_company(row_id) or {}
    field_map = {
        "company_name": company.get("name") or existing.get("company_name", ""),
        "street_1": company.get("street_1") or existing.get("street_1", ""),
        "street_2": company.get("street_2") or existing.get("street_2", ""),
        "zip": company.get("zip") or existing.get("zip", ""),
        "city": company.get("city") or existing.get("city", ""),
        "country": company.get("country") or existing.get("country", ""),
        "iso_country": company.get("country") or existing.get("iso_country", "US"),
        "email": company.get("support_email") or existing.get("email", ""),
        "phone": company.get("phone_number") or existing.get("phone", ""),
        "company_id": company.get("company_id") or existing.get("company_id", ""),
        "company_vat": company.get("tax_identification") or existing.get("company_vat", ""),
        "bank_account": company.get("bank_account") or existing.get("bank_account", ""),
        "bank_name": company.get("bank_name") or existing.get("bank_name", ""),
        "bank_address": company.get("bank_address") or existing.get("bank_address", ""),
        "splynx_url": company.get("customer_portal_url") or existing.get("splynx_url", ""),
    }

    assignments_parts = []
    for column, value in field_map.items():
        sanitized = (value or "").replace("'", "''")
        assignments_parts.append(f"{column}='{sanitized}'")
    assignments = ", ".join(assignments_parts)
    sql = f"UPDATE {_COMPANY_TARGET_TABLE} SET {assignments} WHERE id={row_id};"
    _run_mysql_query(sql)


def migrate_company() -> None:
    logger.info("Updating Splynx company profile from Sonar backup")
    company = _fetch_sonar_company()
    ids = _get_company_ids()
    for row_id in ids:
        _update_company_row(company, row_id)
    logger.info(f"Updated {len(ids)} company record(s)")


# ---------------------------------------------------------------------------
# Custom field migration helpers

_CUSTOM_FIELDS_TABLE = "graphql_backup__custom_fields"
_CUSTOM_FIELD_DATA_TABLE = "graphql_backup__custom_field_data"
_SONAR_FIELD_ENTITY = "Account"

_FIELDS_TABLE = "customers_fields"
_VALUES_TABLE = "customers_values"

_FIELD_COLUMNS = [
    "name",
    "module",
    "category",
    "title",
    "type",
    "position",
    "default_value",
    "min_length",
    "max_length",
    "select_values",
    "decimals",
    "relation_module",
    "addon",
    "addon_uri",
    "addon_input_type",
    "deleted",
    "show_in_list",
    "is_required",
    "is_unique",
    "is_add",
    "searchable",
    "readonly",
    "hidden",
    "disabled",
]

_DEFAULT_FIELD_VALUES = {
    "category": "0",
    "default_value": "",
    "min_length": "",
    "max_length": "",
    "select_values": "",
    "decimals": "2",
    "relation_module": "",
    "addon": "",
    "addon_uri": "",
    "addon_input_type": "",
    "deleted": "0",
    "show_in_list": "0",
    "is_add": "1",
    "searchable": "0",
    "readonly": "0",
    "hidden": "0",
    "disabled": "0",
}

_TYPE_MAP = {
    "TEXT": "string",
}


_SKIP_ROLE_SLUGS = {
    "portal",
    "portalv2",
    "batcher",
    "minim",
    "netflow_on_premises",
    "serge",
    "no_permissions",
}

_FALLBACK_ROLE_SLUGS = {"preseem", "serverplus"}


def _load_role_permission_codes_from_csv() -> Dict[str, List[str]]:
    base_dir = Path("zips")
    if not base_dir.exists():
        logger.warning("No zips directory found for role permission fallback")
        return {}
    candidates = sorted((p for p in base_dir.iterdir() if p.is_dir()), reverse=True)
    fallback: Dict[str, List[str]] = {}
    import csv

    processed_files: List[Path] = []
    for candidate in candidates:
        file_path = candidate / "roles.csv"
        if not file_path.exists():
            continue
        processed_files.append(file_path)
        try:
            with file_path.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    name = row.get("name") or ""
                    slug = _slugify(name)
                    perms_raw = row.get("applied permissions") or "[]"
                    try:
                        codes = json.loads(perms_raw)
                    except json.JSONDecodeError:
                        logger.warning(f"Unable to parse permissions for role {name}")
                        continue
                    codes = [str(code).strip().lower() for code in codes if str(code).strip()]
                    if not codes:
                        continue
                    if slug in _FALLBACK_ROLE_SLUGS and slug not in fallback:
                        fallback[slug] = codes
        except Exception as exc:  # pragma: no cover - defensive
            logger.exception(f"Failed loading fallback permissions from {file_path}: {exc}")

    if not fallback:
        logger.warning("roles.csv not found in zips directory for fallback permissions")
    else:
        logger.debug(
            f"Loaded fallback permissions for {len(fallback)} role(s) from files: {processed_files}"
        )
    return fallback


def _load_role_mapping() -> Dict[str, str]:
    mapping_path = Path("config/role_map.json")
    if not mapping_path.exists():
        return {}
    with mapping_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return {key.lower(): value for key, value in data.items() if isinstance(value, str)}


def _apply_roles_to_splynx(
    normalized_roles: Iterable[NormalizedRole],
) -> Tuple[Dict[str, str], Set[str]]:
    existing_rows = _run_mysql_query("SELECT name, title FROM roles;")
    existing = {row[0]: row[1] for row in existing_rows}

    default_roles = {
        "administrator",
        "customer-creator",
        "engineer",
        "financial-manager",
        "manager",
        "super-administrator",
        "technician",
    }

    role_mapping = _load_role_mapping()

    created = 0
    created_slugs: Set[str] = set()
    mapped_existing = 0
    role_map: Dict[str, str] = {}

    for entity in normalized_roles:
        name_value = entity.data.get("name") or entity.metadata.get("raw", {}).get("name") or entity.source_id
        title_value = entity.data.get("description") or entity.data.get("name") or name_value
        base_slug = _slugify(name_value)

        if base_slug in _SKIP_ROLE_SLUGS:
            logger.info(
                f"Skipping Sonar role {name_value} (slug={base_slug}); configured to ignore"
            )
            continue

        slug = role_mapping.get(base_slug, base_slug)
        title_formatted = title_value.strip() or slug.replace("_", " ").title()
        is_system = entity.data.get("is_system", False)
        is_base = "1" if is_system else "0"

        if slug in existing:
            logger.debug("Role %s already exists in Splynx; preserving existing title", slug)
            mapped_existing += 1
            role_map[entity.source_id] = slug
            continue

        if slug in default_roles:
            logger.info(
                "Role %s maps to existing Splynx role '%s'; skipping creation",
                name_value,
                slug,
            )
            mapped_existing += 1
            role_map[entity.source_id] = slug
            continue

        sanitized_title = title_formatted.replace("'", "''")
        _run_mysql_query(
            f"INSERT INTO roles (name, title, is_base) VALUES ('{slug}', '{sanitized_title}', '{is_base}');"
        )
        created += 1
        role_map[entity.source_id] = slug
        created_slugs.add(slug)

    logger.info(
        f"Applied roles to Splynx: created={created}, mapped_to_existing={mapped_existing}"
    )
    return role_map, created_slugs


def _load_permission_mapping() -> Dict[str, List[Dict[str, str]]]:
    mapping_path = Path("config/permissions_map.json")
    if not mapping_path.exists():
        logger.warning("permission map %s not found; skipping permission sync", mapping_path)
        return {}
    import json

    with mapping_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    normalized: Dict[str, List[Dict[str, str]]] = {}
    for code, entries in data.items():
        if not isinstance(entries, list):
            continue
        normalized[code] = []
        for entry in entries:
            module = entry.get("module", "admin")
            controller = entry.get("controller", "*")
            action = entry.get("action", "*")
            rule = entry.get("rule", "allow")
            normalized[code].append({
                "module": module,
                "controller": controller,
                "action": action,
                "rule": rule,
            })
    return normalized


def _derive_permission_rules(perm_slug: str, category: Optional[str]) -> List[Dict[str, str]]:
    slug = perm_slug.lower()
    category_slug = _slugify(category or "")
    hints = f"{slug} {category_slug}".strip()

    module = "administration"
    controller = "roles"

    mapping_hints = [
        ("customer", ("customers", "customer")),
        ("account", ("customers", "customer")),
        ("finance", ("finance", "finance")),
        ("billing", ("finance", "finance")),
        ("payment", ("finance", "payments")),
        ("invoice", ("finance", "invoices")),
        ("inventory", ("inventory", "items")),
        ("equipment", ("inventory", "items")),
        ("network", ("networking", "routers")),
        ("ip", ("networking", "ipv4")),
        ("support", ("support", "tickets")),
        ("ticket", ("support", "tickets")),
        ("administration", ("administration", "administrators")),
    ]

    for keyword, target in mapping_hints:
        if keyword in hints:
            module, controller = target
            break

    return [
        {
            "module": module,
            "controller": controller,
            "action": "*",
            "rule": "allow",
        }
    ]


def _apply_permissions_to_splynx(
    role_map: Dict[str, str],
    permission_map: Dict[str, str],
    permission_categories: Dict[str, str],
    assignments: Iterable[NormalizedRolePermission],
    fallback_code_map: Optional[Dict[str, List[str]]] = None,
    created_slugs: Optional[Set[str]] = None,
) -> None:
    mapping_config = _load_permission_mapping()
    if not mapping_config:
        logger.warning("No permission mapping available; skipping permission writes")
        return

    perms_by_role: Dict[str, Set[Tuple[str, str, str, str]]] = defaultdict(set)
    skipped = 0

    for assignment in assignments:
        role_source_id = assignment.data.get("role_id")
        perm_source_id = assignment.data.get("permission_id")
        if not role_source_id or not perm_source_id:
            continue
        role_slug = role_map.get(role_source_id)
        perm_slug = permission_map.get(perm_source_id)
        category = permission_categories.get(perm_source_id)
        if not role_slug or not perm_slug:
            skipped += 1
            continue
        target_rules = mapping_config.get(perm_slug)
        if not target_rules:
            target_rules = _derive_permission_rules(perm_slug, category)
        for rule in target_rules:
            module = rule["module"].replace("'", "''")
            controller = rule["controller"].replace("'", "''")
            action = rule["action"].replace("'", "''")
            rule_value = rule.get("rule", "allow").replace("'", "''")
            perms_by_role[role_slug].add((module, controller, action, rule_value))

    if fallback_code_map:
        target_slugs: Set[str] = set(created_slugs or [])
        if not target_slugs:
            target_slugs = {
                slug for slug in role_map.values() if slug in fallback_code_map
            }
        target_slugs = {slug for slug in target_slugs if slug in _FALLBACK_ROLE_SLUGS}
        if target_slugs:
            logger.debug(
                f"Applying fallback permissions for roles: {sorted(target_slugs)}"
            )
        for slug in target_slugs:
            codes = fallback_code_map.get(slug, [])
            logger.debug(f"Fallback codes for role '{slug}': {codes}")
            for code in codes:
                perm_slug = code.lower()
                target_rules = mapping_config.get(perm_slug)
                if not target_rules:
                    logger.warning(
                        f"No permission mapping for code '{perm_slug}' used by role '{slug}'"
                    )
                    continue
                for rule in target_rules:
                    module = rule["module"].replace("'", "''")
                    controller = rule["controller"].replace("'", "''")
                    action = rule["action"].replace("'", "''")
                    rule_value = rule.get("rule", "allow").replace("'", "''")
                    perms_by_role[slug].add((module, controller, action, rule_value))

    client = _get_splynx_client()
    updated_roles = 0
    total_rules = 0
    for slug, rule_set in perms_by_role.items():
        payload = [
            {
                "module": module,
                "controller": controller,
                "action": action,
                "rule": rule_value,
            }
            for module, controller, action, rule_value in sorted(rule_set)
        ]
        response = client.set_role_permissions(slug, payload)
        if response.get("success"):
            updated_roles += 1
            total_rules += len(payload)
            logger.info(
                f"Set {len(payload)} permission rule(s) for role '{slug}' via Splynx API"
            )
        else:
            logger.error(
                f"Failed to update permissions for role '{slug}': {response.get('error')}"
            )

    logger.info(
        f"Applied permissions to Splynx via API: updated_roles={updated_roles}, total_rules={total_rules}, skipped_assignments={skipped}"
    )


def _fetch_sonar_fields() -> List[Dict[str, str]]:
    url, _ = _connect_backup()
    fields: List[Dict[str, str]] = []
    with connect(url) as conn, conn.cursor() as cur:
        cur.execute(
            f"SELECT data FROM {_CUSTOM_FIELDS_TABLE} WHERE data ->> 'entity_type' = %s",
            (_SONAR_FIELD_ENTITY,),
        )
        for (row,) in cur.fetchall():
            fields.append(row)
    return fields


def _fetch_sonar_values(field_id: str) -> List[Dict[str, str]]:
    url, _ = _connect_backup()
    values: List[Dict[str, str]] = []
    with connect(url) as conn, conn.cursor() as cur:
        cur.execute(
            f"SELECT data FROM {_CUSTOM_FIELD_DATA_TABLE} WHERE data ->> 'custom_field_id' = %s",
            (field_id,),
        )
        for (row,) in cur.fetchall():
            values.append(row)
    return values


def _get_existing_field_names() -> Dict[str, Dict[str, str]]:
    rows = _run_mysql_query(f"SELECT name, title FROM {_FIELDS_TABLE};")
    return {row[0]: {"title": row[1]} for row in rows}


def _next_position() -> int:
    rows = _run_mysql_query(f"SELECT COALESCE(MAX(position),0) FROM {_FIELDS_TABLE};")
    return int(rows[0][0]) + 1 if rows else 1


def _slugify(name: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_").lower()
    return slug or "custom_field"


def _map_field_type(sonar_type: str) -> str:
    mapped = _TYPE_MAP.get((sonar_type or "TEXT").upper())
    if not mapped:
        raise RuntimeError(f"Unsupported Sonar custom field type: {sonar_type}")
    return mapped


def _insert_definition(field: Dict[str, str], position: int) -> str:
    name = _slugify(field.get("name", ""))
    splynx_type = _map_field_type(field.get("type", "TEXT"))
    is_required = "1" if field.get("required") else "0"
    is_unique = "1" if field.get("unique") else "0"

    values = {
        "name": name,
        "module": "customers",
        "title": field.get("name", name.title()),
        "type": splynx_type,
        "position": str(position),
        "is_required": is_required,
        "is_unique": is_unique,
    }
    values.update(_DEFAULT_FIELD_VALUES)

    assignments = []
    for column in _FIELD_COLUMNS:
        val = values.get(column, _DEFAULT_FIELD_VALUES.get(column, "")) or ""
        assignments.append("'%s'" % val.replace("'", "''"))

    sql = (
        f"INSERT INTO {_FIELDS_TABLE} ({', '.join(_FIELD_COLUMNS)}) "
        f"VALUES ({', '.join(assignments)});"
    )
    _run_mysql_query(sql)
    return name


def _insert_values(field_name: str, sonar_values: List[Dict[str, str]]) -> None:
    if not sonar_values:
        return
    rows = []
    for item in sonar_values:
        customer_id = item.get("customfielddataable_id")
        value = item.get("value", "")
        if not customer_id:
            continue
        sanitized = value.replace("'", "''")
        rows.append((int(customer_id), field_name, sanitized))
    if not rows:
        return

    formatted = []
    for customer_id, name, value in rows:
        escaped_name = name.replace("'", "''")
        escaped_value = value.replace("'", "''")
        formatted.append(f"({customer_id}, '{escaped_name}', '{escaped_value}')")
    values_clause = ", ".join(formatted)
    sql = (
        f"INSERT INTO {_VALUES_TABLE} (id, name, value) VALUES "
        + values_clause
        + " ON DUPLICATE KEY UPDATE value=VALUES(value);"
    )
    _run_mysql_query(sql)


def migrate_custom_fields() -> None:
    logger.info("Synchronizing custom fields from Sonar backup")
    sonar_fields = _fetch_sonar_fields()
    existing = _get_existing_field_names()
    position = _next_position()

    inserted = 0
    for field in sonar_fields:
        name = _slugify(field.get("name", ""))
        if name not in existing:
            _insert_definition(field, position)
            position += 1
            inserted += 1
        values = _fetch_sonar_values(field.get("id"))
        _insert_values(name, values)
    logger.info(
        f"Processed {len(sonar_fields)} custom field(s); added {inserted} new definition(s)."
    )


# ---------------------------------------------------------------------------
# Roles & permissions normalization helpers


def normalize_roles(output_path: Optional[str] = None, apply_to_splynx: bool = False) -> None:
    logger.info("Normalizing Sonar roles and permissions")
    backup_url = os.getenv("BACKUP_DATABASE_URL")
    if not backup_url:
        raise RuntimeError("BACKUP_DATABASE_URL must be set to normalize roles")
    extractor = SonarSecurityExtractor(backup_url)
    transformer = RoleTransformer()
    try:
        roles = extractor.fetch_roles()
        permissions = extractor.fetch_permissions()
        categories = extractor.fetch_permission_categories()
        assignments = extractor.fetch_role_permissions()
        normalized_roles, normalized_permissions, normalized_assignments = transformer.transform(
            roles=roles,
            permissions=permissions,
            permission_categories=categories,
            role_permissions=assignments,
        )
        logger.info(
            f"Normalized roles={len(normalized_roles)} permissions={len(normalized_permissions)} assignments={len(normalized_assignments)}"
        )
        fallback_code_map: Optional[Dict[str, List[str]]] = None
        if not normalized_permissions and not normalized_assignments:
            fallback_code_map = _load_role_permission_codes_from_csv()
            if fallback_code_map:
                logger.info(
                    f"Loaded fallback permission codes for {len(fallback_code_map)} role(s) from CSV"
                )
        if output_path:
            import json

            with open(output_path, "w", encoding="utf-8") as handle:
                json.dump(
                    {
                        'roles': [entity.to_dict() for entity in normalized_roles],
                        'permissions': [entity.to_dict() for entity in normalized_permissions],
                        'role_permissions': [entity.to_dict() for entity in normalized_assignments],
                    },
                    handle,
                    indent=2,
                )
            logger.info(f"Wrote normalized roles to {output_path}")

        if apply_to_splynx:
            role_slug_map, created_slugs = _apply_roles_to_splynx(normalized_roles)
            permission_slug_map = {entity.source_id: entity.data.get('code') for entity in normalized_permissions}
            permission_category_map = {entity.source_id: entity.data.get('category') for entity in normalized_permissions}
            _apply_permissions_to_splynx(
                role_slug_map,
                permission_slug_map,
                permission_category_map,
                normalized_assignments,
                fallback_code_map,
                created_slugs,
            )
    finally:
        extractor.close()


# ---------------------------------------------------------------------------
# Orchestrator


def run_foundation_phase(output_roles: Optional[str] = None) -> None:
    load_env()
    migrate_company()
    migrate_custom_fields()
    normalize_roles(output_roles, apply_to_splynx=True)
    try:
        from src.migration.phases.admin_users import import_sonar_administrators

        result = import_sonar_administrators()
        logger.info(
            "Imported Sonar administrators: created=%s, skipped=%s, failed=%s",
            len(result.created),
            len(result.skipped),
            len(result.failed),
        )
    except Exception as exc:
        logger.warning(f"Administrator import skipped due to error: {exc}")


__all__ = [
    "run_foundation_phase",
    "migrate_company",
    "migrate_custom_fields",
    "normalize_roles",
]
