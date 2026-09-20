# Contributing

Thanks for taking a look. Recovery Proof Kit is intentionally small and safety-first.

## Before opening an issue

- Reproduce the behavior with synthetic or redacted data.
- Do not include credentials, backup contents, private URLs, or customer identifiers.
- Check whether the behavior is already covered by an existing issue.

## Local checks

Run the test suite from the repository root:

```powershell
python -m unittest discover -s tests -v
```

Compile the scripts before submitting a change:

```powershell
python -m compileall kit tests
```

For behavior changes, add or update a test and update the changelog when appropriate.

## Scope and safety

Changes must preserve the read-only default. Restore commands, credential handling, production mutations, and uploads require a separate design discussion before implementation.

Please describe what you tested, the environment used, and any known limitations in pull requests.
