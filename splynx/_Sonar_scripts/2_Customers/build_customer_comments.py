#!/usr/bin/env python3
import argparse
import re
import pandas as pd
from pathlib import Path

def resolve_col(df, name_guess, alt_guesses=None):
    cols = {c.strip().lower(): c for c in df.columns}
    keys = [name_guess] + (alt_guesses or [])
    for guess in keys:
        key = guess.strip().lower()
        if key in cols:
            return cols[key]
        for k, c in cols.items():
            if re.sub(r"\s+", "", k) == re.sub(r"\s+", "", key):
                return c
    # Handle small typos like 'noteable' vs 'notable'
    for k, c in cols.items():
        if k.replace("eable", "able") == name_guess.strip().lower().replace("eable", "able"):
            return c
    raise KeyError(f"Column '{name_guess}' not found. Available: {list(df.columns)}")

def parse_dt(series, shift_hours=0):
    def _parse_one(x):
        if pd.isna(x):
            return pd.NaT
        s = str(x).strip().replace("T", " ")
        s = re.sub(r"(Z|[+-]\d{2}:?\d{2})$", "", s)
        m = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(\.\d+)?$", s)
        if m:
            s = m.group(1)
        return pd.to_datetime(s, errors="coerce")
    dt = series.map(_parse_one)
    if shift_hours and shift_hours != 0:
        dt = dt + pd.to_timedelta(shift_hours, unit="h")
    return dt.dt.strftime("%Y-%m-%d %H:%M:%S")

def main():
    ap = argparse.ArgumentParser(description="Build customer_comments.csv from Sonar notes.csv")
    ap.add_argument("--input", "-i", required=True, help="Path to notes.csv from Sonar")
    ap.add_argument("--output", "-o", required=True, help="Path to write customer_comments.csv")
    ap.add_argument("--shift-hours", type=int, default=0, help="Hour offset to apply to created/updated timestamps (can be negative)")
    ap.add_argument("--accounts", help="Optional accounts.csv path to filter comments to existing customer IDs")
    args = ap.parse_args()

    # Read notes CSV (auto delimiter)
    try:
        df = pd.read_csv(args.input)
    except Exception:
        df = pd.read_csv(args.input, sep=";")

    # Filter notable type = Account (handle 'noteable')
    col_notable_type = resolve_col(df, "notable type", ["noteable type"])
    df = df[df[col_notable_type].astype(str).str.strip().str.lower() == "account"].copy()

    # Resolve columns
    col_id = resolve_col(df, "ID")
    col_notable_id = resolve_col(df, "notable ID", ["noteable ID"])
    col_created_at = resolve_col(df, "created at")
    col_updated_at = resolve_col(df, "updated at")
    col_user_id = resolve_col(df, "user ID")
    col_message = resolve_col(df, "message")
    col_priority = resolve_col(df, "priority")

    out = pd.DataFrame()
    out["id"] = df[col_id].astype("Int64")
    out["customer_id"] = df[col_notable_id].astype("Int64")
    out["datetime"] = parse_dt(df[col_created_at], shift_hours=args.shift_hours)
    out["administrator_id"] = df[col_user_id].astype("Int64")
    out["type"] = "comment"
    out["comment"] = df[col_message].fillna("").astype(str)
    out["updated_at"] = parse_dt(df[col_updated_at], shift_hours=args.shift_hours)

    pnorm = df[col_priority].astype(str).str.upper().str.strip()
    out["is_pinned"] = pnorm.map(
        {"NORMAL": 0, "STICKY": 1, "STICKY_WITH_CONFIRMATION": 1}
    ).fillna(0).astype(int)

    # Optional filtering by accounts.csv
    if args.accounts:
        try:
            acc = pd.read_csv(args.accounts)
        except Exception:
            acc = pd.read_csv(args.accounts, sep=";")
        try:
            acc_id_col = resolve_col(acc, "ID", ["id", "customer id", "account id"])
        except Exception as e:
            raise SystemExit(f"Could not resolve ID column in accounts CSV: {e}")
        valid_ids = set(pd.to_numeric(acc[acc_id_col], errors="coerce").dropna().astype("Int64").tolist())
        before = len(out)
        out = out[out["customer_id"].isin(valid_ids)].copy()
        removed = before - len(out)
        print(f"Filtered by accounts: kept {len(out)}/{before} rows, removed {removed} missing customers.")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows to {args.output}")

if __name__ == "__main__":
    main()
