#!/usr/bin/env python3
"""Parse the saved Splynx documentation and summarize default role permissions."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from bs4 import BeautifulSoup

DOC_PATH = Path("Splynx_ Roles.html")

STATUS_KEYWORDS = {
    "full access": "Full access",
    "no access": "No access",
    "read-only": "Read-only",
}


def extract_role_permissions(doc_path: Path) -> Dict[str, List[str]]:
    soup = BeautifulSoup(doc_path.read_text(encoding="utf-8"), "html.parser")
    summary: Dict[str, List[str]] = {}

    for details in soup.find_all("details"):
        summary_tag = details.find("summary")
        if not summary_tag:
            continue
        role_name = summary_tag.get_text(strip=True)
        permissions: List[str] = []

        for table in details.find_all("table"):
            cells = table.find_all("td")
            if len(cells) < 2:
                continue
            module = cells[0].get_text(strip=True)
            if not module:
                continue
            description = " ".join(cells[1].stripped_strings)
            description_lower = description.lower()
            status_text = None
            for key, value in STATUS_KEYWORDS.items():
                if key in description_lower:
                    status_text = value
                    break
            if status_text:
                permissions.append(f"{module}: {status_text}")

        summary[role_name] = permissions

    return summary


def main() -> None:
    if not DOC_PATH.exists():
        raise SystemExit(f"Documentation file {DOC_PATH} not found")

    summary = extract_role_permissions(DOC_PATH)
    for role, entries in summary.items():
        print(f"Role: {role}")
        if not entries:
            print("  (no textual permission statements; see source document)")
        else:
            for entry in entries:
                print(f"  - {entry}")
        print()


if __name__ == "__main__":
    main()

