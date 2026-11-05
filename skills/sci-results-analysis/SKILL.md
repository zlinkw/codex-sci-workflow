---
name: sci-results-analysis
description: SCI result analysis and evidence update. Use ONLY when the user asks to inspect completed experiment logs metrics tables statistical tests mean standard deviation p values ablations sensitivity results inference time GFLOPs parameters memory throughput or failure cases. Do not use for literature search or drafting prose unless the task depends on analyzed results.
---

## Execution constraints

Follow the active global progress/remaining-time, evidence and authorization requirements. Keep updates concise and parallelize independent reads/checks; serialize shared state, dependent writes and live operations. Do not expose hidden reasoning, automatically delegate to another AI, or trade required verification for speed.

# SCI Results Analysis

Convert raw experiment outputs into defensible evidence.

## Analysis workflow

1. Resolve the actual project contract, then locate existing logs, tables, configs, seeds, datasets, and checkpoints. Reuse known endpoints and comparisons; ask only about genuinely unresolved analysis scope.
2. Check that runs are comparable.
3. Compute or verify summary metrics.
4. Report mean and standard deviation when repeated runs, folds, or cases exist.
5. Run or recommend statistical tests for key comparisons.
6. Inspect ablations and sensitivity analysis.
7. Check efficiency values such as inference time, GFLOPs, parameters, memory, and throughput.
8. Identify failure cases with concrete examples and likely causes.
9. Update existing evidence/result records at the actual documented locations when authorized evidence changes. A paper-only analysis keeps findings in its existing review/local comments; it does not create research directories or Markdown trackers.

## Formal result artifact contract

Separate final outcomes from process artifacts using the current project's documented contract. Inspect available context before asking about final endpoints or comparisons; do not rediscover settled choices or treat an arbitrary discovered file as an official result.

Only for a project whose contract requires paired reports under `experiments/results`, use its family naming, for example:

- Baseline: `baseline.csv` + `baseline.md`.
- Overall cross-experiment result: `final.csv` + `final.md`.
- Comparison method: `<model_name>.csv` + `<model_name>.md` (for example `dpl.csv` + `dpl.md`), never a generic `comparison` prefix.

Under that paired-report contract, the Markdown reproduces the complete CSV table and states scope, seed aggregation, endpoints, key findings, CSV SHA256, and interpretation limits; refresh the affected pair and aggregate when needed. Other projects retain their actual schema and result locations. Do not create duplicate machine tables/reports, impose this example on a new paper workspace, or regenerate unaffected files. Historical logs, searches, previews, and diagnostic tables remain audit evidence rather than formal results.

A Markdown report may embed a same-prefix image asset for a required curve or comparison figure. Such an image is a visualization of the formal table, not an additional result table or report.

## Evidence categories

Use these labels in the existing canonical evidence record (`paper/claims.md` when the actual project uses it):

- `supported`: evidence directly supports the claim.
- `weakened`: evidence is mixed or weaker than expected.
- `refuted`: evidence contradicts the claim.
- `needs experiment`: no adequate experiment exists.
- `unsupported`: claim is stated without evidence.

## Statistical caution

Do not claim significance without a valid test or explicitly justified alternative. If assumptions are unclear, state the uncertainty and recommend the test or additional runs needed.
