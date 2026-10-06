# Lesson 38/41: Measuring Automation ROI

[Watch the lesson](https://youtu.be/XnRWq8_ESmA) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Measure a baseline and pilot time; include review effort and tool cost.

## Reference workflow

Trigger: Pilot review.

Subtract pilot plus review time from baseline; report measured and estimated inputs separately.

Read `blueprint.json`, fill appropriately typed values in `test-data.json`, and use `prompt.txt` with `system-instructions.txt`. Produce a field-mapping table and record each test result. These are portable design files, not Make/Zapier/n8n imports.

## Local controls demonstration

```text
python track-3-automation/simulator.py
```

Expected statuses include simulated_sent, duplicate_suppressed, approval_required and needs_review. This shared simulator demonstrates controls, not a working implementation of this lesson’s provider integration. No messages, events, posts or payments are sent.

## Verify

Test valid input, missing required fields, ambiguous content, repeated events and service failure. Keep unvalidated output in review. Do not promise ten hours saved without measurements.

## Continue

[Previous lesson](https://youtu.be/s2u2it3ZNmQ) · [Next lesson](https://youtu.be/xnL515DcruQ)

If a video is not released yet, save the master Course and complete the exercise before returning.
