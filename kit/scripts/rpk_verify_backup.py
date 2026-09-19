#!/usr/bin/env python3
"""Read-only backup artifact verification for Recovery Proof Kit."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a backup artifact without modifying it.")
    parser.add_argument("--path", required=True, type=Path)
    parser.add_argument("--max-age-hours", required=True, type=float)
    parser.add_argument("--min-size-bytes", type=int, default=1)
    parser.add_argument("--sha256", help="Expected lowercase SHA-256 digest")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    if args.max_age_hours < 0 or args.min_size_bytes < 0:
        parser.error("age and minimum size must be non-negative")

    now = utc_now()
    checks = []
    path = args.path

    exists = path.exists()
    checks.append({"name": "exists", "passed": exists, "detail": str(path)})
    if not exists:
        return emit(args.json_out, path, now, checks, None)

    if path.is_file():
        size = path.stat().st_size
        modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        digest = sha256_file(path)
        kind = "file"
    else:
        files = [item for item in path.rglob("*") if item.is_file()]
        size = sum(item.stat().st_size for item in files)
        modified = max((datetime.fromtimestamp(item.stat().st_mtime, timezone.utc) for item in files), default=now)
        digest = None
        kind = "directory"

    age_hours = max(0.0, (now - modified).total_seconds() / 3600)
    size_ok = size >= args.min_size_bytes
    age_ok = age_hours <= args.max_age_hours
    checks.append({"name": "minimum_size", "passed": size_ok, "actual_bytes": size, "required_bytes": args.min_size_bytes})
    checks.append({"name": "freshness", "passed": age_ok, "age_hours": round(age_hours, 3), "maximum_age_hours": args.max_age_hours, "modified_at": iso(modified)})

    digest_ok = True
    if args.sha256:
        if kind != "file":
            digest_ok = False
            detail = "SHA-256 comparison is supported for files only"
        else:
            digest_ok = digest == args.sha256.lower()
            detail = digest
        checks.append({"name": "sha256", "passed": digest_ok, "expected": args.sha256.lower(), "actual": detail})

    return emit(args.json_out, path, now, checks, digest)


def emit(output: Path | None, path: Path, now: datetime, checks: list[dict], digest: str | None) -> int:
    passed = all(bool(item["passed"]) for item in checks)
    result = {
        "schema_version": "0.1",
        "tool": "recovery-proof-kit",
        "check_type": "artifact",
        "status": "PASS" if passed else "FAIL",
        "checked_at": iso(now),
        "path": str(path),
        "sha256": digest,
        "checks": checks,
    }
    encoded = json.dumps(result, indent=2)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except OSError as exc:
        print(f"configuration or filesystem error: {exc}", file=sys.stderr)
        raise SystemExit(2)

