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
    ap = argparse.ArgumentParser(description="Build ticket notes from ticket_comments.csv")
    ap.add_argument("--comments", required=True, help="ticket_comments.csv")
    ap.add_argument("--tickets", required=True, help="tickets.csv (not used, kept for compatibility)")
    ap.add_argument("--imported-tickets", required=True, help="CSV with actually imported tickets (7_4_tickets_out.csv)")
    ap.add_argument("--out", required=True, help="Output CSV")
    ap.add_argument("--shift-hours", type=int, default=0, help="Hour offset for datetime fields")
    args = ap.parse_args()

    com = read_csv_auto(args.comments)

    c_id = find_col(com, ["ID","id"])
    c_ticket = find_col(com, ["ticket id","ticket_id","ticket"])
    c_body = find_col(com, ["body","message","comment","note"])
    c_created = find_col(com, ["created at","created_at","created"])
    c_updated = find_col(com, ["updated at","updated_at","updated"], required=False)
    c_admin_id = find_col(com, ["admin id","admin_id","administrator id","user id"], required=False)

    out = pd.DataFrame()
    dt_created = to_dt(com[c_created], args.shift_hours)
    dt_updated = to_dt(com[c_updated], args.shift_hours) if c_updated else pd.Series([pd.NaT]*len(com))
    out["date"] = dt_created.dt.strftime("%Y-%m-%d").fillna("")
    out["time"] = dt_created.dt.strftime("%H:%M:%S").fillna("")
    out["updated_at"] = fmt_dt(dt_updated)
    out["message"] = com[c_body].fillna("").astype(str)
    out["message_type"] = "note"
    out["source"] = "administration"
    out["hide_for_customer"] = 1
    out["author_type"] = "admin"
    out["ticket_id"] = pd.to_numeric(com[c_ticket], errors="coerce")
    out["admin_id"] = pd.to_numeric(com[c_admin_id], errors="coerce") if c_admin_id else ""

    # Filter by imported tickets
    imported_ids = load_imported_ticket_ids(args.imported_tickets)
    before = len(out)
    out = out[out["ticket_id"].apply(lambda x: pd.notna(x) and int(x) in imported_ids)]
    print(f"Filtered by imported tickets: kept {len(out)}/{before} rows.")

    for c in out.columns:
        out[c] = out[c].astype(object).where(pd.notna(out[c]), "")

    out = out[["date","time","updated_at","message","message_type","source","hide_for_customer","author_type","ticket_id","admin_id"]]
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()