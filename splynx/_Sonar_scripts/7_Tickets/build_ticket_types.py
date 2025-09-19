#!/usr/bin/env python3
import argparse
import pandas as pd
import re

def resolve_col(df, name, alts=None):
    alts = (alts or []) + [name]
    cmap = {c.strip().lower(): c for c in df.columns}
    for g in alts:
        k = g.strip().lower()
        if k in cmap:
            return cmap[k]
        for ck, cn in cmap.items():
            if re.sub(r"[\s_]+","", ck) == re.sub(r"[\s_]+","", k):
                return cn
    raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")

def read_csv_auto(path):
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_csv(path, sep=";")

def main():
    ap = argparse.ArgumentParser(description="Build ticket_types_out.csv from Sonar ticket_categories.csv")
    ap.add_argument("--in", dest="infile", required=True, help="Input ticket_categories.csv")
    ap.add_argument("--out", dest="outfile", required=True, help="Output ticket_types_out.csv")
    args = ap.parse_args()

    df = read_csv_auto(args.infile)
    col_id = resolve_col(df, "ID", ["id"])
    col_name = resolve_col(df, "name", ["Name", "title", "category name"])

    out = pd.DataFrame({
        "id": pd.to_numeric(df[col_id], errors="coerce").astype("Int64"),
        "title": df[col_name].fillna("").astype(str),
    })
    out = out[~out["id"].isna()].copy()
    out.to_csv(args.outfile, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.outfile}")

if __name__ == "__main__":
    main()
