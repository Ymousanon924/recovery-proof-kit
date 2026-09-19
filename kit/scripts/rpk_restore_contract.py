#!/usr/bin/env python3
"""Create a non-destructive restore-test contract.

This writes a plan; it never runs restore commands or touches production.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a safe restore-test contract.")
    parser.add_argument("--service", required=True)
    parser.add_argument("--backup-reference", required=True)
    parser.add_argument("--target", required=True, help="Explicit isolated target, e.g. docker-compose project name")
    parser.add_argument("--rpo-minutes", required=True, type=int)
    parser.add_argument("--rto-minutes", required=True, type=int)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    if args.rpo_minutes < 0 or args.rto_minutes <= 0:
        parser.error("RPO must be non-negative and RTO must be positive")

    contract = {
        "schema_version": "0.1",
        "contract_type": "isolated_restore_test",
        "created_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "service": args.service,
        "backup_reference": args.backup_reference,
        "isolated_target": args.target,
        "rpo_target_minutes": args.rpo_minutes,
        "rto_target_minutes": args.rto_minutes,
        "steps": [
            "Confirm the target is isolated from production and has an automatic cleanup plan.",
            "Restore the backup reference into the target using the platform's documented restore procedure.",
            "Run application-level smoke checks against the restored target.",
            "Record restore start/end timestamps and calculate RTO.",
            "Record the newest recovered data timestamp and calculate RPO.",
            "Destroy or quarantine the isolated target according to the approved procedure.",
            "Attach logs and the final result to the evidence report.",
        ],
        "status": "PLANNED",
        "warning": "This contract is documentation only. No restore action is executed by this tool.",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

