# Scrollme

An installable agent skill for building scroll-driven 3D parallax websites for
schools and institutions, from a confirmed brief through measured quality checks.

It coordinates Motion, Three.js, React Three Fiber/drei, GSAP and Lenis without
giving multiple libraries control of the same scroll loop. Optional motion-web
use is gated by its separate non-commercial terms.

## Install

Requires Git and a coding agent that supports `SKILL.md`. Python 3.10+ is needed
only for the bundled document initializer and validation tools. Website builds
need the runtime supported by the selected framework, normally Node.js LTS.

For Codex and agents using `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/almanalaysay93-gif/Scrollme.git ~/.agents/skills/scrollme
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/almanalaysay93-gif/Scrollme.git ~/.claude/skills/scrollme
```

Restart or refresh your agent's skill discovery if required. Invoke `/scrollme`
where supported, or ask: “Use the scrollme skill to build our school's website.”
Slash-command and automatic discovery support depend on the host.

## What happens

1. The agent asks about the school, story, audience, assets, stack and constraints.
2. You review and confirm `BRIEF.md`.
3. It creates `PLAN.md`, researches sources and records asset licenses.
4. Specialists build the selected stack, with a sequential fallback on single-agent hosts.
5. It tests the result, repairs failures and writes `QC_REPORT.md`.
6. It launches a local preview and reports the actual verification status.

No website is bundled or deployed by installing this repository. The skill does
not ship upstream libraries, third-party assets, paid examples, or motion-web content.
The MIT license covers this repository; generated projects retain their dependencies'
and assets' separate terms. See [sources and licenses](references/sources-and-licenses.md).

## Optional planning helper

```bash
python3 ~/.agents/skills/scrollme/scripts/init_project.py ./school-site
```

Creates `BRIEF.md`, `PLAN.md`, `references/CONTEXT.md`, `references/images/`, and
`QC_REPORT.md`. Existing destination documents are never overwritten. This is a
planning helper, not a Vite/Next.js scaffolder. Install and initialize the actual
framework after the brief is approved.

## Validate this skill

From the repository root, with no third-party Python packages:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

Validation checks package structure, metadata, local Markdown links and Python
syntax. These checks validate the skill package, not a generated website's quality.
GitHub Actions runs the same checks on pushes and pull requests.

The workflow is implemented in [SKILL.md](SKILL.md). Start there to customize it;
the `references/` files contain integration and QC details, and `templates/`
contains the output documents.
