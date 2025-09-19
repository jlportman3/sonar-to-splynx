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

def resolve_col(df: pd.DataFrame, name_guess: str, alts=None, required=True) -> str:
    alts = (alts or []) + [name_guess]
    cols = {c.strip().lower(): c for c in df.columns}
    for guess in alts:
        key = guess.strip().lower()
        if key in cols:
            return cols[key]
        # loose match: ignore spaces/underscores/case
        for k, c in cols.items():
            if re.sub(r"[\s_]+","",k) == re.sub(r"[\s_]+","",key):
                return c
    if required:
        raise KeyError(f"Column '{name_guess}' not found. Available: {list(df.columns)}")
    return None

def normalize_email(s):
    if s is None:
        return None
    s = str(s).strip()
    if not s:
        return None
    # Extract email if embedded in text
    m = re.search(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', s, re.I)
    if m:
        return m.group(0).lower()
    return s.lower()

def main():
    ap = argparse.ArgumentParser(description="Build incoming_customer.csv (email,name,customer_id)")
    ap.add_argument("--replies", required=True, help="ticket_replies.csv")
    ap.add_argument("--accounts", required=False, help="accounts.csv")
    ap.add_argument("--contacts", required=False, help="contacts.csv")
    ap.add_argument("--out", required=True, help="Output incoming_customer.csv")
    args = ap.parse_args()

    rdf = read_csv_auto(args.replies)
    adf = read_csv_auto(args.accounts) if args.accounts else pd.DataFrame()
    cdf = read_csv_auto(args.contacts) if args.contacts else pd.DataFrame()

    # Replies columns
    r_author = resolve_col(rdf, "author", ["from","name"], required=False)
    r_author_email = resolve_col(rdf, "author email", ["author_email","email"], required=False)

    name_series = rdf[r_author].fillna("").astype(str) if r_author else pd.Series([""]*len(rdf))
    email_series = rdf[r_author_email].fillna("").astype(str) if r_author_email else pd.Series([""]*len(rdf))
    # Fallback: pull email from author if author_email empty
    extracted = name_series.map(normalize_email)
    primary_email = email_series.map(normalize_email)
    primary_email = primary_email.where(primary_email.notna(), extracted)

    out = pd.DataFrame()
    out["email"] = primary_email.fillna("").astype(str)
    out["name"] = name_series.str.strip()

    # Build customer_id via accounts first
    cust = pd.Series([""]*len(out), dtype=object)
    if not adf.empty:
        # Identify ID and any email columns
        acc_id_col = resolve_col(adf, "ID", ["id","customer id"], required=False) or adf.columns[0]
        email_cols = [c for c in adf.columns if "email" in c.lower()]
        acc_map = {}
        for c in email_cols:
            tmp = adf[[acc_id_col, c]].copy()
            tmp[c] = tmp[c].map(normalize_email)
            for e, cid in zip(tmp[c], tmp[acc_id_col]):
                if e and str(cid).strip().isdigit():
                    acc_map[e] = str(int(cid))
        mapped = out["email"].map(lambda e: acc_map.get(e, None))
        cust = mapped.fillna("")

    # Enhance from contacts where still NULL
    if not cdf.empty:
        co_col = resolve_col(cdf, "contact owner", ["owner","owner type","contact owner type"], required=False)
        oid_col = resolve_col(cdf, "contact owner id", ["owner id","owner_id","contact owner ID"], required=False)
        email_col = resolve_col(cdf, "email address", ["email","email address(es)","contact email"], required=False)
        if oid_col and email_col:
            tmp = cdf[[oid_col, email_col]].copy()
            # If contact owner column present, restrict to Account
            if co_col:
                tmp = tmp[cdf[co_col].astype(str).str.strip().str.lower().eq("account")]
            tmp[email_col] = tmp[email_col].map(normalize_email)
            contact_map = {}
            for e, cid in zip(tmp[email_col], tmp[oid_col]):
                if e and str(cid).strip().isdigit():
                    contact_map[e] = str(int(cid))
            # fill where cust == "NULL"
            fill_vals = out["email"].map(lambda e: contact_map.get(e, None))
            cust = cust.where(cust != "", fill_vals.fillna(""))

    out["customer_id"] = cust

    # Keep only rows with email
    out = out[out["email"] != ""]

    # Deduplicate by email (keep first non-empty name)
    out = out.sort_values(by=["email"])
    out = out.drop_duplicates(subset=["email"], keep="first").copy()
    out["name"] = out.apply(lambda r: r["name"] if str(r["name"]).strip() else r["email"].split("@")[0], axis=1)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.insert(0, "id", range(1, len(out) + 1))  # додаємо колонку id з автонумерацією
    
    # ---- Prepend static DESCRIPTION row with id=1 ----
    # Ensure no pre-existing id column, we will rebuild it.
    if "id" in out.columns:
        out = out.drop(columns=["id"])
    # Build ids starting from 2 for existing rows
    out.insert(0, "id", range(2, len(out) + 2))
    # Create the first static row
    _desc_row = {"id": 1, "email": "", "name": "DESCRIPTION", "customer_id": ""}
    out = pd.concat([pd.DataFrame([_desc_row]), out], ignore_index=True)
    # ---------------------------------------------------
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()
