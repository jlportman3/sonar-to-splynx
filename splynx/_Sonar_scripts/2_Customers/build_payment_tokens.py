#!/usr/bin/env python3
import argparse
import pandas as pd
import re
from pathlib import Path
from typing import Dict, Tuple

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
        # relaxed
        for ck, cn in cmap.items():
            if re.sub(r'[\s_]+' ,'' , ck) == re.sub(r'[\s_]+' ,'' , k):
                return cn
    if required:
        raise KeyError(f"Column '{name}' not found. Available: {list(df.columns)}")
    return None

def normalize_last4(masked: str) -> str:
    if not masked or pd.isna(masked): 
        return ""
    s = str(masked).strip()
    # extract last 4 digits
    digits = re.findall(r"\d", s)
    if not digits:
        return ""
    last = "".join(digits[-4:])
    return last.zfill(4)

def build_processor_map(proc_df: pd.DataFrame) -> Dict[int, str]:
    col_id = resolve_col(proc_df, "ID", ["id","processor id"])
    col_provider = resolve_col(proc_df, "provider", ["name","title","processor","gateway"])
    ids = pd.to_numeric(proc_df[col_id], errors="coerce").astype("Int64")
    providers = proc_df[col_provider].astype(str).str.upper()
    return dict(zip(ids, providers))

def choose_records(cards: pd.DataFrame, key_cols: Tuple[str, str]) -> pd.Series:
    """
    Return boolean mask of rows chosen for import per (account ID, processor).
    Rule: prefer auto==1; if multiple, pick with latest expiration (year, month). If none auto, pick latest expiration.
    """
    acct_col, proc_col = key_cols
    # Prepare expiration comparable key (YYYY-MM)
    year_col = resolve_col(cards, "expiration year", ["exp year","expiration_year","year"])
    month_col = resolve_col(cards, "expiration month", ["exp month","expiration_month","month"])
    exp_year = pd.to_numeric(cards[year_col], errors="coerce").fillna(0).astype(int)
    exp_month = pd.to_numeric(cards[month_col], errors="coerce").fillna(0).astype(int)
    exp_key = exp_year * 100 + exp_month
    auto_col = None
    try:
        auto_col = resolve_col(cards, "auto", ["is auto","autopay","default"], required=False)
    except KeyError:
        auto_col = None
    auto = pd.to_numeric(cards[auto_col], errors="coerce").fillna(0).astype(int) if auto_col else pd.Series([0]*len(cards))

    cards = cards.copy()
    cards["__expkey"] = exp_key
    cards["__auto"] = auto
    cards["__idx"] = range(len(cards))

    def pick_group(g: pd.DataFrame) -> pd.Series:
        # choose index of the row
        if (g["__auto"] == 1).any():
            g2 = g[g["__auto"] == 1]
            # pick max exp
            row = g2.loc[g2["__expkey"].idxmax()]
        else:
            row = g.loc[g["__expkey"].idxmax()]
        chosen_idx = row["__idx"]
        return g["__idx"] == chosen_idx

    chosen_mask = cards.groupby([acct_col, proc_col], group_keys=False, observed=True).apply(pick_group, include_groups=False)
    # chosen_mask is boolean Series aligned to group, ensure full alignment
    chosen_mask = chosen_mask.astype(bool).reindex(cards.index, fill_value=False)
    return chosen_mask

def main():
    ap = argparse.ArgumentParser(description="Build per-processor payment token files from Sonar credit cards CSVs")
    ap.add_argument("--credit-cards", required=True, help="credit_cards.csv")
    ap.add_argument("--processors", required=True, help="credit_card_processors.csv")
    ap.add_argument("--out-dir", required=True, help="Output directory")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cards = read_csv_auto(Path(args.credit_cards))
    procs = read_csv_auto(Path(args.processors))

    # Resolve columns in cards
    col_account = resolve_col(cards, "account ID", ["account id","customer id","customer_id"])
    col_proc_id = resolve_col(cards, "credit card processor ID", ["processor id","credit_card_processor_id","processor"])
    col_profile = resolve_col(cards, "customer profile ID", ["customer profile id","profile id"], required=False)
    col_token = resolve_col(cards, "token", ["payment token","vault token","token id"])
    col_name = resolve_col(cards, "name on card", ["card name","holder name","cardholder name"])
    col_masked = resolve_col(cards, "masked number", ["masked","last digits","last4","last 4"])
    col_exp_y = resolve_col(cards, "expiration year", ["exp year","year"])
    col_exp_m = resolve_col(cards, "expiration month", ["exp month","month"])
    col_job_auto = None
    try:
        col_job_auto = resolve_col(cards, "auto", ["autopay","is auto","default"], required=False)
    except KeyError:
        col_job_auto = None

    # Processor provider lookup
    proc_map = build_processor_map(procs)

    # Normalize basic fields
    cards_norm = pd.DataFrame()
    cards_norm["customer_id"] = pd.to_numeric(cards[col_account], errors="coerce").astype("Int64")
    cards_norm["processor_id_raw"] = pd.to_numeric(cards[col_proc_id], errors="coerce").astype("Int64")
    cards_norm["payment_type_id"] = cards_norm["processor_id_raw"].map(proc_map).fillna("")
    cards_norm["customer_profile_ID"] = cards[col_profile] if col_profile else ""
    cards_norm["token"] = cards[col_token].fillna("")
    cards_norm["card_name"] = cards[col_name].fillna("")
    cards_norm["last_digits"] = cards[col_masked].map(normalize_last4)
    # exp_date YYYY-MM
    exp_y = pd.to_numeric(cards[col_exp_y], errors="coerce").fillna(0).astype(int)
    exp_m = pd.to_numeric(cards[col_exp_m], errors="coerce").fillna(0).astype(int).clip(0, 12)
    cards_norm["exp_date"] = exp_y.astype(str).str.zfill(4) + "-" + exp_m.astype(str).str.zfill(2)
    cards_norm["auto"] = pd.to_numeric(cards[col_job_auto], errors="coerce").fillna(0).astype(int) if col_job_auto else 0

    # Attach group keys
    cards_norm["__acct"] = cards_norm["customer_id"].astype("Int64")
    cards_norm["__proc"] = cards_norm["processor_id_raw"].astype("Int64")

    # Choose per (acct, proc)
    cards_for_choice = cards_norm.copy()
    cards_for_choice["expiration year"] = exp_y
    cards_for_choice["expiration month"] = exp_m
    chosen_mask = choose_records(cards_for_choice, ("__acct","__proc"))
    cards_norm["__chosen"] = chosen_mask.values

    # Split by provider names
    prov = cards_norm["payment_type_id"].str.upper()
    buckets = {
        "AUTHORIZE": cards_norm[prov.str.contains("AUTHORIZE", na=False)],
        "IPPAY": cards_norm[prov.str.contains("IPPAY", na=False)],
        "SONARPAY": cards_norm[prov.str.contains("SONARPAY", na=False)],
    }

    created_files = []

    for name, dfb in buckets.items():
        if dfb.empty:
            continue

        # Export main selection
        selected = dfb[dfb["__chosen"]].copy()

        if name == "IPPAY":
            cols = ["customer_id","payment_type_id","token","card_name","last_digits","exp_date"]
        else:  # AUTHORIZE, SONARPAY
            cols = ["customer_id","payment_type_id","customer_profile_ID","token","card_name","last_digits","exp_date"]

        if not selected.empty:
            out_file = out_dir / f"{name}.csv"
            selected[cols].to_csv(out_file, index=False, encoding="utf-8")
            created_files.append(str(out_file))

        # Export duplicates report
        dup_groups = dfb.groupby(["__acct","__proc"], observed=True).filter(lambda g: len(g) > 1)
        if not dup_groups.empty:
            dup = dup_groups.copy()
            dup["imported"] = dup["__chosen"].map(lambda x: "yes" if x else "no")
            if name == "IPPAY":
                dup_cols = cols + ["auto","imported"]
            else:
                dup_cols = cols + ["auto","imported"]
            out_dup = out_dir / f"{name}_duplicates.csv"
            dup[dup_cols].to_csv(out_dup, index=False, encoding="utf-8")
            created_files.append(str(out_dup))

    if created_files:
        print("Created files:")
        for f in created_files:
            print(" -", f)
    else:
        print("No files created (no matching records).")

if __name__ == "__main__":
    main()
