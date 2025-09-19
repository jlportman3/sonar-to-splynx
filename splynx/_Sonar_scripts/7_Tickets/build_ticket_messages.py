
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
    for g in alts:
        k = g.strip().lower()
        if k in cols:
            return cols[k]
        for low, orig in cols.items():
            if re.sub(r'[\s_]+','', low) == re.sub(r'[\s_]+','', k):
                return orig
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

def normalize_email_series(s: pd.Series) -> pd.Series:
    return s.fillna('').astype(str).str.strip().str.lower()

def main():
    ap = argparse.ArgumentParser(description="Build Splynx ticket_messages.csv from Sonar ticket_replies.csv")
    ap.add_argument('--replies', required=True, help='Path to ticket_replies.csv')
    ap.add_argument('--tickets', required=True, help='Path to tickets.csv (to find customer/account)')
    ap.add_argument('--imported-tickets', required=True, help='CSV with actually imported tickets')
    ap.add_argument('--accounts', required=False, help='Optional accounts.csv to validate customer IDs')
    ap.add_argument('--contacts', required=False, help='Optional contacts.csv to map author email -> customer_id')
    ap.add_argument('--incoming', required=False, help='Optional incoming_customer.csv (id,email,name,customer_id)')
    ap.add_argument('--out', required=True, help='Output ticket_messages_out.csv')
    ap.add_argument('--shift-hours', type=int, default=0, help='Hour offset for datetime fields')
    args = ap.parse_args()

    rdf = read_csv_auto(args.replies)
    tdf = read_csv_auto(args.tickets)
    itf = read_csv_auto(args.imported_tickets)
    idf = read_csv_auto(args.incoming) if args.incoming else pd.DataFrame()
    adf = read_csv_auto(args.accounts) if args.accounts else pd.DataFrame()
    cdf = read_csv_auto(args.contacts) if args.contacts else pd.DataFrame()

    it_id = resolve_col(itf, 'id', ['ID','ticket id','ticket_id'])
    imported_ids = set(pd.to_numeric(itf[it_id], errors='coerce').dropna().astype(int).tolist())

    r_ticket_id = resolve_col(rdf, 'ticket ID', ['ticket id','ticket_id'])
    r_body = resolve_col(rdf, 'body', ['message'])
    r_author_email = resolve_col(rdf, 'author email', ['author_email','email'], required=False)
    r_admin_id = resolve_col(rdf, 'admin ID', ['admin id','administrator id','user id'], required=False)
    r_created = resolve_col(rdf, 'created at', ['created','created_at'])
    r_updated = resolve_col(rdf, 'updated at', ['updated','updated_at'], required=False)

    out = pd.DataFrame()
    created = parse_dt(rdf[r_created], args.shift_hours)
    out['date'] = created.str.slice(0,10)
    out['time'] = created.str.slice(11,19)
    out['updated_at'] = parse_dt(rdf[r_updated], args.shift_hours) if r_updated else ''
    author_email_series = rdf[r_author_email].fillna('').astype(str) if r_author_email else pd.Series(['']*len(rdf))
    out['mail_cc'] = ''
    out['mail_to'] = author_email_series.str.strip()
    out['message'] = rdf[r_body].fillna('').astype(str)
    out['ticket_id'] = pd.to_numeric(rdf[r_ticket_id], errors='coerce').astype('Int64')
    out['admin_id'] = pd.to_numeric(rdf[r_admin_id], errors='coerce').astype('Int64') if r_admin_id else pd.Series([pd.NA]*len(rdf), dtype='Int64')

    # customer_id from tickets when Account
    t_id = resolve_col(tdf, 'ID', ['id'])
    t_ticketable_id = resolve_col(tdf, 'ticketable ID', ['account id','customer id'], required=False)
    t_ticketable_type = resolve_col(tdf, 'ticketable type', ['ticket owner type','owner type','notable type'], required=False)
    out['customer_id'] = 0
    if t_ticketable_id is not None and t_ticketable_type is not None:
        tmap = tdf.copy()
        tmap['_tid'] = pd.to_numeric(tmap[t_id], errors='coerce').astype('Int64')
        is_acc = tmap[t_ticketable_type].astype(str).str.strip().str.lower().eq('account')
        tmap = tmap.loc[is_acc, ['_tid', t_ticketable_id]].dropna()
        tmap['_cid'] = pd.to_numeric(tmap[t_ticketable_id], errors='coerce').astype('Int64')
        tid_to_cid = dict(zip(tmap['_tid'].dropna().astype(int), tmap['_cid'].dropna().astype(int)))
        out['customer_id'] = out['ticket_id'].map(lambda x: tid_to_cid.get(int(x), 0) if pd.notna(x) else 0)

    # Optional contacts mapping
    if not cdf.empty and r_author_email:
        email_col = None; oid_col = None; co_col = None
        for c in cdf.columns:
            lc = c.strip().lower()
            if lc in ('email address','email','author email'): email_col = c
            if lc in ('contact owner id','owner id','ticketable id'): oid_col = c
            if lc in ('contact owner','owner','noteable type','notable type'): co_col = c
        if email_col and oid_col:
            tmp = cdf[[email_col, oid_col]].copy()
            if co_col:
                tmp = tmp[cdf[co_col].astype(str).str.strip().str.lower().eq('account')]
            tmp['_email_lc'] = normalize_email_series(tmp[email_col])
            email_to_acc = dict(zip(tmp['_email_lc'], pd.to_numeric(tmp[oid_col], errors='coerce').fillna(0).astype(int)))
            pe = normalize_email_series(author_email_series)
            mapped = pe.map(lambda e: int(email_to_acc.get(e, 0)))
            cur = out['customer_id'].fillna(0).astype(int)
            out['customer_id'] = cur.where(cur != 0, mapped)

    # Validate by accounts if provided
    if not adf.empty:
        acc_id_col = None
        for c in ['ID','id','customer id']:
            if c in adf.columns:
                acc_id_col = c; break
        if acc_id_col is None:
            acc_id_col = adf.columns[0]
        valid_ids = set(pd.to_numeric(adf[acc_id_col], errors='coerce').dropna().astype(int).tolist())
        out['customer_id'] = out['customer_id'].map(lambda v: int(v) if int(v) in valid_ids else 0)

    # incoming mapping
    out['incoming_customer_id'] = pd.Series([pd.NA]*len(rdf), dtype='Int64')
    if not idf.empty:
        cols = {c.lower(): c for c in idf.columns}
        id_col = cols.get('id')
        email_col = cols.get('email')
        cust_col = cols.get('customer_id') or cols.get('customer id')
        if id_col and email_col:
            tmp = idf[[id_col, email_col]].copy()
            tmp[email_col] = normalize_email_series(tmp[email_col])
            email_to_inc = dict(zip(tmp[email_col], pd.to_numeric(tmp[id_col], errors='coerce').astype('Int64')))
            pe = normalize_email_series(author_email_series)
            out['incoming_customer_id'] = pe.map(email_to_inc)
        if cust_col:
            tmpc = idf[[email_col, cust_col]].copy()
            tmpc[email_col] = normalize_email_series(tmpc[email_col])
            email_to_cust = dict(zip(tmpc[email_col], pd.to_numeric(tmpc[cust_col], errors='coerce').fillna(0).astype(int)))
            pe = normalize_email_series(author_email_series)
            mapped_cust = pe.map(lambda e: int(email_to_cust.get(e, 0)))
            cur = out['customer_id'].fillna(0).astype(int)
            out['customer_id'] = cur.where(cur != 0, mapped_cust)

    # author_type/source
    out['author_type'] = 'system'
    has_admin = out['admin_id'].notna()
    out.loc[has_admin, 'author_type'] = 'admin'
    has_inc = out['incoming_customer_id'].notna()
    has_cust = out['customer_id'].fillna(0).astype(int) > 0
    out.loc[has_inc | has_cust, 'author_type'] = 'customer'
    out['source'] = 'administration'
    out.loc[has_inc | has_cust, 'source'] = 'incoming'
    out['message_type'] = 'message'
    out['hide_for_customer'] = 0

    # Filter by imported tickets
    before = len(out)
    out = out[out['ticket_id'].apply(lambda x: int(x) in imported_ids if pd.notna(x) else False)].copy()
    print(f"Filtered by imported tickets: kept {len(out)}/{before} rows")

    cols = ['date','time','updated_at','mail_cc','mail_to','customer_id','incoming_customer_id',
            'hide_for_customer','author_type','message','ticket_id','admin_id','message_type','source']
    out = out[cols]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding='utf-8')
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == '__main__':
    main()
