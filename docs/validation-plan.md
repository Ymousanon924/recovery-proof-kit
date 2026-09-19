# Validation plan

## First five interviews

Recruit:

- two small SaaS operators;
- two MSP or agency operators;
- one independent DevOps consultant.

Ask for a screen-share walkthrough of their current backup process. Do not ask only whether they like the idea.

## Evidence to collect

- backup systems and storage targets;
- how success is currently determined;
- last time a real restore was performed;
- most recent silent failure;
- current reporting or ticketing process;
- acceptable RPO and RTO;
- number of clients or environments;
- budget and purchasing authority.

## Paid validation gate

Do not build hosted multi-tenant features until at least three people agree to run the kit against a real non-production environment and at least one pays.

## Success criteria for version 0.1

- five real installations;
- first useful result in under 30 minutes;
- no customer backup data leaves the customer environment;
- at least one previously unknown failure detected;
- fewer than two support requests per installation;
- at least one request for recurring reporting or monitoring.

## Interview red flags

- They only want a free script.
- They already perform regular isolated restore tests and have no reporting pain.
- They cannot identify who owns recovery.
- They want a fully managed backup service rather than evidence tooling.
- Their environment is too regulated for an unreviewed early product.

