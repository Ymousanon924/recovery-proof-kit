#!/usr/bin/env python3
"""Render local verification JSON into a portable Markdown evidence report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a verification report.")
    parser.add_argument("--verification", required=True, type=Path)
    parser.add_argument("--contract", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--customer", default="Unassigned customer")
    args = parser.parse_args()

    verification = json.loads(args.verification.read_text(encoding="utf-8"))
    contract = json.loads(args.contract.read_text(encoding="utf-8")) if args.contract else None
    lines = [
        f"# Recovery Evidence Report — {args.customer}",
        "",
        f"**Overall artifact status:** `{verification.get('status', 'UNKNOWN')}`  ",
        f"**Checked at:** `{verification.get('checked_at', 'unknown')}`  ",
        f"**Artifact:** `{verification.get('path', 'unknown')}`  ",
        "",
        "> This report records an artifact verification result. It is not, by itself, proof that the production application can be restored.",
        "",
        "## Artifact checks",
        "",
        "| Check | Result | Details |",
        "|---|---|---|",
    ]
    for check in verification.get("checks", []):
        details = ", ".join(f"{key}={value}" for key, value in check.items() if key not in {"name", "passed"})
        lines.append(f"| {check.get('name')} | {'PASS' if check.get('passed') else 'FAIL'} | {details} |")

    if contract:
        lines.extend([
            "",
            "## Restore-test contract",
            "",
            f"- Service: `{contract.get('service')}`",
            f"- Isolated target: `{contract.get('isolated_target')}`",
            f"- Backup reference: `{contract.get('backup_reference')}`",
            f"- RPO target: `{contract.get('rpo_target_minutes')} minutes`",
            f"- RTO target: `{contract.get('rto_target_minutes')} minutes`",
            f"- Restore-test status: `{contract.get('status')}`",
        ])

    lines.extend([
        "",
        "## Operator notes",
        "",
        "- Record the restore target, start/end time, and application-level smoke-test results.",
        "- Keep backup credentials and encryption keys separate from the production environment.",
        "- Do not claim successful recovery until an isolated restore and application test pass.",
        "",
    ])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

