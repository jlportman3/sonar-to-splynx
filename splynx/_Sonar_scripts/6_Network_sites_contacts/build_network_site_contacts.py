#!/usr/bin/env python3
import pandas as pd
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Build Network Site Contacts CSV from contacts.csv")
parser.add_argument("--input", "-i", required=True, help="Path to contacts.csv")
parser.add_argument("--output", "-o", required=True, help="Path to output CSV")
args = parser.parse_args()

# Завантаження CSV
try:
    df = pd.read_csv(args.input)
except Exception:
    df = pd.read_csv(args.input, sep=";")

# Фільтруємо лише NetworkSite
df = df[df["contact owner"].astype(str).str.strip().str.lower() == "networksite"]

# Формуємо вихідний датафрейм
out = pd.DataFrame()
out["id"] = df["ID"]
out["network_site_id"] = df["contact owner ID"]
out["contact_name"] = df["name"]
out["email"] = df["email address"]
out["comment"] = df["role"]
out["is_default"] = df["primary"]

# Зберігаємо результат
Path(args.output).parent.mkdir(parents=True, exist_ok=True)
out.to_csv(args.output, index=False, encoding="utf-8")
print(f"Wrote {len(out)} rows to {args.output}")