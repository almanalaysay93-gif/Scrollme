# Architecture and integration contracts

## Select one stack

| Stack | Dependencies | Notes |
| --- | --- | --- |
| React / Vite | motion, three, @react-three/fiber, @react-three/drei; gsap and lenis when needed | Align React, R3F and drei peer versions. |
| Next.js | Same selected React dependencies | Keep WebGL/browser APIs behind client boundaries; preserve server-rendered story text. |
| Vanilla / Vite | three; motion, gsap and lenis when needed | No React hooks or R3F. Motion's JavaScript APIs replace useScroll. |

Do not install all libraries merely to satisfy the roster. Read current docs and
record versions in PLAN.md. Avoid adding a second framework to an existing app.

## One scroll owner

Default to the document as the scroll container. Normalize progress as
`clamp(scrollTop / max(1, scrollHeight - clientHeight), 0, 1)` for the chosen story
container, with measured offsets if the story covers part of a page. Recompute
bounds after asset loads and resize. Specify camera keyframes at 0, .25, .5, .75,
and 1 with both position and look target; interpolate without abrupt direction changes.

Choose either document-driven scrolling or drei ScrollControls. ScrollControls
creates its own scroll container: do not add a second Lenis/document scroller on
top. If using it, drive the story from its offset and verify keyboard/focus and
semantic overlay behavior explicitly. OrbitControls is a debug or user-controlled
mode; disable its camera writes while the scroll camera is active.

Motion's React `useScroll` exposes `scrollX`, `scrollY`, `scrollXProgress`, and
`scrollYProgress`. Subscribe once and keep the shared progress in a ref/store;
Three/R3F samples that same value in its frame callback. Secondary DOM layers can
use `useTransform` and `useSpring`; declare stiffness, damping and mass.

If GSAP owns a scrubbed camera timeline, Motion must not also write the camera.
SplitText is optional: preserve a readable accessible heading, wait for fonts,
and revert splits on teardown. Scope GSAP with contexts and clean them up.

## Lenis and GSAP

If both are selected, use one Lenis instance with its automatic RAF disabled when
driven by a shared ticker. Bridge Lenis scroll events to `ScrollTrigger.update`.
GSAP ticker time is in seconds; Lenis `raf` expects milliseconds. Retain the same
callback reference for removal. Call `ScrollTrigger.refresh` after layout changes,
not every frame. Do not combine autoRaf and a manual Lenis tick. Avoid changing
global ticker settings without documenting why and how they affect other features.

R3F manages its own canvas rendering: one render loop per canvas is sufficient.
It can sample the shared scroll state without calling renderer.render externally.

## Performance and resilience

- Start with low geometry/material counts, instancing repeated windows/trees,
  compressed textures, and a bounded device pixel ratio (usually 1–1.5 on mobile).
- Give media explicit dimensions; reserve canvas space; avoid layout animation
  during scrolling. Use transforms and opacity for DOM layers.
- Lazy-load heavy 3D assets without delaying headings, navigation or the CTA.
- Provide loading, error and WebGL context-loss treatments with a static scene.
- Adapt shadows, resolution and model detail to the agreed target devices.
- Avoid scrolljacking: links, anchors, PageDown, Home/End and touch still work.
- React StrictMode must not leave duplicate listeners, tickers or canvases.
- Reduced motion disables Lenis smoothing, camera traversal, pinning and spring
  displacement. Unhide all content and preserve section order and focus behavior.
