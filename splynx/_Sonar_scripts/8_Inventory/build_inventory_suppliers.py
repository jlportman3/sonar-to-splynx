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

def resolve_col(df, name, alts=None, required=True):
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

def main():
    ap = argparse.ArgumentParser(description="Build inventory_suppliers from vendors, addresses, contacts, phone_numbers")
    ap.add_argument("--vendors", required=True, help="vendors.csv")
    ap.add_argument("--addresses", required=True, help="addresses.csv")
    ap.add_argument("--contacts", required=True, help="contacts.csv")
    ap.add_argument("--phones", required=True, help="phone_numbers.csv")
    ap.add_argument("--out", required=True, help="Output CSV inventory_suppliers")
    args = ap.parse_args()

    vdf = read_csv_auto(Path(args.vendors))
    adf = read_csv_auto(Path(args.addresses))
    cdf = read_csv_auto(Path(args.contacts))
    pdf = read_csv_auto(Path(args.phones))

    # Vendors
    v_id = resolve_col(vdf, "ID", ["id","vendor id"])
    v_name = resolve_col(vdf, "name", ["Name","title"])

    # Addresses (owner = Vendor)
    a_owner = resolve_col(adf, "address owner", ["owner type","address owner type"])
    a_owner_id = resolve_col(adf, "address owner ID", ["owner id"])
    a_line1 = resolve_col(adf, "line 1", ["address line 1","street 1","street"])
    a_line2 = resolve_col(adf, "line 2", ["address line 2","street 2"], required=False)
    a_city = resolve_col(adf, "city", ["City"], required=False)
    a_zip = resolve_col(adf, "ZIP", ["zip","postal code","postcode"], required=False)

    adf_vendor = adf[adf[a_owner].astype(str).str.strip().str.lower().eq("vendor")].copy()
    # build concatenated address parts, skip empties
    def _concat_addr(row):
        parts = []
        for col in [a_line1, a_line2, a_city, a_zip]:
            if col and col in row and pd.notna(row[col]) and str(row[col]).strip() != "":
                parts.append(str(row[col]).strip())
        return ", ".join(parts)
    adf_vendor["addr"] = adf_vendor.apply(_concat_addr, axis=1)
    # group by owner id, combine multiple addresses with " | "
    addr_map = adf_vendor.groupby(a_owner_id)["addr"].apply(lambda s: " | ".join([x for x in dict.fromkeys([x for x in s.astype(str) if x.strip()!=''])])).to_dict()

    # Contacts (owner = Vendor)
    co_owner = resolve_col(cdf, "contact owner", ["owner type"])
    co_owner_id = resolve_col(cdf, "contact owner ID", ["owner id"])
    co_id = resolve_col(cdf, "ID", ["id","contact id"])
    co_name = resolve_col(cdf, "name", ["contact name"], required=False)
    co_email = resolve_col(cdf, "email address", ["email"], required=False)
    co_role = resolve_col(cdf, "role", ["position"], required=False)

    c_vendor = cdf[cdf[co_owner].astype(str).str.strip().str.lower().eq("vendor")].copy()
    def agg_unique(series):
        vals = [str(x).strip() for x in series if pd.notna(x) and str(x).strip()!=""]
        seen = []
        for v in vals:
            if v not in seen:
                seen.append(v)
        return " | ".join(seen)

    names_map = c_vendor.groupby(co_owner_id)[co_name].apply(agg_unique).to_dict() if co_name else {}
    emails_map = c_vendor.groupby(co_owner_id)[co_email].apply(agg_unique).to_dict() if co_email else {}
    roles_map = c_vendor.groupby(co_owner_id)[co_role].apply(agg_unique).to_dict() if co_role else {}

    # Phones: contact ID -> numbers, then vendor -> combined
    p_contact_id = resolve_col(pdf, "contact ID", ["contact id"])
    p_number = resolve_col(pdf, "number", ["phone","phone number","mobile"])
    phone_by_contact = pdf.groupby(p_contact_id)[p_number].apply(
        lambda s: ", ".join(sorted(set([str(x).strip() for x in s if pd.notna(x) and str(x).strip()!=""])))
    ).to_dict()

    contact_ids_by_vendor = c_vendor.groupby(co_owner_id)[co_id].apply(
        lambda s: [int(x) for x in pd.to_numeric(s, errors="coerce") if pd.notna(x)]
    ).to_dict()

    phones_map = {}
    for vend_id, cids in contact_ids_by_vendor.items():
        nums = []
        for cid in cids:
            entry = phone_by_contact.get(cid, "")
            if entry:
                nums.extend([n.strip() for n in entry.split(",") if n.strip()])
        # dedupe keep order
        seen = []
        for n in nums:
            if n not in seen:
                seen.append(n)
        phones_map[vend_id] = ", ".join(seen)

    # Build output
    out = pd.DataFrame()
    out["id"] = pd.to_numeric(vdf[v_id], errors="coerce").astype("Int64")
    out["name"] = vdf[v_name].astype(str).fillna("")
    out["address"] = out["id"].map(addr_map).fillna("")
    out["contact_name"] = out["id"].map(names_map).fillna("")
    out["email"] = out["id"].map(emails_map).fillna("")
    out["phone"] = out["id"].map(phones_map).fillna("")
    out["role"] = out["id"].map(roles_map).fillna("")

    # Ensure empties are strings (no <NA>)
    for c in out.columns:
        out[c] = out[c].astype(object).where(pd.notna(out[c]), "")

    out = out[["id","name","address","contact_name","email","phone","role"]]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()
