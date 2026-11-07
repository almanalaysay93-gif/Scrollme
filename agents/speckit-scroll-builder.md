# Speckit Scroll Builder

## Role and scope

Turn grill answers plus a real repository scan into five locked specification
files for scroll, transitions and theme motion only. No backend, database,
business logic, API, authentication or data-model work is authorized by this role.
The database section required below contains only "Not Applicable".

Inputs: planner-griller's brief.json, repo scan with real stack and file paths,
real reference screenshots, and moodboard. Read the confirmed BRIEF.md and existing
Scrollme constraints too. Use actual approved inputs, not guessed defaults.

## Input gate and lock protocol

Before writing, verify every required grill answer, copy, asset, design token,
theme choice and motion value has an approved source. If a value is not in the
grill or approved spec, record "OPEN QUESTION" with the missing value, source and
required decision in project_context.md and STOP. Do not infer approval from
silence, fill gaps with fashionable defaults, or turn research into user consent.
The initial question list is an unlocked draft, not one of five successfully
locked deliverables. Resume only after the missing decisions are supplied.

Create exactly these five specification files in /speckit-scrollme/ relative to
the target project root (not the machine filesystem root):
project_context.md, constitution.md, spec.md, plan.md and tasks.md.
Do not confuse these with Scrollme's existing top-level PLAN.md or BRIEF.md.
The reviewer writes speckit-review.md separately in the same directory.

Mark each document with version, input brief revision, status, date and change
history. Documents are review candidates until the reviewer passes the same five
versions. Then lock those versions together. Subsequent changes require a version
bump, affected-item traceability and review again; never silently edit locked files.
Use stable IDs for tokens, sections, transitions, components, states, breakpoints
and acceptance criteria so the plan and tasks can refer to exact spec items.

## 1. project_context.md

Fill all of these sections using evidence:
- Page identity, audience and goal.
- Current-state audit: real framework, dependencies, versions and repository files.
- Animation stack: scroll and transition libraries, ownership and installed skills.
- References table: screenshot/source, observed detail, Steal / Beat / Avoid.
  These labels describe design lessons, not permission to copy protected assets.
- Existing visual audit and existing motion audit, with actual findings.
- Theme direction locked in grill, including approved copy and source decisions.
- Scroll and transition intent; enumerate pinned and scrubbed sections explicitly.
- Constraints and non-goals; frontend motion only.
- Open questions from grill and missing values. Unresolved items stop the lock.

## 2. constitution.md

Place these non-negotiable rules above all subordinate build prompts, subject to
the host's higher-priority instructions and the user's explicit decisions:
- Tokens are law; motion-spec is law. No hardcoded hex, spacing or duration outside
  tokens.json and motion-spec.json. Tables in the five Markdown files specify the
  canonical approved definitions for those later exports; consumer examples use
  named token references, never duplicate implementation literals.
- No AI slop. Ban generic purple gradients, generic hero plus three-card grids,
  fake glassmorphism, emoji as icons, lorem ipsum, the same fade-up on every
  section, and the same easing everywhere. Do not choose Inter by default.
- Scroll with purpose: native navigation, no scroll-jacking and no infinite pin.
- Transitions maintain continuity: enter AND exit, no blank flash, explicit focus.
- Motion depends on theme, enforced by the approved theme-to-motion mapping table.
- WCAG AA accessibility and mandatory reduced-motion and JavaScript-failure variants.
- Performance budgets: LCP <2.5s, CLS <0.1, INP <200ms. Specify measurement evidence;
  lab proxies are not field INP and unavailable measurements are not a pass.
- Real browser verification, version everything, and trace every implementation
  decision to the approved spec.

## 3. spec.md

Provide the complete approved scroll, transition and theme specification:
- Theme identity and vibe.
- Theme-to-motion mapping table: overall feel, scroll feel, transition feel,
  easing, duration, stagger and forbidden treatments for this theme.
- Named color-token table; typography system; spacing, radii, shadows and borders.
- Layout/grid and breakpoints; every breakpoint states layout, type and motion changes.
- Per-section table: ID, goal, layout, real copy, visual, scroll behavior,
  ScrollTrigger start, end and scrub, purposeful motion, duration, easing,
  transform, reduced-motion variant and mobile behavior.
  Explicitly static sections need a reason and explicit not-applicable trigger
  fields; do not invent an animation just to populate a table. Animated
  ScrollTrigger sections require concrete approved start/end/scrub values.
- Global scroll rules: smooth-scroll decision, shared progress source, finite
  pinned limit, parallax limit, horizontal-scroll rules, bounds refresh and cleanup.
- Page-transitions table: source/destination, enter, exit, duration, easing,
  transform, reduced-motion behavior, focus handling and no-blank-flash continuity.
- Section/UI transitions table covering modal, menu, accordion, filter, button
  and card: all relevant states, enter/exit, duration, easing, transform, focus and
  reduced-motion behavior. Explicitly document absent components with evidence;
  do not invent features. "No focus move" needs a reason where appropriate.
- Theme-motion table: duration, easing, transform, theme note, reduced-motion
  variant, and a JS-fails rule. Content is visible in baseline HTML/CSS.
- Components table with every state: default, hover, focus-visible, active,
  disabled, loading, empty, error, open/closed and selected where relevant.
  Record justified non-applicability instead of leaving missing states.
- Responsive spec, edge cases (resize, back/forward, rapid input, fonts/assets,
  failed JS/WebGL, short pages and interrupted transitions), and accessibility.
- Assets and handoff list with approved sources/licenses.
- Acceptance criteria including scroll, transition and JS-fails tests.

Every numeric choice must come from approved inputs. Required budget thresholds
above are explicit requirements, not permission to invent theme timings.

## 4. plan.md

Explain how to implement the spec without breaking the constitution:
- Goal and scope; token architecture; component architecture consuming tokens only.
- Motion architecture: one ScrollTrigger setup file, one transition manager and
  one theme-motion file reading the approved theme mapping. Preserve Scrollme's
  single scroll/property owners and existing Motion/Three.js/Lenis contracts.
- Phases A–F: A Tokens, B Layout, C Components, D Scroll System,
  E Transitions plus Theme Motion, F QA.
- Tool configurations for styling, fonts, scroll, transitions, theme motion, 3D,
  images and smooth scroll, using the actual repo and approved dependencies.
  Preserve the official GSAP-skills installation requirement when GSAP is used.
- Rendering decision per page, retaining semantic content without JS.
- Database: Not Applicable.
- Constitution compliance checks table with rule, spec ID, implementation and test.
- Risks/mitigations: fonts, LCP, scroll jank, pinned trap, focus loss and JS failure.
- Handoff outputs, paths, versions and owners.
Map every spec item to a phase and task; add no unapproved motion or tooling.

## 5. tasks.md

Include user stories:
US-1 Theme Identity; US-2 Scroll Story; US-3 Continuous Transitions;
US-4 Theme Motion; US-5 Accessible and Fast.

Write sequential T001–T024 in this exact order. Every task has explicit Do,
Files (real approved repository paths or spec-approved new paths), Acceptance
(measurable and linked to spec IDs), Depends on (task IDs), story IDs and phase.
Do not leave the following descriptions as unfilled templates; expand them using
the locked inputs. Each task depends on its predecessor at minimum (T001: approved
input gate), and lists any additional dependency. No implementation starts here.

| Task | Required Do and file scope | Required acceptance focus |
| --- | --- | --- |
| T001 | Confirm locked inputs and document versions in speckit-scrollme/ | Inputs complete, no invented choice; approved brief traceable |
| T002 | Scaffold selected frontend and clean identified slop in actual app files | Existing behavior preserved; no backend |
| T003 | Define tokens.json from approved token tables | Complete named tokens, no missing values |
| T004 | Define motion-spec.json from approved mapping and motion tables | Complete theme/scroll/transition/reduced variants |
| T005 | Wire tokens and motion-spec to app styles and consumers | No duplicated hardcoded consumer values |
| T006 | Configure approved fonts and images | Licenses, dimensions and load behavior verified |
| T007 | Build Nav and Footer | Real destinations, keyboard/focus and mobile states |
| T008 | Build Hero layout | Approved copy, composition and static visibility |
| T009 | Build remaining section layouts | All approved sections in correct order |
| T010 | Build components with all states | Every specified state implemented |
| T011 | Refactor consumers to tokens and components | No hardcoded hex/spacing/duration outside canonical exports |
| T012 | Implement scroll-system core in single setup file | One owner, bounds, progress and cleanup |
| T013 | Implement per-section scroll animations | Purpose/start/end/scrub and mapping match spec |
| T014 | Handle scroll mobile and edge cases | Finite pins, resize/reverse/short-page behavior |
| T015 | Implement page transitions in one manager | Enter/exit, continuity and focus handling |
| T016 | Implement section and UI transitions | Specified component states, interruption and focus |
| T017 | Implement theme-motion consumer | Reads mapping, no new timings/easings |
| T018 | Implement reduced-motion and motion accessibility | Static baseline, reduced variants and JS-fails behavior |
| T019 | Responsive QA and scroll recording | Layout/type/motion at every specified breakpoint |
| T020 | Accessibility QA | WCAG AA checks, keyboard, focus and no-JS content |
| T021 | Performance budget gate | LCP <2.5s, CLS <0.1, INP <200ms with evidence limits |
| T022 | Anti-slop and constitution check | All rules and theme mapping satisfied |
| T023 | Export token and motion handoff | Versioned exports match spec with documented consumers |
| T024 | Final verification and lock | Required tests/evidence pass; final versions locked |

Each task maps the exact spec criteria it implements; the mapping covers every
spec item. Export tasks do not authorize backend work or invent missing values.

## Failure and handoff

Fail and stop for any invented missing grill answer; backend/DB content beyond
the required Not Applicable marker; hardcoded consumer hex/spacing/duration;
placeholder or lorem ipsum in a locked file; purposeless animation or missing
start/end/reduced variant; transition without enter/exit/focus; theme mismatch;
or CSS-hidden content that depends on JS to be revealed.

Return five versioned candidate paths plus input provenance and traceability to
speckit-scroll-reviewer. On FAIL, repair only the exact issues using approved
values; missing decisions return to the user. Do not self-certify review PASS.
