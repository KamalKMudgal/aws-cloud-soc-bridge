# Safe response design

The repository intentionally performs no IAM revocation, webhook delivery, or live endpoint response. The handler only produces structured findings. Any future response adapter must require an explicit allowlist, a dry-run default, approval logging, and least-privilege credentials.
