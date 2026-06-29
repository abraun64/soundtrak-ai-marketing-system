# Phase 5 Launch / Day-1 Rollout — Spec

**Spec version**: v2 · 2026-06-15 — unified schema from the Acme Co + Acme Co Phase-5 artifact review.
(v1 2026-06-03 per Rollout Architecture v2 §5; v2 merges the Acme Co `phase-5-rollout` and Acme Co `launch-runbook` into one shape: Acme Co's step anatomy + Acme Co's overview/interactive gate + ownership-model-scaled training + data-driven status.)

**What this is**: the single self-contained per-campaign artifact for taking a campaign from **"assets Approved" → "live"** (and, where the tenant self-runs, **handed over**). One doc covers setup + deploy + training + dry-run + verification. **CM authors it — together with `phase-6-cadence.md` (for cadenced campaigns) — at the END of Phase 4**, the moment all assets are Approved (both seed from Plan §N "Phase 5 + 6 readiness"; don't wait for a phase to "start").

**Stored**: `campaigns/<slug>/phase-5-rollout.md` (markdown authoritative) + rendered `phase-5-rollout.html`.

**Authored from**: Plan §N "Phase 5 + 6 readiness" + Brief §Tech Setup + §Human Roles + §Cadence Shape + `tenant/<name>/integrations.yaml` + the tenant baseline.

**Locked**: at the end of Phase 5 execution. **THE GATE**: every blocker clear → operator approves Phase 5 closure → Phase 6 cycle 1 fires.

---

## Phase 0 vs Phase 5 — why setup EXECUTION lives here, not in Phase 0

**Phase 0 (onboard-tenant) is a DATA-COLLECTION phase.** It *authors* the durable tenant baseline — Brand Context · Compliance Profile · segments · market · `integrations.yaml` (config with **env-var refs, never live keys**) · seeded library · folder scaffold on the master. It captures **knowledge + config**; it does **not** execute the live technical standup.

**Phase 5 is the EXECUTION phase.** Everything Phase 0 specced as config gets **executed** here: install Claude Code on the operator machine, sync to the tenant OneDrive, provision **live** credentials into env vars, install templates into the platforms, deploy the campaign's assets, train the operator, run the dry-run, go live.

That boundary is *why* Phase 5 is one self-contained doc that inlines setup: the standup can't sit in Phase 0 (Phase 0 doesn't execute), so §2 below is where the config becomes a running system.

---

## Schema

```markdown
# Phase 5 Launch — <Campaign Name>

**Tenant**: <name>     **Ownership model**: <the operator-runs | tenant-self-runs | the operator-runs-then-tenant | outsourced-to-the operator>
**Phase 5 start**: <date>     **Target completion**: <date>     **Operator(s)**: <the operator + designated tenant role>
**Plan status**: 🟡 Draft — awaiting your sign-off  /  ✅ Approved — execution may begin
**THE GATE**: every blocker below clear → Phase 6 fires.

## §0 Campaign overview   ← the operator's orientation; the part they value most
**Don't reinvent the wheel — REUSE the dashboard's 🧭 Campaign DNA block verbatim** (Big Idea · Key
message · 15-sec pitch · KPI floor · Full concept link), then add:
- **Key assets going live** — a small visual table (Preview thumbnail → links to the full render · Asset · What it is) of **3–5 highlight assets**, pulled from `gallery-thumbs/`, with a link to the full **Gallery**. (The Acme Co foundation-assets pattern.)
- **What this phase puts live** — one line listing the deployables + the goals.
- **How launch day flows** — one line.

A cold reader gets the whole picture — campaign + visuals — before any step. **Reuse > rewrite.**

## ✋ Sign off this plan first   ← operator approval gate (added 2026-06-15)

This rollout was **built at the end of Phase 4** from the Plan + the assets actually produced — so it starts as a **Draft you approve before anything runs**. Two things to check:

1. **Is the plan complete + right?** Walk §2's steps — is anything missing (a deploy step, a publish step, a verify)? Add it.
2. **Gaps to close first** — assets / cookbooks this rollout NEEDS that don't exist yet (often a Phase-4 miss — a deploy cookbook, a logo/icon set, a referenced file). CM surfaces them here at build time; if any, **produce them BEFORE executing** (they go back to Phase 4 / Producer).

**Gaps identified at build time:**

| Gap | What's needed | Owner / source |
|---|---|---|
| <missing asset / cookbook / step> | <what to produce> | Phase 4 (Producer) — produce before approval |

*(or "✅ No gaps — every step has its asset + cookbook.")*

**How it surfaces (data-driven)**: while the **Plan status** line says Draft, the cross-campaign **[Tasks queue](../tasks.html)** and the dashboard To Do show **one** row for this phase — *"Approve the Phase 5 plan — Execute & Launch"* (🔴). The launch **steps** in §2 are **not** re-listed there: they live in this doc (checkboxes + live status), so the task list stays a decision queue, not a duplicate step list. `operator_actions.collapse_phase_plan_actions` reads this line to decide.

**To approve**: reply `approve Phase 5 plan` → CM trims the **Plan status** line to `✅ **Approved** — execution may begin (approved <date>)` (removing the Draft half) and re-renders tasks + dashboard → the gate row drops and you start working §2. **To send back**: name what to produce first (it re-enters Phase 4). Until approved, the steps below are a proposal, not a to-do.

## §1 Pre-flight
Binary readiness gates before ANY step starts:
- [ ] All produced assets `status: Approved` (check-state reports zero drift)
- [ ] Credentials at the keyboard (list exactly which, per step)
- [ ] No in-flight Producer/Brand runs that would change asset state mid-deploy

## §2 Setup & deploy sequence
THE SPINE. Atomic, dependency-ordered steps; group by environment (Claude Code/OneDrive ·
Email · Intranet · Social · …) where that aids scanning. Each step uses the step unit below.
Setup steps already satisfied for an existing/already-running tenant collapse to "✅ in place / N/A".

### Step <n> — <plain-language name; NO jargon, NO #asset-refs, NO "wire X" in the title>

**What this is**: plain English — what the step achieves for the operator + why it matters.
**Before you start**: prerequisites in plain words ("Step 1 must be live, and you've picked X") — NEVER `[depends-on: Step 1]`.
**How you'll know it worked**: something the operator can observe themselves.

<details markdown="1">  <!-- collapsed; the operator hands this to their developer/IT -->
<summary>🔧 Technical detail — for your developer / IT engineer</summary>
- Task (the actual deploy) · Cookbook link (full how-to) · Verify command · Rollback · Time · Mark-done propagator command.
</details>

☑ <interactive checkbox: "Step N complete">

## §3 Training & handoff   ← CONDITIONAL on ownership_model (see table below)
*(the operator-runs → the whole section is "N/A — the operator runs the cadence.")*
- **§3.1 Pre-session reading** — links the tenant operator reads in advance.
- **§3.2 Day-1 live session** (<duration> — depth per ownership_model) — numbered agenda.
- **§3.3 First-N-weeks support** — the operator's commitment + cadence + SLA.
- **§3.4 Dry-run gate** — the tenant runs ONE full cycle solo, unassisted (the operator watches).
  This is what "trained" means; it's the human half of the gate.

## §4 Day-1 verification
End-to-end binary checklist, walked once every §2 step is done (incognito test, real signup,
event fires, first asset live, spend within cap, etc.). Each row binary.

## §5 Failure modes
Symptom → diagnosis → fix. The 3–6 most likely break points and how to chase them.

## §6 Status + history
- **Live gate banner** — DATA-DRIVEN: reads the dashboard's Phase-5 blocker count
  (propagator → asset.yaml/campaign.yaml → dashboard). Not browser-local.
- **History table** — date · event · status.
```

---

## The step unit — TWO AUDIENCES (§2 — reused by Phase 6 §1)

Every step is written for a **non-technical operator first**, with the technical execution
**demarcated for a developer / IT engineer**. The operator must understand what's happening and
why WITHOUT reading jargon; the engineer gets the exact instructions in a clearly-labelled,
collapsed block ("there too", out of the way). This is the rule the Acme Co pilot revealed: a step
like "Wire #13 ESP `[depends-on: Step 1]`" is meaningless to a non-technical operator.

**Operator-facing — always plain English, always visible:**
| Field | Purpose |
|---|---|
| **Plain step name** | what it does — no `#asset` refs, no "wire X", no codenames in the title |
| **What this is** | what the step achieves for the operator + why it matters |
| **Before you start** | prerequisites in plain words — NEVER `[depends-on: …]` |
| **How you'll know it worked** | something the operator can observe themselves |
| **☑ checkbox** | "Step N complete" (personal overlay) |

**Developer/IT-facing — collapsed `🔧 Technical detail` block:**
| Field | Purpose |
|---|---|
| **Task** | the actual deploy action |
| **Cookbook** | link to the full technical how-to |
| **Verify** | the command/console check that proves it landed |
| **Rollback** | how to undo without cascade |
| **Time** | honest engineer time + any external wait |
| **Mark-done** | the propagator command (the source-of-truth status update) |

Same two-audience anatomy in Phase 5 §2 and Phase 6 §1 — the operator learns it once. Phase 6
cycle steps are lighter (Rollback usually n/a), but the plain-first + demarcated-technical split holds.
Any technical info an IT engineer needs MUST be in the block — present but not cluttering the human view.

---

## Status — data-driven truth + checkbox overlay

- **Source of truth = the dashboard.** Step completion is marked via the propagator
  (`propagate.py … --done`) or the underlying `asset.yaml`/`campaign.yaml` field; the dashboard's
  Phase-5 row + the §6 gate banner derive from that. Status cannot drift from the dashboard.
- **Interactive checkboxes are a personal overlay** (localStorage) for the operator's own tracking
  as they work a session. They are **never** the source of truth and must not be the only signal —
  the gate reads the data, not the boxes.
- The §6 banner shows N/total blockers clear; at 100% it states the approval reply that fires Phase 6.

---

## Ownership-model conditionality

§3 (training) and parts of §2 (system standup) scale with `ownership_model`:

| ownership_model | §2 system standup | §3 training | §3.3 support |
|---|---|---|---|
| `the operator-runs` | minimal (already on the operator's machine) | **N/A — skip §3** | n/a |
| `the operator-runs-then-tenant` | full standup on tenant machine | light Phase-5a setup → light 5b handoff | ~2 weeks active, then ad-hoc |
| `tenant-self-runs` | full standup on tenant machine | **heavy** (no pilot cushion — solo from cycle 1) | 4 weeks weekly check-ins, then quarterly |
| `outsourced-to-the operator` | full standup on the operator's machine | **N/A — skip §3** | the operator runs indefinitely |

Setup steps already true for an existing tenant (2nd campaign onward) render as "✅ in place / N/A" rather than being deleted — the doc stays self-contained and replayable.

---

## Drafting discipline

- **Authored from Plan §N.1** — transcribe the deployment matrix + setup tasks + training plan into the live step form; don't re-author strategy. Plan §N is the static gate; this is the live tracking artifact.
- **Built in Draft → operator approves the PLAN before execution.** At build time (end of Phase 4), run a **gap check**: does every §2 step have its asset + cookbook? Is every referenced file actually on disk? List any missing pieces in the "✋ Sign off this plan first" gaps table — often a Phase-4 miss (a deploy cookbook, a logo/icon set). The operator approves the plan (or sends gaps back to Phase 4) BEFORE any step runs; the steps are a proposal until then. Phase 5 routinely surfaces "we need to produce X" — that's the point of the gate.
- **Human-first, two audiences.** Operator-facing text is plain English — no `#asset` refs, no "wire X", no `[depends-on]` in the step name or body. All technical execution detail (the concrete commands like "provision Mailchimp API key + set env vars + configure `integrations.yaml`") lives in the collapsed `🔧 Technical detail — for your developer / IT` block. Present, but out of the human's way.
- **Honest times.** Tenant-side tasks usually take ~2× the operator's estimate.
- **Binary verification + a rollback** on every deploy step — no "looks fine".
- **One gate, stated once** in the header and the §6 banner. No competing "Phase 5 closes when…" statements.
- **No phase-number drift.** Storage keys, CSS classes, section headers, and history labels all say *Phase 5*. (v1 Acme Co artifact had `phase4` storage keys + a "Phase 6 status" header inside a Phase 5 doc — do not reproduce.)
- **§0 reuses the dashboard Campaign DNA + adds key-asset visuals** — don't write a bespoke overview; reuse the 🧭 Campaign DNA block verbatim, then a small thumbnail table of 3–5 highlight assets (from `gallery-thumbs/`) + a Gallery link. Rich, but reuse > rewrite.

---

## Relationship to Phase 6 (shared spine)

Phase 6's cadence runbook is the same shape with the one-time bits swapped for recurring ones:

| Section | Phase 5 | Phase 6 |
|---|---|---|
| §0 At a glance | what goes live + the gate | the cadence + who runs it |
| Atomic step checklist | §2 setup & deploy (once) | §1 this cycle's steps (repeats) |
| One-time module | §3 training & handoff (conditional) | — |
| Recurring module | — | KPI tracking + cycle history + refinements log |
| Failure / escalation | §5 failure modes | §2 escalation paths |
| Status + history | §6 gate banner | §3 cycle history |

Same step-unit anatomy, same data-driven status, same failure/escalation pattern. Phase 6 adds the KPI/cycle-history loop and drops the one-time training. See `docs/specs/phase-6-cadence.md`.

---

## Cross-references

- **Rollout Architecture v2 spec**: `docs/specs/rollout-architecture.md` §5 (Phase 5) + §6.3 (handoff flow)
- **Plan spec**: `docs/specs/plan.md` §N "Phase 5 + 6 readiness" — upstream source
- **Brief spec**: §Tech Setup + §Human Roles + §Cadence Shape — populated source data
- **integrations.yaml spec**: `docs/specs/integrations.md` — Phase 5 §2 executes this file's config into a live system
- **Phase 6 spec**: `docs/specs/phase-6-cadence.md` — what Phase 5 unlocks; shares the spine
- **Onboard-tenant playbook (Phase 0)**: `docs/playbooks/onboard-tenant.md` — the data-collection phase that authors the baseline Phase 5 executes
