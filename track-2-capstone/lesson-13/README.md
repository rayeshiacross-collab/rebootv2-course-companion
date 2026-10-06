# Lesson 13/41: Plan a Coding Project You Can Actually Finish — Capstone Scope

[Watch the lesson](https://youtu.be/0B0B3o-eo3M) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Complete a capstone scope brief with acceptance criteria, exclusions and risks.

## Companion

Complete [SCOPE_TEMPLATE.md](../SCOPE_TEMPLATE.md). The shared CSV-to-JSON capstone is a separate synthetic practice project supporting this topic.

```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
python -m unittest discover -s tests -v
```

Expected first run: accepted=2, rejected=1, duplicates=1. A repeated run refuses to overwrite; inspect the existing output before deliberately using `--overwrite`.

## Continue

[Previous lesson](https://youtu.be/pyEGcV8AHI0) · [Next lesson](https://youtu.be/Xgz3Qlu_lAY)

If a video is not released yet, save the master Course and complete the exercise before returning.
