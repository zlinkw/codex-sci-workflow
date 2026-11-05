---
name: sci-paper-review
description: Review scientific manuscripts, claims, experiments and consistency, including medical-imaging CLAIM reporting checks. Automatically handle 论文自审、模拟审稿、检查图文一致性 and critique requests. Author replies and final prose drafting use sci-paper-writing; discovery and experiment execution retain their own workflows.
---

Follow the current global progress, timing, parallelism and evidence rules. No silence-only override or automatic delegation applies.

# SCI Paper Review

Use a code review style for manuscripts and experiments. Findings come first, ordered by severity.

## Manuscript consistency and pending revisions

Resolve the actual manuscript/include graph, CODEX-RULES, relevant local plans and the existing unique CODEX-REVIEW-STATE. When tracked readings matter, use the current writing skill's review-round.md; actual manuscript/reply reconciliation additionally uses review-consistency.md. Clean real source with immutable per-round baselines is the default. Judge accepted and candidate readings separately; existing colored marks are legacy or explicit opt-in, never silently removed or accepted. A critique authorizes neither rewriting nor experiments. Reference templates guide structure, not research facts. Do not create paper Markdown trackers or duplicate state.

Locate each consequential finding in the real manuscript and evidence, explain the mismatch and its implication, then give the smallest useful correction and a verification method. Separate critical/major/minor findings from optional presentation suggestions. Missing material is unavailable/not reported, not automatically disproven. Reporting completeness, scientific validity, author acceptance and editorial decisions are different judgments. Do not manufacture findings or acceptance predictions. For external peer review, apply the real venue's confidentiality/AI policy; self-review needs no invented editor-intake process.

For medical-imaging AI self-review, reviewer assessment or requested submission checks, load [CLAIM review](references/claim-review.md). Ordinary polishing does not trigger the entire checklist. Check changed model diagrams against their actual source and existing manuscript bindings. Dedicated drawing skills are not bundled here. Real response precedents use [ReviewSearch](../sci-paper-writing/references/review-precedents.md). This implies no additional writing AI or automatic experiment execution.

## Review priorities

Prioritize:

- Unsupported claims
- Missing baselines
- Data leakage risk
- Metric misuse
- Unfair comparisons
- Missing mean and standard deviation
- Missing p values or statistical analysis
- Missing hyperparameter sensitivity analysis
- Missing failure case analysis
- Missing limitations
- Missing inference time, GFLOPs, parameter count, memory, or throughput when relevant
- Inconsistent terminology
- Tense and style violations

## Tense and style

Review findings may use past tense. For requested manuscript suggestions, the current writing skill and author rules own style. Preserve official names/acronyms and scientific qualifiers; the following are reminders, not a separate style authority:

- Avoid uppercase module names except headings and fixed names.
- Avoid hyphens, underscores, and dashes in prose unless required.
- Avoid filler.
- Avoid unnecessary colons and parentheses.
- Avoid ambiguous sentence initial `This`.
- Avoid point by point summaries except contribution lists after the introduction.

## Output shape

For review requests, lead with findings. Include file or section references when available. Add open questions only when they block a defensible conclusion.

Report the inspected scope, unavailable evidence and unrun checks. The location/evidence/action pattern is informed by [K-Dense peer-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md); do not import its separate tracker/intake pipeline or compulsory service setup.

