# Lesson 17/41: From Idea to Working App: Complete Python Capstone Walkthrough

[Watch the lesson](https://youtu.be/AGePQjS-4Ro) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Run a complete sample input through the capstone and show the resulting output.

## Companion

Complete [DEMO_AND_REVIEW.md](../DEMO_AND_REVIEW.md). The shared CSV-to-JSON capstone is a separate synthetic practice project supporting this topic.

```text
python track-2-capstone/src/app.py --input track-2-capstone/fixtures/leads.csv --output output/leads.json
python -m unittest discover -s tests -v
```

Expected first run: accepted=2, rejected=1, duplicates=1. A repeated run refuses to overwrite; inspect the existing output before deliberately using `--overwrite`.

## Continue

[Previous lesson](https://youtu.be/c_j539EXAkM) · [Next lesson](https://youtu.be/hdTeJy2eUPs)

If a video is not released yet, save the master Course and complete the exercise before returning.
