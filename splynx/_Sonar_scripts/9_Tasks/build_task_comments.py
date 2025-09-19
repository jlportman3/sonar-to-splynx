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

def to_dt(series: pd.Series, shift_hours: int = 0) -> pd.Series:
    s = pd.to_datetime(series, errors="coerce")
    if shift_hours:
        s = s + pd.to_timedelta(shift_hours, unit="h")
    return s

def fmt_dt(series: pd.Series) -> pd.Series:
    return series.dt.strftime("%Y-%m-%d %H:%M:%S").fillna("")

def main():
    ap = argparse.ArgumentParser(description="Build scheduling_task_comment from Sonar notes.csv (only notable type = Job)")
    ap.add_argument("--notes", required=True, help="notes.csv from Sonar")
    ap.add_argument("--out", required=True, help="Output CSV scheduling_task_comment")
    ap.add_argument("--shift-hours", type=int, default=0, help="Shift datetime columns by N hours")
    args = ap.parse_args()

    df = read_csv_auto(Path(args.notes))

    c_id = resolve_col(df, "ID", ["id"])
    c_notable_type = resolve_col(df, "notable type", ["noteable type","owner type","target type"])
    c_notable_id = resolve_col(df, "notable ID", ["noteable id","owner id","target id"])
    c_user_id = resolve_col(df, "user ID", ["user id","author id","admin id"])
    c_message = resolve_col(df, "message", ["body","note","comment"])
    c_created = resolve_col(df, "created at", ["created","created_at"])

    # filter notable type = Job
    mask = df[c_notable_type].astype(str).str.strip().str.lower().eq("job")
    filtered = df[mask].copy()

    out = pd.DataFrame()
    out["id"] = pd.to_numeric(filtered[c_id], errors="coerce")
    out["task_id"] = pd.to_numeric(filtered[c_notable_id], errors="coerce")
    out["user_id"] = pd.to_numeric(filtered[c_user_id], errors="coerce")
    out["comment"] = filtered[c_message].fillna("").astype(str)
    created = to_dt(filtered[c_created], args.shift_hours)
    out["created_at"] = fmt_dt(created)

    # ensure empty strings instead of NaN for text; numbers leave as-is (empty -> '')
    for col in out.columns:
        if out[col].dtype.kind in "iufc":
            out[col] = out[col].astype(object).where(pd.notna(out[col]), "")
        else:
            out[col] = out[col].fillna("")

    # order
    out = out[["id","task_id","user_id","comment","created_at"]]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()