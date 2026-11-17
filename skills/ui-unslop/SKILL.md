---
name: ui-unslop
description: Audit and refine AI-generated or cluttered web application interfaces into clear, cohesive, accessible designs. Use when asked to unslop, polish, redesign, clean up, modernize, or improve UI/UX, layout, typography, copy, spacing, cards, pricing pages, dashboards, forms, loading states, or calls to action in an existing frontend. Do not use for backend-only tasks or to change a product's brand without authorization.
---

# UI Unslop

Make an existing interface look intentionally designed, not generically AI-generated. Apply the 20 recommendations in `references/20-principles.md` as a practical review checklist, not as absolute rules. Preserve the product's meaning, architecture, and business logic.

## Working sequence

1. **Identify scope.** Read the user's goal, repository instructions, framework, design tokens, shared components, and affected screens. Inspect actual code and screenshots/preview if available. Never claim you reviewed a screen you could not see.
2. **Audit before editing.** Evaluate the 20 principles, identify 3–7 concrete issues with file/component locations, and prioritize by user impact. Read `references/audit-rubric.md` for scoring and exceptions. Do not fabricate observations.
3. **Protect existing intent.** Preserve branding, current flows, data, content accuracy, accessibility, responsive behavior, and functionality. Ask for approval only if a decision would materially change brand identity, product requirements, or destructive behavior. Otherwise proceed with reasonable defaults.
4. **Plan a coherent design direction.** Reuse existing typography, colour tokens, component patterns and spacing scale where possible. Create visual hierarchy through content, contrast, alignment, and restrained accents instead of decorative noise.
5. **Implement deliberately.** Make the smallest coherent set of code changes that resolves the highest-priority issues. Keep responsive breakpoints, semantic HTML, keyboard focus, colour contrast, form labels, reduced-motion preferences, and loading/error/empty states. Don't replace actual data with invented testimonials, metrics, or pricing. Don't remove meaningful information just to shorten the layout.
6. **Verify.** Run relevant lint, typecheck, tests, and build when available. Inspect mobile and desktop views, hover/focus states, and representative content lengths if visual tooling exists. State exactly what was run and what was not.
7. **Report concisely.** Summarize the main problems addressed, files/components changed, test results, and outstanding limitations. If asked for audit only, provide recommendations without editing files.

## The 20-point checklist

Use the detailed descriptions, caveats, and examples in `references/20-principles.md`:

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
14. Inner radius = outer radius minus padding (when geometrically appropriate)
15. Improve text contrast
16. Wrap headlines properly
17. Align by eye, not pixels
18. Use tabular numbers
19. Add loading states
20. Animate useful feedback

## Implementation rules

- No mandatory UI framework, CSS library, font, or icon package. Follow the project's existing stack and conventions.
- Prioritize information architecture and readability over trendy visual effects.
- Respect component APIs and avoid unrelated refactors.
- Prefer authentic product screenshots and real content to stock visuals or unverifiable claims.
- Use concise, descriptive copy without stripping legally required labels, a11y labels, or helpful instructions.
- Follow WCAG contrast and focus guidance; treat visual tricks as conditional, not hard-coded formulas.
- Use animation only for state-change communication; respect `prefers-reduced-motion`.
- Never retrieve secrets or transmit code, designs, screenshots, or files to external services without user authorization.

## Outputs

For **audit requests**, use `references/report-template.md` and give prioritized findings, evidence, and suggested fixes.
For **implementation requests**, apply fixes to project files, explain notable decisions, and document verification.
For **greenfield design requests**, adapt the principles to a clean, expressive system without pretending a before-state existed.
