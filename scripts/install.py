#!/usr/bin/env python3
"""Install the bundled UI Unslop skill for Codex, Claude Code, or both."""
import argparse
import os
import shutil
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'skills' / 'ui-unslop'
DEST = {'codex': Path('.agents/skills/ui-unslop'), 'claude': Path('.claude/skills/ui-unslop')}


def install(agent, scope, project=None, force=False, home=None):
    if agent not in ('codex', 'claude', 'both'):
        raise ValueError('Unsupported agent')
    if scope not in ('project', 'user'):
        raise ValueError('Unsupported scope')
    if not (SKILL / 'SKILL.md').is_file():
        raise FileNotFoundError(f'Skill definition missing: {SKILL}')
    base = (Path(home).expanduser() if home is not None else Path.home()) if scope == 'user' else Path(project or os.getcwd()).expanduser()
    targets = ['codex', 'claude'] if agent == 'both' else [agent]
    paths = []
    # Check every target before changing any of them.
    for target in targets:
        out = base / DEST[target]
        if (out.exists() or out.is_symlink()) and not force:
            raise FileExistsError(f'{out} exists; use --force to replace this skill installation')
        if out.exists() and not out.is_dir() and not out.is_symlink():
            raise FileExistsError(f'{out} is not a directory')
        paths.append(out)
    for out in paths:
        if out.is_symlink() or out.is_file():
            out.unlink()
        elif out.exists():
            shutil.rmtree(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL, out)
        print(f'Installed: {out}')
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=('codex', 'claude', 'both'), default='both')
    parser.add_argument('--scope', choices=('user', 'project'), default='project')
    parser.add_argument('--project', help='Target project directory (project scope only)')
    parser.add_argument('--force', action='store_true', help='Replace existing UI Unslop installation(s)')
    args = parser.parse_args()
    if args.project and args.scope != 'project':
        parser.error('--project requires --scope project')
    try:
        install(args.agent, args.scope, args.project, args.force)
    except (FileExistsError, FileNotFoundError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
