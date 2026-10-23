# Website verification protocol

This is a protocol for the website built by the skill. Package validation is a
separate check. Use Playwright or the host's browser automation; do not claim a
browser check ran when only source inspection was available.

## Instrument the real behavior

For development/test builds only, expose a read-only snapshot such as
`window.__SCROLLME_DEBUG__ = () => ({ progress, camera: [x,y,z], target: [x,y,z], reducedMotion })`.
Populate it from the real scene state, not a test-only duplicate. Remove it or
gate it out of production. Evidence must connect native scroll to actual camera
values and visible frames; a changing progress bar alone does not prove 3D motion.

## Required checks

| Check | Procedure and evidence |
| --- | --- |
| Build | Run project's production build and configured type/lint checks; record commands and exit codes. |
| Scroll mapping | At 0, 25, 50, 75 and 100% of the story, scroll the real container, wait for documented spring settling, capture actual camera/target and screenshot. Compare against PLAN keyframes with a stated tolerance. Repeat backward. |
| Real visuals | Review screenshots at desktop (e.g. 1440×900) and mobile (e.g. 390×844). Campus reads as architecture, text remains readable, no blank canvas, overlap, clipping or generic stand-ins. |
| Interactions | Click every primary nav and CTA; verify correct destinations or implemented actions, not merely clickability. Verify anchors land without hidden headings. |
| Keyboard | Traverse controls with Tab/Shift+Tab; use Enter, Space, PageDown, Home and End. No traps; visible focus; all narrative sections reachable. |
| Reduced motion | Emulate prefers-reduced-motion before navigation. Assert smoothing, camera traversal and pinning are off; all sections and CTA visible. Test changing the preference at runtime when supported. |
| WebGL failure | Inject context-creation failure before startup and test context loss after startup. Static replacement and semantic story remain usable; no unhandled crash. |
| Layout stability | Observe layout shifts after initial load and during scrolling. Target CLS ≤0.1; reserve dimensions for imagery/canvas. Record trace or observer output. |
| Runtime health | Capture page errors, console errors and failed asset requests during the full traversal. No unexplained failures. |
| Asset/code review | Verify asset ledger against local files, license gates, resource cleanup and no unresolved scaffolding markers or exposed credentials. Do not print secret values in reports. |

## Performance targets and limits

Agree target hardware/browser in BRIEF.md. Aim for a 16.7 ms frame budget at 60 Hz
and interaction latency below 200 ms. Record a repeatable timed traversal, warm/cold
conditions, throttling, viewport, browser and device. Use performance traces for
long tasks and dropped frames. A requestAnimationFrame counter in headless CI is
only a diagnostic, not proof of a smooth 60 fps experience on a phone. Lab click
timings are not field INP. Label metric definitions explicitly.

If hardware or tooling is unavailable, mark performance BLOCKED and retain trace
instructions for a human review. Do not silently lower the target to get PASS.

## Repair loop and reporting

Write a ticket with owner, reproduction steps, expected/observed values, artifact
paths and severity. Fix implementation failures and rerun affected checks. A new
camera/scroll integration change requires rerunning scroll, keyboard and reduced
motion checks. Overall status is FAIL if any required check fails, otherwise
BLOCKED if any required check lacks evidence, otherwise PASS. Link screenshots
and logs in QC_REPORT.md; distinguish observations from manual review still needed.

## Required UX laws gate

Follow [the mandatory UX workflow](ux-laws-workflow.md) independently of optional
UX tools. QC owns `UX_LAWS_AUDIT.md`: cover all 14 laws using the source template,
attach browser/screenshots/code/measurement evidence, assign fixes and re-audit.
Any Violated finding makes overall QC FAIL. Missing evidence makes QC BLOCKED.
Link justified Partial results and their scope reasons from `QC_REPORT.md`.
