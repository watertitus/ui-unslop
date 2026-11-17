# The 20 UI Unslop principles

Source: the user-provided short video titled “20 Ways to Unslop AI Designs.” Wording follows its on-screen checklist; implementation notes below are original elaborations, not a transcript of the creator's narration.

1. **Delete filler badges.** Remove labels such as “NEW,” “POWERFUL,” or “AI-POWERED” unless they convey a verifiable distinction. Keep important status badges.
2. **Drop redundant labels.** Avoid repeating the same category/title/value in nearby UI. Preserve accessible names and necessary context.
3. **Unitalicize random words.** Italics should convey meaning or a consistent editorial treatment, not randomly decorate hero copy.
4. **Mono only where needed.** Reserve monospace for code, identifiers, structured data or a deliberate brand pattern; use legible body fonts elsewhere.
5. **Use a design system.** Establish reusable type scales, spacing steps, colour tokens, surface styles and interactive states; prefer existing tokens.
6. **Show the actual product.** Replace vague promises with genuine screenshots, interactive demos or meaningful representations. Never invent screenshots or results.
7. **Enlarge the main feature.** Give the central product capability and useful visual evidence enough size and prominence to be understood.
8. **Group with spacing.** Use proximity and whitespace to separate concepts. Avoid unnecessary dividers and box-within-box stacks.
9. **Make headlines specific.** State the outcome, audience or concrete capability, rather than generic slogans. Don't overclaim.
10. **Emphasize the CTA.** Establish one visually primary action per decision context; preserve useful secondary actions and clear labels.
11. **Add an accent colour.** Use a restrained brand-compatible accent to mark key interactive elements or hierarchy. Don't add unrelated colour or rely on colour alone.
12. **Keep icons consistent.** Align stroke/filled style, visual weight, optical size and meaning; icons are optional where text is clearer.
13. **Remove embellishments.** Eliminate purely decorative glows, emojis, gradients, shadows and ornamental graphics that compete with content; retain intentional brand expression.
14. **Inner radius = outer radius − padding.** For nested rounded rectangles, a sensible starting geometry is inner corner radius ≈ max(0, outer radius − inset spacing). This is a heuristic, not universal: adjust for borders, mixed padding and visual fit.
15. **Improve text contrast.** Make body copy, supporting copy, controls and states readable across actual backgrounds; test against accessibility criteria, not visual impression alone.
16. **Wrap headlines properly.** Control measure, line breaks and type scaling so headings read naturally on narrow and wide screens; avoid fragile hard-coded breaks.
17. **Align by eye, not pixels.** Account for optical imbalance of glyphs, icons and shapes while retaining a consistent layout grid and predictable responsive alignment.
18. **Use tabular numbers.** Apply tabular numerals to aligned prices, metrics, clocks, counters and columns, where consistent digit widths improve scanning.
19. **Add loading states.** Show meaningful pending, success, error and empty states for async interactions, ideally without layout shifts; don't fake progress.
20. **Animate useful feedback.** Motion should confirm selection, progress, completion or changes of state; keep subtle and support reduced-motion preferences.

## When principles conflict

Usability, correctness, brand requirements and accessibility outrank aesthetic minimalism. A required form label is not a redundant label; a contrast-safe brand palette is preferable to a fashionable low-contrast palette; a status badge is not filler when it conveys material state. Explain any intentional exception.
