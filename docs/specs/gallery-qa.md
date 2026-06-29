# Gallery pre-surface QA — checklist

**Spec version**: v1 · 2026-06-15 (extracted from CM SKILL.md — operator flagged it as "overkill" inline; it's a real check, just not skill-body material).

CM runs this **before surfacing any Phase-4 asset to the operator**. The operator should never be the one who catches a gallery issue — that's CM's job. Read the asset's `asset.yaml` and verify each row against the Plan's **Review shape** + **Copy file** columns.

| Check | Verify | Fix if wrong |
|---|---|---|
| **Status** | `status: "For Human Review"` in asset.yaml | set it (the badge depends on it) |
| **Rationale** | `rationale:` written (1–3 sentences: what it is + why) | write from the Plan asset description (gallery modal shows it first) |
| **Review-shape match** | files in asset.yaml match the Plan shape — `output` → 1 tile · `template [+N]` → 1 `type: Template` + N `type: Instance` · `variant-comp [N×M]` → N comp tiles, all production instances `ship: false` | fix `type:` + `ship: false` on instances |
| **Copy file** | if Plan Copy file ≠ `none`: `copy_file:` points to an existing file | declare it (operator needs the edit button) |
| **Production file** | binary the operator downloads (PDF/PPTX/DOCX): `production_file:` on the PNG/HTML tile | add `production_file:` |
| **View source** | thumbnail file ≠ shipped deliverable: `view_source:` on the thumbnail entry | add `view_source:` |
| **Tile count** | count expected tiles — `variant-comp [6×4]` = 3–6 comp tiles (NOT 42); `template [+6]` = 1+6; `output` = 1 | `ship: false` on over-tiling files |
| **Scroll check** | any multi-section "View in full" HTML scrolls to the bottom (no `overflow: hidden` on body from copied inner-frame CSS) | add `overflow: auto` to outer body |
| **Deploy instructions** | any HTML web-page asset has a deploy cookbook (`cookbooks/deploy.md` / `deploy.md`) | author one before surfacing |

**Then**: `python .claude/skills/asset-gallery/build-gallery.py --campaign <slug>` and confirm the tile count looks right.

**Automated pre-check (SYS-003)**: `python .claude/skills/asset-gallery/build-gallery.py --campaign <slug> --check` validates the *machine-checkable* rows above — every `ship: true` file (and any declared `copy_file` / `production_file` / `view_source`) exists on disk, each asset folder has an `asset.yaml`, review assets carry a `rationale`, and `gallery.html` is at least as new as the newest ship-affecting file (no stale gallery). It exits non-zero on drift, so CM and the smoke test can gate on it. It does **not** check tile-count vs Review-shape — eyeball that. Worktree-aware (resolves `campaigns/` to the main checkout).

**Re-occurrence policy**: operator catches a gallery issue (wrong tile count · missing download · wrong "View in full" · missing status badge · empty rationale) = **P1 CM process failure**. CM owns this check.

## Cross-references
- `asset.md` — the `asset.yaml` schema (`ship` / `type` / `copy_file` / `production_file` / `view_source`)
- `plan.md` — the Review-shape + Ships + Copy-file columns this checks against
- `.claude/skills/asset-gallery/build-gallery.py` — the builder
