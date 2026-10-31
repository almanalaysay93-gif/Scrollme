# Unslop design-polish adapter

Adapted from [Unslop by Damir Sokolovsky (@heydamir)](https://github.com/heydamir/unslop)
at [`4652254daff5`](https://github.com/heydamir/unslop/tree/4652254daff586ff4739849395a127b56f7f8cc7),
inspected on 2026-10-31. This adapted reference is licensed under
[CC BY 4.0](../third-party/unslop/LICENSE), not Scrollme's MIT license.
Changes: selected compatible visual-design guidance, limited file ownership,
protected Scrollme's motion and brand contracts, excluded generation/video
workflows, and integrated the existing brief, UX audit and QC gates.
See [third-party notices](../THIRD_PARTY_NOTICES.md).

## Role and timing

Scrollme remains the sole coordinator. Assign this adapter to a design-polish
specialist after initial integration and before final QC, or perform the same
pass sequentially if delegation is unavailable. Read the approved BRIEF.md,
PLAN.md, design tokens, UX-law mapping and actual rendered page first.

Audit the desktop and mobile interface. Record concrete findings by component,
selector or file in the existing QC_REPORT.md. For a good interface, report that
no changes are needed. For small issues, fix only the identified issues. For a
rough interface, derive a short direction from the approved institution and
audience: purpose, character, visual world, one or two focal moments and one
distinctive detail. Reuse the approved brief and existing brand rather than
starting a second interview. A material change to the approved direction goes
through Scrollme's existing brief-change process.

## Included passes, in order

1. **Spacing:** establish a consistent scale, normally 4px with small optical
   adjustments. Align repeated labels, icons and figures. Keep spacing within a
   group smaller than between groups. Preserve the UX reference's 44×44 CSS-pixel
   touch targets even if compact icon artwork is smaller.
2. **Color:** consolidate redundant surface and text colors into coherent roles.
   Use the approved brand accent deliberately and keep decoration from competing
   with the campus scene. Check text contrast, including text on buttons. Remove
   only unapproved decorative glows or gradients; preserve approved brand colors,
   scene lighting, materials, and intentional visual treatments.
3. **Icons:** use the existing icon family consistently; remove redundant
   decorative icons, align boxes and label gaps, and keep accessible names.
   Replace decorative emoji only when appropriate to the approved identity.
   Use an already installed set or inline SVG; no paid icon pack is required.
4. **Copy:** make headings and actions specific to the school and task. Reduce
   repetitive hype. Keep approved facts, claims, proper names and section order.
   Flag unsupported claims for verification; never substitute fabricated school
   statistics, testimonials or sample data that could be mistaken for facts.
5. **Typography:** use the approved fonts, a readable size hierarchy and consistent
   weights. Keep small text legible and use tabular figures where useful. Avoid
   unnecessary font downloads; use system or already licensed project fonts.
   Do not impose Unslop's blanket weight, capitalization or italic restrictions
   on an established school brand.
6. **Local composition:** improve text measure, alignment and responsive wrapping
   inside existing UI components. Preserve semantic order and the approved scene
   composition. Document scroll geometry changes for the coordinator.
7. **Details:** make border, radius, focus, hover and selected states consistent.
   Give interactive controls visible feedback and focus without adding effects
   that compete with the narrative. Improve the school-specific character using
   approved assets and purposeful details already present in the project.

## Protected behavior and ownership

This role owns only coordinator-assigned UI files and tokens. It must not edit
camera code, scroll adapters, GSAP timelines, Lenis configuration, render loops,
spring parameters, pinning, model geometry, scene lighting or material code.
It must not remove or flatten approved parallax, springs, reveals or 3D camera
travel. Preserve existing reduced-motion and WebGL fallbacks. Flag questionable
motion for the owning specialist rather than rewriting it.

Do not import Unslop's motion-removal pass, generated scene/image preference,
placeholder slots, screenshot/live-site reconstruction, story-video workflow,
or three-render review cap. Work on the real project; screenshots are evidence,
not a replacement for the live 3D scene. Scrollme's required test coverage takes
priority over any upstream render limit.

Changing UI sizes or fonts can move scroll boundaries even without touching
animation code. The coordinator reviews those changes, refreshes measurements
through the existing scroll owner, and reruns forward/reverse camera mapping,
keyboard navigation, reduced motion, mobile layout and performance checks.
Any required failed check remains FAIL; missing evidence remains BLOCKED.

## No additional paid dependencies

This bundled adapter requires no separate plugin, API key, subscription, model
purchase, paid font, paid asset, image generator or rendering service. Do not
install the full upstream skill or invoke paid generation as part of this pass.
Use the existing agent, project code, local browser tools and approved assets.
There is no image generation or story video in this integration.

CC BY 4.0 allows commercial use with its attribution and other conditions.
The adapter adds no service fees, but it does not make the user's existing
coding-agent provider, hosting or unrelated dependencies free.

## Handoff and completion

In QC_REPORT.md record the source/ref, scope and reviewer, findings, file changes,
before/after evidence, protected motion checks and remaining limitations.
Apply the existing UX-laws audit and repair process; do not add a competing audit
or waive a violation for aesthetics. The design pass itself cannot grant overall
QC PASS. If no visual tool is available, label conclusions code-only and retain
BLOCKED for the required visual checks.

Keep this attribution, the license notice, disclaimer and modification history
when sharing or adapting this reference. Preserve approved brand choices even
when they differ from the upstream design preferences.
