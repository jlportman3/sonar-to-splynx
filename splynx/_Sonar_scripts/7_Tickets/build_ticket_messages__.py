
#!/usr/bin/env python3
import argparse
import pandas as pd
from pathlib import Path
import re

def read_csv_auto(p: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(p)
    except Exception:
        return pd.read_csv(p, sep=';')

def resolve_col(df: pd.DataFrame, name: str, alts=None, required=True) -> str:
    alts = (alts or []) + [name]
    cmap = {c.strip().lower(): c for c in df.columns}
    for g in alts:
        k = g.strip().lower()
        if k in cmap:
            return cmap[k]
        for ck, cn in cmap.items():
            if re.sub(r'[\s_]+','', ck) == re.sub(r'[\s_]+','', k):
                return cn
    if required:
        raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")
    return None

def to_dt(series: pd.Series, shift_hours: int = 0) -> pd.Series:
    s = pd.to_datetime(series, errors='coerce')
    if shift_hours:
        s = s + pd.to_timedelta(shift_hours, unit='h')
    return s

def normalize_email(s: str) -> str:
    return (s or "").strip().lower()

def main():
    ap = argparse.ArgumentParser(description="Build ticket_messages.csv from ticket_replies.csv with ticket/account filtering")
    ap.add_argument("--replies", required=True, help="ticket_replies.csv")
    ap.add_argument("--tickets", required=True, help="tickets.csv for filtering valid ticket IDs")
    ap.add_argument("--accounts", required=True, help="accounts.csv for validating customers")
    ap.add_argument("--contacts", required=False, help="contacts.csv (optional, for customer mapping)")
    ap.add_argument("--incoming-customer", required=False, help="incoming_customer.csv (optional, for incoming_customer_id)")
    ap.add_argument("--out", required=True, help="Output CSV")
    ap.add_argument("--shift-hours", type=int, default=0, help="Shift datetime columns by N hours")
    args = ap.parse_args()

    r = read_csv_auto(Path(args.replies))
    t = read_csv_auto(Path(args.tickets))
    a = read_csv_auto(Path(args.accounts))
    c = read_csv_auto(Path(args.contacts)) if args.contacts else None
    inc = read_csv_auto(Path(args.incoming_customer)) if args.incoming_customer else None

    # valid accounts
    a_id = resolve_col(a, "ID", ["id","account id","customer id"])
    valid_accounts = set(pd.to_numeric(a[a_id], errors='coerce').dropna().astype(int).tolist())

    # valid tickets
    t_id = resolve_col(t, "ID", ["id","ticket id"])
    try:
        t_type = resolve_col(t, "ticketable type", ["owner type","source type"])
        t_acc = resolve_col(t, "ticketable ID", ["owner id","source id"])
        t_mask = t[t_type].astype(str).str.strip().str.lower().eq("account") & pd.to_numeric(t[t_acc], errors='coerce').isin(valid_accounts)
        valid_tickets = set(pd.to_numeric(t.loc[t_mask, t_id], errors='coerce').dropna().astype(int).tolist())
    except KeyError:
        valid_tickets = set()

    # replies cols
    r_tid = resolve_col(r, "ticket ID", ["ticket id","id ticket"])
    r_created = resolve_col(r, "created at", ["created","created_at"])
    r_updated = resolve_col(r, "updated at", ["updated","updated_at"], required=False)
    r_body = resolve_col(r, "body", ["message","text"])
    r_admin_id = resolve_col(r, "admin_id", ["admin id","user id"], required=False)
    r_cust_id = resolve_col(r, "customer_id", ["customer id","account id"], required=False)
    r_author = resolve_col(r, "author", ["from","sender"], required=False)
    r_author_email = resolve_col(r, "author email", ["author_email","from email","sender email"], required=False)

    # Filter only valid tickets
    r2 = r[pd.to_numeric(r[r_tid], errors='coerce').isin(valid_tickets)].copy()

    # datetime
    created = to_dt(r2[r_created], args.shift_hours)
    updated = to_dt(r2[r_updated], args.shift_hours) if r_updated else pd.Series([pd.NaT]*len(r2))

    out = pd.DataFrame()
    out["date"] = created.dt.strftime("%Y-%m-%d").fillna("")
    out["time"] = created.dt.strftime("%H:%M:%S").fillna("")
    out["updated_at"] = updated.dt.strftime("%Y-%m-%d %H:%M:%S").fillna("")
    out["mail_cc"] = ""
    out["mail_to"] = (r2[r_author_email].fillna("").astype(str) if r_author_email else "")
    out["customer_id"] = (pd.to_numeric(r2[r_cust_id], errors='coerce').astype(object).where(lambda s: s.notna(), "") if r_cust_id else "")
    # incoming_customer_id
    if inc is not None and r_author_email:
        ic_email = resolve_col(inc, "email", ["author email","mail_to","mail to"])
        ic_id = resolve_col(inc, "id", ["ID"])
        ic_map = {normalize_email(e): i for e, i in zip(inc[ic_email].astype(str), inc[ic_id])}
        out["incoming_customer_id"] = r2[r_author_email].astype(str).map(lambda e: ic_map.get(normalize_email(e), ""))
    else:
        out["incoming_customer_id"] = ""
    # message & ids
    out["message"] = r2[r_body].fillna("").astype(str)
    out["ticket_id"] = pd.to_numeric(r2[r_tid], errors='coerce').astype(object).where(lambda s: s.notna(), "")
    out["admin_id"] = (pd.to_numeric(r2[r_admin_id], errors='coerce').astype(object).where(lambda s: s.notna(), "") if r_admin_id else "")
    out["message_type"] = "message"
    # source
    def _source(row):
        if str(row.get("incoming_customer_id","")).strip() != "" or (str(row.get("customer_id","")).strip() not in ("", "0")):
            return "incoming"
        return "administration"
    out["source"] = out.apply(_source, axis=1)
    # author_type
    def _author_type(row):
        try:
            if str(row["incoming_customer_id"]).strip() != "":
                return "customer"
            cid = row.get("customer_id", "")
            if cid != "" and int(float(cid)) > 0:
                return "customer"
        except Exception:
            pass
        return "admin" if (not (row.get("admin_id","") in ("", None))) else "system"
    out["author_type"] = out.apply(_author_type, axis=1)

    out = out[[
        "date","time","updated_at","mail_cc","mail_to","customer_id","incoming_customer_id",
        "author_type","message","ticket_id","admin_id","message_type","source"
    ]]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()
