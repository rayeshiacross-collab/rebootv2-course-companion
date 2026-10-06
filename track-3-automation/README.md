# Applied automation practice

The 24 lesson guides cover the working map for lessons 18–41. The matching JSON blueprints specify inputs, decisions, tests and controls. They are vendor-neutral reference designs, not native import files.

Run `python track-3-automation/simulator.py` from the repository root. The simulator validates synthetic intake, applies deterministic category rules, routes ambiguous input to review, binds approval to a draft digest, simulates one send per event ID and records minimal logs. It never calls an AI model or external service.

Edit a draft after approval to see why the approval must be renewed. Replay an approved event to see duplicate suppression. Restarting the process loses the sent set: production persistence and concurrency are explicitly out of scope.

For a real integration, record vendor, sandbox destination, credential method, schema, retry limits, idempotency behavior, approval policy, logs and execution evidence. Keep external integrations marked unverified until actually tested.
