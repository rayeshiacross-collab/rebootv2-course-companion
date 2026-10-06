# Record cleaning capstone

Run commands from the repository root. `src/app.py` reads CSV columns `name` and `email`, trims whitespace, preserves the learner's name capitalization, lowercases example emails, rejects blank or minimally malformed records, and retains the first occurrence of each normalized email.

```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
python -m unittest discover -s tests -v
```

Expected summary: accepted=2, rejected=1, duplicates=1. The output JSON contains `records`, `rejected` and `duplicates`. Errors mention row numbers rather than copying rejected personal fields. Existing output is protected unless `--overwrite` is supplied. This is an offline exercise, not a production CRM or full email validator.

## Milestones

13: initialize Git and inspect ignore rules. 14: explain the input/validate/process/output architecture. 15: run and extend the MVP. 16: demonstrate happy and failure cases. 17: write a reproducible README and portfolio explanation. These numbers require footage matching.
