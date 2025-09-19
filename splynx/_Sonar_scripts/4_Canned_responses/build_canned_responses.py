#!/usr/bin/env python3
import argparse
import pandas as pd
import re
from pathlib import Path

def read_csv_auto(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_csv(path, sep=";")

def resolve_col(df: pd.DataFrame, name_guess: str, alts=None) -> str:
    alts = (alts or []) + [name_guess]
    cols = {c.strip().lower(): c for c in df.columns}
    for guess in alts:
        key = guess.strip().lower()
        if key in cols:
            return cols[key]
        # ignore spaces/underscores/case
        for k, c in cols.items():
            if re.sub(r"[\s_]+","",k) == re.sub(r"[\s_]+","",key):
                return c
    raise KeyError(f"Column '{name_guess}' not found. Available: {list(df.columns)}")

def build_groups(categories_csv: str) -> pd.DataFrame:
    cat = read_csv_auto(categories_csv)
    col_id = resolve_col(cat, "ID")
    col_name = resolve_col(cat, "name", ["title"])
    out = pd.DataFrame()
    out["id"] = pd.to_numeric(cat[col_id], errors="coerce").astype("Int64")
    out["title"] = cat[col_name].fillna("").astype(str)
    return out

def build_responses(replies_csv: str) -> pd.DataFrame:
    rep = read_csv_auto(replies_csv)
    col_id = resolve_col(rep, "ID")
    col_name = resolve_col(rep, "name", ["title"])
    col_body = resolve_col(rep, "body", ["code","content","text"])
    col_cat  = resolve_col(rep, "canned reply category ID", ["category id","group id","canned group id"])
    out = pd.DataFrame()
    out["id"] = pd.to_numeric(rep[col_id], errors="coerce").astype("Int64")
    out["title"] = rep[col_name].fillna("").astype(str)
    out["code"] = rep[col_body].fillna("").astype(str)
    out["canned_group"] = pd.to_numeric(rep[col_cat], errors="coerce").astype("Int64")
    return out

def main():
    ap = argparse.ArgumentParser(description="Build Splynx canned responses from Sonar CSVs")
    ap.add_argument("--categories", required=True, help="Path to Sonar canned_reply_categories.csv")
    ap.add_argument("--replies", required=True, help="Path to Sonar canned_replies.csv")
    ap.add_argument("--out-groups", required=True, help="Output CSV for ticket_canned_response_group")
    ap.add_argument("--out-responses", required=True, help="Output CSV for ticket_canned_response")
    args = ap.parse_args()

    groups = build_groups(args.categories)
    responses = build_responses(args.replies)

    Path(args.out_groups).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_responses).parent.mkdir(parents=True, exist_ok=True)
    groups.to_csv(args.out_groups, index=False, encoding="utf-8")
    responses.to_csv(args.out_responses, index=False, encoding="utf-8")

    print(f"Wrote groups: {len(groups)} rows -> {args.out_groups}")
    print(f"Wrote responses: {len(responses)} rows -> {args.out_responses}")

if __name__ == "__main__":
    main()
