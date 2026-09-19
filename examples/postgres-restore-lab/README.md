# Postgres restore lab

This is a deliberately isolated example for testing a Postgres backup. It is documentation only until an operator supplies a backup and explicitly chooses a non-production target.

## Safe sequence

1. Create a disposable Postgres instance with no production network access.
2. Restore a copy of the backup into a new database name.
3. Run the smoke checks in `smoke-check.sql`.
4. Record the restore start/end timestamps.
5. Record the newest recovered application timestamp.
6. Destroy the disposable instance after collecting evidence.

For custom-format archives, inspect contents before restoring:

```powershell
pg_restore --list .\backup.dump
```

Never point the restore command at a production database. Keep the backup credentials and encryption keys separate from the production runtime credentials.

