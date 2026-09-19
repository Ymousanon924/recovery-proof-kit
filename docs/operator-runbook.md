# Operator runbook

## Before running a check

1. Confirm the path is a backup artifact or backup staging directory.
2. Confirm the command will run with read-only access.
3. Confirm no production restore target is configured.
4. Confirm reports will be stored securely because they can contain infrastructure details.

## Artifact verification

Run:

```powershell
python kit/scripts/rpk_verify_backup.py `
  --path C:\path\to\backup `
  --max-age-hours 26 `
  --min-size-bytes 1024 `
  --json-out artifacts\verification.json
```

Interpretation:

- `PASS` means the artifact checks passed.
- `FAIL` means the artifact should not be treated as recoverable evidence.
- A passing artifact check does not prove that the application can be restored.

## Recovery manifest review

Copy the template, fill in facts without adding secrets, and run:

```powershell
python kit/scripts/rpk_manifest_report.py `
  --manifest kit\templates\recovery-manifest.json `
  --out artifacts\manifest-report.json
```

Treat `GAPS_FOUND` as a remediation list, not as a failed backup.

## Isolated restore test

The restore target must be separate from production. Record:

- backup reference;
- restore start and end timestamps;
- newest recovered data timestamp;
- application-level smoke-test results;
- cleanup confirmation;
- operator and reviewer.

Only after those checks pass should the result be called recovery proof.

