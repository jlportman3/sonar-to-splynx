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
            if re.sub(r"[\s_]+","", ck) == re.sub(r"[\s_]+","", k):
                return cn
    if required:
        raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")
    return None

def unique_with_dots(series: pd.Series) -> pd.Series:
    seen = {}
    result = []
    for v in series.fillna("").astype(str):
        key = v
        if key == "":
            result.append("")
            continue
        cnt = seen.get(key, 0) + 1
        seen[key] = cnt
        if cnt == 1:
            result.append(key)
        else:
            result.append(key + ("." * (cnt-1)))
    return pd.Series(result, index=series.index)

def build_field_maps(fields_csv: Path, field_data_csv: Path):
    fdf = read_csv_auto(fields_csv)
    ddf = read_csv_auto(field_data_csv)

    # Identify columns
    f_id = resolve_col(fdf, "ID", ["id"])
    f_name = resolve_col(fdf, "name", ["Name","field name","label"])
    d_item_id = resolve_col(ddf, "inventory item ID", ["inventory item id","item id","inventoryitem id","inventory item"], required=True)
    d_field_id = resolve_col(ddf, "inventory model field ID", ["inventory model field id","field id"], required=True)
    d_value = resolve_col(ddf, "value", ["Value","field value","data"], required=True)

    # Field IDs by type (mac / serial)
    names = fdf[f_name].astype(str).str.lower()
    mac_field_ids = set(fdf.loc[names.str.contains("mac"), f_id].astype(str))
    serial_field_ids = set(fdf.loc[names.str.contains("serial"), f_id].astype(str))

    # Build maps: item_id -> value (prefer first non-empty; if multiple, last non-empty wins)
    mac_map = {}
    serial_map = {}

    for _, row in ddf.iterrows():
        item_id = str(row[d_item_id])
        field_id = str(row[d_field_id])
        val = "" if pd.isna(row[d_value]) else str(row[d_value]).strip()
        if not val:
            continue
        if field_id in mac_field_ids:
            mac_map[item_id] = val
        if field_id in serial_field_ids:
            serial_map[item_id] = val

    return mac_map, serial_map

def build_stock_name_maps(loc_csv: Path, iloc_csv: Path, ga_csv: Path, veh_csv: Path, ns_csv: Path):
    maps = {}  # type -> {id -> name}

    def add_map(t, df, id_guess="ID", name_guess="name", alts_name=None):
        if df is None or df.empty: 
            return
        col_id = resolve_col(df, id_guess, ["id"])
        try:
            col_name = resolve_col(df, name_guess, (alts_name or []) + ["Name","title","label","identifier"])
        except Exception:
            # fallback to first str-like column
            col_name = df.columns[1] if len(df.columns) > 1 else df.columns[0]
        sub = df[[col_id, col_name]].copy()
        sub[col_id] = sub[col_id].astype(str)
        sub[col_name] = sub[col_name].astype(str).str.strip()
        maps[t] = dict(zip(sub[col_id], sub[col_name]))

    # Read and build
    df_loc = read_csv_auto(loc_csv) if loc_csv and loc_csv.exists() else None
    df_iloc = read_csv_auto(iloc_csv) if iloc_csv and iloc_csv.exists() else None
    df_ga = read_csv_auto(ga_csv) if ga_csv and ga_csv.exists() else None
    df_veh = read_csv_auto(veh_csv) if veh_csv and veh_csv.exists() else None
    df_ns = read_csv_auto(ns_csv) if ns_csv and ns_csv.exists() else None

    add_map("InventoryLocation", df_loc, name_guess="name", alts_name=["location name"])
    add_map("InternalLocation", df_iloc, name_guess="name", alts_name=["location name"])
    add_map("GenericInventoryAssignee", df_ga, name_guess="name", alts_name=["label"])
    add_map("Vehicle", df_veh, name_guess="name", alts_name=["identifier","label"])
    add_map("NetworkSite", df_ns, name_guess="name", alts_name=["title","site name"])
    return maps


def build_address_to_customer(addresses_csv: Path):
    """
    Build a mapping Address ID -> Customer/Account ID.

    Priority:
      1) "address owner" == "Account" and use "address owner id"
      2) Fallback to "account ID" directly if present
      3) Fallback to older fields: "addressable type" == "Account" and "addressable ID"
    """
    if not addresses_csv.exists():
        return {}
    adf = read_csv_auto(addresses_csv)

    # Address ID
    col_addr_id = resolve_col(adf, "ID", ["id","address id"])

    # Priority 1: address owner == Account
    try:
        col_owner_type = resolve_col(adf, "address owner", ["owner","address owner type"], required=False)
    except KeyError:
        col_owner_type = None
    try:
        col_owner_id = resolve_col(adf, "address owner id", ["owner id","address owner ID"], required=False)
    except KeyError:
        col_owner_id = None

    if col_owner_type and col_owner_id:
        tmp = adf[[col_addr_id, col_owner_type, col_owner_id]].copy()
        tmp = tmp[tmp[col_owner_type].astype(str).str.strip().str.lower().eq("account")]
        if not tmp.empty:
            return dict(zip(tmp[col_addr_id].astype(str), 
                            pd.to_numeric(tmp[col_owner_id], errors="coerce").fillna(0).astype(int)))

    # Priority 2: direct account ID column
    try:
        col_acc = resolve_col(adf, "account ID", ["account id","customer id","account_id","customer_id"], required=False)
    except KeyError:
        col_acc = None
    if col_acc:
        return dict(zip(adf[col_addr_id].astype(str), 
                        pd.to_numeric(adf[col_acc], errors="coerce").fillna(0).astype(int)))

    # Priority 3: older "addressable" fields
    try:
        col_addr_type = resolve_col(adf, "addressable type", ["owner type","address owner type"], required=False)
        col_addr_owner = resolve_col(adf, "addressable ID", ["owner id","address owner id"], required=False)
        if col_addr_type and col_addr_owner:
            tmp = adf[[col_addr_id, col_addr_type, col_addr_owner]].copy()
            tmp = tmp[tmp[col_addr_type].astype(str).str.strip().str.lower().eq("account")]
            if not tmp.empty:
                return dict(zip(tmp[col_addr_id].astype(str), 
                                pd.to_numeric(tmp[col_addr_owner], errors="coerce").fillna(0).astype(int)))
    except KeyError:
        pass

    return {}


def main():
    ap = argparse.ArgumentParser(description="Build Splynx inventory_items.csv from Sonar CSVs")
    ap.add_argument("--items", required=True, help="inventory_items.csv from Sonar")
    ap.add_argument("--fields", required=True, help="inventory_model_fields.csv")
    ap.add_argument("--field-data", required=True, help="inventory_model_field_data.csv")
    ap.add_argument("--stocks", required=True, help="Path to inventory_stocks.csv (generated earlier)")
    ap.add_argument("--locations", required=True, help="inventory_locations.csv")
    ap.add_argument("--internal-locations", required=True, help="internal_locations.csv")
    ap.add_argument("--generic-assignees", required=True, help="generic_inventory_assignees.csv")
    ap.add_argument("--vehicles", required=True, help="vehicles.csv")
    ap.add_argument("--network-sites", required=True, help="network_sites.csv")
    ap.add_argument("--addresses", required=True, help="addresses.csv (to resolve Address -> customer_id)")
    ap.add_argument("--out", required=True, help="Output CSV for Splynx inventory_items")
    args = ap.parse_args()

    items = read_csv_auto(Path(args.items))
    fields_csv = Path(args.fields)
    data_csv = Path(args.field_data)
    stocks_csv = read_csv_auto(Path(args.stocks))

    # Column resolution for items
    col_id = resolve_col(items, "ID", ["id"])
    col_model_id = resolve_col(items, "inventory model ID", ["inventory model id","model id"])
    col_owner_type = resolve_col(items, "inventoryitemable type", ["inventory itemable type","owner type","assignee type"])
    col_owner_id = resolve_col(items, "inventoryitemable ID", ["inventory itemable id","owner id","assignee id"])
    col_purchase = resolve_col(items, "purchase price", ["purchase_price","price","cost"], required=False)

    # Build field maps
    mac_map, serial_map = build_field_maps(fields_csv, data_csv)

    # Build stock name maps per type
    name_maps = build_stock_name_maps(Path(args.locations), Path(args.internal_locations), Path(args.generic_assignees), Path(args.vehicles), Path(args.network_sites))

    # Build stock name -> id map from stocks file
    s_name = resolve_col(stocks_csv, "name", ["Name","title"])
    s_id = resolve_col(stocks_csv, "id", ["ID","Id"])
    stock_name_to_id = dict(zip(stocks_csv[s_name].astype(str).str.strip(), pd.to_numeric(stocks_csv[s_id], errors="coerce").astype("Int64")))

    # Address -> customer map
    addr_to_cust = build_address_to_customer(Path(args.addresses))

    # Helper to compute stock_id by item owner
    def resolve_stock_id(owner_type: str, owner_id: str):
        t = str(owner_type or "").strip()
        oid = str(owner_id or "").strip()
        if t == "Address":
            return int(stock_name_to_id.get("Customer premises", 0) or 0)
        if t == "User":
            return int(stock_name_to_id.get("Admins", 0) or 0)
        # Other types -> look up name in corresponding map and then find same name in stocks
        if t in name_maps:
            name_map = name_maps[t]
            name = name_map.get(oid, "").strip()
            if name:
                return int(stock_name_to_id.get(name, 0) or 0)
        return 0

    # Compute columns
    out = pd.DataFrame()
    out["id"] = pd.to_numeric(items[col_id], errors="coerce").astype("Int64")
    out["product_id"] = pd.to_numeric(items[col_model_id], errors="coerce").astype("Int64")

    # barcode from MAC (via fields)
    item_ids_str = items[col_id].astype(str)
    macs = item_ids_str.map(lambda k: mac_map.get(k, ""))
    serials = item_ids_str.map(lambda k: serial_map.get(k, ""))

    # enforce uniqueness with dots for non-empty values
    out["barcode"] = unique_with_dots(pd.Series(macs))
    out["serial_number"] = unique_with_dots(pd.Series(serials))

    # status by owner type
    owner_type = items[col_owner_type].astype(str)
    status = pd.Series(["stock"]*len(items), dtype=str)
    status = status.mask(owner_type.eq("Vehicle"), "in_transit")
    status = status.mask(owner_type.eq("Address"), "assigned")
    status = status.mask(owner_type.eq("User"), "internal_usage")
    out["status"] = status

    # mark: new if InventoryLocation else used
    mark = pd.Series(["used"]*len(items), dtype=str)
    mark = mark.mask(owner_type.eq("InventoryLocation"), "new")
    out["mark"] = mark

    # customer_id / admin_id
    owner_id_str = items[col_owner_id].astype(str)
    owner_id_num = pd.to_numeric(items[col_owner_id], errors="coerce").astype("Int64")

    # For Address: map address ID -> account/customer ID via addresses.csv
    cust_from_addr = owner_id_str.map(lambda aid: addr_to_cust.get(str(aid), ""))
    cust_series = pd.to_numeric(cust_from_addr, errors="coerce").astype("Int64")
    cust_series = cust_series.where(owner_type.eq("Address"), pd.NA)

    out["customer_id"] = cust_series
    out["admin_id"] = owner_id_num.where(owner_type.eq("User"), pd.NA)

    # stock_id via name lookup
    out["stock_id"] = [
        resolve_stock_id(t, oid) for t, oid in zip(items[col_owner_type], items[col_owner_id])
    ]

    # cost_price
    if col_purchase:
        pr = pd.to_numeric(items[col_purchase], errors="coerce") / 100.0
        out["cost_price"] = pr.round(2)
    else:
        out["cost_price"] = ""

    # Reorder columns
    out = out[["id","barcode","serial_number","status","mark","customer_id","admin_id","product_id","stock_id","cost_price"]]

    # Save
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()