# Practice 28: Lead CRM Automation

**Inventory match pending.** Preserve the original uploaded video. This topic is the planning map, not a verified title.

## Do

Normalize email, search for an existing record, then update or create using an idempotency or uniqueness mechanism.

## Verify

Repeated input results in one record, including concurrent retries.

## Challenge

Preserve fields absent from the update request.

## Troubleshoot

Search then create alone is not concurrency safe. Explain the expected result and use the checks before moving on.

## Continuity

Prerequisite practice: 8. Next: Lesson 29. Use [the map](../../COURSE_MAP.md) to navigate. Public video links remain pending inventory verification.

## Reference implementation

Read blueprint.json and [the simulator guide](../README.md). The simulator demonstrates selected cross-cutting controls, not a real implementation of every integration in this track.
