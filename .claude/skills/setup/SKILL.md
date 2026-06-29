---
name: setup
description: First-run setup for a fresh Marketing AI System instance. Triggers on "set yourself up", "set up the system", "first run", "get me started", or when an operator opens a freshly-downloaded instance and asks how to begin. Installs missing prerequisites, verifies the install, and turns on backup. Do NOT trigger for campaign work or once setup is already complete (a tenant baseline exists).
---

# First-run setup

You are setting up a fresh instance for a (possibly non-technical) operator. Be plain-spoken
and encouraging. Run the steps in order; say in one line what each does *before* you run it.
You run the commands — never ask the operator to type pip/git commands themselves.

## 1. Install + verify prerequisites

Run:

```
python .claude/skills/system-smoke-test/doctor.py --fix
```

This installs anything missing (the `markdown` and `pyyaml` libraries, Playwright + its
browser) and prints a health report. If a line is still `[FAIL]` afterwards, show the
operator the exact fix it printed and stop — don't go on until it reads **READY**. The most
common cause is Python being installed without "Add to PATH" ticked; if `python` isn't
found at all, point them back to the deployment guide §1.

## 2. Turn on backup (so they never lose work)

- If this folder isn't a git repo yet (`git rev-parse --git-dir` fails), run `git init`,
  then `git add -A` and commit `"Initial setup"`.
- Ask: "Do you have a private online repository to back up to (GitHub/GitLab), or shall we
  keep backups local for now?"
  - **Has one** → `git remote add origin <their-url>` then `git push -u origin main`.
  - **Not sure / no** → fine. Explain: their work is committed locally every session, and if
    this folder lives in OneDrive/Dropbox that's their offsite copy. They can connect an
    online backup later by re-running setup.
- The system auto-saves (commits, and pushes if a remote is connected) at the end of each
  session — they don't have to remember to save.

## 3. Confirm + hand off

Run the doctor once more (no `--fix`) to confirm **READY**, then say:

> "You're set up. To begin, just say: **Onboard \<your business name\>** — I'll walk you
> through it."

## Do NOT do here

- Don't author any campaign or tenant content — that's Phase 0 (the Onboard step).
- Don't make the operator run commands themselves; you run them and report what happened.
