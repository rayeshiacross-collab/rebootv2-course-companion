# Lesson 35/41: Building Multi-Step Automations With Make

[Watch the lesson](https://youtu.be/Ci02vAe0icM) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Design a Make router with success and error paths; reference JSON is not an import.

## Reference workflow

Trigger: Make scenario prototype.

Design webhook, validation, router and logging stages; document field mappings.

Read `blueprint.json`, fill appropriately typed values in `test-data.json`, and use `prompt.txt` with `system-instructions.txt`. Produce a field-mapping table and record each test result. These are portable design files, not Make/Zapier/n8n imports.

## Local controls demonstration

```text
python track-3-automation/simulator.py
```

Expected statuses include simulated_sent, duplicate_suppressed, approval_required and needs_review. This shared simulator demonstrates controls, not a working implementation of this lesson’s provider integration. No messages, events, posts or payments are sent.

## Verify

Test valid input, missing required fields, ambiguous content, repeated events and service failure. Keep unvalidated output in review. Reference JSON is not a verified Make import.

## Continue

[Previous lesson](https://youtu.be/3YOdasi1uWE) · [Next lesson](https://youtu.be/hAGAU-mXb8U)

If a video is not released yet, save the master Course and complete the exercise before returning.
