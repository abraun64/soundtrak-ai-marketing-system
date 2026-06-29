# Soundtrak Voice — Sub-Edit Rules

These are the five rules applied on every sub-edit pass. Run them in order.
Flag every violation. Fix every violation before saving the file.

---

## RULE 1 — EM-DASHES (near-zero)

Default: **no em-dashes (—).** Replace every one with a comma where the sentence breathes.
*Calibration (the operator's lived edits, 2026-06):* keep an em-dash **only** where a comma would
create genuine ambiguity, or where the structural pause is genuinely load-bearing. In practice
almost all body em-dashes become commas — a kept em-dash should be rare and defensible.

**Fix:** Replace with a comma as the default. Use a regular hyphen only for a true compound word.
Flag any em-dash you keep, with the one-line reason it's load-bearing (in the Step 5 report).

---

## RULE 2 — BANNED WORDS AND PHRASES

Flag any occurrence of the following. Delete or rephrase — never keep.

### AI vocabulary
delve, delving, tapestry, intricate, intricacies, interplay, foster, fostering,
garner, garnering, underscore, underscores, pivotal, showcase, enduring, realm,
multifaceted, robust, seamless, seamlessly, holistic, leverage (as a verb),
unlock, unlocking, transformative, transformation (used loosely), game-changer,
game-changing, synergy, synergies, ecosystem (unless a literal biological or
technical ecosystem), curate, curated (unless actual curation is being described),
navigate (as a metaphor — "navigating challenges", "navigate the landscape")

### Banned words added by the operator
genuinely, honestly (when used as a filler — "honestly, this is...")

### Padding phrases
"It's worth noting that", "It's important to remember that",
"Highlighting the importance of", "Plays a crucial role in",
"This further underscores", "In today's rapidly evolving landscape",
"In an ever-changing world", "At the end of the day",
"It goes without saying", "Needless to say", "First and foremost",
"I wanted to reach out", "Hope this finds you well",
"Look forward to connecting", "Hope to hear from you"

### Structural AI tells
- "Not only... but also..." — delete the whole construction
- "From X to Y" used vaguely ("from ancient wisdom to modern innovation")
- The automatic rule of three ("speed, efficiency, and innovation") — only when there are genuinely three distinct things
- "In conclusion...", "To summarize...", "Overall..." — if the point has been made, stop writing
- "Let's walk through...", "Below is a detailed overview...", "In this section we will explore..." — meta-commentary; just say the thing
- "It is important to note that..." — if it's important, it doesn't need to announce itself

---

## RULE 3 — PUNCHY FRAGMENT PATTERN

Two distinct AI rhythm tells. Both must be flagged.

**3a — The reframe pair:**
- "Not X. Not Y."
- "That's not X. That's Y."
- "Most X are Y. Yours is Z."
- Any pair where the second sentence exists solely to reframe the first as a dramatic standalone conclusion.

**3b — The staccato parallel series:**
Three or more consecutive short sentences (under ~50 characters each) built on the
same grammatical pattern. Classic form: "Same X. Same Y. Same Z. Different outcome."
Also flagged: "No X. No Y. No Z." / "More X. Less Y." repeated three or more times.
This pattern creates fake drama through repetition rather than through an actual idea.

**Limit (calibrated to the operator's lived edits, 2026-06 — the short sentence is a deliberate Soundtrak device, not a banned tell):**
- The short-sentence / reframe technique (3a) is **permitted but rare: one per piece, two absolute max**, and only if the two serve **different argumentative moments**. It lands precisely *because* it's rare — at 3+ it becomes a mannerism and loses all force. This applies across forms (LinkedIn and Substack alike).
- The **3b mechanical staccato series** (3+ identical-pattern fragments in a row, "Same X. Same Y. Same Z.") is still **never permitted** — a single such series already counts as the overuse the rule guards against.
- Named §2 voice devices (e.g. the four-word declarative "That's the Trailer. This is the Playbook.") count toward the 1-2 budget but are not auto-stripped — they're the device working as intended.

**Fix:** Absorb the contrast into a single longer sentence, then let a short sentence
land the point. Pattern: longer setup → short landing.

Examples:
- Before (3a): "Structure and flexibility aren't opposites. Agile makes them the same system."
- After: "Running at two speeds means structure and flexibility stop being opposites, with the sprint handling adaptation and the strategy holding direction."

- Before (3b): "Same broadcasting window. Same advertising inventory. Same viewers. Different outcome."
- After: "It ran in the same advertising break as a dozen other spots, to the same audience, with the same reach."

---

## RULE 4 — RESTATEMENT

Flag any sentence that restates or summarises the sentence immediately before it
without adding new information.

**Test:** Could you delete the second sentence without losing any meaning not already
present in the first? If yes, delete it.

**Common forms:**
- "X is important. Without X, Y suffers." (if "Y suffers" was already implied)
- "We built four newsletters. These newsletters grew our subscriber base." (when the
  implication was obvious)

**Fix:** Delete the restating sentence. If both halves carry distinct information,
merge them into one sentence.

---

## RULE 5 — RECAP CLOSING

Flag any final paragraph (last paragraph of the piece) that summarises or recaps
the argument rather than ending on the point itself.

**Test:** Does the closing paragraph restate the key ideas from earlier in the piece?
If yes, it is a recap and must be cut or rewritten.

**What the closing should do instead:**
- Land on the sharpest version of the point
- End on an image or implication that makes the reader sit with it
- Or end on a question worth sitting with (LinkedIn only — Substack earns a statement)
- If the case has been made, stop writing

**What it should never do:**
- Restate the article's argument in summary form
- Use "In conclusion...", "To summarise...", or any variant
- Repeat the article's structure as a final beat ("strategy for direction, sprints for momentum")

---

## HOW TO RUN THE SUB-EDIT

1. Read the full content of the file.
2. Work through Rules 1–5 in order. For each rule, list every violation found.
3. If violations exist, fix them in the content.
4. Check that fixes haven't introduced new violations.
5. Report: number of violations found per rule, what was changed, and the corrected text.
6. If the content was generated via a Python script, update the script with the corrected text
   and re-run it to overwrite both _Original and _Edit files.

---

## CHANNEL-SPECIFIC SUMMARY

| Rule | Substack (long) | LinkedIn (medium) |
|------|----------------|-------------------|
| Em-dashes | Near-zero (keep rare load-bearing) | Near-zero (keep rare load-bearing) |
| Banned words | Zero | Zero |
| Punchy / short-sentence technique | 1 per piece (2 max) | 1 per piece (2 max) |
| Mechanical staccato series (3b) | Never | Never |
| Restatements | Zero | Zero |
| Recap closing | Not permitted | Not permitted |
