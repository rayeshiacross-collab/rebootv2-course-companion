# Lesson 32/41: Data Entry And Document Processing

[Watch the lesson](https://youtu.be/P0DeUubFaRc) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Extract synthetic document fields; reject missing values and low-confidence results.

## Reference workflow

Trigger: Synthetic document received.

Extract named fields and mark unknown values explicitly.

Read `blueprint.json`, fill appropriately typed values in `test-data.json`, and use `prompt.txt` with `system-instructions.txt`. Produce a field-mapping table and record each test result. These are portable design files, not Make/Zapier/n8n imports.

## Local controls demonstration

```text
python track-3-automation/simulator.py
```

Expected statuses include simulated_sent, duplicate_suppressed, approval_required and needs_review. This shared simulator demonstrates controls, not a working implementation of this lesson’s provider integration. No messages, events, posts or payments are sent.

## Verify

Test valid input, missing required fields, ambiguous content, repeated events and service failure. Keep unvalidated output in review. Do not guess missing identifiers or retain private documents.

## Continue

[Previous lesson](https://youtu.be/yguls6WAqy0) · [Next lesson](https://youtu.be/FeyPmDjP84M)

If a video is not released yet, save the master Course and complete the exercise before returning.
