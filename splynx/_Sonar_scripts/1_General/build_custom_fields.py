#!/usr/bin/env python3
import pandas as pd
import argparse
import os
import re

VALID_TYPES = {
    'string','integer','decimal','numeric','date','datetime','boolean','select',
    'select_multiple','password','file','relation','relation_multiple','add-on',
    'ip','textarea','ipv6'
}

MODULE_TABLE_MAP = {
    "Account": ("customers", "customers_fields"),
    "Job": ("scheduling_task", "scheduling_task_fields"),
    "NetworkSite": ("network_sites", "network_site_fields"),
    "Ticket": ("ticket", "ticket_fields"),
}

def sanitize_name(name: str) -> str:
    """leave only a-z, 0-9, underscore; lowercased"""
    if name is None:
        return ""
    name = str(name).strip().lower()
    return re.sub(r'[^a-z0-9_]', '_', name)

def sql_escape(s: str) -> str:
    if s is None:
        return ""
    return str(s).replace("'", "''")

def main():
    ap = argparse.ArgumentParser(description="Build custom fields CSV+SQL per entity type")
    ap.add_argument("--input", required=True, help="custom_fields.csv (from Sonar)")
    ap.add_argument("--out-dir", required=True, help="Output directory")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    df = pd.read_csv(args.input)

    # Normalize column names for safer access
    norm_map = {c:c for c in df.columns}
    lower_map = {c.lower().strip(): c for c in df.columns}
    def col(name, alts=None):
        alts = (alts or []) + [name]
        for g in alts:
            k = g.lower().strip()
            if k in lower_map:
                return lower_map[k]
        raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")

    col_entity = col("entity type", ["entity_type","entity"])
    col_name = col("name")
    col_type = col("type")
    col_unique = col("unique", ["is_unique"])

    for entity, (module, table) in MODULE_TABLE_MAP.items():
        sub = df[df[col_entity] == entity].copy()
        if sub.empty:
            continue

        rows = []
        pos = 1
        for _, r in sub.iterrows():
            raw_name = r.get(col_name, "")
            field_type = str(r.get(col_type, "")).strip().lower()
            unique_val = str(r.get(col_unique, "")).strip().lower()

            name = sanitize_name(raw_name)
            if field_type not in VALID_TYPES:
                field_type = "string"
            is_unique = 1 if unique_val in ("1","true","yes","y") else 0

            row = {
                "name": name,
                "module": module,
                "title": str(raw_name),
                "type": field_type,
                "position": pos,
                "show_in_list": 1,
                "is_unique": is_unique,
                "is_add": 1,
                "searchable": 1,
            }
            # category ONLY for customers
            if module == "customers":
                row["category"] = 0
            rows.append(row)
            pos += 1

        out_df = pd.DataFrame(rows)

        # CSV columns (category only for customers)
        if module == "customers":
            csv_cols = ["name","module","category","title","type","position","show_in_list","is_unique","is_add","searchable"]
        else:
            csv_cols = ["name","module","title","type","position","show_in_list","is_unique","is_add","searchable"]
        out_df.to_csv(os.path.join(args.out_dir, f"{module}_custom_fields.csv"), index=False, columns=csv_cols, encoding="utf-8")

        # SQL build
        sql_path = os.path.join(args.out_dir, f"{module}_custom_fields.sql")
        with open(sql_path, "w", encoding="utf-8") as f:
            if module == "customers":
                cols = ["name","module","category","title","type","position","show_in_list","is_unique","is_add","searchable"]
            else:
                cols = ["name","module","title","type","position","show_in_list","is_unique","is_add","searchable"]
            col_list = ", ".join(f"`{c}`" for c in cols)
            for _, rr in out_df.iterrows():
                vals = []
                for c in cols:
                    v = rr.get(c, "")
                    if isinstance(v, (int, float)) and c not in ("title","type","name","module"):
                        # numeric fields: position, flags, category
                        # but ensure integers
                        if pd.isna(v):
                            vals.append("0")
                        else:
                            if float(v).is_integer():
                                vals.append(str(int(v)))
                            else:
                                vals.append(str(v))
                    else:
                        vals.append(f"'{sql_escape(v)}'")
                f.write(f"INSERT INTO `{table}` ({col_list}) VALUES ({', '.join(vals)});\n")

        print(f"Wrote {len(out_df)} rows for {entity} -> {module}_custom_fields.csv / .sql")

if __name__ == "__main__":
    main()
