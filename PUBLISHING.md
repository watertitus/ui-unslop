# Publish UI Unslop publicly on GitHub

This package is prepared for publication but **is not automatically public** until you complete the steps below.

1. In GitHub, create a **new public repository** named `ui-unslop` under `watertitus`. Leave the automatic README, license and gitignore options unchecked because the package already includes them.
2. From the unzipped `ui-unslop` directory, run:

```bash
git init
git branch -M main
git add .
git commit -m "Initial release: UI Unslop agent skill"
git remote add origin https://github.com/watertitus/ui-unslop.git
git push -u origin main
```

3. Open `https://github.com/watertitus/ui-unslop` in a signed-out browser session to confirm public access.
4. Check **Actions** to confirm `Validate skill` passes. In repository settings, keep visibility **Public** and enable Issues (optionally Discussions). Consider enabling private vulnerability reporting.
5. Add repository topics, e.g. `agent-skills`, `codex`, `claude-code`, `ui-design`, `ux`, `frontend`, `design-system`.
6. Create a GitHub release, e.g. `v1.0.0`, after passing checks. Share the README's installation instructions with users.

Do not publish the original video: only the derived checklist and original implementation guidance are included here.
