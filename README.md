# AWS Cloud SOC Bridge

## Threat scenario

A simulated credential-theft scenario: an unusual `AssumeRole` event from an unfamiliar IP is correlated with a recent simulated endpoint process event and elevated to a Security Hub finding.

## Why it matters

Cloud identity compromise can precede endpoint telemetry. Correlating both signals reduces the time from control-plane anomaly to actionable SOC context.

## Architecture

CloudTrail events flow through EventBridge to a Python Lambda. The Lambda correlates event metadata with simulated EDR JSON stored in DynamoDB, writes correlation state, and emits a Security Hub custom finding. Notification/remediation adapters are deliberately dry-run only.

## Deploy

```sh
terraform init
terraform plan
terraform apply
```

Use a sandbox account. Estimated low-volume lab cost is roughly $5/month, excluding optional notification providers.

## Evidence

Run `python scripts/simulate_event.py` with the sample events, then capture the CloudWatch log and Security Hub finding. Do not commit webhook URLs, account IDs, or credentials.
