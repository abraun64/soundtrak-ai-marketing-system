---
name: render-html
description: Convert markdown artifact + template type → HTML file in the same folder. Invoked by Campaign Manager after every markdown write (Brief, Brand Context, Concept, Plan, Per-Step Brief, Asset, Dashboard, Tasks, Index). Single source of truth for the operator-facing UI. Wraps `render.py` which uses Python + the `markdown` library (one-time `pip install markdown`). Templates live in `.claude/skills/render-html/templates/`. Triggers include "render the brief", "regenerate dashboard HTML", or any CM workflow step that writes markdown.
---

# Render HTML

You convert a markdown artifact into a rendered HTML view for the operator. This is the **only** path by which markdown becomes HTML in this system. CM invokes you on every artifact write; you produce the HTML; CM tells the operator the `file:///` URL.

## When you're invoked

CM invokes you with:
- `markdown_path`: the source markdown file
- `template`: which template to apply — one of `brief` / `concept-trio` / `plan` / `asset-preview` / `dashboard` / `tasks` / `index` / `brand-context`
- `output_path` (optional): where to write the HTML (default: same folder, same basename, `.html` extension)
- `extra_context` (optional, asset-preview only): JSON object describing in-situ mockups (see below)

## extra_context contract (asset-preview only)

When the asset is a feed/inbox/scroll-state form, supply `extra_context` so the renderer can produce the **collapsed + expanded** dual-view per docs/specs/per-step-brief.md §9. If `extra_context` is omitted or `form` is missing, the mockup zone is empty and the markdown body renders alone.

```jsonc
{
  "form": "linkedin-post" | "email" | "twitter-post" | "instagram-post" | "substack-feed",

  // Variants: 1 entry for single-asset; multiple for A/B (e.g. Shape B vs Shape C).
  // If omitted, top-level keys are treated as the single variant.
  "variants": [
    {
      "label": "Shape B — argument-only",      // optional; shown above the variant pair
      "post_path": "shape-b/post.md",          // OR "post_text": "raw inline body…"
      "tile_path": "shape-b/tile.png",         // relative to markdown_path's folder
      "tile_alt": "Trailer tile — Issue 11",
      "collapsed_chars": 220                   // optional override; defaults per-form
    }
  ],

  // Form-common fields — for linkedin-post / twitter-post / instagram-post:
  "author": "the operator",
  "author_title": "CMO-in-a-box · Soundtrak",
  "author_meta": "7:30am · Tuesday · 🌐",
  "author_initials": "ab",
  "author_handle": "@operator",             // twitter / instagram
  "reactions": { "count": 47, "names": "Mark Tonks, Sasha Petrov" },
  "comments_count": 14,
  "comments": [
    { "author": "Mark Tonks · CMO @ Finova", "body": "…", "meta": "2h · 8 likes · Reply" }
  ],

  // Form-common fields — for email:
  // (variants[].subject + variants[].preview_text + variants[].body_path live in the variant)
  "from_name": "the operator",
  "from_email": "the operator@soundtrak.com",
  "from_initials": "AB",
  "sent_date": "Tue 10:30am",

  // Form-common fields — for substack-feed:
  "publication": "The Signal"
}
```

**Post body resolution**: `post_text` inline wins, else `post_path` (or `body_path` for email) is read. Files that begin with a `# heading` followed by a `---` separator have that header stripped automatically (so author annotation in `post.md` doesn't leak into the mockup).

**Default collapsed-state cutoffs** (override per variant with `collapsed_chars`):
- linkedin-post: 220 chars
- twitter-post: 280 chars
- instagram-post: 125 chars
- email: 90 chars (inbox preview snippet)
- substack-feed: 180 chars

**Tile paths** are resolved relative to the markdown file's directory — same as the markdown's own `![](…)` references.

**Layout**: each variant renders a 2-column grid (collapsed | expanded) above the markdown narrative. Mobile collapses to 1 column.

## What you do

1. Read the markdown file
2. Convert markdown body to HTML using `python -m markdown` (requires `pip install markdown` — operator one-time setup)
3. Wrap in the template specified
4. Inject any per-tenant CSS variables (palette, fonts) if applicable
5. Write the HTML file to the output path
6. Return the file path

## Implementation

Run the script:

```bash
python .claude/skills/render-html/render.py \
  --markdown <markdown_path> \
  --template <template_name> \
  --output <output_path> \
  [--extra-context '<json>']
```

The script is self-contained — it handles markdown conversion, template wrapping, and writes the output.

## Templates available

| Template | What it renders |
|---|---|
| `brief` | Phase 1 Brief — 1-page operator-facing summary |
| `brand-context` | Durable tenant Brand Context record |
| `concept-trio` | Three concepts side-by-side for operator comparison + pick |
| `plan` | Phase 3 Plan — asset list table + scope check + budget |
| `asset-preview` | Finished asset in in-context mockup (LinkedIn post / email / landing page / etc. per form) |
| `dashboard` | Per-campaign live state (waiting actions, KPI, budget, next 7 days) |
| `tasks` | Cross-campaign review queue (Awaiting Your Approval + Awaiting Publish) |
| `index` | All active campaigns at a glance |

## Styling

- **System UI** (dashboard, tasks, index, plan): clean-default-minimal — system fonts, generous whitespace, Stripe/Linear aesthetic. Lives in `templates/styles/system.css`.
- **Tenant-branded** (asset-preview): per-tenant palette + fonts loaded from Brand Context. Tenant CSS variables injected at render time.

## Setup (one-time)

```bash
pip install markdown
```

That's the only dependency.

## Return envelope

```json
{
  "ok": true | false,
  "skill": "render-html",
  "markdown_path": "...",
  "template": "...",
  "output_path": "...",
  "errors": []
}
```
