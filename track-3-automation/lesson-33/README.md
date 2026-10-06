# Practice 33: Database Workspace Automation

**Inventory match pending.** Preserve the original uploaded video. This topic is the planning map, not a verified title.

## Do

Find by stable ID; update only intended fields; create only on an explicit missing-record rule.

## Verify

Same name with different IDs remains separate; repeated update is safe.

## Challenge

Reject an update without a stable ID.

## Troubleshoot

Display name used as unique key. Explain the expected result and use the checks before moving on.

## Continuity

Prerequisite practice: 28. Next: Lesson 34. Use [the map](../../COURSE_MAP.md) to navigate. Public video links remain pending inventory verification.

## Reference implementation

Read blueprint.json and [the simulator guide](../README.md). The simulator demonstrates selected cross-cutting controls, not a real implementation of every integration in this track.
