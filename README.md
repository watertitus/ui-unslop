# UI Unslop

**A reusable AI agent skill that turns cluttered, generic interfaces into cleaner, more intentional product UI.** Built from the 20-item checklist shown in the supplied “20 Ways to Unslop AI Designs” video, with implementation guidance and accessibility safeguards for real codebases.

Works with **OpenAI Codex** and **Claude Code** using the open `SKILL.md` convention. It is an instruction-based skill, not a hosted service or automatic visual-testing engine.

## What it does

- Audits actual frontend files and available screenshots against 20 concrete design principles.
- Plans and implements focused UI changes that fit your existing framework and brand.
- Checks typography, content, spacing, contrast, states, CTA hierarchy and responsive behavior.
- Avoids changing business logic, inventing product claims, or removing accessibility affordances for aesthetics.
- Reports what changed, what was tested and what could not be verified.

## Get started

### Option A: Clone and install (recommended)

```bash
git clone https://github.com/watertitus/ui-unslop.git
cd ui-unslop
python3 scripts/install.py --agent both --scope user
```

The URL above becomes valid **only after this repository is created and published on GitHub**. Until then, use the downloaded ZIP as the source folder and run the same installer from it.

The installer supports `--agent codex`, `--agent claude`, or `--agent both`, and `--scope user` (all projects) or `--scope project --project /path/to/project` (one project). Use `--force` only when you intend to replace an earlier installation of this skill; it does not overwrite unrelated skills.

### Option B: Manual installation

Copy the **whole** `skills/ui-unslop/` directory, including `references/`, into either or both of these locations:

| Agent | Global (user) | Project |
|---|---|---|
| Codex | `~/.agents/skills/ui-unslop/` | `<project>/.agents/skills/ui-unslop/` |
| Claude Code | `~/.claude/skills/ui-unslop/` | `<project>/.claude/skills/ui-unslop/` |

Restart the agent session or refresh skills if not detected.

### Option C: Agent Skills installer

After the GitHub repository is public, skill installers that support repository-based `SKILL.md` packages can install `skills/ui-unslop` from the repo. For example, in Codex ask its skill installer to install the skill from `https://github.com/watertitus/ui-unslop/tree/main/skills/ui-unslop`. Review third-party skills before installing them.

## Use it

In **Codex**:

```text
$ui-unslop Audit the pricing page and fix the three highest-impact problems. Preserve our brand colours, API calls, and payment flow. Run available checks.
```

In **Claude Code**:

```text
/ui-unslop Audit and refine the dashboard UI. Maintain existing components and accessibility, and explain each change.
```

You can also ask the agent naturally to polish a screen, reduce visual clutter or improve the UI. Implicit activation depends on the agent's skills configuration.

## The original 20 principles

1. Delete filler badges
2. Drop redundant labels
3. Unitalicize random words
4. Mono only where needed
5. Use a design system
6. Show the actual product
7. Enlarge the main feature
8. Group with spacing
9. Make headlines specific
10. Emphasize the CTA
11. Add an accent colour
12. Keep icons consistent
13. Remove embellishments
14. Inner radius = outer radius − padding
15. Improve text contrast
16. Wrap headlines properly
17. Align by eye, not pixels
18. Use tabular numbers
19. Add loading states
20. Animate useful feedback

Implementation notes and exceptions are in [`references/20-principles.md`](skills/ui-unslop/references/20-principles.md). The corner-radius equation is a visual heuristic, not a universal CSS rule.

## Project layout

```text
ui-unslop/
├── skills/ui-unslop/
│   ├── SKILL.md                 # shared skill entrypoint
│   └── references/
│       ├── 20-principles.md     # detailed checklist
│       ├── audit-rubric.md      # prioritization and guardrails
│       └── report-template.md   # audit/report format
├── scripts/install.py          # cross-platform installer
├── tests/test_install.py       # no-dependency installer tests
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── README.md
```

## How to contribute

Issues and pull requests are welcome once the GitHub repository is published. Read [CONTRIBUTING.md](CONTRIBUTING.md). Never submit secrets, proprietary project screenshots, or copyrighted video/audio material.

## Attribution and scope

The 20 headings and inspiration are based on a short user-supplied video titled **“20 Ways to Unslop AI Designs”**, visibly credited to **@charles.unemployed** on TikTok. This repository does **not** bundle or claim ownership of that video. The workflow, implementation guidance, installer and examples are original derivative commentary and software instructions. No endorsement by the creator, OpenAI, or Anthropic is implied.

## License

MIT License for this repository's original skill instructions, scripts and documentation. See [LICENSE](LICENSE). This license does not cover third-party video content or trademarks.
