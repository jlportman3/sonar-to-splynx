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
    ap = argparse.ArgumentParser(description="Build scheduling_task_worklog from Sonar job_check_ins.csv")
    ap.add_argument("--check-ins", required=True, help="job_check_ins.csv from Sonar")
    ap.add_argument("--out", required=True, help="Output CSV scheduling_task_worklog")
    ap.add_argument("--shift-hours", type=int, default=0, help="Shift datetime columns by N hours")
    args = ap.parse_args()

    df = read_csv_auto(Path(args.check_ins))

    c_id = resolve_col(df, "ID", ["id"])
    c_job_id = resolve_col(df, "job ID", ["job id","jobId"])
    c_user_id = resolve_col(df, "user ID", ["user id","admin id","employee id"])
    c_created = resolve_col(df, "created at", ["created","created_at"], required=False)
    c_in = resolve_col(df, "check in date/time", ["check in","check-in","check in datetime","check in date time","check_in"], required=False)
    c_out = resolve_col(df, "check out date/time", ["check out","check-out","check out datetime","check out date time","check_out"], required=False)

    out = pd.DataFrame()
    out["id"] = pd.to_numeric(df[c_id], errors="coerce")
    out["task_id"] = pd.to_numeric(df[c_job_id], errors="coerce")
    out["user_id"] = pd.to_numeric(df[c_user_id], errors="coerce")

    created = to_dt(df[c_created], args.shift_hours) if c_created else pd.Series([pd.NaT]*len(df))
    started = to_dt(df[c_in], args.shift_hours) if c_in else pd.Series([pd.NaT]*len(df))
    stopped = to_dt(df[c_out], args.shift_hours) if c_out else pd.Series([pd.NaT]*len(df))

    out["created_at"] = fmt_dt(created)
    out["started_at"] = fmt_dt(started)
    out["stopped_at"] = fmt_dt(stopped)

    # time_spent in seconds, minimum 60
    dur = (stopped - started).dt.total_seconds()
    dur = dur.fillna(0).clip(lower=60).astype(int)
    out["is_manual"] = 1
    out["time_spent"] = dur

    # Replace NaNs in numeric with empty strings except is_manual and time_spent we keep numeric
    for col in ["id", "task_id", "user_id"]:
        out[col] = out[col].astype(object).where(pd.notna(out[col]), "")

    # Final order
    out = out[["id","task_id","user_id","created_at","started_at","stopped_at","is_manual","time_spent"]]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

if __name__ == "__main__":
    main()