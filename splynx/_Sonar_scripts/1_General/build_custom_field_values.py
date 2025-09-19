
#!/usr/bin/env python3
import argparse
import pandas as pd
from pathlib import Path
import re, os

VALID_ENTITIES = {"Account":"customers_values",
                  "NetworkSite":"network_site_values",
                  "Job":"scheduling_task_values",
                  "Ticket":"ticket_values"}

def sanitize_name(name: str) -> str:
    return re.sub(r'[^a-z0-9_]', '_', str(name).strip().lower())

def read_csv_auto(p: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(p)
    except Exception:
        return pd.read_csv(p, sep=';')

def find_col(df, wanted, alts=None, required=True):
    alts = (alts or []) + [wanted]
    low = {c.lower().strip(): c for c in df.columns}
    for w in alts:
        k = w.lower().strip()
        if k in low:
            return low[k]
        # normalize removing spaces/underscores
        for lk, orig in low.items():
            if re.sub(r'[\s_]+','', lk) == re.sub(r'[\s_]+','', k):
                return orig
    if required:
        raise KeyError(f"Column '{wanted}' not found. Available: {list(df.columns)}")
    return None

def escape_sql(s: str) -> str:
    return s.replace("'", "''")

def dedupe_last_nonempty(df: pd.DataFrame) -> pd.DataFrame:
    # df contains rows of single group
    if "value" in df.columns:
        # prefer last non-empty (notna and not '')
        m = df["value"].astype(str).ne("") & df["value"].notna()
        if m.any():
            return df[m].iloc[[-1]]
    return df.iloc[[-1]]

def main():
    ap = argparse.ArgumentParser(description="Build values for additional fields per module, dedup (id,name).")
    ap.add_argument("--fields", required=True, help="custom_fields.csv (source of names/types)")
    ap.add_argument("--data", required=True, help="custom_field_data.csv (values)")
    ap.add_argument("--out-dir", required=True, help="Output directory")
    args = ap.parse_args()

    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    fdf = read_csv_auto(Path(args.fields))
    ddf = read_csv_auto(Path(args.data))

    # columns in fields
    f_id = find_col(fdf, "ID", ["id"])
    f_name = find_col(fdf, "name", ["Name","title"])
    f_entity = find_col(fdf, "entity type", ["entity","owner type","object type"])

    # map id -> (sanitized_name, entity)
    fmap = {}
    for _, r in fdf.iterrows():
        fid = r[f_id]
        nm = sanitize_name(r[f_name])
        ent = str(r[f_entity]).strip()
        fmap[fid] = (nm, ent)

    # data columns
    d_field_id = find_col(ddf, "custom field ID", ["custom_field_id","field id"])
    d_entity = find_col(ddf, "custom field dataable type", ["dataable type","owner type","entity type"])
    d_id = find_col(ddf, "custom field dataable ID", ["dataable id","owner id","entity id"])
    d_value = find_col(ddf, "value", ["data","val"])

    created_counts = {}
    dropped_dups = {}

    for ent, table in VALID_ENTITIES.items():
        sub = ddf[ddf[d_entity].astype(str).str.strip().eq(ent)].copy()
        if sub.empty:
            continue
        # map names
        sub["name"] = sub[d_field_id].map(lambda x: fmap.get(x, (None, None))[0])
        sub = sub[sub["name"].notna()]
        sub["id"] = pd.to_numeric(sub[d_id], errors="coerce")
        sub["value"] = sub[d_value].fillna("").astype(str)

        # keep only needed cols
        sub = sub[["id","name","value"]]

        before = len(sub)
        # dedupe by (id,name): keep last non-empty value else last
        sub = (sub
               .groupby(["id","name"], sort=False, group_keys=False)
               .apply(dedupe_last_nonempty)
               .reset_index(drop=True))
        after = len(sub)
        created_counts[ent] = after
        dropped_dups[ent] = before - after

        # write CSV
        csv_path = outdir / f"{table}.csv"
        sub.to_csv(csv_path, index=False, encoding="utf-8")

        # write SQL
        sql_path = outdir / f"{table}.sql"
        with open(sql_path, "w", encoding="utf-8") as f:
            for _, r in sub.iterrows():
                f.write(
                    "INSERT INTO `{}` (`id`,`name`,`value`) VALUES ('{}','{}','{}');\n".format(
                        table,
                        str(r["id"]).replace("'", "''"),
                        escape_sql(str(r["name"])),
                        escape_sql(str(r["value"])),
                    )
                )
        print(f"Wrote {after} rows to {csv_path.name} (dropped {before-after} duplicates by (id,name))")

if __name__ == "__main__":
    main()
