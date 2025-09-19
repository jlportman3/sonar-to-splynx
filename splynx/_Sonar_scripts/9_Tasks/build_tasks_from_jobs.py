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

def to_dt(series: pd.Series, shift_hours: int = 0) -> pd.Series:
    s = pd.to_datetime(series, errors='coerce')
    if shift_hours:
        s = s + pd.to_timedelta(shift_hours, unit='h')
    return s

def fmt_dt(series: pd.Series) -> pd.Series:
    return series.dt.strftime('%Y-%m-%d %H:%M:%S').fillna('')

def esc_sql(s: str) -> str:
    return s.replace("'", "''")

def main():
    ap = argparse.ArgumentParser(description="Build Splynx scheduling_task (from Sonar jobs.csv)")
    ap.add_argument("--jobs", required=True, help="jobs.csv")
    ap.add_argument("--job-types", required=True, help="job_types.csv")
    ap.add_argument("--accounts", required=True, help="accounts.csv")
    ap.add_argument("--network-sites", required=True, help="network_sites.csv")
    ap.add_argument("--out", required=True, help="Output tasks CSV")
    ap.add_argument("--sql-out", required=False, help="Optional SQL file with INSERT statements")
    ap.add_argument("--table-name", default="scheduling_task", help="SQL table name (default: scheduling_task)")
    ap.add_argument("--shift-hours", type=int, default=0, help="Shift all datetime fields by N hours")
    args = ap.parse_args()

    jdf = read_csv_auto(Path(args.jobs))
    tdf = read_csv_auto(Path(args.job_types))
    adf = read_csv_auto(Path(args.accounts))
    ndf = read_csv_auto(Path(args.network_sites))

    # Resolve job columns
    j_id = resolve_col(jdf, "ID", ["id"])
    j_type_id = resolve_col(jdf, "job type ID", ["job type id","type id"])
    j_completion_notes = resolve_col(jdf, "completion notes", ["completion note","notes","description"], required=False)
    j_created = resolve_col(jdf, "created at", ["created","created_at"])
    j_updated = resolve_col(jdf, "updated at", ["updated","updated_at"], required=False)
    j_completed_at = resolve_col(jdf, "completion date/time", ["completed at","completion datetime","completion date time"], required=False)
    j_complete_flag = resolve_col(jdf, "complete", ["is complete","completed","done"])
    j_jobbable_type = resolve_col(jdf, "jobbable type", ["job owner type","owner type"])
    j_jobbable_id = resolve_col(jdf, "jobbable ID", ["job owner id","owner id"])
    j_completed_by = resolve_col(jdf, "completed by user ID", ["completed by","completed by id","completed_by_id"], required=False)
    j_assigned_to_admin = resolve_col(jdf, "assigned to administrator", ["assigned to admin","assigned_to_administrator","assigned admin id"], required=False)
    j_address_on_completion = resolve_col(jdf, "address on completion", ["completion address","address"], required=False)
    j_sched_dt = resolve_col(jdf, "scheduled date/time", ["scheduled at","schedule date/time","scheduled datetime","scheduled date time"], required=False)
    j_length_min = resolve_col(jdf, "length in minutes", ["length minutes","duration minutes","length"], required=False)

    # Resolve job type name
    t_id = resolve_col(tdf, "ID", ["id"])
    t_name = resolve_col(tdf, "name", ["Name","title","job type name"])
    type_map = dict(zip(pd.to_numeric(tdf[t_id], errors="coerce"), tdf[t_name].astype(str)))

    # Resolve account and network site names + partner/company id
    a_id = resolve_col(adf, "ID", ["id","account id"])
    a_name = resolve_col(adf, "name", ["Name","account name","title"])
    try:
        a_company = resolve_col(adf, "company ID", ["company id","partner id","company"], required=False)
    except KeyError:
        a_company = None

    acc_name_map = dict(zip(pd.to_numeric(adf[a_id], errors="coerce"), adf[a_name].astype(str)))
    company_map = dict(zip(pd.to_numeric(adf[a_id], errors="coerce"),
                           pd.to_numeric(adf[a_company], errors="coerce"))) if a_company else {}

    # network sites
    try:
        n_id = resolve_col(ndf, "ID", ["id","site id"])
    except KeyError:
        n_id = ndf.columns[0]
    try:
        n_name = resolve_col(ndf, "name", ["Name","title","site name"])
    except KeyError:
        n_name = ndf.columns[1] if len(ndf.columns) > 1 else ndf.columns[0]
    ns_name_map = dict(zip(pd.to_numeric(ndf[n_id], errors="coerce"), ndf[n_name].astype(str)))

    # Build dataframe
    out = pd.DataFrame()
    out["id"] = pd.to_numeric(jdf[j_id], errors="coerce")

    # Title
    jt_series = pd.to_numeric(jdf[j_type_id], errors="coerce")
    job_type_name = jt_series.map(type_map).fillna("")
    job_owner_type = jdf[j_jobbable_type].astype(str)
    job_owner_id = pd.to_numeric(jdf[j_jobbable_id], errors="coerce")

    owner_name = pd.Series([""]*len(jdf), dtype=str)
    owner_name = owner_name.mask(job_owner_type.eq("Account"), job_owner_id.map(acc_name_map).fillna(""))
    owner_name = owner_name.mask(job_owner_type.eq("NetworkSite"), job_owner_id.map(ns_name_map).fillna(""))
    out["title"] = (job_type_name.str.strip() + " - " + owner_name.str.strip()).str.strip(" -")

    # Description -> convert bullets to lines and render as <br>
    if j_completion_notes:
        desc = jdf[j_completion_notes].fillna("").astype(str)
        def _fix_desc(s: str) -> str:
            s = s.replace("\r\n", "\n")
            # if single line with bullets separated by " - ", insert breaks
            if "\n" not in s and " - " in s:
                s = re.sub(r"\s+-\s+", "\n- ", s)
            # finally replace newlines with <br>
            s = s.replace("\n", "<br>")
            return s
        out["description"] = desc.map(_fix_desc)
    else:
        out["description"] = ""

    # partner_id: default to 1 when missing
    partner = job_owner_id.map(company_map) if company_map else pd.Series([None]*len(jdf))
    partner = partner.fillna(1).astype(int)
    out["partner_id"] = partner

    # reporter_id & related_customer_id
    out["reporter_id"] = pd.to_numeric(jdf[j_completed_by], errors="coerce") if j_completed_by else ""
    related_cust = job_owner_id.where(job_owner_type.eq("Account"), "")
    out["related_to_id"] = ""
    out["parent_task_id"] = ""
    out["project_id"] = 1
    out["location_id"] = ""
    out["related_customer_id"] = related_cust
    out["related_service_id"] = ""

    # Dates with shift
    created = to_dt(jdf[j_created], args.shift_hours)
    updated = to_dt(jdf[j_updated], args.shift_hours) if j_updated else pd.Series([pd.NaT]*len(jdf))
    completed = to_dt(jdf[j_completed_at], args.shift_hours) if j_completed_at else pd.Series([pd.NaT]*len(jdf))
    out["created_at"] = fmt_dt(created)
    out["updated_at"] = fmt_dt(updated)
    out["resolved_at"] = fmt_dt(completed)

    # Assignment
    out["assigned_to"] = pd.to_numeric(jdf[j_assigned_to_admin], errors="coerce") if j_assigned_to_admin else ""
    out["assignee"] = pd.to_numeric(jdf[j_completed_by], errors="coerce") if j_completed_by else ""
    out["assinged_at"] = ""  # left empty
    out["priority"] = ""     # left empty

    # Scheduling
    sched_dt = to_dt(jdf[j_sched_dt], args.shift_hours) if j_sched_dt else pd.Series([pd.NaT]*len(jdf))
    out["is_sceduled"] = sched_dt.notna().astype(int)
    out["scheduled_from"] = fmt_dt(sched_dt)

    if j_length_min:
        mins = pd.to_numeric(jdf[j_length_min], errors="coerce").fillna(0).astype(int)
        sched_to = sched_dt + mins.map(lambda m: pd.Timedelta(minutes=int(m)))
    else:
        sched_to = pd.Series([pd.NaT]*len(jdf))
    out["scheduled_to"] = fmt_dt(sched_to)

    # Travel/checklist
    out["travel_time_to"] = ""
    out["travel_time_from"] = ""
    out["checklist_template_id"] = ""

    # Closed/deleted/workflow/is_archived
    closed_flag = pd.to_numeric(jdf[j_complete_flag], errors="coerce").fillna(0).astype(int)
    out["closed"] = closed_flag
    out["deleted"] = 0
    out["workflow_status_id"] = closed_flag.map(lambda v: 3 if v == 1 else 2)
    out["is_archived"] = 0

    # Address at completion
    out["address"] = jdf[j_address_on_completion].fillna("").astype(str) if j_address_on_completion else ""

    # Final order
    cols = [
        "id","title","description","partner_id","reporter_id","related_to_id","parent_task_id",
        "project_id","location_id","related_customer_id","related_service_id","created_at","updated_at",
        "resolved_at","assigned_to","assignee","assinged_at","priority","is_sceduled","scheduled_from",
        "scheduled_to","travel_time_to","travel_time_from","checklist_template_id","closed","deleted",
        "workflow_status_id","is_archived","address"
    ]
    out = out[cols]

    # Ensure empty strings instead of NaN (except partner_id which is int)
    for c in out.columns:
        if c == "partner_id":
            out[c] = out[c].fillna(1).astype(int)
        else:
            out[c] = out[c].astype(object).where(pd.notna(out[c]), "")

    # Save CSV
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows -> {args.out}")

    # Optional SQL
    if args.sql_out:
        tbl = args.table_name
        lines = []
        for _, r in out.iterrows():
            vals = []
            for c in cols:
                v = r[c]
                if c == "partner_id":
                    vals.append(str(int(v)))
                else:
                    s = "" if (pd.isna(v) or v is None) else str(v)
                    s_esc = s.replace("'", "''")
                    vals.append(f"'{s_esc}'")
            line = f"INSERT INTO `{tbl}` (`" + "`,`".join(cols) + "`) VALUES (" + ",".join(vals) + ");"
            lines.append(line)
        Path(args.sql_out).write_text("\n".join(lines), encoding="utf-8")
        print(f"Wrote SQL with {len(lines)} INSERTs -> {args.sql_out}")

if __name__ == "__main__":
    main()
