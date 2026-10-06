# Practice 23: Webhooks

**Inventory match pending.** Preserve the original uploaded video. This topic is the planning map, not a verified title.

## Do

Receive a mock lead.created event, verify provider authentication where supported, validate fields and deduplicate event IDs.

## Verify

Valid event is processed once; missing email is rejected; replay causes no duplicate.

## Challenge

Test two deliveries of the same event.

## Troubleshoot

Unauthenticated intake and repeated deliveries. Explain the expected result and use the checks before moving on.

## Continuity

Prerequisite practice: 22. Next: Lesson 24. Use [the map](../../COURSE_MAP.md) to navigate. Public video links remain pending inventory verification.

## Reference implementation

Read blueprint.json and [the simulator guide](../README.md). The simulator demonstrates selected cross-cutting controls, not a real implementation of every integration in this track.
