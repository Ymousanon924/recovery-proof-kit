# Recovery Evidence Report — Example SaaS

**Overall artifact status:** `PASS`  
**Checked at:** `2026-09-19T20:56:33Z`  
**Artifact:** `[redacted backup path]`

> This report records an artifact verification result. It is not, by itself, proof that the production application can be restored.

## Artifact checks

| Check | Result | Details |
|---|---|---|
| exists | PASS | artifact found |
| minimum_size | PASS | artifact exceeded minimum size |
| freshness | PASS | artifact was within the configured age window |

## Restore-test contract

- Service: `example-saas`
- Isolated target: `example-restore-isolated`
- RPO target: `60 minutes`
- RTO target: `120 minutes`
- Restore-test status: `PLANNED`

## Notes

This is a redacted example. Never publish customer paths, hostnames, bucket names, credentials, or identifiers.

