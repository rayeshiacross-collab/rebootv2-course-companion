# Lesson 28/41: Social Media Content At Scale

[Watch the lesson](https://youtu.be/Imbo1i2HQ5A) · [Master Course](https://www.youtube.com/playlist?list=PLLJzVRttUfqU)

Matched to the verified uploaded title and course position. This is a newly authored companion, not a transcript or a claim to reproduce unseen footage. Availability follows the YouTube release schedule.

## Hands-on task

Adapt one approved message to three platforms; check length and approval state.

## Reference workflow

Trigger: Approved master message.

Adapt wording for each supplied platform limit and queue review.

Read `blueprint.json`, fill appropriately typed values in `test-data.json`, and use `prompt.txt` with `system-instructions.txt`. Produce a field-mapping table and record each test result. These are portable design files, not Make/Zapier/n8n imports.

## Local controls demonstration

```text
python track-3-automation/simulator.py
```

Expected statuses include simulated_sent, duplicate_suppressed, approval_required and needs_review. This shared simulator demonstrates controls, not a working implementation of this lesson’s provider integration. No messages, events, posts or payments are sent.

## Verify

Test valid input, missing required fields, ambiguous content, repeated events and service failure. Keep unvalidated output in review. Do not silently post or create unsupported promises.

## Continue

[Previous lesson](https://youtu.be/mK9mZJQFnqs) · [Next lesson](https://youtu.be/a2DIyRyergo)

If a video is not released yet, save the master Course and complete the exercise before returning.
