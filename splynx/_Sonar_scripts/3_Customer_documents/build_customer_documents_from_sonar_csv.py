#!/usr/bin/env python3
import argparse
import pandas as pd
import re
import hashlib
from pathlib import Path

def read_csv_auto(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_csv(path, sep=";")

def parse_dt(series: pd.Series, shift_hours: int = 0) -> pd.Series:
    """Robust datetime parser → returns string 'YYYY-MM-DD HH:MM:SS'; empty/unparseable -> ''"""
    s = series.astype(str).str.strip().str.replace('T', ' ', regex=False)
    s = s.str.replace(r'(Z|[+-]\d{2}:?\d{2})$', '', regex=True)
    dt = pd.to_datetime(s, errors='coerce')
    if shift_hours:
        dt = dt + pd.to_timedelta(shift_hours, unit='h')
    out = dt.dt.strftime('%Y-%m-%d %H:%M:%S')
    return out.fillna('')

def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()

def build_description(custom_message, sig_row: pd.Series, sig_dt_shifted: str) -> str:
    parts = []
    if pd.notna(custom_message):
        cm = str(custom_message).strip()
        if cm:
            parts.append(cm)
    if sig_row is not None:
        lines = []
        for label, key in [
            ("Signer name", "signer name"),
            ("Contact name", "contact name"),
            ("Contact email", "contact email address"),
            ("Contact role", "contact role"),
            ("Signer IP", "signer IP"),
        ]:
            if key in sig_row and pd.notna(sig_row[key]) and str(sig_row[key]).strip():
                lines.append(f"{label}: {sig_row[key]}")
        if sig_dt_shifted:
            lines.append(f"Signature created at: {sig_dt_shifted}")
        if lines:
            parts.append("**Signature details:**\n" + "\n".join(lines))
    return "\n\n".join([p for p in parts if p]).strip()

def main():
    ap = argparse.ArgumentParser(description="Build Splynx customer_documents CSV from Sonar contracts export")
    ap.add_argument("--contracts", required=True, help="Path to Sonar contracts.csv")
    ap.add_argument("--signatures", required=False, help="Optional path to Sonar handwritten_signatures.csv")
    ap.add_argument("--accounts", required=False, help="Optional path to accounts.csv for validating existing customers")
    ap.add_argument("--output", required=True, help="Path to write customer_documents.csv")
    ap.add_argument("--sql", required=True, help="Path to write customer_documents.sql")
    ap.add_argument("--short-customer", type=int, help="Optional customer_id to create short CSV/SQL for verification")
    ap.add_argument("--shift-hours", type=int, default=0, help="Hour offset to apply to timestamps (created/updated and signature timestamps)")
    ap.add_argument("--visible-by-customer", choices=["0","1"], default="1", help="Whether document is visible in portal (default 1)")
    args = ap.parse_args()

    contracts = read_csv_auto(args.contracts)
    signatures = read_csv_auto(args.signatures) if args.signatures else pd.DataFrame()
    accounts_df = read_csv_auto(args.accounts) if args.accounts else pd.DataFrame()

    # Source columns
    col_id = "ID"
    col_account = "account ID"
    col_name = "name"
    col_body = "body"
    col_custom_msg = "custom message"
    col_term_months = "term in months"
    col_created = "created at"
    col_updated = "updated at"
    col_hs_id = "handwritten signature ID"

    # Index signatures by their ID (normalize keys to string)
    sig_index = {}
    if not signatures.empty and "ID" in signatures.columns:
        for _, srow in signatures.iterrows():
            key = str(srow["ID"]).strip()
            sig_index[key] = srow

    out = pd.DataFrame()
    out["id"] = pd.to_numeric(contracts[col_id], errors="coerce").astype("Int64")
    out["customer_id"] = pd.to_numeric(contracts[col_account], errors="coerce").astype("Int64")
    out["type"] = "contract"
    out["title"] = contracts[col_name].fillna("").astype(str)
    out["created_at"] = parse_dt(contracts[col_created], args.shift_hours)
    out["updated_at"] = parse_dt(contracts[col_updated], args.shift_hours)
    out["code"] = contracts[col_body].fillna("").astype(str)
    out["visible_by_customer"] = args.visible_by_customer
    out["terms_month"] = pd.to_numeric(contracts[col_term_months], errors="coerce").astype("Int64")

    has_hs = contracts[col_hs_id].notna() & (contracts[col_hs_id].astype(str).str.strip()!="")
    out["status"] = has_hs.map(lambda v: "signed" if v else "new")

    # Description = custom message + signature block
    desc_values = []
    for _, row in contracts.iterrows():
        custom_msg = row.get(col_custom_msg, "")
        sig_row = None
        sig_dt = ""
        hs_id_val = row.get(col_hs_id, "")
        if pd.notna(hs_id_val) and str(hs_id_val).strip():
            key = str(hs_id_val).strip()
            sig_row = sig_index.get(key)
        if sig_row is not None and "created at" in sig_row:
            sig_dt = parse_dt(pd.Series([sig_row["created at"]]), args.shift_hours).iloc[0]
        desc_values.append(build_description(custom_msg, sig_row, sig_dt))
    out["description"] = desc_values

    # Optional filter by accounts (keep only existing customers)
    if not accounts_df.empty:
        acc_id_col = None
        for cand in ["ID", "id", "customer id"]:
            if cand in accounts_df.columns:
                acc_id_col = cand; break
        if acc_id_col is None:
            acc_id_col = accounts_df.columns[0]
        valid_ids = set(pd.to_numeric(accounts_df[acc_id_col], errors='coerce').dropna().astype(int).tolist())
        before = len(out)
        out = out[out["customer_id"].isin(valid_ids)].copy()
        removed = before - len(out)
        print(f"Filtered by accounts: kept {len(out)}/{before}, removed {removed} with missing customers.")

    # hash_id stable by customer+id
    out["hash_id"] = out.apply(lambda r: hashlib.md5(f"{r['customer_id']}-{r['id']}".encode("utf-8")).hexdigest(), axis=1)

    cols = ["id","hash_id","customer_id","type","title","created_at","updated_at","description",
            "visible_by_customer","code","terms_month","status"]
    out = out[cols]

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False, encoding="utf-8")

    def sql_q(s):
        if s is None or (isinstance(s, float) and pd.isna(s)):
            return "NULL"
        v = str(s).replace("'", "''")
        return f"'{v}'"
    def sql_q_datetime(s):
        if s is None or (isinstance(s, float) and pd.isna(s)) or str(s).strip() == "":
            return "NULL"
        v = str(s).replace("'", "''")
        return f"'{v}'"

    sql_lines = ["START TRANSACTION;"]
    for _, r in out.iterrows():
        idv = "NULL" if pd.isna(r["id"]) else int(r["id"])
        customer_id = "NULL" if pd.isna(r["customer_id"]) else int(r["customer_id"])
        terms = "NULL" if pd.isna(r["terms_month"]) else int(r["terms_month"])
        line = (
            "INSERT INTO customer_documents "
            "(id, hash_id, added_by, added_by_id, customer_id, type, title, created_at, updated_at, "
            "description, visible_by_customer, code, terms_month, deleted, status) VALUES ("
            f"{idv}, {sql_q(r['hash_id'])}, 'system', 1, {customer_id}, "
            f"{sql_q(r['type'])}, {sql_q(r['title'])}, {sql_q_datetime(r['created_at'])}, {sql_q_datetime(r['updated_at'])}, "
            f"{sql_q(r['description'])}, {sql_q(r['visible_by_customer'])}, {sql_q(r['code'])}, "
            f"{terms}, '0', {sql_q(r['status'])}) "
            "ON DUPLICATE KEY UPDATE "
            "hash_id=VALUES(hash_id), added_by=VALUES(added_by), added_by_id=VALUES(added_by_id), "
            "customer_id=VALUES(customer_id), type=VALUES(type), title=VALUES(title), "
            "created_at=VALUES(created_at), updated_at=VALUES(updated_at), "
            "description=VALUES(description), visible_by_customer=VALUES(visible_by_customer), "
            "code=VALUES(code), terms_month=VALUES(terms_month), deleted=VALUES(deleted), "
            "status=VALUES(status);"
        )
        sql_lines.append(line)
    sql_lines.append("COMMIT;")
    Path(args.sql).write_text("\n".join(sql_lines), encoding="utf-8")

    if args.short_customer:
        short = out[out["customer_id"] == args.short_customer].copy()
        short_csv = Path(args.output).with_name(f"customer_documents_{args.short_customer}.csv")
        short_sql = Path(args.sql).with_name(f"customer_documents_{args.short_customer}.sql")
        short.to_csv(short_csv, index=False, encoding="utf-8")

        sql_lines_s = ["START TRANSACTION;"]
        for _, r in short.iterrows():
            idv = "NULL" if pd.isna(r["id"]) else int(r["id"])
            customer_id = "NULL" if pd.isna(r["customer_id"]) else int(r["customer_id"])
            terms = "NULL" if pd.isna(r["terms_month"]) else int(r["terms_month"])
            line = (
                "INSERT INTO customer_documents "
                "(id, hash_id, added_by, added_by_id, customer_id, type, title, created_at, updated_at, "
                "description, visible_by_customer, code, terms_month, deleted, status) VALUES ("
                f"{idv}, {sql_q(r['hash_id'])}, 'system', 1, {customer_id}, "
                f"{sql_q(r['type'])}, {sql_q(r['title'])}, {sql_q_datetime(r['created_at'])}, {sql_q_datetime(r['updated_at'])}, "
                f"{sql_q(r['description'])}, {sql_q(r['visible_by_customer'])}, {sql_q(r['code'])}, "
                f"{terms}, '0', {sql_q(r['status'])}) "
                "ON DUPLICATE KEY UPDATE "
                "hash_id=VALUES(hash_id), added_by=VALUES(added_by), added_by_id=VALUES(added_by_id), "
                "customer_id=VALUES(customer_id), type=VALUES(type), title=VALUES(title), "
                "created_at=VALUES(created_at), updated_at=VALUES(updated_at), "
                "description=VALUES(description), visible_by_customer=VALUES(visible_by_customer), "
                "code=VALUES(code), terms_month=VALUES(terms_month), deleted=VALUES(deleted), "
                "status=VALUES(status);"
            )
            sql_lines_s.append(line)
        sql_lines_s.append("COMMIT;")
        short_sql.write_text("\n".join(sql_lines_s), encoding="utf-8")
        print(f"Wrote short CSV: {short_csv}")
        print(f"Wrote short SQL: {short_sql}")

    print(f"Wrote CSV: {args.output}")
    print(f"Wrote SQL: {args.sql}")

if __name__ == "__main__":
    main()
