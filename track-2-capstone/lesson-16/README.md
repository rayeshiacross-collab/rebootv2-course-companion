# Lesson 16/41: Finish Your Coding Project — Capstone QA, Demo and Portfolio Handoff

[Watch the lesson](https://youtu.be/c_j539EXAkM) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Demonstrate capstone QA evidence, README reproducibility and a portfolio handoff.

## Companion

Complete [QA_CHECKLIST.md](../QA_CHECKLIST.md). The shared CSV-to-JSON capstone is a separate synthetic practice project supporting this topic.

```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
python -m unittest discover -s tests -v
```

Expected first run: accepted=2, rejected=1, duplicates=1. A repeated run refuses to overwrite; inspect the existing output before deliberately using `--overwrite`.

## Continue

[Previous lesson](https://youtu.be/d6Cn-dw6i7c) · [Next lesson](https://youtu.be/AGePQjS-4Ro)

If a video is not released yet, save the master Course and complete the exercise before returning.
