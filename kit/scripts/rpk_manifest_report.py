#!/usr/bin/env python3
"""Score a recovery manifest without connecting to customer infrastructure."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {
    "service",
    "owner",
    "backup_provider",
    "backup_location",
    "backup_frequency",
    "encryption",
    "immutability",
    "offsite_copy",
    "rpo_minutes",
    "rto_minutes",
    "last_restore_test",
    "restore_target",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Report gaps in a recovery manifest.")
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    missing = sorted(field for field in REQUIRED if manifest.get(field) in (None, "", "unknown", "未設定"))
    warnings = []
    if manifest.get("immutability") is not True:
        warnings.append("Immutability is not confirmed.")
    if manifest.get("offsite_copy") is not True:
        warnings.append("An offsite copy is not confirmed.")
    if not manifest.get("last_restore_test"):
        warnings.append("No restore-test date is recorded.")

    result = {
        "schema_version": "0.1",
        "check_type": "recovery_manifest",
        "service": manifest.get("service", "unknown"),
        "status": "PASS" if not missing and not warnings else "GAPS_FOUND",
        "missing_fields": missing,
        "warnings": warnings,
        "manifest": manifest,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

