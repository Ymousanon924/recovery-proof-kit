# Changelog

All notable changes to Recovery Proof Kit are documented here.

## [0.1.0] - 2026-09-19

### Added

- Read-only backup artifact verification for freshness, size, and optional SHA-256 integrity.
- JSON verification output and Markdown recovery evidence reports.
- Non-destructive isolated restore-test contracts.
- Recovery manifest gap reporting.
- Postgres restore-lab example and sample redacted report.
- Unit tests and GitHub Actions verification of the example and test suite.

### Safety

- The toolkit does not upload backup contents, store credentials, or run restore commands against production.
- A checksum pass is explicitly separate from application-level recovery proof.

## Unreleased

Future changes will be recorded here before release.
