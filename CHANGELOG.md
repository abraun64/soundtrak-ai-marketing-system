# Changelog — Soundtrak AI Studio

All notable changes to the **system** (the product) are recorded here — the public release log.
Each version is a clean Seed cut published to GitHub. Format follows
[Keep a Changelog](https://keepachangelog.com); versioning follows [SemVer](https://semver.org).

Only **system-layer** changes appear here. Tenant- and campaign-layer work is never recorded —
the `build_seed` allowlist defines what counts as "system" (i.e. what ships). Maintained by the
System Manager; see "Cutting a release" at the foot of this file.

## [Unreleased]

### Fixed
- **Campaign To Do shows only current-stage tasks.** The dashboard To Do and the
  cross-campaign tasks queue no longer surface tasks for phases the campaign hasn't
  reached yet (e.g. launch or cadence steps while still in asset production) — only the
  current stage's tasks, plus any still-open earlier work.
- **A malformed campaign no longer blanks the campaigns index.** A bad `campaign.yaml`
  used to crash the Active-campaign list so the index rendered empty; the index now
  tolerates the bad entry, and any unexpected render failure degrades to a basic roster
  with a warning instead of silently showing nothing.
- **System Manager backlog/ideas/audit resolve to one canonical store.** Edits and id
  allocation always target the main checkout (never a per-worktree copy), with a
  duplicate-id guard — preventing ticket-id collisions when work spans git worktrees.

### Changed
- **Campaign dashboard — one authoritative link per phase.** The Phases & Artifacts
  table now shows a single primary link per phase (the gate document to review), with
  earlier/supporting/superseded docs moved to a collapsed "Earlier & supporting
  documents" block below — so it's unambiguous what each gate is asking you to review.

- **Copy-review files are just the copy now.** A `copy.md` (the operator's edit surface)
  is held to a strict minimum — a one-line orientation, the copy as labelled fields, and the
  few constraints that bind it. Strategic rationale, version-history, and design/production
  notes no longer clutter the edit surface (they live in the asset record).
- **Copy-surface guard.** The state checker now flags any copy file that regrows a
  banned section (a thesis, a version-history log, or design annotations), so the edit
  surface stays clean over time.
- **Board-currency guard.** The state checker + the turn-boundary gate now flag any
  to-do item that's still pending in a phase the campaign has already moved past — so the
  board reflects reality during long working sessions instead of silently lagging.

### Added
- **Docs-currency check.** A new `docs-audit` diagnostic (run in the smoke test + the
  weekly digest) catches stale agent counts, dropped navigation-index columns, and public
  docs that fell behind the agent/spec set — so the reference docs stay honest automatically.

- **Proactive scheduled cadences.** Four optional weekly/monthly sweeps (competitor &
  library scan · tenant brand-drift · stale-asset/surface · per-tenant shipped/blocked
  rollup) that surface findings to the inbox on a timer — read-only, never auto-act.
- **Disqualifiers / hard-nos card.** Each tenant playbook gains an always-loaded section
  for who you don't target and what you won't say (the inverse of audience truths), sliced
  into every brief — referencing the compliance profile rather than duplicating it.

- **Categorised spec index.** `docs/specs/README.md` groups the specs into artifact
  schemas / asset-type specs / architecture & process, so the folder is navigable at a
  glance without moving any files.

- **Machine-checkable agent handoffs.** CM and the specialist agents now exchange a
  structured envelope alongside their prose, and CM validates each return (status,
  required fields, and that every claimed deliverable actually exists on disk) before
  acting — so a silently-incomplete handoff fails loudly instead of breaking downstream.

## [1.0.0] — 2026-06-29

Initial public release — the standalone, single-tenant "Seed".

### Added
- **Seven-role marketing system**: Campaign Manager (orchestrator) + Creative Director,
  Insights Manager, Governance Manager, Brand Manager, Producer, and Marketing Forensic Analyst.
- **Full campaign pipeline**: Phase-0 tenant baseline (with a hard gate) → Brief → Concept →
  Plan → Asset, with compliance and brand gates before the operator sees any asset.
- **Data-driven operator surfaces** — index, campaign dashboards, asset gallery, and tasks,
  auto-rendered from YAML so the data is the single source of truth.
- **System Manager** — a backlog / idea-inbox / audit dashboard for evolving the system itself,
  independent of any campaign.
- **Tooling** — install doctor, Phase-0 gate, and the `build_seed` clean-cut + secret-leak scanner.
- **Self-service docs** — Help & Guides hub, deployment guide, getting-started, FAQ, and an
  illustrated training guide.
- **Legal** — PolyForm Internal Use license plus trademark, notice, and data-handling notes.

---

## Cutting a release

_For the maintainer (the System Manager owns this):_

1. Make sure **[Unreleased]** lists every system-layer change since the last cut.
2. Rename **[Unreleased]** to the new version with today's date, and add a fresh empty
   **[Unreleased]** above it. Bump per SemVer — MAJOR (breaking) · MINOR (feature) · PATCH (fix).
3. Tag the commit: `git tag -a vX.Y.Z -m "Soundtrak AI Studio vX.Y.Z"`.
4. Cut + scan the Seed: `python .claude/lib/build_seed.py --out <dir> --git`.
5. Eyeball it, then push the Seed to the public repo — the human-gated step.
