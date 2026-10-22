# Official sources and license boundaries

This package contains original workflow instructions and templates under MIT.
It links to upstream projects rather than vendoring their code or instructions.
Check the actual version's license before copying, installing, or shipping it.

| Project | Official starting point | License guidance |
| --- | --- | --- |
| Motion | https://github.com/motiondivision/motion and https://motion.dev/docs | Core library MIT; Motion+ examples/features have separate paid terms. |
| Motion AI kit | https://github.com/motiondivision/ai-kit | Read current installer docs; the free skill does not grant access to paid content. |
| Three.js | https://github.com/mrdoob/three.js and https://threejs.org/docs/ | MIT; example models/textures can have separate licenses. |
| React Three Fiber | https://github.com/pmndrs/react-three-fiber and https://r3f.docs.pmnd.rs/ | MIT; check dependency versions and peers. |
| drei | https://github.com/pmndrs/drei and https://drei.docs.pmnd.rs/ | MIT; downloaded HDRIs/models remain separately licensed. |
| GSAP | https://github.com/greensock/GSAP and https://gsap.com/community/standard-license/ | Custom Standard License, not MIT. Free use includes commercial work subject to its terms; do not equate no charge with unrestricted redistribution. |
| GSAP skills | https://github.com/greensock/gsap-skills | Official instructions; inspect current license before redistribution. |
| Lenis | https://github.com/darkroomengineering/lenis | MIT; use current README integration guidance. |
| motion-web | https://github.com/feitangyuan/motion-web/blob/main/LICENSE | CC BY-NC 4.0 with stated commercial licensing requirements. Excluded by default. |

Upstream Motion README, official gsap-skills repository metadata and motion-web
LICENSE were checked on 2026-10-22 while packaging this skill. This is not a
perpetual license audit of every upstream version. Recheck sources during builds.

## motion-web gate

Do not copy or bundle its SKILL.md, prompts, scripts, examples or derivative
workflows into the MIT package. Simply building a school site does not establish
non-commercial use: a paid agency delivery can still be commercial. Use the
independent Motion/Three.js/GSAP/Lenis path unless the user explicitly selects
motion-web and confirms compatible use or supplies appropriate permission.
Keep attribution, license link and modification notices if material is reused.

## Asset policy

Prefer user-owned models, original procedural geometry and CC0 assets. MIT assets
need their copyright and license notices. For each actual downloaded file, verify
the asset-specific page and record author, source, license, local destination,
modifications and required credit in references/CONTEXT.md. Search-result snippets,
“free” labels and GitHub's NOASSERTION metadata are not license grants.

Potential sources include https://polyhaven.com/ and
https://ambientcg.com/ (verify each asset's terms). Unsplash uses its own license,
https://unsplash.com/license; it is not CC0. Use it only as an approved exception,
with the relevant terms recorded. Do not copy visual references as production
assets without permission. If access is unavailable, record the research blocker
and use approved procedural assets rather than inventing credits.
