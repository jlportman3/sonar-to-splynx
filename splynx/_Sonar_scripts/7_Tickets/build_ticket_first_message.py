#!/usr/bin/env python3
import argparse
import pandas as pd
from pathlib import Path
import re

def read_csv_auto(path: str) -> pd.DataFrame:
    p = Path(path)
    try:
        return pd.read_csv(p)
    except Exception:
        return pd.read_csv(p, sep=';')

def norm_cols(df: pd.DataFrame):
    return {c: c for c in df.columns}

def find_col(df: pd.DataFrame, candidates, required=True):
    cmap = {re.sub(r'[\s_]+','', c.strip().lower()): c for c in df.columns}
    for name in candidates:
        key = re.sub(r'[\s_]+','', name.strip().lower())
        if key in cmap:
            return cmap[key]
    if required:
        raise KeyError(f"Column not found; tried {candidates}. Available: {list(df.columns)}")
    return None

def to_dt(s: pd.Series, shift: int):
    dt = pd.to_datetime(s, errors='coerce')
    if shift:
        dt = dt + pd.to_timedelta(shift, unit='h')
    return dt

def fmt_dt(s: pd.Series):
    return s.dt.strftime("%Y-%m-%d %H:%M:%S").fillna("")

def load_imported_ticket_ids(path: str) -> set:
    df = read_csv_auto(path)
    col = find_col(df, ["ticket id","ticket_id","id","ID"])
    return set(pd.to_numeric(df[col], errors="coerce").dropna().astype(int).tolist())

def main():
    ap = argparse.ArgumentParser(description="Build first ticket message (note) from tickets.csv")
    ap.add_argument("--tickets", required=True, help="tickets.csv (original Sonar)")
    ap.add_argument("--imported-tickets", required=True, help="CSV with actually imported tickets (7_4_tickets_out.csv)")
    ap.add_argument("--out", required=True, help="Output CSV")
    ap.add_argument("--shift-hours", type=int, default=0, help="Hour offset for datetime fields")
    args = ap.parse_args()

    tickets = read_csv_auto(args.tickets)
    tid_col = find_col(tickets, ["ID","id","ticket id","ticket_id"])
    created_col = find_col(tickets, ["created at","created_at","created"])
    updated_col = find_col(tickets, ["updated at","updated_at","updated"], required=False)
    desc_col = find_col(tickets, ["description","body","message"], required=False)
    t_id = pd.to_numeric(tickets[tid_col], errors="coerce")

    out = pd.DataFrame()
    created = to_dt(tickets[created_col], args.shift_hours)
    updated = to_dt(tickets[updated_col], args.shift_hours) if updated_col else pd.Series([pd.NaT]*len(tickets))
    out["date"] = created.dt.strftime("%Y-%m-%d").fillna("")
    out["time"] = created.dt.strftime("%H:%M:%S").fillna("")
    out["updated_at"] = fmt_dt(updated)
    out["mail_cc"] = ""
    out["mail_to"] = ""
    out["customer_id"] = 0
    out["incoming_customer_id"] = 1
    out["hide_for_customer"] = 1
    out["author_type"] = "customer"
    out["message"] = tickets[desc_col].fillna("").astype(str) if desc_col else ""
    out["ticket_id"] = t_id
    out["admin_id"] = 0
    out["message_type"] = "note"
    out["source"] = "incoming"

    # Filter by imported tickets list
    imported_ids = load_imported_ticket_ids(args.imported_tickets)
    before = len(out)
    out = out[out["ticket_id"].apply(lambda x: pd.notna(x) and int(x) in imported_ids)]
    print(f"Filtered by imported tickets: kept {len(out)}/{before} rows.")

    # Ensure empty strings instead of NaN
    for c in out.columns:
        out[c] = out[c].astype(object).where(pd.notna(out[c]), "")

    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()