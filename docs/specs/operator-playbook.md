# Operator Playbook — Schema

The **Operator Playbook** is the durable, per-practitioner record of how the operator (the operator) thinks, writes, evaluates work, and runs marketing. It's the upstream input that lets every Phase 1 discovery start from extraction (the operator's read) rather than fabrication (AI's first guess).

**Captured during Retro 001 (2026-05-27) per action item AI-2.**

## Operating principle

> **Reference, don't duplicate.** the operator's playbook lives in his existing Digital Twin folder (`C:/Users/<you>/OneDrive/Claude/Digital Twin/Knowledge Base/`). The system reads it from there. Duplicating into `operator/the operator/` creates a sync problem — which version is authoritative? The Digital Twin is the source of truth; `operator/the operator/index.md` is the reference index the system uses to navigate it.

When the operator updates the Digital Twin, the system reads the new version automatically on next access. No re-ingestion needed.

## File layout

```
operator/
  the operator/
    index.md             ← THE index — maps Digital Twin files + names which ones each agent reads
    overrides/           ← optional — per-campaign overrides if the operator wants to deviate from playbook
      <campaign-slug>.md
```

`operator/the operator/index.md` is the entry point for every agent. CD, Brand Manager, Producer read it during Phase 1 / 2a to determine which Digital Twin files to consult for the specific task.

## What the Operator Playbook covers

The playbook is the source of truth for everything that's *the operator's view* of marketing — distinct from per-tenant Brand Context (which is tenant-specific brand voice/visual/positioning).

| Layer | What it covers | Lives in |
|---|---|---|
| **Identity** | the operator's professional posture, resume, Clarity 4D / HDBI / LSI profiles, Working Profile | `Knowledge Base/01_about_me/` |
| **Voice** | Soundtrak voice register, banned words/phrases, sentence patterns the operator uses | `Knowledge Base/01_about_me/Tone of voice_v2.md` |
| **Marketing principles** | The 24+ principles the operator operates by (brand-vs-performance, journey-as-one-system, intellectual-authority-over-budget, etc.) | `Knowledge Base/02_core_business_philosophies/Soundtrak_Playbook.md` + `extended_principles_11-24.md` |
| **Methodology** | Marketing playbook, Core Marketing Capabilities Framework, UX Design Fundamentals, Work Values | `Knowledge Base/02_core_business_philosophies/` |
| **Case studies** | Real prior Soundtrak/Netwealth case studies the operator has run, including the AdviceTech program | `Knowledge Base/02_core_business_philosophies/Case studies.txt` + `Working folder/case study - brand.docx` + `case_study_01_advicetech.docx` |
| **Influences** | LinkedIn follows, podcasts, newsletters, books — who the operator reads/listens to (signals taste + reference frame) | `Knowledge Base/03_Business_influences/` + `04_Personal-interests_cultural_influences/` |
| **Origin material** | Brain-dump transcripts, voice recordings, raw research that fed the curated layer | `Working folder/` (NOT for direct agent consumption — operator-only reference) |

## How each agent uses the playbook

**Campaign Manager (CM)** during Phase 1:
- Reads `operator/the operator/index.md` first
- Identifies which Digital Twin files are relevant to the campaign's tenant/scope
- Pulls relevant principles into the Brief authoring (e.g. "this campaign tests principle 11 — Research Is a Competitive Content Moat")
- Brief attributes "operator's read" sections by referencing playbook principles (e.g. *"per Operator Playbook §13 — Challenger brands win through intellectual authority, not budget"*)

**Creative Director (CD)** during Phase 2:
- Reads the relevant principles from the index
- Concepts cite which principles they're applying or testing
- Moodboard references can pull from the operator's influences (the LinkedIn follows, podcasts subscribed-to, etc. — these signal the operator's taste reference frame)

**Brand Manager** during Phase 4 asset reviews:
- References the operator's voice doc (`Tone of voice_v2.md`) for voice fidelity checks
- References banned-words list from voice doc — these are the operator's banned words, not just per-tenant
- Verdicts cite which principle the discipline applies (e.g. *"argument-through-contrast pattern per the operator's voice doc §1"*)

**Producer** during Phase 4a:
- Reads relevant Per-Step Brief slices that CM has pulled FROM the playbook
- Does NOT load the playbook directly (CM is the librarian — slices it)
- Voice slice in the Per-Step Brief explicitly references the playbook section it's drawn from

## Schema for `operator/the operator/index.md`

```markdown
# the operator's Operator Playbook — Index

**Source of truth**: `C:/Users/<you>/OneDrive/Claude/Digital Twin/Knowledge Base/`
**Last reviewed by the operator**: <date>
**Version**: <n> (incremented when the operator adds/removes files in the Digital Twin)

## Quick reference — what each agent should read first

| Agent | First read |
|---|---|
| Campaign Manager (Brief authoring) | Soundtrak_Playbook.md + extended_principles_11-24.md |
| Creative Director (Concepts) | Soundtrak_Playbook.md + Case studies.txt + Business Book Inventory.md |
| Brand Manager (Verdicts) | Tone of voice_v2.md + Marketing Playbook.txt |
| Producer (via CM's slices) | None directly — reads what CM slices into Per-Step Brief |

## File index (with descriptions + agent relevance)

### 01_about_me — Identity layer
| File | Path | What it is | Agent relevance |
|---|---|---|---|
| the operator Resume | `01_about_me/the operator Resume.txt` | Professional background | CD (positioning); CM (Brief authoring) |
| Tone of voice v2 | `01_about_me/Tone of voice_v2.md` | THE voice doc — register, sentence patterns, banned words | Brand Manager (every asset); CM (Brief voice slice); Producer (via CM slice) |

### 02_core_business_philosophies — THE playbook layer
| File | Path | What it is | Agent relevance |
|---|---|---|---|
| Soundtrak Playbook | `02_core_business_philosophies/Soundtrak_Playbook.md` | Principles 1-10: brand vs performance, journey-as-system, outcomes-trump-intent, etc. | CM + CD (every campaign); Brand Manager (principle alignment) |
| Soundtrak Playbook Details | `02_core_business_playbook/Soundtrak_Playbook_Details.md` | Extended detail per principle | On-demand when CM/CD needs deeper context |
| Extended Principles 11-24 | `02_core_business_philosophies/extended_principles_11-24.md` | Principles 11-24: research-as-moat, founder-as-brand, evidence-beats-assertion, etc. | CM + CD (every campaign) |
| Marketing Playbook | `02_core_business_philosophies/Marketing Playbook.txt` | Operational playbook layer | CM (Plan authoring) |
| Core Marketing Capabilities Framework | `02_core_business_philosophies/Core Marketing Capabilities Framework.txt` | the operator's capability model | CD (scoping); CM (gap detection) |
| UX Design Fundamentals | `02_core_business_philosophies/UX Design Fundamentals.txt` | the operator's UX-design principles | Producer (for web/landing assets) |
| Work Values | `02_core_business_philosophies/Work Values.txt` | What the operator values in collaboration | CM (operator-handoff design) |
| Case Studies | `02_core_business_philosophies/Case studies.txt` | Real prior case studies the operator has run | CD (concept evidence); CM (case-study sourcing) |

### 03_Business_influences — Reference-frame layer
| File | Path | What it is | Agent relevance |
|---|---|---|---|
| LinkedIn Company Followers | `03_Business_influences/Linkedin Company Followers.txt` | Companies the operator follows | Signals the operator's reference frame (CD moodboards) |
| Podcasts subscribed | `03_Business_influences/Podcasts subscribed.txt` | Podcasts the operator listens to | Signals the operator's taste reference (CD) |
| Substack newsletters I follow | `03_Business_influences/Substack newsletters I follow.txt` | Newsletter influences | Signals the operator's writing/format reference frame |

### 04_Personal-interests_cultural_influences — Cultural layer
| File | Path | What it is | Agent relevance |
|---|---|---|---|
| Business Book Inventory | `04_Personal-interests_cultural_influences/Business Book Inventory.md` | Books the operator has read + key takeaways | CD (intellectual reference frame); CM (concept attribution) |
| Professional library analysis | `04_Personal-interests_cultural_influences/professional_library_analysis (with background info).md` | Analytic layer over library | On-demand for deep concept work |
| AB Kindle Library | `04_Personal-interests_cultural_influences/AB Kindle Library (less business books).txt` | Personal reading layer | Cultural reference only |

### Working folder — Origin material (operator-only; agents skip)
Brain-dump transcripts, voice recordings, raw research. NOT for direct agent consumption — this is the raw material the operator used to curate the Knowledge Base. Agents read the curated layer above; the Working folder is operator-only reference.

## Ingestion discipline (rules of engagement)

1. Agents read the index first, then the specific files relevant to the task.
2. CM is the librarian: in Per-Step Briefs, CM pulls slices from playbook files and attributes them inline (*"per Tone of voice_v2 §1 — Argues through contrast, not assertion"*).
3. Producer does NOT load the playbook directly — operates only on CM's sliced briefs.
4. Brand Manager reads Tone of voice_v2.md for every voice verdict.
5. Brand Manager + CM cite the playbook principle in verdicts where a discipline rule is being applied.
6. The playbook is a UNION with per-tenant Brand Context — both apply. Tenant Brand Context covers tenant-specific brand voice/visual/positioning; the playbook covers the operator's marketing philosophy + practice principles. They don't conflict; they layer.

## Version management

the operator updates files in the Digital Twin Knowledge Base at any time. When the operator adds a new file OR materially restructures a file:
1. the operator flags to CM ("I've added X to my playbook")
2. CM updates `operator/the operator/index.md` to include it + assign agent relevance
3. CM increments the index version
4. Brand Manager + CD + CM re-read on next session

CM does not need to re-read the playbook every turn — only on Phase 1 (when Brief is being authored), Phase 2 (when concepts are being authored), or when an asset's Per-Step Brief is being authored.

## Per-campaign overrides

`operator/the operator/overrides/<campaign-slug>.md` — optional. Used only when the operator wants to deviate from the playbook for a specific campaign (e.g. "this campaign tests a more aggressive register than my normal voice doc allows"). Override file lists the specific principles being deviated from + the reason. Captured at Brief stage; applies for that campaign's lifetime.

If no override file exists for a campaign, the full playbook applies.
