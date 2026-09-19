# Security notes

Recovery Proof Kit is designed to be run inside the customer's environment.

- Do not upload backup contents.
- Do not place backup credentials in source control.
- Use least-privilege, read-only credentials for artifact checks.
- Use separate credentials and an isolated target for restore tests.
- Do not run restore commands against production.
- Treat generated reports as potentially sensitive because paths, service names, timestamps, and infrastructure details may be included.
- Redact customer names, bucket names, hostnames, and identifiers before public examples.
- Use immutable/offline backup controls supplied by the storage provider; this kit does not make storage immutable.
- Review any future hosted service for encryption, tenant isolation, retention, deletion, incident response, and access logging before accepting customer evidence.

