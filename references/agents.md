# Specialist roster

The coordinator researches official instructions before assigning each active
role. If no official skill exists, use the official API documentation and state
that choice. Never invent an upstream SKILL.md or silently execute remote scripts.

| Role | Sources | Owned work | Required handoff |
| --- | --- | --- | --- |
| Interview | Approved user answers | BRIEF.md | Confirmed brief and unresolved choices |
| Planner | Brief and architecture reference | PLAN.md, integration contracts | Scene map, versions, file boundaries, scroll owner |
| Research | Official docs and asset license pages | references/CONTEXT.md and images | Moodboard, tokens, credits and paths |
| Motion | motiondivision/motion; motiondivision/ai-kit | src/agents/motion/ | Progress adapter, secondary springs, reveal teardown |
| Three.js | mrdoob/three.js | src/agents/three/ | Recognizable architecture, lighting, camera keyframes, disposal |
| R3F/drei | pmndrs/react-three-fiber; pmndrs/drei | src/agents/r3f/ | Canvas integration, loaders, WebGL fallback; merges into Three.js for vanilla |
| GSAP | greensock/gsap-skills; official ScrollTrigger docs | src/agents/gsap/ | Scoped timelines, optional pinning and SplitText, cleanup |
| Lenis | darkroomengineering/lenis | src/agents/lenis/ | One scroll instance, ticker sync, native input, destroy |
| motion-web | feitangyuan/motion-web, only after license gate | src/agents/motion-web/ if selected | Separate attribution and compatible usage; otherwise explicitly skipped |
| QC | Verification protocol and approved criteria | QC_REPORT.md | Evidence, status, repair tickets, retest |

For shared workspaces, specialists edit disjoint files and return changes to the
coordinator. Only the coordinator updates package manifests, lockfiles, shared
styles, entry points and commits unless ownership is explicitly reassigned. For
isolated checkouts, review each patch before integration. No specialist pushes
independently merely because the skill was invoked.

Every delegation includes:

```text
Role and official sources read:
Approved brief and plan sections:
Allowed files:
Inputs and output interface:
Scroll/render/property ownership:
Acceptance checks and artifact paths:
License constraints:
Return changed files, validation results, blockers and cleanup instructions.
```

Respect the host's agent limit. Schedule roles in waves if needed. If tools do not
support subagents, keep the same responsibilities and handoff checklist in one
agent; do not fabricate parallel execution.
