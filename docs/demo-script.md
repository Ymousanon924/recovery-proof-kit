# 15-minute demo script

## 0–2 minutes: Establish the problem

Ask: “If your backup job reports success tonight, what evidence will you have tomorrow that the application can actually be restored?”

Listen for:

- email-only alerts;
- no application-level test;
- stale runbooks;
- unknown RPO/RTO;
- backups stored with the same credentials as production.

## 2–6 minutes: Run an artifact check

Run the verifier against the sample or the customer's non-production artifact. Show the JSON result and explain that a clean exit code is not enough; the report records what was checked.

## 6–9 minutes: Show a detected gap

Run the manifest report with `immutability`, `offsite_copy`, or `last_restore_test` missing. Show `GAPS_FOUND` and explain that the product turns assumptions into an explicit remediation list.

## 9–12 minutes: Explain recovery proof

Show the restore contract. Emphasize that the target is isolated, application-level checks are required, and no production mutation is performed by the kit.

## 12–15 minutes: Make the offer

Offer a paid pilot:

> We will help you run the kit against one non-production environment, produce an evidence report, and identify the first recovery gaps. The pilot is fixed-price and does not require uploading backup data.

Do not promise compliance certification, guaranteed recoverability, or zero support requirements.

