# Lesson 15/41: How to Finish Your Coding Project and Put It on GitHub

[Watch the lesson](https://youtu.be/d6Cn-dw6i7c) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Clean code, add docstrings and README, run checks and prepare a 30-second demo.

## Companion

Complete [README_TEMPLATE.md](../README_TEMPLATE.md). The shared CSV-to-JSON capstone is a separate synthetic practice project supporting this topic.

```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
python -m unittest discover -s tests -v
```

Expected first run: accepted=2, rejected=1, duplicates=1. A repeated run refuses to overwrite; inspect the existing output before deliberately using `--overwrite`.

## Continue

[Previous lesson](https://youtu.be/Xgz3Qlu_lAY) · [Next lesson](https://youtu.be/c_j539EXAkM)

If a video is not released yet, save the master Course and complete the exercise before returning.
