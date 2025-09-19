#!/usr/bin/env python3
"""Create a mysqldump backup of the Splynx MariaDB database."""

from __future__ import annotations

import argparse
import gzip
import os
import subprocess
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv

DEFAULT_OUTPUT_DIR = Path("backups/splynx")


def load_db_config() -> Dict[str, str]:
    load_dotenv(dotenv_path=Path(".env"))

    host = os.getenv("SPLYNX_DB_HOST", "localhost")
    port = os.getenv("SPLYNX_DB_PORT", "3306")
    user = os.getenv("SPLYNX_DB_USER")
    password = os.getenv("SPLYNX_DB_PASSWORD")
    socket = os.getenv("SPLYNX_DB_SOCKET")
    db_name = os.getenv("SPLYNX_DB_NAME", "splynx")

    missing = [name for name, value in {
        "SPLYNX_DB_USER": user,
        "SPLYNX_DB_PASSWORD": password,
    }.items() if not value]
    if missing:
        raise ValueError(
            "Missing database credentials: " + ", ".join(missing)
        )

    return {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "socket": socket,
        "db_name": db_name,
    }


def build_command(cfg: Dict[str, str], mysqldump_path: str) -> list[str]:
    command = [
        mysqldump_path,
        "--single-transaction",
        "--routines",
        "--triggers",
        "--events",
        "--set-gtid-purged=OFF",
        "--default-character-set=utf8mb4",
        "--no-tablespaces",
        "-u",
        cfg["user"],
    ]

    if cfg.get("socket"):
        command.extend(["--socket", cfg["socket"]])
    else:
        command.extend(["--host", cfg["host"], "--port", str(cfg["port"])])

    command.append(cfg["db_name"])
    return command


def default_output_path(gzip_enabled: bool) -> Path:
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    filename = f"splynx-backup-{timestamp}.sql"
    if gzip_enabled:
        filename += ".gz"
    return DEFAULT_OUTPUT_DIR / filename


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dump the Splynx MariaDB database using mysqldump.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to write the backup file. If omitted a timestamped file is placed in backups/splynx/",
    )
    parser.add_argument(
        "--mysqldump",
        default="mysqldump",
        help="Path to the mysqldump executable",
    )
    parser.add_argument(
        "--no-gzip",
        action="store_true",
        help="Store a plain .sql file (no gzip compression)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_db_config()

    output_path = args.output or default_output_path(gzip_enabled=not args.no_gzip)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    command = build_command(cfg, args.mysqldump)

    env = os.environ.copy()
    env["MYSQL_PWD"] = cfg["password"]

    print("Running:", " ".join(part for part in command if part != env["MYSQL_PWD"]))

    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, env=env)
    except FileNotFoundError as exc:
        raise SystemExit(f"mysqldump not found: {exc}")

    assert proc.stdout is not None

    try:
        if args.no_gzip:
            with output_path.open("wb") as fh:
                shutil.copyfileobj(proc.stdout, fh)
        else:
            with gzip.open(output_path, "wb") as fh:
                shutil.copyfileobj(proc.stdout, fh)
    finally:
        proc.stdout.close()
        returncode = proc.wait()

    if returncode != 0:
        output_path.unlink(missing_ok=True)
        raise SystemExit(f"mysqldump failed with exit code {returncode}")

    print(f"Backup written to {output_path}")


if __name__ == "__main__":
    main()
