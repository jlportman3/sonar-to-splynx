#!/usr/bin/env python3
import argparse
import pandas as pd
from pathlib import Path
import re

def read_csv_auto(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_csv(path, sep=';')

def resolve_col(df: pd.DataFrame, wanted: str, alts=None, required=True) -> str:
    alts = (alts or []) + [wanted]
    # build map lower->orig
    cmap = {c.lower().strip(): c for c in df.columns}
    def norm(s): return re.sub(r'[\s_]+', ' ', s.lower().strip())
    for name in alts:
        key = norm(name)
        for k, orig in cmap.items():
            if norm(k) == key:
                return orig
        # try contains-style
        for orig in df.columns:
            if norm(orig) == key:
                return orig
    if required:
        raise KeyError(f"Column '{wanted}' not found in {list(df.columns)}")
    return None

def main():
    ap = argparse.ArgumentParser(description="Build inventory_supplier_invoices_items from purchase_order_items + vendor_items")
    ap.add_argument("--purchase-items", required=True, help="purchase_order_items.csv")
    ap.add_argument("--vendor-items", required=True, help="vendor_items.csv")
    ap.add_argument("--inventory-models", required=False, help="inventory_models.csv (optional, for validation)")
    ap.add_argument("--out", required=True, help="Output CSV")
    args = ap.parse_args()

    poi = read_csv_auto(Path(args.purchase_items))
    vi = read_csv_auto(Path(args.vendor_items))
    im = read_csv_auto(Path(args.inventory_models)) if args.inventory_models else None

    # Resolve columns in purchase_order_items
    c_id = resolve_col(poi, "ID", ["id"])
    c_po_id = resolve_col(poi, "purchase order ID", ["purchase order id","order id"])
    c_vendor_item_id = resolve_col(poi, "vendor item ID", ["vendor item id","vendor_item_id","vendor item id."])
    c_qty_per = resolve_col(poi, "quantity per unit", ["quantity per unit","qty per unit","quantity"])
    c_units = resolve_col(poi, "system of units", ["system of units","units per system","units"], required=False)
    c_price = resolve_col(poi, "price", ["unit price","price cents","amount"])
    c_tax = resolve_col(poi, "calculated tax", ["calculated tax","tax"], required=False)

    # Resolve columns in vendor_items
    v_id = resolve_col(vi, "ID", ["id","vendor item id"])
    v_type = resolve_col(vi, "vendoritemable type", ["vendoritemable type","itemable type","type"])
    v_model_id = resolve_col(vi, "vendoritemable ID", ["vendoritemable id","itemable id","model id"])

    # optional validation against inventory_models
    valid_models = None
    if im is not None:
        m_id = resolve_col(im, "ID", ["id"])
        valid_models = set(pd.to_numeric(im[m_id], errors="coerce").dropna().astype(int).tolist())

    # Map vendor item -> product_id (inventory model id) only where type == InventoryModel
    vi_filtered = vi[vi[v_type].astype(str).str.strip().str.lower() == "inventorymodel"].copy()
    vendor_to_model = dict(zip(pd.to_numeric(vi_filtered[v_id], errors="coerce"),
                               pd.to_numeric(vi_filtered[v_model_id], errors="coerce")))

    # Build output
    out = pd.DataFrame()
    out["id"] = pd.to_numeric(poi[c_id], errors="coerce")
    out["supplier_invoice_id"] = pd.to_numeric(poi[c_po_id], errors="coerce")

    vend_ids = pd.to_numeric(poi[c_vendor_item_id], errors="coerce")
    product_ids = vend_ids.map(vendor_to_model)
    # optionally blank out non-existing models
    if valid_models is not None:
        product_ids = product_ids.where(product_ids.isin(valid_models), other=pd.NA)

    out["product_id"] = product_ids

    qty_per = pd.to_numeric(poi[c_qty_per], errors="coerce").fillna(0)
    if c_units:
        units = pd.to_numeric(poi[c_units], errors="coerce").fillna(1)
    else:
        units = 1
    out["quantity"] = (qty_per * units).fillna(0)

    price = pd.to_numeric(poi[c_price], errors="coerce").fillna(0)
    tax = pd.to_numeric(poi[c_tax], errors="coerce").fillna(0) if c_tax else 0
    out["price"] = ((price + tax) / 100).round(6)

    # Clean: empty string for NaNs where needed
    for col in ["product_id"]:
        out[col] = out[col].astype(object).where(pd.notna(out[col]), "")

    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()
