
#!/usr/bin/env python3
import argparse
import pandas as pd
import re
from pathlib import Path

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

def to_date(series: pd.Series, shift_hours: int = 0) -> pd.Series:
    s = pd.to_datetime(series, errors='coerce')
    if shift_hours:
        s = s + pd.to_timedelta(shift_hours, unit='h')
    return s.dt.strftime('%Y-%m-%d').fillna('')

def main():
    ap = argparse.ArgumentParser(description="Build inventory_supplier_invoices from purchase_orders.csv")
    ap.add_argument("--orders", required=True, help="purchase_orders.csv")
    ap.add_argument("--out", required=True, help="Output CSV inventory_supplier_invoices")
    ap.add_argument("--shift-hours", type=int, default=0, help="Shift created_at by N hours before formatting date")
    args = ap.parse_args()

    df = read_csv_auto(Path(args.orders))

    c_id = resolve_col(df, "ID", ["id"])
    c_vendor = resolve_col(df, "vendor ID", ["vendor id","supplier id","supplier ID"])
    c_order_no = resolve_col(df, "order number", ["order no","po number","po #","number"])
    c_created = resolve_col(df, "created at", ["created","created_at","date"])

    out = pd.DataFrame()
    out["id"] = pd.to_numeric(df[c_id], errors="coerce")
    out["supplier_id"] = pd.to_numeric(df[c_vendor], errors="coerce")
    out["original_invoice_number"] = df[c_order_no].fillna("").astype(str)
    out["date"] = to_date(df[c_created], args.shift_hours)

    # Clean NaNs to empty strings where appropriate
    for col in ["id","supplier_id"]:
        out[col] = out[col].astype(object).where(pd.notna(out[col]), "")
    out = out[["id","supplier_id","original_invoice_number","date"]]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()
