# Repository validation

October 6, 2026 — companion version 0.1.0

- 19 unittest methods passed on Python 3.12.14, including twelve solution executions and branch/error subcases.
- Capstone checks passed for normalization, blank/type rejection, duplicate handling, malformed CSV headers, JSON persistence and overwrite protection.
- Simulator checks passed for approval, changed drafts, ambiguous and malformed decisions, failed service recovery, duplicate suppression and minimal logs.
- Simulator command-line demonstration passed.
- 41 provisional lesson guides, 12 runnable solutions and 24 reference blueprint JSON files are present.
- Relative Markdown links resolve; JSON files parse; ZIP integrity passed.

The test environment used a workspace temporary directory because the sandbox's system temporary directory was not writable. No external services were called. Footage alignment, provider integrations, other Python versions, production readiness and licensing are not verified. Repository destination: https://github.com/rayeshiacross-collab/rebootv2-course-companion (private). The local folder is initialized as a Git repository; the ZIP contains source only, without Git internals or caches.
