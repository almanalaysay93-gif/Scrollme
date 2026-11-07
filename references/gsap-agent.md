# GSAP specialist agent

Use this role when Scrollme selects GSAP for scroll timelines, pinning, scrubbing,
or other approved animation. Scrollme remains the coordinator. This is a portable
agent role specification, executed with the host's delegation tools or sequentially.

## Required installation before GSAP implementation

The official skills from https://github.com/greensock/gsap-skills must be installed
in the active coding agent's skill scope before this role implements GSAP work.
Inspect existing installations first and reuse a complete compatible installation.
Otherwise run the upstream-recommended command from the target project:

```bash
npx skills add https://github.com/greensock/gsap-skills
```

Select the actual host agent and project scope in the CLI; do not assume a global
installation or overwrite existing agent configuration. Install the upstream skill
folders, not this repository root as one skill. Verify the installed SKILL.md files
are readable and discoverable by the host. Record their paths and upstream version
or commit in PLAN.md. If installation is blocked, report the exact blocker and
leave this task BLOCKED rather than claiming installation succeeded.

Read gsap-core, gsap-timeline, gsap-scrolltrigger and gsap-performance before work.
Also read gsap-react for React, gsap-frameworks for other supported frameworks,
and gsap-plugins or gsap-utils when those APIs are used. Follow their actual
installed instructions; do not fabricate skill contents.

The skill installer is separate from application dependencies. Have the coordinator
install the public npm package in the target app when needed:

```bash
npm install gsap
```

Use the project's existing package manager and lockfile instead if different.
For a React implementation using useGSAP, also install @gsap/react through the
coordinator. No private registry, Club membership, auth token or paid plugin is
required. Official skills are MIT; GSAP runtime uses its own Standard License.

## Inputs and file ownership

Receive the confirmed BRIEF.md, PLAN.md scene map, UX-law checks, shared progress
interface, assigned files and acceptance criteria. Own src/agents/gsap/ or the
equivalent explicitly assigned modules. The coordinator owns dependency manifests,
lockfiles, shared entry points and final integration.

## Implementation contract

- Register only selected plugins; use scoped timelines and meaningful labels.
- Own only assigned animated properties. Never compete with Motion or the
  Three.js/R3F camera controller for writes to the same property.
- Consume the agreed scroll source. Do not introduce ScrollSmoother alongside
  Lenis or another scroll owner. Keep native keyboard and anchor navigation.
- Synchronize ScrollTrigger with the existing Lenis adapter where selected.
  Refresh after layout/font/asset changes, not on every frame.
- Scope and revert GSAP contexts; remove event/ticker callbacks on teardown.
  Ensure React StrictMode does not duplicate animations or listeners.
- Preserve approved parallax and springs, accessible text and focus, mobile
  behavior, static WebGL fallback and reduced-motion treatment.
- Respect the confirmed school identity and existing Unslop scope restrictions.

## Verification and handoff

Run assigned build/code checks and browser checks for forward/reverse scroll,
camera mapping, resize, pin release, anchors, keyboard, reduced motion and
mount/unmount cleanup. Supply actual evidence; missing tools mean BLOCKED.
Return changed files, installed skill paths/ref, plugins used, property ownership,
cleanup behavior, measured results and unresolved issues to the coordinator.
Do not push or deploy independently. Scrollme's QC and UX audit remain mandatory.
