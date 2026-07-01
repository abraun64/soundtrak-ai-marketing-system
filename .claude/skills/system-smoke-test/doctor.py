#!/usr/bin/env python3
"""Install doctor (Retro-5) - fresh-machine prerequisite check for the Marketing AI System.

Where system-smoke-test asks "is the system working?", the doctor asks "is THIS MACHINE
set up to run it?" - the first thing a new operator runs after cloning the Seed. Each
failed check prints a one-line remediation. Read-only, ASCII output (cp1252-safe).

  python .claude/skills/system-smoke-test/doctor.py
Exit 0 = ready; exit 1 = one or more blocking prerequisites missing.
"""
from __future__ import annotations
import argparse
import importlib.util
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # .claude/skills/system-smoke-test/ -> root


def run() -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []  # (level ok|warn|fail, label, remediation)

    # Python version
    v = sys.version_info
    rows.append(("ok" if v >= (3, 10) else "warn",
                 f"Python {v.major}.{v.minor}.{v.micro}",
                 "" if v >= (3, 10) else "Python 3.10+ recommended"))

    # Required importable libraries
    for mod, fix in (("markdown", "pip install markdown"), ("yaml", "pip install pyyaml")):
        if importlib.util.find_spec(mod):
            rows.append(("ok", f"python module: {mod}", ""))
        else:
            rows.append(("fail", f"python module: {mod} MISSING", fix))

    # Playwright + chromium (gallery thumbnails)
    if importlib.util.find_spec("playwright"):
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                exe = p.chromium.executable_path
            if exe and Path(exe).exists():
                rows.append(("ok", "playwright + chromium", ""))
            else:
                rows.append(("fail", "playwright: chromium not installed", "playwright install chromium"))
        except Exception as e:
            rows.append(("fail", "playwright present but unusable",
                         f"playwright install chromium  ({str(e)[:70]})"))
    else:
        rows.append(("fail", "python module: playwright MISSING",
                     "pip install playwright && playwright install chromium"))

    # git (+ optional git-lfs)
    rows.append(("ok" if shutil.which("git") else "fail", "git",
                 "" if shutil.which("git") else "install Git"))
    rows.append(("ok" if shutil.which("git-lfs") else "warn", "git-lfs (optional - video assets)",
                 "" if shutil.which("git-lfs") else "install git-lfs only if shipping MP4 assets"))

    # Credential env vars referenced in tenant integrations.yaml
    refs: dict[str, list[str]] = {}
    for p in ROOT.glob("tenant/*/integrations.yaml"):
        try:
            for m in re.findall(r"\$\{([A-Z0-9_]+)\}", p.read_text(encoding="utf-8")):
                refs.setdefault(m, []).append(p.parent.name)
        except OSError:
            continue
    unset = sorted(k for k in refs if not os.environ.get(k))
    if not refs:
        rows.append(("ok", "credential env vars", "none referenced yet"))
    elif unset:
        rows.append(("warn", f"credential env vars: {len(unset)} unset",
                     "set before publishing: " + ", ".join(unset)))
    else:
        rows.append(("ok", f"credential env vars ({len(refs)} all set)", ""))

    return rows


def attempt_fix() -> None:
    """Install any missing Python prerequisites. Idempotent — safe to re-run."""
    print("=== doctor --fix: installing prerequisites (safe to re-run) ===")
    pkgs = []
    if not importlib.util.find_spec("markdown"):
        pkgs.append("markdown")
    if not importlib.util.find_spec("yaml"):
        pkgs.append("pyyaml")
    if not importlib.util.find_spec("playwright"):
        pkgs.append("playwright")
    if pkgs:
        subprocess.run([sys.executable, "-m", "pip", "install", *pkgs])
    # Chromium browser for Playwright (downloads only if missing)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"])
    print("=== fix attempt done; re-checking below ===\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Install doctor - check (and optionally fix) prerequisites.")
    ap.add_argument("--fix", action="store_true", help="attempt to install any missing prerequisites")
    ap.add_argument("--accept-license", action="store_true",
                    help="accept the license non-interactively (first-run gate)")
    a = ap.parse_args()

    # First-run license gate (SYS-048): show the disclaimer + require acceptance before any
    # setup work runs. Accepted once per install; recorded locally (never shipped in the Seed).
    sys.path.insert(0, str(ROOT / ".claude" / "lib"))
    try:
        import accept_license
        if not accept_license.require(ROOT, auto_accept=a.accept_license,
                                      interactive=sys.stdin.isatty()):
            print("\nInstall doctor halted: accept the license to continue.")
            return 2
    except Exception as e:  # noqa: BLE001 — a gate failure must never brick the doctor
        print(f"(license gate skipped: {e})", file=sys.stderr)

    if a.fix:
        attempt_fix()
    sym = {"ok": "[ OK ]", "warn": "[WARN]", "fail": "[FAIL]"}
    rows = run()
    print("=== Marketing AI System - install doctor ===")
    for level, label, fix in rows:
        print(f"{sym[level]} {label}" + (f"  -> {fix}" if fix else ""))
    fails = sum(1 for r in rows if r[0] == "fail")
    warns = sum(1 for r in rows if r[0] == "warn")
    print(f"\n{fails} blocking, {warns} warning(s).")
    print("READY." if not fails else "NOT READY - resolve the [FAIL] items above.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
