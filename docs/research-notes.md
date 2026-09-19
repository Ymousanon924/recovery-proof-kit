# Research notes

## Design conclusions

- CISA guidance emphasizes offline backups, regular backup and restoration, encryption, immutability, and coverage of the organization’s data infrastructure.
- NIST SP 800-34 treats contingency planning as an ongoing lifecycle that includes recovery strategies, testing, training, exercises, and maintenance.
- Community discussions repeatedly report silent backup failures, noisy notifications, stale runbooks, and backup files that have never been restored.
- Existing platforms already cover generic heartbeat monitoring and MSP backup result aggregation. The differentiator must be application-level recovery evidence.

## Product implications

1. Check the effect of a backup, not only the process exit code.
2. Make checks read-only by default.
3. Keep customer data in the customer’s environment during the first release.
4. Require an explicit isolated restore target for destructive or state-changing tests.
5. Produce portable JSON and Markdown evidence instead of locking customers into a dashboard.
6. Treat a successful artifact check and a successful application restore as different statuses.

## Important terminology

- **Artifact check:** the expected backup exists, is fresh, meets minimum size, and passes integrity checks.
- **Restore check:** a copy is restored into an isolated target and the application is exercised.
- **Recovery proof:** artifact check plus restore check plus recorded RPO/RTO results.
- **RPO:** maximum acceptable data loss measured in time.
- **RTO:** maximum acceptable time to restore service.

## Sources

- CISA StopRansomware guidance: https://www.cisa.gov/stopransomware/ransomware-guide
- NIST SP 800-34 contingency planning: https://csrc.nist.gov/pubs/sp/800/34/final
- CISA MSP guidance: https://www.cisa.gov/news-events/alerts/2022/05/11/protecting-against-cyber-threats-managed-service-providers-and-their-customers
- PostgreSQL backup and restore documentation: https://www.postgresql.org/docs/current/backup.html
- Docker Compose health checks: https://docs.docker.com/compose/how-tos/startup-order/
- AWS S3 Object Lock: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html
- Cloudflare R2 S3 API: https://developers.cloudflare.com/r2/api/s3/api/

