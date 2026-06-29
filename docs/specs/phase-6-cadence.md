# Phase 6 Ongoing Cadence — Spec

**Spec version**: v2 · 2026-06-15 — aligned to the shared operator-runbook spine introduced in `phase-5-rollout.md` v2. (v1 2026-06-03 per Rollout Architecture v2 §6.)

**What this is**: the per-campaign **operator runbook for steady state** — what the operator opens on cadence day and executes top to bottom. **Authored by CM at the END of Phase 4, alongside `phase-5-rollout.md`** (both seed from Plan §N) — only for cadenced campaigns (`cadence_shape.type` != "one-off").

**Stored**: `campaigns/<slug>/phase-6-cadence.md` (markdown authoritative) + rendered `phase-6-cadence.html`. **Canonical filename** — not `cadence-playbook.md` (a legacy drift; retrofits rename to this).

**Authored from**: Plan §N.2 + Brief §Tech/Human/Cadence + `tenant/<name>/integrations.yaml` + Phase 5 closure learnings.

**Living document**: updated after each cycle — current §1 always reflects current best practice; history accretes in §3/§5. NOT versioned; current state is canonical.

---

## Same spine as Phase 5

Phase 6 IS the Phase 5 runbook with the one-time bits swapped for recurring ones, so the operator learns **one shape**:

| Section | Phase 5 | Phase 6 (this spec) |
|---|---|---|
| Cold-start context | §0 At a glance | §0 At a glance |
| **Atomic step checklist** (shared step unit) | §2 setup & deploy (once) | **§1 this cycle's checklist (repeats)** |
| Failure / escalation | §5 failure modes | §2 escalation paths |
| Status + history | §6 gate banner | §3 cycle history |
| One-time module | §3 training & handoff | — |
| Recurring module | — | §4 KPI tracking · §5 refinements |

The **step unit** (see `phase-5-rollout.md` §"The step unit") and the **data-driven status + checkbox overlay** rule are identical here. Phase 6 cycle steps are lighter than Phase 5 deploy steps — *Rollback* is usually n/a for a repeating step — but the anatomy (title · owner · method · time · verify · status) and the discipline (atomic, honest times, data-driven status) are the same.

---

## Schema

```markdown
# Phase 6 Ongoing Cadence — <Campaign Name>

**Tenant**: <name>     **Cadence**: <frequency> · <day + time + timezone>
**Operator**: <designated role + name OR "tenant-managed internally">
**Operator mode**: Mode 1 (the operator/Code) | Mode 2 v1 (Code+OneDrive on tenant machine)
**Phase 6 start date**: <date>     **Cycles completed**: <count>
**Plan status**: 🟡 Draft — awaiting your sign-off  /  ✅ Approved — the cadence may run

## §0 Campaign overview
**Reuse the dashboard's 🧭 Campaign DNA block verbatim** (as Phase 5 does), then add a **cycle-workflow visual** — an Acme Co-style `<pre>` timeline of what happens each cycle/week (passive trigger → operator opens Code → runs the cadence skill → answers N questions → reviews gallery → adapter pushes → operator sends/posts → done · total time), with the **Phase-6 assets linked directly inside the workflow** (`<a>` links inside the `<pre>`).
- **No separate key-asset thumbnail table** for Phase 6 — the workflow links the assets it uses; add one "→ all assets in the Gallery" line.
- Close §0 with: who runs it · "cycle complete when …" · total operator time.
(Phase 5 keeps its key-asset visual table; Phase 6 swaps it for this cycle-workflow because the *flow* is what the operator needs to internalise, not a static asset grid.)

## ✋ Sign off this plan first   ← operator approval gate (added 2026-06-15)

Built at the end of Phase 4 alongside the Phase 5 doc — a **Draft you approve before the cadence runs**. Check: is the cycle complete + right, and does every step have its asset / cadence skill / cookbook? CM lists any gaps here at build time; gaps go back to Phase 4 before approval.

| Gap | What's needed | Owner / source |
|---|---|---|
| <missing asset / cadence skill / cookbook> | <what to produce> | Phase 4 (Producer / CM) — produce before approval |

*(or "✅ No gaps — every cycle step has what it needs.")*

**How it surfaces (data-driven)**: while the **Plan status** line says Draft, the cross-campaign **[Tasks queue](../tasks.html)** and the dashboard To Do show **one** row for this phase — *"Approve the Phase 6 plan — Manage & Report"* (🔴). The cycle steps in §1 are **not** re-listed there: they live in this doc, so the task list stays a decision queue, not a duplicate step list. `operator_actions.collapse_phase_plan_actions` reads this line.

**To approve**: reply `approve Phase 6 plan` → CM trims the **Plan status** line to `✅ **Approved** — the cadence may run (approved <date>)` and re-renders → the gate row drops and the cadence runs. Until then it's a proposal.

## §1 This cycle's checklist
**Cycle <N>** · <episode/issue title> · <recorded/authored date> · Target ship <date>

| # | Step | Owner | Method | Time | Verify | Status |
|---|---|---|---|---|---|---|
| 1 | <trigger — passive, e.g. "new episode airs Wed"> | n/a | — | — | — | 🟢 |
| 2 | <operator opens Claude Code on cadence day> | <role> | manual | 1 min | session loads | ⏳ |
| 3 | <runs slash command — e.g. /weekly-episode-pack> | <role> | slash cmd | 5 min | CM interviews | ⏳ |
| 4 | <answers N structured questions> | <role> | chat | <min> | inputs captured | ⏳ |
| 5 | <reviews approved assets in gallery> | <role> | gallery.html | <min> | tiles on-brand | ⏳ |
| 6 | <adapter-handled step fires> | CM (auto) | API | <sec> | draft created | ⏳ |
| 7 | <operator manual step — Send, social post, etc.> | <role> | <UI> | <min> | live | ⏳ |
| ... | | | | | | |

**Cycle complete when**: <criterion>. Total operator time: ~<min>.
Status is data-driven (cadence entry / propagator → dashboard Phase-6 row); interactive checkboxes are a personal overlay, never the source of truth.

## §2 Escalation paths
| If this happens | Do this | Then (fallback) |
|---|---|---|
| <condition 1> | <first action> | <escalation if first fails> |
| ... | | |
(Sourced from `tenant/<name>/integrations.yaml#escalation`. Don't duplicate — cross-reference.)

## §3 Cycle history (last 8 cycles; older → collapsible)
| Cycle | Title | Ship date | Operator | Send count | Open rate | Notes |
|---|---|---|---|---|---|---|
| <N> | <title> | <date> | <name> | <count> | <%> | <notes> |

## §4 KPI tracking
Against Brief §Goal & KPI:
- **Primary**: <metric + target + current>
- **Secondary**: ...
**Cycle-over-cycle trend**: <observations>

## §5 Procedural refinements
Living log of cycle-over-cycle improvements (what changed + why):
- <date>: <refinement>
```

---

## Drafting discipline

- **§1 is THE thing.** Operator opens this on cadence day, executes top to bottom, done. Everything else is reference.
- **Step rows are atomic** — one operator action OR one automated step per row. Don't batch. (Same unit as Phase 5 §2.)
- **Honest times.** If a step takes 10 min, write 10.
- **Data-driven status + checkbox overlay** — identical rule to Phase 5: the dashboard's Phase-6 row is the truth (cadence entries with `status: done` / propagator); checkboxes are personal tracking only.
- **Escalation mirrors integrations.yaml** — cross-reference, don't duplicate.
- **Cycle history bounded** — last 8 visible; older rows archive to a `<details>` collapsible.
- **No phase-number drift** — storage keys, classes, headers, history labels all say *Phase 6*.
- **Living-document** — refinements log in §5; §1 always reflects current best practice.

---

## Mode-specific guidance

### Mode 1 (the operator/Code)
- All steps execute on the operator's machine; "open Claude Code" = the operator's existing project; gates resolve in chat with the operator.

### Mode 2 v1 (Code+OneDrive on tenant machine)
- Operator opens Claude Code on THEIR machine pointed at THEIR tenant OneDrive; same skills/agents/commands.
- Gates resolve in chat with the tenant operator (the operator not in the loop unless escalated).
- Escalation = Slack/email to the operator per `integrations.yaml#escalation`.

---

## Cross-references

- **Phase 5 spec**: `docs/specs/phase-5-rollout.md` — the shared spine + step unit + status rule; what Phase 6 follows from.
- **Rollout Architecture v2 spec**: `docs/specs/rollout-architecture.md` §6 (Phase 6) + §6.2 (Mode 1 vs Mode 2 v1).
- **Plan spec**: `docs/specs/plan.md` §N.2 — upstream skeleton.
- **integrations.yaml spec**: `docs/specs/integrations.md` — §escalation block sourced here.
- **Brief spec**: §Cadence Shape — frequency + ownership_model upstream of this file.
