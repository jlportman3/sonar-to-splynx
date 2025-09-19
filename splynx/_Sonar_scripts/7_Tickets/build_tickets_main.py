#!/usr/bin/env python3
import argparse
import pandas as pd
import re
from pathlib import Path

def read_csv_auto(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_csv(path, sep=';')

def resolve_col(df: pd.DataFrame, name_guess: str, alts=None, required=True) -> str:
    alts = (alts or []) + [name_guess]
    cols = {c.strip().lower(): c for c in df.columns}
    for guess in alts:
        key = guess.strip().lower()
        if key in cols:
            return cols[key]
        for k, c in cols.items():
            if re.sub(r'[\s_]+','',k) == re.sub(r'[\s_]+','',key):
                return c
    if required:
        raise KeyError(f"Column '{name_guess}' not found. Available: {list(df.columns)}")
    return None

def parse_dt(series: pd.Series, shift_hours: int = 0) -> pd.Series:
    s = series.astype(str).str.strip().str.replace('T',' ', regex=False)
    s = s.str.replace(r'(Z|[+-]\d{2}:?\d{2})$', '', regex=True)
    dt = pd.to_datetime(s, errors='coerce')
    if shift_hours:
        dt = dt + pd.to_timedelta(shift_hours, unit='h')
    out = dt.dt.strftime('%Y-%m-%d %H:%M:%S')
    return out.fillna('')

def map_status_id(s: pd.Series) -> pd.Series:
    # Sonar -> Splynx status_id
    m = {
        'closed': 3,
        'open': 1,
        'pending_external': 4,
        'pending-internal': 5,
        'pending_internal': 5,
        'pending-in': 5,
        'pending-ex': 4,
        'pending': 4,  # fallback to external
        'solved': 3,   # treat as closed
        'resolved': 3,
        'archived': 3,
    }
    return s.astype(str).str.strip().str.lower().map(lambda x: m.get(x, 1)).astype(int)

def map_priority(s: pd.Series) -> pd.Series:
    m = {'low':'low','medium':'medium','med':'medium','high':'high','critical':'urgent','urgent':'urgent'}
    return s.astype(str).str.strip().str.lower().map(lambda x: m.get(x, 'medium'))

def main():
    ap = argparse.ArgumentParser(description="Build Splynx tickets.csv from Sonar tickets.csv")
    ap.add_argument('--tickets', required=True, help='Path to Sonar tickets.csv')
    ap.add_argument('--accounts', required=False, help='Optional accounts.csv to validate customer IDs')
    ap.add_argument('--out', required=True, help='Path to write tickets_out.csv')
    ap.add_argument('--shift-hours', type=int, default=0, help='Hour offset for datetime fields')
    args = ap.parse_args()

    tdf = read_csv_auto(args.tickets)
    adf = read_csv_auto(args.accounts) if args.accounts else pd.DataFrame()

    # Resolve columns
    col_id = resolve_col(tdf, 'ID', ['id'])
    col_created = resolve_col(tdf, 'created at', ['created','created_at'])
    col_updated = resolve_col(tdf, 'updated at', ['updated','updated_at'], required=False)
    col_priority = resolve_col(tdf, 'priority', ['ticket priority'], required=False)
    col_status = resolve_col(tdf, 'status', ['state'])
    col_subject = resolve_col(tdf, 'subject', ['title','name'])
    col_group_id = resolve_col(tdf, 'ticket group ID', ['ticket group id','group id','group'], required=False)
    col_user_id = resolve_col(tdf, 'user ID', ['user id','assigned to id','assignee id','administrator id'], required=False)
    col_ticketable_id = resolve_col(tdf, 'ticketable ID', ['account id','customer id'], required=False)
    col_ticketable_type = resolve_col(tdf, 'ticketable type', ['ticket owner type','owner type','notable type'], required=False)
    col_category_id = resolve_col(tdf, 'ticket category ID', ['ticket category id','category id','type id'], required=False)

    out = pd.DataFrame()
    out['id'] = pd.to_numeric(tdf[col_id], errors='coerce').astype('Int64')
    out['created_at'] = parse_dt(tdf[col_created], args.shift_hours)
    out['updated_at'] = parse_dt(tdf[col_updated], args.shift_hours) if col_updated else ''
    out['priority'] = map_priority(tdf[col_priority]) if col_priority else 'medium'
    out['status_id'] = map_status_id(tdf[col_status])
    out['subject'] = tdf[col_subject].fillna('').astype(str)
    out['group_id'] = pd.to_numeric(tdf[col_group_id], errors='coerce').astype('Int64') if col_group_id else pd.Series([pd.NA]*len(tdf), dtype='Int64')
    out['reporter_id'] = ''  # per your spec
    out['reporter_type'] = 'admin'  # default
    out['assign_to'] = pd.to_numeric(tdf[col_user_id], errors='coerce').astype('Int64') if col_user_id else pd.Series([pd.NA]*len(tdf), dtype='Int64')

    # customer_id only if ticketable_type == 'Account'
    cust = pd.Series([pd.NA]*len(tdf), dtype='Int64')
    if col_ticketable_id and col_ticketable_type:
        is_acc = tdf[col_ticketable_type].astype(str).str.strip().str.lower().eq('account')
        cust = pd.to_numeric(tdf.loc[is_acc, col_ticketable_id], errors='coerce').astype('Int64')
        cust = cust.reindex(tdf.index)  # align index
    out['customer_id'] = cust

    # type_id: use Sonar category id if present, else 1
    if col_category_id:
        type_id = pd.to_numeric(tdf[col_category_id], errors='coerce').astype('Int64').fillna(1).astype(int)
    else:
        type_id = pd.Series([1]*len(tdf), dtype=int)
    out['type_id'] = type_id

    # closed flag if status == CLOSED
    closed = tdf[col_status].astype(str).str.strip().str.upper().eq('CLOSED').astype(int)
    out['closed'] = closed

    # Accounts filter (optional): keep only existing customers (but allow blank customer_id)
    if not adf.empty:
        # detect ID column
        acc_id_col = None
        for c in ['ID','id','customer id']:
            if c in adf.columns:
                acc_id_col = c; break
        if acc_id_col is None:
            acc_id_col = adf.columns[0]
        valid_ids = set(pd.to_numeric(adf[acc_id_col], errors='coerce').dropna().astype(int).tolist())
        before = len(out)
        mask_ok = out['customer_id'].isna() | out['customer_id'].isin(valid_ids)
        out = out[mask_ok].copy()
        print(f"Tickets filtered by accounts: kept {len(out)}/{before}, removed {before-len(out)} (non-existing customers).")

    # Drop rows with missing id
    out = out[~out['id'].isna()].copy()

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding='utf-8')
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == '__main__':
    main()
