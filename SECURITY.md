# Security and limitations

Never commit secrets, private customer data or production webhook URLs. `.gitignore` does not remove already tracked secrets. Rotate exposed credentials with the provider and address prior copies.

All examples are local teaching exercises. The capstone email check is a minimal shape check, not proof of deliverability. The simulator uses a deterministic classifier, an in-memory sent set and a caller-provided approval value. It does not authenticate approvers or persist state. Production systems require authenticated approval records, access controls, durable transactional idempotency, observability, timeouts and provider-specific failure handling. A changed draft invalidates the simulated approval.

Use only synthetic fixtures. Do not report secrets publicly. A private vulnerability reporting contact must be configured by the repository owner before public launch.
