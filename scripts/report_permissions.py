#!/usr/bin/env python3
"""Generate a detailed permissions comparison between Sonar and Splynx."""

from __future__ import annotations

import json
import os
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from dotenv import load_dotenv
from psycopg import connect

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in os.sys.path:
    os.sys.path.insert(0, str(PROJECT_ROOT))

from src.apis.splynx_client import SplynxAPIClient, SplynxConfig

SONAR_PERMISSIONS_TABLE = "graphql_backup__roles"
PERMISSION_MAP_PATH = Path("config/permissions_map.json")


@dataclass
class SonarRole:
    id: str
    name: str
    slug: str
    permissions: List[str]


@dataclass
class SplynxRole:
    name: str
    title: str
    rules: Set[Tuple[str, str, str, str]]  # (module, controller, action, rule)


# ---------------------------------------------------------------------------
# Utilities


def slugify(value: str) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "_" for ch in value or "")
    slug = "_".join(part for part in slug.split("_") if part)
    return slug or "role"


# ---------------------------------------------------------------------------
# Sonar extraction


def fetch_sonar_roles(database_url: str) -> List[SonarRole]:
    roles: List[SonarRole] = []
    with connect(database_url) as conn, conn.cursor() as cur:
        cur.execute(
            f"SELECT data FROM {SONAR_PERMISSIONS_TABLE} ORDER BY data ->> 'name'"
        )
        for (row,) in cur.fetchall():
            name = row.get("name") or row.get("title") or f"role_{row.get('id')}"
            permissions = row.get("applied_permissions") or []
            if not isinstance(permissions, list):
                permissions = []
            roles.append(
                SonarRole(
                    id=str(row.get("id")),
                    name=name,
                    slug=slugify(name),
                    permissions=[perm.lower() for perm in permissions],
                )
            )
    return roles


# ---------------------------------------------------------------------------
# Splynx extraction (via mysql CLI)


def load_splynx_db_config() -> Dict[str, str]:
    cfg = {
        "host": os.getenv("SPLYNX_DB_HOST", "localhost"),
        "port": os.getenv("SPLYNX_DB_PORT", "3306"),
        "user": os.getenv("SPLYNX_DB_USER"),
        "password": os.getenv("SPLYNX_DB_PASSWORD"),
        "socket": os.getenv("SPLYNX_DB_SOCKET"),
        "database": os.getenv("SPLYNX_DB_NAME", "splynx"),
    }
    if not cfg["user"] or not cfg["password"]:
        raise SystemExit("SPLYNX_DB_USER and SPLYNX_DB_PASSWORD must be set in .env")
    return cfg


def run_mysql_query(cfg: Dict[str, str], sql: str) -> List[List[str]]:
    command = ["mysql", "-u", cfg["user"], f"-p{cfg['password']}", "--batch", "--skip-column-names", "-e", sql]
    if cfg.get("socket"):
        command.extend(["-S", cfg["socket"]])
    else:
        command.extend(["-h", cfg.get("host", "localhost"), "-P", str(cfg.get("port", "3306"))])
    command.append(cfg["database"])

    env = os.environ.copy()
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"MySQL query failed: {result.stderr.strip()}\nSQL: {sql}")

    rows: List[List[str]] = []
    for line in result.stdout.strip().splitlines():
        if line:
            rows.append(line.split("\t"))
    return rows


def fetch_splynx_roles(cfg: Dict[str, str]) -> Dict[str, SplynxRole]:
    api_key = os.getenv("SPLYNX_API_KEY")
    api_secret = (
        os.getenv("SPLYNX_API_SECRET")
        or os.getenv("SPLYNX_API_PASSWORD")
        or os.getenv("SPLYNX_SECRET")
    )
    base_url = os.getenv("SPLYNX_URL")

    roles: Dict[str, SplynxRole] = {}

    if base_url and api_key and api_secret:
        client = SplynxAPIClient(SplynxConfig(base_url=base_url, api_key=api_key, api_secret=api_secret))
        response = client.get("admin/administration/roles", params={"limit": 200})
        if response.get("success"):
            for item in response.get("data", []) or []:
                slug = item.get("id") or item.get("name")
                if not slug:
                    continue
                detail = client.get(f"admin/administration/roles/{slug}")
                permissions = []
                if detail.get("success"):
                    permissions = detail.get("data", {}).get("permissions", []) or []
                role = roles.setdefault(slug, SplynxRole(name=slug, title=item.get("name", slug), rules=set()))
                for perm in permissions:
                    module = perm.get("module", "")
                    controller = perm.get("controller", "")
                    action = perm.get("action", "*")
                    rule = perm.get("rule", "allow")
                    role.rules.add((module, controller, action, rule))
        else:
            print("Warning: Splynx API call failed; falling back to DB-only view")

    if not roles:
        for name, title, is_base in run_mysql_query(cfg, "SELECT name,title,is_base FROM roles;"):
            roles[name] = SplynxRole(name=name, title=title, rules=set())

        rule_rows = run_mysql_query(
            cfg,
            "SELECT id, module, controller, action, rule FROM permissions_role ORDER BY id;",
        )
        for role_id, module, controller, action, rule in rule_rows:
            role = roles.setdefault(role_id, SplynxRole(name=role_id, title=role_id, rules=set()))
            role.rules.add((module, controller, action, rule))

    return roles


# ---------------------------------------------------------------------------
# Mapping utilities


def load_permission_mapping() -> Dict[str, List[Dict[str, str]]]:
    if not PERMISSION_MAP_PATH.exists():
        return {}
    with PERMISSION_MAP_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    mapping: Dict[str, List[Dict[str, str]]] = {}
    for key, entries in data.items():
        if isinstance(entries, list):
            mapping[key.lower()] = entries
    return mapping


def derive_rules(perm_slug: str) -> List[Dict[str, str]]:
    slug = perm_slug.lower()
    hints = slug.replace("_", " ")
    module = "administration"
    controller = "roles"

    heuristics = [
        ("finance", ("finance", "finance")),
        ("billing", ("finance", "finance")),
        ("invoice", ("finance", "invoices")),
        ("payment", ("finance", "payments")),
        ("customer", ("customers", "customer")),
        ("account", ("customers", "customer")),
        ("inventory", ("inventory", "items")),
        ("network", ("networking", "routers")),
        ("ip", ("networking", "ipv4")),
        ("ticket", ("support", "tickets")),
        ("support", ("support", "tickets")),
    ]
    for keyword, target in heuristics:
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


# ---------------------------------------------------------------------------
# Reporting


def build_report() -> None:
    load_dotenv(Path(".env"))
    backup_url = os.getenv("BACKUP_DATABASE_URL")
    if not backup_url:
        raise SystemExit("BACKUP_DATABASE_URL is not set")

    sonar_roles = fetch_sonar_roles(backup_url)
    sonar_permissions = sorted({perm for role in sonar_roles for perm in role.permissions})

    mapping = load_permission_mapping()

    splynx_cfg = load_splynx_db_config()
    splynx_roles = fetch_splynx_roles(splynx_cfg)

    print("# Permissions Report\n")
    print(f"Sonar roles: {len(sonar_roles)}")
    print(f"Splynx roles: {len(splynx_roles)}\n")

    sonar_slugs = {role.slug for role in sonar_roles}
    splynx_slugs = set(splynx_roles.keys())
    missing_roles = sorted(sonar_slugs - splynx_slugs)
    extra_roles = sorted(splynx_slugs - sonar_slugs)

    if missing_roles:
        print("## Roles missing in Splynx")
        for slug in missing_roles:
            print(f"- {slug}")
        print()
    if extra_roles:
        print("## Roles only in Splynx")
        for slug in extra_roles:
            print(f"- {slug}")
        print()

    print("## Role Comparison")
    print("| Role | Sonar perms | Splynx rules |")
    print("| --- | ---: | ---: |")
    for role in sonar_roles:
        sp_role = splynx_roles.get(role.slug)
        sp_count = len(sp_role.rules) if sp_role else 0
        print(f"| {role.slug} | {len(role.permissions)} | {sp_count} |")
    print()

    mapped = [perm for perm in sonar_permissions if perm in mapping]
    unmapped = [perm for perm in sonar_permissions if perm not in mapping]

    print("## Permission Mapping Status")
    print(f"Total Sonar permission codes: {len(sonar_permissions)}")
    print(f"Mapped via config: {len(mapped)}")
    print(f"Unmapped (heuristic only): {len(unmapped)}\n")

    if unmapped:
        print("### Unmapped permissions")
        for perm in unmapped:
            print(f"- {perm}")
        print()

    missing_rules = defaultdict(list)  # role_slug -> list of rule dicts

    for role in sonar_roles:
        sp_role = splynx_roles.get(role.slug)
        if not sp_role:
            continue
        existing_rules = sp_role.rules
        for perm in role.permissions:
            target_rules = mapping.get(perm)
            if target_rules is None:
                target_rules = derive_rules(perm)
            for rule in target_rules:
                key = (rule["module"], rule["controller"], rule["action"], rule.get("rule", "allow"))
                if key not in existing_rules:
                    missing_rules[role.slug].append(rule)

    print("## Missing permission rules")
    if not missing_rules:
        print("All mapped permission rules are present in Splynx.\n")
    else:
        for role_slug, rules in missing_rules.items():
            print(f"### {role_slug}")
            for rule in rules:
                print(
                    "- {module}/{controller}:{action} ({rule})".format(
                        module=rule["module"],
                        controller=rule["controller"],
                        action=rule["action"],
                        rule=rule.get("rule", "allow"),
                    )
                )
            print()

    # Sample Splynx roles
    print("## Sample Splynx rules")
    for slug, sp_role in list(splynx_roles.items())[:5]:
        print(f"### {slug} ({sp_role.title})")
        if not sp_role.rules:
            print("- (no rules)")
        else:
            for module, controller, action, rule in sorted(sp_role.rules):
                print(f"- {module}/{controller}:{action} ({rule})")
        print()


def main() -> None:
    build_report()


if __name__ == "__main__":
    main()
