# Recovery Proof Kit

[![Verify example backup](https://github.com/Ymousanon924/recovery-proof-kit/actions/workflows/verify-example.yml/badge.svg)](https://github.com/Ymousanon924/recovery-proof-kit/actions/workflows/verify-example.yml)
[![Latest tag](https://img.shields.io/github/v/tag/Ymousanon924/recovery-proof-kit)](https://github.com/Ymousanon924/recovery-proof-kit/tags)

Recovery Proof Kit is a small, safety-first toolkit for proving that scheduled backups are fresh, intact, and usable.

The first release is intentionally a local, dependency-free starter kit. It does not copy, delete, restore, or upload customer data. It verifies backup artifacts, produces a machine-readable result, and can optionally send a heartbeat only after verification succeeds.

## Product promise

> Turn “the backup job says success” into evidence that the backup artifact exists, is fresh, passes integrity checks, and has a documented recovery path.

## Current scope

- Verify a backup file or directory exists.
- Check freshness, minimum size, and optional SHA-256 digest.
- Emit JSON suitable for CI, ticketing, or a future hosted service.
- Optionally send a heartbeat after a successful verification.
- Provide a safe restore-test contract without running destructive commands.
- Generate a starter recovery manifest and client-facing report.

## Recovery manifest

Use `kit/templates/recovery-manifest.json` to record ownership, storage, encryption, immutability, offsite-copy, RPO, RTO, and restore-test facts. It contains no credential fields. Review it with:

```powershell
python .\kit\scripts\rpk_manifest_report.py `
  --manifest .\kit\templates\recovery-manifest.json `
  --out .\artifacts\manifest-report.json
```

## Quick start

```powershell
python .\kit\scripts\rpk_verify_backup.py `
  --path .\examples\sample-backup.bin `
  --max-age-hours 48 `
  --min-size-bytes 16 `
  --json-out .\artifacts\verification.json
```

Exit code `0` means the checks passed. Exit code `1` means a check failed. Exit code `2` means the configuration or invocation was invalid.

To test the example with a real digest calculated locally:

```powershell
$expectedHash = (Get-FileHash .\examples\sample-backup.bin -Algorithm SHA256).Hash.ToLower()

python .\kit\scripts\rpk_verify_backup.py `
  --path .\examples\sample-backup.bin `
  --max-age-hours 48 `
  --min-size-bytes 16 `
  --sha256 $expectedHash `
  --json-out .\artifacts\verification.json
```

The command above calculates the expected digest from the local sample. The digest is never copied from a documentation example.

Render a portable evidence report:

```powershell
python .\kit\scripts\rpk_report.py `
  --verification .\artifacts\verification.json `
  --contract .\artifacts\restore-contract.json `
  --customer "Example SaaS" `
  --out .\artifacts\recovery-evidence.md
```

## Safety boundary

This starter kit never treats a file checksum as proof that an application can be restored. Full recovery proof requires a restore into an isolated environment and an application-level check. The included restore contract documents that next step without executing it automatically.

## Research basis

The design follows the principles of regular backup and restoration testing, offline/encrypted/immutable copies, and 3-2-1-style resilience guidance from CISA and NIST. See `docs/research-notes.md`.

## Roadmap

1. Validate the kit with five real operators.
2. Add Postgres and Docker Compose adapters.
3. Add restore-test evidence and RTO/RPO measurement.
4. Add signed, client-ready reports.
5. Add a small hosted heartbeat/reporting service only after users request it.

## Development status

This repository is an early beta, currently released as `v0.1.0`. The free Community Edition is the primary product. The project is being validated with operators before larger integrations or hosted features are built. See [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md), and the [open issues](https://github.com/Ymousanon924/recovery-proof-kit/issues).

## Optional guided help

- Community Edition: free and self-serve.
- Beta Edition: $19 for one setup walkthrough and one evidence report.
- Guided Pilot: $79 for hands-on implementation help.

These are optional validation offers, not required for using the repository. No payment is required to inspect or run the Community Edition.
