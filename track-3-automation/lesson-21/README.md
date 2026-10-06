# Lesson 21/41: Setting Up Your First AI Workflow

[Watch the lesson](https://youtu.be/gM4RTfQDpK4) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Pass a synthetic trigger through validate, transform, approve and record stages.

## Reference workflow

Trigger: Synthetic form submitted.

Validate fields, classify intent, draft a response, hold for approval.

Read `blueprint.json`, fill appropriately typed values in `test-data.json`, and use `prompt.txt` with `system-instructions.txt`. Produce a field-mapping table and record each test result. These are portable design files, not Make/Zapier/n8n imports.

## Local controls demonstration

```text
python track-3-automation/simulator.py
```

Expected statuses include simulated_sent, duplicate_suppressed, approval_required and needs_review. This shared simulator demonstrates controls, not a working implementation of this lesson’s provider integration. No messages, events, posts or payments are sent.

## Verify

Test valid input, missing required fields, ambiguous content, repeated events and service failure. Keep unvalidated output in review. Repeat event IDs must not duplicate an action.

## Continue

[Previous lesson](https://youtu.be/STOYql6QL2A) · [Next lesson](https://youtu.be/CAGT6GDVvaY)

If a video is not released yet, save the master Course and complete the exercise before returning.
