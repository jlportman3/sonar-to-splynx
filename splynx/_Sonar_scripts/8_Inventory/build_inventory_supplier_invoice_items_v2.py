
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
    def norm(s: str) -> str:
        return re.sub(r'[^0-9a-z]+','', str(s).lower())
    cmap = {norm(c): c for c in df.columns}
    for g in alts:
        key = norm(g)
        if key in cmap:
            return cmap[key]
    if required:
        raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")
    return None

def main():
    ap = argparse.ArgumentParser(description="Build inventory_supplier_invoices_items from purchase_order_items + vendor_items + inventory_models")
    ap.add_argument("--purchase-items", required=True, help="purchase_order_items.csv")
    ap.add_argument("--vendor-items", required=True, help="vendor_items.csv")
    ap.add_argument("--inventory-models", required=False, help="inventory_models.csv (optional, for validation)")
    ap.add_argument("--out", required=True, help="Output CSV inventory_supplier_invoices_items")
    args = ap.parse_args()

    poi = read_csv_auto(Path(args.purchase_items))
    vi = read_csv_auto(Path(args.vendor_items))
    im = read_csv_auto(Path(args.inventory_models)) if args.inventory_models else None

    # Resolve columns in purchase_order_items
    p_id = resolve_col(poi, "ID", ["id"])
    p_po_id = resolve_col(poi, "purchase order ID", ["purchase order id","po id","order id"])
    p_vendor_item_id = resolve_col(poi, "vendor item ID", ["vendor item id","vendor_item_id","vendoritem_id","vendor item id."])
    p_qty_per_unit = resolve_col(poi, "quantity per unit", ["qty per unit","quantity_per_unit","quantity"])
    p_system_units = resolve_col(poi, "system of units", ["system of units","units per system","units"], required=False)
    p_price = resolve_col(poi, "price", ["unit price","price cents","price (cents)"])

    # Resolve columns in vendor_items
    v_id = resolve_col(vi, "ID", ["id"])
    v_vendoritemable_type = resolve_col(vi, "vendoritemable type", ["vendor itemable type","itemable type","type"])
    v_vendoritemable_id = resolve_col(vi, "vendoritemable ID", ["vendor itemable id","itemable id","target id"])

    # Build mapping: vendor item ID -> product_id (inventory model ID) when type == InventoryModel
    vi_filtered = vi[vi[v_vendoritemable_type].astype(str).str.replace(r'\s+', '', regex=True).str.lower().eq("inventorymodel")].copy()
    vendor_to_model = dict(zip(pd.to_numeric(vi_filtered[v_id], errors="coerce"), pd.to_numeric(vi_filtered[v_vendoritemable_id], errors="coerce")))

    # Optional: validate against inventory_models
    valid_models = set()
    if im is not None and not im.empty:
        im_id = resolve_col(im, "ID", ["id"])
        valid_models = set(pd.to_numeric(im[im_id], errors="coerce").dropna().astype(int).tolist())

    # Compute quantity = quantity per unit * system of units
    qty_per_unit = pd.to_numeric(poi[p_qty_per_unit], errors="coerce").fillna(0)
    if p_system_units:
        system_units = pd.to_numeric(poi[p_system_units], errors="coerce").fillna(1)
    else:
        system_units = pd.Series([1]*len(poi), dtype="int64")
    quantity = qty_per_unit * system_units

    # price = price / 100
    price = pd.to_numeric(poi[p_price], errors="coerce") / 100.0

    out = pd.DataFrame()
    out["id"] = pd.to_numeric(poi[p_id], errors="coerce")
    out["supplier_invoice_id"] = pd.to_numeric(poi[p_po_id], errors="coerce")
    # product_id from vendor item mapping
    vi_ids = pd.to_numeric(poi[p_vendor_item_id], errors="coerce")
    prod = vi_ids.map(vendor_to_model)
    if valid_models:
        prod = prod.where(prod.isin(valid_models), pd.NA)
    out["product_id"] = prod

    out["quantity"] = quantity
    out["price"] = price

    # Final order
    cols = ["id","supplier_invoice_id","product_id","quantity","price"]
    out = out[cols]

    # Convert NaNs to empty strings per your convention
    for c in out.columns:
        if out[c].dtype.kind in "iufc":
            out[c] = out[c].astype(object).where(pd.notna(out[c]), "")
        else:
            out[c] = out[c].fillna("")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()
