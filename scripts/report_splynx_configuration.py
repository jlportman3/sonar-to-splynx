#!/usr/bin/env python3
"""Generate a configuration report for the local Splynx MariaDB instance."""

from __future__ import annotations

import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List

from dotenv import load_dotenv

REPORT_PATH = Path("docs/splynx/configuration_report.md")
DEFAULT_DB = "splynx"


def load_config() -> dict:
    load_dotenv(Path(".env"))
    cfg = {
        "host": os.getenv("SPLYNX_DB_HOST", "localhost"),
        "port": os.getenv("SPLYNX_DB_PORT", "3306"),
        "user": os.getenv("SPLYNX_DB_USER"),
        "password": os.getenv("SPLYNX_DB_PASSWORD"),
        "socket": os.getenv("SPLYNX_DB_SOCKET"),
        "database": os.getenv("SPLYNX_DB_NAME", DEFAULT_DB),
    }
    if not cfg["user"] or not cfg["password"]:
        raise SystemExit("Missing SPLYNX_DB_USER or SPLYNX_DB_PASSWORD in environment")
    return cfg


def run_query(cfg: dict, sql: str) -> List[List[str]]:
    command = ["mysql", "-u", cfg["user"], "--batch", "--skip-column-names", "-e", sql]
    if cfg.get("socket"):
        command.extend(["-S", cfg["socket"]])
    else:
        command.extend(["-h", cfg.get("host", "localhost"), "-P", str(cfg.get("port", "3306"))])
    command.append(cfg["database"])

    env = os.environ.copy()
    env["MYSQL_PWD"] = cfg["password"]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        if "doesn't exist" in stderr or "Unknown table" in stderr:
            return []
        raise RuntimeError(f"MySQL query failed: {stderr}\nSQL: {sql}")

    rows: List[List[str]] = []
    for line in result.stdout.strip().splitlines():
        if not line:
            continue
        rows.append(line.split("\t"))
    return rows


def fetch_count(cfg: dict, table: str) -> int:
    rows = run_query(cfg, f"SELECT COUNT(*) FROM `{table}`;")
    return int(rows[0][0]) if rows else 0


def fetch_samples(cfg: dict, table: str, columns: str, order: str = "1", limit: int = 5) -> List[str]:
    rows = run_query(cfg, f"SELECT {columns} FROM `{table}` ORDER BY {order} LIMIT {limit};")
    return [" | ".join(row) for row in rows]


def bullet_list(entries: List[str]) -> str:
    if not entries:
        return "  - (none)\n"
    return "".join(f"  - {entry}\n" for entry in entries)


def format_count(label: str, count: int) -> str:
    if count:
        return f"- {label}: {count}"
    return f"- {label}: 0 (⚠️ none configured)"


def main() -> None:
    cfg = load_config()
    generated_at = datetime.utcnow().isoformat()

    sections: List[str] = []

    # Administration
    admins_count = fetch_count(cfg, "admins")
    admins_samples = fetch_samples(cfg, "admins", "login, name, email", order="id", limit=5)
    roles_count = fetch_count(cfg, "roles")
    roles_samples = fetch_samples(cfg, "roles", "name", order="name", limit=5)
    sections.append(
        "## Administration\n"
        + format_count("Admin users", admins_count)
        + "\n"
        + format_count("Roles", roles_count)
        + "\n\n**Sample admins**\n\n"
        + bullet_list(admins_samples)
        + "\n**Sample roles**\n\n"
        + bullet_list(roles_samples)
    )

    # Partners / Locations
    partner_count = fetch_count(cfg, "partners")
    partner_samples = fetch_samples(cfg, "partners", "id, name", order="id", limit=5)
    location_count = fetch_count(cfg, "locations")
    location_samples = fetch_samples(cfg, "locations", "id, name", order="id", limit=5)
    sections.append(
        "## Partners & Locations\n"
        + format_count("Partners", partner_count)
        + "\n"
        + format_count("Locations", location_count)
        + "\n\n**Sample partners**\n\n"
        + bullet_list(partner_samples)
        + "\n**Sample locations**\n\n"
        + bullet_list(location_samples)
    )

    # Tariffs
    internet_tariffs = fetch_count(cfg, "tariffs_internet")
    internet_samples = fetch_samples(cfg, "tariffs_internet", "id, title, price", order="id", limit=5)
    voice_tariffs = fetch_count(cfg, "tariffs_voice")
    voice_samples = fetch_samples(cfg, "tariffs_voice", "id, title, price", order="id", limit=5)
    onetime_tariffs = fetch_count(cfg, "tariffs_one_time")
    onetime_samples = fetch_samples(cfg, "tariffs_one_time", "id, title, price", order="id", limit=5)
    sections.append(
        "## Tariffs\n"
        + format_count("Internet tariffs", internet_tariffs)
        + "\n"
        + format_count("Voice tariffs", voice_tariffs)
        + "\n"
        + format_count("One-time tariffs", onetime_tariffs)
        + "\n\n**Sample internet tariffs**\n\n"
        + bullet_list(internet_samples)
        + "\n**Sample voice tariffs**\n\n"
        + bullet_list(voice_samples)
        + "\n**Sample one-time tariffs**\n\n"
        + bullet_list(onetime_samples)
    )

    # Payments
    payment_type_count = fetch_count(cfg, "payments_types")
    payment_type_samples = fetch_samples(cfg, "payments_types", "id, name, is_active", order="id", limit=5)
    sections.append(
        "## Payments\n"
        + format_count("Payment types", payment_type_count)
        + "\n\n**Sample payment types**\n\n"
        + bullet_list(payment_type_samples)
    )

    # Inventory
    inventory_count = fetch_count(cfg, "inventory_items")
    inventory_samples = fetch_samples(
        cfg,
        "inventory_items",
        "id, serial_number, status, product_id, customer_id",
        order="id",
        limit=5,
    )
    product_count = fetch_count(cfg, "inventory_products")
    product_samples = fetch_samples(cfg, "inventory_products", "id, name, vendor_id", order="id", limit=5)
    vendor_count = fetch_count(cfg, "inventory_vendors")
    vendor_samples = fetch_samples(cfg, "inventory_vendors", "id, name", order="id", limit=5)
    sections.append(
        "## Inventory\n"
        + format_count("Inventory items", inventory_count)
        + "\n"
        + format_count("Inventory products", product_count)
        + "\n"
        + format_count("Inventory vendors", vendor_count)
        + "\n\n**Sample inventory items**\n\n"
        + bullet_list(inventory_samples)
        + "\n**Sample inventory products**\n\n"
        + bullet_list(product_samples)
        + "\n**Sample inventory vendors**\n\n"
        + bullet_list(vendor_samples)
    )

    # Network
    site_count = fetch_count(cfg, "network_sites")
    site_samples = fetch_samples(cfg, "network_sites", "id, title, address", order="id", limit=5)
    router_count = fetch_count(cfg, "routers")
    router_samples = fetch_samples(cfg, "routers", "id, title, ip", order="id", limit=5)
    ipv4_count = fetch_count(cfg, "ipv4_networks")
    ipv6_count = fetch_count(cfg, "ipv6_networks")
    sections.append(
        "## Network\n"
        + format_count("Network sites", site_count)
        + "\n"
        + format_count("Routers", router_count)
        + "\n"
        + format_count("IPv4 networks", ipv4_count)
        + "\n"
        + format_count("IPv6 networks", ipv6_count)
        + "\n\n**Sample network sites**\n\n"
        + bullet_list(site_samples)
        + "\n**Sample routers**\n\n"
        + bullet_list(router_samples)
    )

    # Security
    admin_perm = fetch_count(cfg, "permissions_administrator")
    role_perm = fetch_count(cfg, "permissions_role")
    api_perm = fetch_count(cfg, "permissions_api_key")
    sections.append(
        "## Security & Permissions\n"
        + format_count("Admin permission records", admin_perm)
        + "\n"
        + format_count("Role permission records", role_perm)
        + "\n"
        + format_count("API key permissions", api_perm)
    )

    # Support
    ticket_count = fetch_count(cfg, "ticket")
    ticket_samples = fetch_samples(cfg, "ticket", "id, subject, status_id, priority", order="id", limit=5)
    sections.append(
        "## Support\n"
        + format_count("Tickets", ticket_count)
        + "\n\n**Sample tickets**\n\n"
        + bullet_list(ticket_samples)
    )

    # Documents / Contracts
    document_count = fetch_count(cfg, "documents")
    contract_count = fetch_count(cfg, "contracts")
    sections.append(
        "## Documents & Contracts\n"
        + format_count("Documents", document_count)
        + "\n"
        + format_count("Contracts", contract_count)
    )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w", encoding="utf-8") as fh:
        fh.write("# Splynx Configuration Report\n\n")
        fh.write(f"Generated: {generated_at} UTC\n\n")
        fh.write(f"Database: `{cfg['database']}`\n\n")
        fh.write("\n".join(sections))
        fh.write("\n")

    print(f"Report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
