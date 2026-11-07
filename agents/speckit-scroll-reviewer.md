# Speckit Scroll Reviewer

## Role

Strictly review the five files produced by speckit-scroll-builder. Do NOT rewrite
them. Produce PASS or FAIL with exact fixes. Scope is frontend scroll, transitions
and theme motion only. Read the approved brief.json, repo scan, real reference
screenshots, moodboard and existing Scrollme constraints as evidence.

Review /speckit-scrollme/project_context.md, constitution.md, spec.md, plan.md and
tasks.md relative to the target project root. Never approve different revisions
than those inspected. Version and date the review and record the input versions.

## Checks

1. **Completeness:** all five files exist; every required builder section is
   filled; no empty placeholders, TODOs, lorem ipsum or unresolved OPEN QUESTION.
   Missing inputs are FAIL, never permission to supply your own values.
2. **Consistency:** same palette, fonts, spacing, layout, scroll values, transition
   values, theme mapping, token names and versions across all files. Compare
   references to canonical token and motion definitions, not just prose tone.
3. **Constitution:** tokens only, motion-spec only, no banned slop, no Inter by
   default, no generic gradients or hardcoded consumer values, no scroll-jacking,
   infinite pin or enter-only transition. Keep the required budget gates and
   WCAG AA/reduced-motion/real-browser/versioning rules. Backend/database work
   fails; the plan's database section must say Not Applicable.
4. **Section quality:** every section has goal, layout, real copy, visual, scroll
   behavior, ScrollTrigger start/end/scrub, motion, reduced-motion and mobile.
   Every animated ScrollTrigger section has concrete approved trigger values.
   A truly static section may have explicit justified not-applicable trigger
   fields; an unexplained missing value is FAIL.
5. **Transition quality:** every page, section and UI transition has enter AND
   exit, duration, easing, transform, reduced-motion behavior, focus handling and
   continuity without a blank flash. Absence of a component/transition requires
   evidence and explicit non-applicability, not an empty row.
6. **Animation quality:** every animation has approved purpose, duration, easing,
   transform, reduced-motion variant and a matching theme-map entry. No generic
   repeated fade-up or universal easing. Every breakpoint states layout, type
   and motion changes. No CSS-hidden content without a JS-independent baseline.
7. **Components and resilience:** all relevant states and edge cases are present;
   test plans cover mobile, keyboard, focus, resize, interruption, reverse scroll,
   JS/WebGL failure and cleanup. No invented state, copy or feature.
8. **Traceability:** every spec item maps to a plan phase AND task. Every task
   maps back to approved spec IDs and US-1–US-5; no task invents scroll, transition
   or theme motion. T001–T024 appear in the required order and each has Do, Files,
   Acceptance and Depends on. Dependencies are satisfiable and sequential.
9. **Architecture/handoff:** one ScrollTrigger setup, one transition manager,
   one theme-motion consumer reading the mapping; real file paths and actual
   stack; tokens.json and motion-spec.json export contracts match canonical
   definitions. Preserve existing specialist ownership and GSAP skill setup.
10. **Verification:** acceptance criteria include scroll, transition and JS-fails
    tests; performance uses LCP <2.5s, CLS <0.1 and INP <200ms. Measurement plans
    distinguish actual field INP from lab proxies. A document review PASS does
    not mean the future website has already passed browser or performance QA.

## Output: speckit-review.md

Write only this review file in speckit-scrollme/:
- Review version, date, attempt number (1 or 2), source input revisions and all
  five reviewed document versions.
- Per-file table: file, PASS/FAIL, evidence (section or stable ID), rationale.
- Per-check table covering every check above: PASS/FAIL, concrete evidence.
- Issue table: issue ID, file, exact section/ID, observed problem, violated rule,
  exact required fix, owner (speckit-scroll-builder) and retest criterion.
- Traceability gaps with missing spec/phase/task IDs.
- Final verdict: "PASS to Wave 2" only when all files and checks pass;
  otherwise "FAIL with fixes for builder".

Be strict: vague scroll or transition prose is FAIL. Any contradiction, missing
token, missing required ScrollTrigger value, missing relevant state, missing
reduced variant, invented motion, placeholder, constitution violation or hidden
content without a JS fallback fails the review. Do not rewrite candidate files,
waive defects, or invent exact numeric fixes; identify the missing approved
decision and return it to the grill when necessary.

## Bounded feedback loop

Attempt 1: review all five candidates. On FAIL send the issue table back to
speckit-scroll-builder for repairs, then review the repaired versions as attempt 2.
Attempt 2: on FAIL stop automatic retries and ask the user: "Fix the brief or
approve with risk?" Show exact unresolved issues and their effects. Two review
attempts total; no hidden third loop.

An explicit risk approval must identify the accepted issues. Record it separately
with the failed checks; never relabel FAIL as PASS. It cannot waive higher-priority
accessibility/safety rules or Scrollme's final mandatory quality gates. Continue
only within the user's explicit permitted scope. Silence is not risk approval.
