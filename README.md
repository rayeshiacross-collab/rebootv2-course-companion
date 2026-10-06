# Rebootv2 course companion

Hands-on Python practice, a runnable record-cleaning capstone, and offline automation reference exercises for the Rebootv2 learning path.

**Status: companion draft, October 6, 2026.**

**Live audit update:** All 41 video identities and master order are now verified in Studio. See [the verified video-to-practice crosswalk](COURSE_MAP.md). Existing practice-folder labels differ from several actual video topics; do not treat them as matched lesson downloads. The 41 lesson labels are a provisional map from the production documents. They are not verified video titles. Lesson 01 has a conflicting user-supplied planning title; other numbering conflicts are recorded in [the inventory notes](docs/INVENTORY_STATUS.md). Existing videos stay intact. Match these exercises to actual footage before public course rollout.

## Start here

Use Python 3.12 or newer. The complete local suite is tested on Python 3.12.14; other versions are not yet verified. There are no third-party Python dependencies, API keys, paid accounts, or network calls.

From this repository folder, run:

```text
python -m unittest discover -s tests -v
```

On systems where the command is `python3`, substitute it for `python`. A virtual environment is optional because these exercises use only the standard library.

1. [Python practice 01–12](track-1-python/README.md): starter files, solutions, inputs and expected results.
2. [Git and capstone 13–17](track-2-capstone/README.md): a working CSV-to-JSON application with validation and tests.
3. [Automation 18–41](track-3-automation/README.md): topic guides, portable blueprints and a deterministic local workflow simulator.

## Run the capstone

```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
```

The first run writes two valid unique records, rejects one blank record and counts one duplicate. It refuses to overwrite an existing output unless you add `--overwrite`.

## Run the automation simulator

```text
python track-3-automation/simulator.py
```

It prints an approved result, suppresses a repeated send, and displays review and rejection cases. It does not contact AI services, send mail, create calendar events or write to a CRM.

## What is included

- 41 provisional lesson guides with tasks, evidence checks and next steps.
- Twelve runnable Python solutions and separate starter exercises.
- Capstone input fixtures, validation, deduplication and JSON output.
- Twenty-four portable automation design records and an offline simulator.
- Automated tests, contribution guidance, security notes and release instructions.

The automation JSON files are reference specifications, **not Make, Zapier or n8n imports**. The simulator demonstrates application controls, not real model behavior or production-grade distributed processing.

## Rights and support

No open-source license has been selected by the owner. See [RIGHTS.md](RIGHTS.md) before redistribution. Do not assume the course videos or branding inherit rights from code. Use synthetic data and never submit credentials or private customer records in an issue.
