# Practice 37: Secrets Privacy and Security

**Inventory match pending.** Preserve the original uploaded video. This topic is the planning map, not a verified title.

## Do

Read an environment variable using os.getenv and stop if absent. Keep .env ignored; use an explicit loader only if chosen.

## Verify

Missing secret stops safely; logs and staged diff contain no secret.

## Challenge

Explain provider rotation after exposure.

## Troubleshoot

os.getenv does not automatically load .env. Explain the expected result and use the checks before moving on.

## Continuity

Prerequisite practice: 13. Next: Lesson 38. Use [the map](../../COURSE_MAP.md) to navigate. Public video links remain pending inventory verification.

## Reference implementation

Read blueprint.json and [the simulator guide](../README.md). The simulator demonstrates selected cross-cutting controls, not a real implementation of every integration in this track.
