#!/usr/bin/env python3
import argparse
import re
import pandas as pd
from pathlib import Path
from html import unescape

US_STATE_MAP = {
    "AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut",
    "DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana",
    "IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts",
    "MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska",
    "NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina",
    "ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island",
    "SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont",
    "VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming","DC":"District of Columbia"
}

def resolve_col(df, name_guess, alt=None):
    """Resolve column name by flexible matching (+alts)."""
    alts = (alt or []) + [name_guess]
    cols = {c.strip().lower(): c for c in df.columns}
    for guess in alts:
        key = guess.strip().lower()
        if key in cols:
            return cols[key]
        # ignore spaces/underscores/case
        for k, c in cols.items():
            if re.sub(r"[\s_]+","",k) == re.sub(r"[\s_]+","",key):
                return c
        # tolerate 'noteable' vs 'notable'
        for k, c in cols.items():
            if k.replace("eable","able") == key.replace("eable","able"):
                return c
    raise KeyError(f"Column '{name_guess}' not found. Available: {list(df.columns)}")

def parse_dt(series, shift_hours=0):
    """Parse timestamps to 'YYYY-MM-DD HH:MM' and apply hour shift."""
    def _parse_one(x):
        if pd.isna(x): return pd.NaT
        s = str(x).strip().replace("T"," ")
        # drop timezone suffix and microseconds
        s = re.sub(r"(Z|[+-]\d{2}:?\d{2})$","",s)
        m = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})(?::\d{2})?(?:\.\d+)?$", s)
        if m: s = m.group(1)+":00" if len(m.group(1))==16 else m.group(1)
        return pd.to_datetime(s, errors="coerce")
    dt = series.map(_parse_one)
    if shift_hours:
        dt = dt + pd.to_timedelta(shift_hours, unit="h")
    return dt.dt.strftime("%Y-%m-%d %H:%M")


def extract_height_m(sites_row, col_height_m=None, col_height_ft=None):
    """Return height in meters if available; try meters first, else feet->meters; parse strings with units."""
    def parse_val(v):
        if v is None or (isinstance(v, float) and pd.isna(v)):
            return None
        s = str(v).strip()
        # try pure number
        try:
            return float(s)
        except Exception:
            pass
        # try patterns like "21.3 m" or "70 ft"
        m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*(m|meter|meters|ft|feet)?", s, flags=re.I)
        if m:
            val = float(m.group(1))
            unit = (m.group(2) or "m").lower()
            if unit in ["m", "meter", "meters"]:
                return val
            if unit in ["ft", "feet"]:
                return val * 0.3048
        return None

    # meters first
    if col_height_m and col_height_m in sites_row:
        hm = parse_val(sites_row[col_height_m])
        if hm is not None:
            return hm
    # feet next
    if col_height_ft and col_height_ft in sites_row:
        hf = parse_val(sites_row[col_height_ft])
        if hf is not None:
            return hf  # already converted in parse_val if feet
    # fallback: scan any column named like height
    for k, v in sites_row.items():
        if re.search(r"height", str(k), flags=re.I):
            hv = parse_val(v)
            if hv is not None:
                return hv
    return None


def html_to_text_preserve_lines(s: str) -> str:
    """Convert HTML to plain text while preserving logical line breaks between paragraphs/list items/br."""
    if s is None: return ""
    txt = str(s)
    # Normalize newlines for block-level closers and <br>
    txt = re.sub(r"(?i)</\s*p\s*>", "\n", txt)
    txt = re.sub(r"(?i)<\s*br\s*/?>", "\n", txt)
    txt = re.sub(r"(?i)</\s*li\s*>", "\n", txt)
    txt = re.sub(r"(?i)</\s*div\s*>", "\n", txt)
    # Remove remaining tags
    txt = re.sub(r"<[^>]+>", "", txt)
    # Unescape entities
    txt = unescape(txt)
    # Collapse multiple blank lines to single
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    # Trim spaces around line starts
    txt = "\n".join(line.strip() for line in txt.splitlines()).strip()
    return txt



def format_meters(value) -> str:
    try:
        hv = float(value)
        s = f"{hv:.3f}"
        s = s.rstrip('0').rstrip('.')
        return s
    except Exception:
        return str(value).strip()

def build_description(height_val, notes_df, shift_hours=0, strip_html=False):
    parts = []
    height_line = ""
    if pd.notna(height_val):
        try:
            hv = float(height_val)
            height_line = f"Height: {hv:g} m"
        except Exception:
            height_line = f"Height: {str(height_val).strip()}"
    # Prepare notes (strip HTML and drop timestamps)
    note_lines = []
    if notes_df is not None and len(notes_df):
        msgs = notes_df["message"].astype(str).fillna("")
        if strip_html:
            msgs = msgs.map(html_to_text_preserve_lines)
        # split multiline and strip trailing spaces, keep blank lines between HTML paragraphs
        for m in msgs:
            for ln in str(m).splitlines():
                note_lines.append(ln.strip())
    # Build description with CRLF and a space-only line between height and notes to force visible gap
    if height_line and note_lines:
        desc = height_line + "\r\n \r\n" + "\r\n".join(note_lines)
    elif height_line:
        desc = height_line
    else:
        desc = "\r\n".join(note_lines)
    return desc


def state_full_name(subdivision: str):
    if not subdivision: return ""
    s = str(subdivision).strip()
    s = s.replace("US_", "").replace("US-", "")
    s = s.upper()
    return US_STATE_MAP.get(s, subdivision)

def format_address(addr):
    line1 = addr.get("line1","")
    city = addr.get("city","")
    state = state_full_name(addr.get("subdivision",""))
    zipc = addr.get("zip","")
    parts = [line1, city, state, zipc]
    items = [str(x).strip() for x in parts if str(x).strip()]
    return ", ".join(items)

def main():
    ap = argparse.ArgumentParser(description="Build network_sites_import.csv")
    ap.add_argument("--sites", required=True, help="network_sites.csv from Sonar")
    ap.add_argument("--notes", required=True, help="notes.csv from Sonar")
    ap.add_argument("--addresses", required=True, help="addresses.csv from Sonar")
    ap.add_argument("--output", required=True, help="Output CSV path")
    ap.add_argument("--strip-html", action="store_true", help="Strip HTML and preserve line breaks in notes")
    ap.add_argument("--shift-hours", type=int, default=0, help="Hour offset to apply to note timestamps")
    args = ap.parse_args()

    # Load inputs
    try: sites = pd.read_csv(args.sites)
    except Exception: sites = pd.read_csv(args.sites, sep=";")
    try: notes = pd.read_csv(args.notes)
    except Exception: notes = pd.read_csv(args.notes, sep=";")
    try: addrs = pd.read_csv(args.addresses)
    except Exception: addrs = pd.read_csv(args.addresses, sep=";")

    # Resolve site columns
    col_sid = resolve_col(sites, "ID")
    col_title = resolve_col(sites, "name", ["title", "site name"])
    # height columns (meters and feet) - optional
    try:
        col_height_m = resolve_col(sites, "height", ["height m","height (m)","height meters","tower height (m)","tower height"])
    except Exception:
        col_height_m = None
    try:
        col_height_ft = resolve_col(sites, "height ft", ["height (ft)","height feet","tower height ft","tower height (ft)"])
    except Exception:
        col_height_ft = None

    # Resolve address columns & filter
    col_owner = resolve_col(addrs, "address owner")
    col_owner_id = resolve_col(addrs, "address owner ID")
    col_line1 = resolve_col(addrs, "address line 1", ["line 1","street","address1"])
    # city/state/zip can vary
    col_city = resolve_col(addrs, "city", ["town"])
    col_subdiv = resolve_col(addrs, "subdivision", ["state","region","province"])
    col_zip = resolve_col(addrs, "zip code", ["zip","postal code","postcode"])
    col_lat = resolve_col(addrs, "latitude", ["lat"])
    col_lon = resolve_col(addrs, "longitude", ["lon","long","lng"])

    addrs_ns = addrs[addrs[col_owner].astype(str).str.replace(" ","").str.lower().isin(["networksite","network site"])].copy()

    # Build an address dict keyed by owner_id
    addr_map = {}
    for _, r in addrs_ns.iterrows():
        oid = r[col_owner_id]
        addr_map[oid] = {
            "line1": r.get(col_line1, ""),
            "city": r.get(col_city, ""),
            "subdivision": r.get(col_subdiv, ""),
            "zip": r.get(col_zip, ""),
            "lat": r.get(col_lat, ""),
            "lon": r.get(col_lon, ""),
        }

    # Resolve notes columns & filter to Network site
    n_type = resolve_col(notes, "notable type", ["noteable type"])
    n_id = resolve_col(notes, "notable ID", ["noteable ID"])
    n_created = resolve_col(notes, "created at")
    n_msg = resolve_col(notes, "message")

    notes_ns = notes[notes[n_type].astype(str).str.replace(" ","").str.lower().isin(["networksite","network site"])].copy()
    notes_ns = notes_ns.rename(columns={n_created:"created_at", n_msg:"message", n_id:"site_id"})
    # group by site_id
    grouped = notes_ns.groupby("site_id")

    rows = []
    for _, srow in sites.iterrows():
        sid = srow[col_sid]
        title = srow[col_title]
        height_val = extract_height_m(srow, col_height_m, col_height_ft)
        # Description: height + notes (shifted)
        site_notes = None
        if sid in grouped.groups:
            site_notes = grouped.get_group(sid)[["created_at","message"]].sort_values("created_at")
        desc = build_description(height_val, site_notes, shift_hours=args.shift_hours, strip_html=args.strip_html)

        # Address & coords
        addr = addr_map.get(sid, {})
        address_str = format_address(addr)
        geo = ""
        lat = addr.get("lat")
        lon = addr.get("lon")
        if pd.notna(lat) and pd.notna(lon) and str(lat) != "" and str(lon) != "":
            geo = f"{float(lat)},{float(lon)}"

        rows.append({
            "id": sid,
            "location": 1,
            "title": title,
            "description": desc,
            "address": address_str,
            "geo coordinates": geo
        })

    out = pd.DataFrame(rows, columns=["id","location","title","description","address","geo coordinates"])
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} rows to {args.output}")

if __name__ == "__main__":
    main()
