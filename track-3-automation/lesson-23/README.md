# Lesson 23/41: Automating Email Responses And Follow-Ups

[Watch the lesson](https://youtu.be/gsK5gHSyuWE) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Draft an email from synthetic intake; require approval and suppress duplicate sends.

## Reference workflow

Trigger: Customer email received.

Prepare a reply with the approved template; queue a follow-up only after approval.

Read `blueprint.json`, fill appropriately typed values in `test-data.json`, and use `prompt.txt` with `system-instructions.txt`. Produce a field-mapping table and record each test result. These are portable design files, not Make/Zapier/n8n imports.

## Local controls demonstration

```text
python track-3-automation/simulator.py
```

Expected statuses include simulated_sent, duplicate_suppressed, approval_required and needs_review. This shared simulator demonstrates controls, not a working implementation of this lesson’s provider integration. No messages, events, posts or payments are sent.

## Verify

Test valid input, missing required fields, ambiguous content, repeated events and service failure. Keep unvalidated output in review. No real send without consent and owner review.

## Continue

[Previous lesson](https://youtu.be/CAGT6GDVvaY) · [Next lesson](https://youtu.be/FZa7f6789ZI)

If a video is not released yet, save the master Course and complete the exercise before returning.
