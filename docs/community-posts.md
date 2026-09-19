# Community launch posts

These drafts are intentionally different by community. They ask for useful feedback first and keep the offer secondary.

## Reddit — r/selfhosted New Project Megathread

Use as a top-level comment in the current New Project Megathread. That thread explicitly asks for a project name, repo/site, description, deployment instructions, and AI involvement. Standalone project posts are redirected there.

**Project Name:** Recovery Proof Kit  
**Repo/Website Link:** [add public repository link]  

**Description:**

I kept finding the same uncomfortable gap in small self-hosted and SaaS setups: the backup job says “success,” but nobody has recently proved that the application can actually be restored.

Recovery Proof Kit is a small, read-only toolkit for turning that assumption into evidence. The first version checks backup freshness, minimum size, and optional SHA-256 integrity, then writes JSON and Markdown reports. It also creates a restore-test contract that documents an isolated restore target, RPO/RTO targets, smoke checks, and cleanup steps.

It does not replace a backup system, upload backup contents, or touch production. A checksum is deliberately not treated as proof of application recovery.

I’m looking for feedback from people running Docker, Postgres, VPS, WordPress, or small SaaS backups. In particular: what is the first check you perform before trusting a restore, and what evidence do you actually give customers or teammates?

**Deployment:**

Python standard library only for the current scripts. Example:

```text
python kit/scripts/rpk_verify_backup.py --path /path/to/backup --max-age-hours 26 --min-size-bytes 1024 --json-out artifacts/verification.json
```

**AI Involvement:**

AI was used to help draft and refine parts of the implementation. The scope, safety boundaries, examples, and tests were reviewed manually. The project does not send customer backup data to an AI service.

This is an early beta, so blunt technical feedback is more useful than compliments.

## Reddit — r/devops Weekly Self-Promotion Thread

I’m building Recovery Proof Kit, a small read-only toolkit for a problem I’ve seen repeatedly: backup jobs report success, but teams have no recent evidence that the application can be restored.

The first version verifies freshness, size, and optional SHA-256 integrity, then emits JSON/Markdown evidence. It also creates a non-destructive restore-test contract for an isolated target with RPO/RTO and application smoke checks.

I’m deliberately not building another generic cron monitor or backup dashboard. Existing tools cover that well. The question I’m testing is whether a lightweight evidence layer is useful for small SaaS teams, agencies, and MSPs.

Current beta is free to inspect and $19 for a guided setup. No credentials or backup contents leave the customer environment.

If you operate backups professionally: what does your current restore verification actually check beyond exit code and file existence?

## GitHub Discussions — own repository

**Title:** What should count as “recovery proof” for a small SaaS?

I’m building a small toolkit around backup verification and isolated restore testing. The current version checks artifact freshness, size, and optional SHA-256 integrity, and produces portable JSON/Markdown evidence.

I’m trying to avoid building another generic monitoring dashboard. I’d rather make the recovery checks and reports genuinely useful first.

For your own systems, which of these is hardest to prove?

1. The backup job ran.
2. The artifact is complete and intact.
3. The backup is protected from deletion or ransomware.
4. The application can be restored into an isolated target.
5. The restored application passes meaningful smoke tests.
6. The RPO/RTO result is documented for someone else.

If you have a real-world failure mode or a check you wish backup tools exposed, I’d appreciate the example.

## Discord — DevOps/SRE/Infrastructure community

I’m looking for a few operators to critique a small open-source recovery-evidence toolkit.

The problem: backup jobs can report success while the artifact is stale, incomplete, or never tested through an application restore.

The current kit runs locally and read-only. It checks freshness/size/digest, produces a report, and creates a restore-test plan for an isolated target. No backup contents or credentials are uploaded.

I’m not looking for broad “would you use this?” feedback. I’m looking for people who can say what their current backup verification misses, especially around Docker, Postgres, VPS, or MSP-managed environments.

Repository: [add public repository link]

## Hacker News — Show HN

**Show HN: Recovery Proof Kit — evidence that a backup is more than a green checkmark**

I built a small, dependency-free toolkit for verifying backup artifacts and documenting isolated restore tests.

The motivating problem is that “backup completed” is often treated as “we can recover.” The kit currently checks freshness, minimum size, and optional SHA-256 integrity, emits JSON, renders a Markdown evidence report, and creates a non-destructive restore contract with RPO/RTO and application-level smoke checks.

It intentionally does not replace a backup provider, upload backup contents, or run restore commands against production.

I’d especially like feedback from people who operate small SaaS systems, agencies, or MSP environments: what does your restore test verify, and what evidence do you wish you had during an incident?

Repository: [add public repository link]

