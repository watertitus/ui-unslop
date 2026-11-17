# UI audit rubric

Rate each applicable issue on three axes (0–3): **impact** (readability/task completion), **frequency** (how many users or screens affected), and **confidence** (evidence from source/screenshot). Use the combined total to prioritize, not to create an arbitrary universal score. Mark principles **N/A** when the screen does not have the relevant feature.

## Inspect

- Product message: Can a first-time visitor explain what this screen does and the next action?
- Information hierarchy: Is important product evidence prominent? Does the headline say something specific?
- Copy: Remove marketing filler, but retain accuracy, context, a11y and essential labels.
- Visual design: Typography, colour, radii, shadows, icon language, spacing and shared component consistency.
- Interactions: CTA hierarchy, focus/hover, disabled, loading, error, success and empty states.
- Responsiveness: Small phone, tablet and desktop widths; overflow and long-content behavior.
- Accessibility: Semantics, keyboard order, focus visibility, contrast, meaningful alternate text, motion preferences.
- Realism: Genuine screenshots/content; no fabricated metrics, customers or product claims.

## Recommended output

1. Scope and evidence reviewed (files, screen captures, viewport, limits).
2. Top 3–7 findings: principle(s), severity, direct evidence, recommended change.
3. Proposed design direction: tokens, composition, interaction conventions.
4. Implemented changes (when requested) and checks actually run.
5. Remaining uncertainties or manual verification needed.

## Guardrails

Do not state an issue as fact if a viewport, component state, or feature was unavailable for inspection. Distinguish observed issues from potential risks. Do not install dependencies without a reason. Do not claim WCAG compliance without validating the relevant criteria.
