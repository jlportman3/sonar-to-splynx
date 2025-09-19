#!/usr/bin/env python3
import argparse
import pandas as pd
import re
from pathlib import Path

def read_csv_auto(p: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(p)
    except Exception:
        return pd.read_csv(p, sep=";")

def resolve_col(df: pd.DataFrame, name: str, alts=None, required=True) -> str:
    alts = (alts or []) + [name]
    cmap = {c.strip().lower(): c for c in df.columns}
    for g in alts:
        k = g.strip().lower()
        if k in cmap:
            return cmap[k]
        for ck, cn in cmap.items():
            if re.sub(r"[\\s_]+","", ck) == re.sub(r"[\\s_]+","", k):
                return cn
    if required:
        raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")
    return None

def build_vendors(manufacturers_csv: Path, out_csv: Path):
    if not manufacturers_csv.exists():
        print(f"[WARN] {manufacturers_csv} not found. Skipping inventory_vendors.")
        return
    df = read_csv_auto(manufacturers_csv)
    col_id = resolve_col(df, "ID", ["id"])
    col_name = resolve_col(df, "name", ["Name","title","manufacturer"])
    out = pd.DataFrame({
        "id": pd.to_numeric(df[col_id], errors="coerce").astype("Int64"),
        "name": df[col_name].fillna("").astype(str),
    })
    out = out[~out["id"].isna()].copy()
    out.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"[OK] Wrote vendors -> {out_csv} ({len(out)} rows)")

def build_categories(model_categories_csv: Path, out_csv: Path):
    df = read_csv_auto(model_categories_csv)
    col_id = resolve_col(df, "ID", ["id"])
    col_name = resolve_col(df, "name", ["Name","title","category name"])
    out = pd.DataFrame({
        "id": pd.to_numeric(df[col_id], errors="coerce").astype("Int64"),
        "title": df[col_name].fillna("").astype(str),
    })
    out = out[~out["id"].isna()].copy()
    out.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"[OK] Wrote categories -> {out_csv} ({len(out)} rows)")

def build_products(models_csv: Path, out_csv: Path):
    df = read_csv_auto(models_csv)
    col_id = resolve_col(df, "ID", ["id"])
    col_name = resolve_col(df, "name", ["Name","model","product name"])
    col_model_name = resolve_col(df, "model name", ["model Name","Model name","model_name","model"], required=False)
    col_manu_id = resolve_col(df, "manufacturer ID", ["manufacturer id","vendor id"], required=False)
    col_cat_id = resolve_col(df, "inventory model category ID", ["inventory model category id","category id"], required=False)

    name = df[col_name].fillna("").astype(str).str.strip()
    if col_model_name:
        model = df[col_model_name].fillna("").astype(str).str.strip()
        composed = name.where((model == "") | (name.str.lower() == model.str.lower()), name + " (" + model + ")")
    else:
        composed = name

    out = pd.DataFrame({
        "id": pd.to_numeric(df[col_id], errors="coerce").astype("Int64"),
        "name": composed,
        "vendor_id": pd.to_numeric(df[col_manu_id], errors="coerce").astype("Int64") if col_manu_id else pd.Series([pd.NA]*len(df), dtype="Int64"),
        "category_id": pd.to_numeric(df[col_cat_id], errors="coerce").astype("Int64") if col_cat_id else pd.Series([pd.NA]*len(df), dtype="Int64"),
    })
    out = out[~out["id"].isna()].copy()
    out.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"[OK] Wrote products -> {out_csv} ({len(out)} rows)")

def build_stocks(inv_locations_csv: Path, internal_locations_csv: Path, generic_assignees_csv: Path, vehicles_csv: Path, network_sites_csv: Path, out_csv: Path):
    frames = []

    # Inventory locations -> type 0
    if inv_locations_csv.exists():
        df = read_csv_auto(inv_locations_csv)
        col_name = resolve_col(df, "name", ["Name","location name","title"])
        frames.append(pd.DataFrame({"name": df[col_name].fillna("").astype(str).str.strip(), "type": 0}))
    else:
        print(f"[WARN] {inv_locations_csv} not found. Skipping locations.")

    # Internal locations -> type 4
    if internal_locations_csv.exists():
        df = read_csv_auto(internal_locations_csv)
        col_name = resolve_col(df, "name", ["Name","location name","title"])
        frames.append(pd.DataFrame({"name": df[col_name].fillna("").astype(str).str.strip(), "type": 4}))
    else:
        print(f"[WARN] {internal_locations_csv} not found. Skipping internal locations.")

    # Generic inventory assignees -> type 4
    if generic_assignees_csv.exists():
        df = read_csv_auto(generic_assignees_csv)
        try:
            col_name = resolve_col(df, "name", ["Name","title","label"])
        except Exception:
            col_name = resolve_col(df, "label", ["name","Name","title"])
        frames.append(pd.DataFrame({"name": df[col_name].fillna("").astype(str).str.strip(), "type": 4}))
    else:
        print(f"[WARN] {generic_assignees_csv} not found. Skipping generic assignees.")

    # Vehicles -> type 6
    if vehicles_csv.exists():
        df = read_csv_auto(vehicles_csv)
        col_name = resolve_col(df, "name", ["Name","vehicle name","label","identifier","title"])
        frames.append(pd.DataFrame({"name": df[col_name].fillna("").astype(str).str.strip(), "type": 6}))
    else:
        print(f"[WARN] {vehicles_csv} not found. Skipping vehicles.")

    # Network sites -> type 3
    if network_sites_csv.exists():
        df = read_csv_auto(network_sites_csv)
        try:
            col_name = resolve_col(df, "name", ["Name","title","site name"])
        except Exception:
            col_name = resolve_col(df, "title", ["name","Name"])
        frames.append(pd.DataFrame({"name": df[col_name].fillna("").astype(str).str.strip(), "type": 3}))
    else:
        print(f"[WARN] {network_sites_csv} not found. Skipping network sites.")

    if frames:
        stocks = pd.concat(frames, ignore_index=True)
    else:
        stocks = pd.DataFrame(columns=["name","type"])

    # Append required static rows
    stocks = pd.concat([
        stocks,
        pd.DataFrame([
            {"name": "Customer premises", "type": 2},
            {"name": "Admins", "type": 4},
        ])
    ], ignore_index=True)

    # Generate ids starting at 1
    stocks.insert(0, "id", range(1, len(stocks) + 1))

    stocks.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"[OK] Wrote stocks -> {out_csv} ({len(stocks)} rows)")

def main():
    ap = argparse.ArgumentParser(description="Build inventory seed CSVs for Splynx")
    ap.add_argument("--manufacturers", default="manufacturers.csv")
    ap.add_argument("--model-categories", default="inventory_model_categories.csv")
    ap.add_argument("--models", default="inventory_models.csv")
    ap.add_argument("--locations", default="inventory_locations.csv")
    ap.add_argument("--internal-locations", default="internal_locations.csv")
    ap.add_argument("--generic-assignees", default="generic_inventory_assignees.csv")
    ap.add_argument("--vehicles", default="vehicles.csv")
    ap.add_argument("--network-sites", default="network_sites.csv")
    ap.add_argument("--out-dir", default=".", help="Output directory")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    build_vendors(Path(args.manufacturers), out_dir / "8_1_inventory_vendors.csv")
    build_categories(Path(args.model_categories), out_dir / "8_2_inventory_products_categories.csv")
    build_products(Path(args.models), out_dir / "8_3_inventory_products.csv")
    build_stocks(Path(args.locations), Path(args.internal_locations), Path(args.generic_assignees), Path(args.vehicles), Path(args.network_sites), out_dir / "8_4_inventory_stocks.csv")

if __name__ == "__main__":
    main()