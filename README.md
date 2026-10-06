# Rebootv2 course companion

Practice materials for the 41-video Python -> Capstone -> Applied AI course.

[Start the Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU) · [41-lesson map](COURSE_MAP.md)

Lesson folders now follow the verified YouTube course order. These are newly authored topic-matched exercises, not transcripts or copies of the original production assets. Some videos are scheduled or private and will become available through the release plan.

## Start here
Use Python 3.12. The checks were run on Python 3.12.14. No third-party Python packages, API keys or paid services are required for the local exercises.
```text
python -m unittest discover -s tests -v
```
1. Open the matching lesson README, attempt starter.py, then compare solution.py for lessons 01–12.
2. Complete the templates and runnable CSV-to-JSON capstone for lessons 13–17.
3. Use the topic-specific reference blueprints, prompt files, synthetic test cases and shared offline controls simulator for lessons 18–41.

## Capstone
```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
```
First run: accepted=2, rejected=1, duplicates=1. Existing output is protected; inspect it before deliberately adding --overwrite.

## Automation boundary
```text
python track-3-automation/simulator.py
```
This is a deterministic offline teaching simulator. It does not call AI providers, send messages, make payments or publish content. Reference JSON is not a verified Make, Zapier or n8n import. Real integrations need provider setup and separate end-to-end testing.

## Rights
[MIT license](LICENSE) applies to companion software and associated documentation. Videos, audio, artwork and branding are excluded; see [rights](RIGHTS.md). No affiliation with MIT is claimed.
