#!/usr/bin/env python3
"""Canonical data-root resolution across git worktrees (SYS-002).

The system repo can be checked out in two shapes:
  - MAIN checkout:     <root>/                              — has campaigns/ (a SEPARATE
                                                              gitignored repo), system/,
                                                              tenant-brand/, docs/, .claude/
  - WORKTREE checkout: <root>/.claude/worktrees/<name>/     — system CODE only; campaigns/
                                                              is NOT present (separate repo)

A worktree is for isolated work on system CODE (skills / specs / hooks). The DATA dirs
(campaigns/, system/, tenant-brand/) are canonical in the MAIN checkout. Any tool that
reads or writes DATA must resolve back to the main checkout when it happens to run from a
worktree — otherwise it sees an absent campaigns/ and silently no-ops or reports false
failures. That silent failure is the "worktree blind spot."

Rule of thumb for callers:
  - CODE paths (render.py, build scripts, templates, hooks): use the running checkout's
    own root — you want the code you're editing.
  - DATA paths (campaigns/, system/, tenant-brand/): use data_root() — always the main
    checkout, whichever checkout you're running from.

Usage:
    import sys; sys.path.insert(0, str(REPO_ROOT / ".claude" / "lib"))
    import repo_paths
    DATA = repo_paths.data_root(REPO_ROOT)
    campaigns = DATA / "campaigns"
"""
from __future__ import annotations
from pathlib import Path


def is_worktree(path) -> bool:
    """True if `path` is inside a `.claude/worktrees/<name>` checkout."""
    parts = Path(path).resolve().parts
    return any(
        parts[i] == ".claude" and parts[i + 1] == "worktrees"
        for i in range(len(parts) - 1)
    )


def data_root(repo_root) -> Path:
    """Canonical root for DATA dirs (campaigns/, system/, tenant-brand/).

    From the main checkout, returns repo_root unchanged. From a worktree
    (<main>/.claude/worktrees/<name>), returns the main checkout above it.
    """
    p = Path(repo_root).resolve()
    parts = p.parts
    for i in range(len(parts) - 1):
        if parts[i] == ".claude" and parts[i + 1] == "worktrees":
            return Path(*parts[:i]) if i > 0 else p
    return p
