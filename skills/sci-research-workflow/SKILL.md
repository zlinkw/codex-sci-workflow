---
name: sci-research-workflow
description: End to end SCI research workflow coordination. Use ONLY when the user asks for a full research workflow, multi step project coordination, experiment to paper pipeline, evidence tracking across code results and manuscript, or unclear SCI tasks that span planning implementation analysis writing and review. Do not use for isolated literature search, isolated paper writing, isolated result analysis, or ordinary coding tasks when a narrower skill fits.
---

Follow global execution/progress requirements. Parallelize independent reads and keep authorization/evidence boundaries; coordination does not authorize another AI or background writer.

# SCI Research Workflow

Use Codex as the default executor and coordinator.

## Core rule

Do not present an experimental claim as true unless it is linked to evidence in one of these places:

- `experiments/runs/`
- `experiments/results.csv`
- `paper/claims.md`

If evidence is missing, mark the claim as `unsupported` or `needs experiment`.

## Default modes

Choose the smallest suitable mode:

- `plan`: clarify the research question, target artifact, metrics, and risks.
- `implement`: edit code, configs, scripts, and tests.
- `reproduce`: rebuild a baseline or paper result from source details.
- `analyze`: inspect logs, tables, metrics, statistical tests, and failure cases.
- `write`: draft manuscript text grounded in existing evidence.
- `review`: critique method, claims, experiments, and writing.
- `literature`: search and extract focused paper information from primary sources.

## Preferred sequence

1. Define the question, artifact, acceptance criteria, and evidence needed.
2. Make scoped code or paper edits with Codex.
3. Run or specify the relevant verification.
4. Preserve meaningful official run artifacts in the project's documented `experiments/runs/` structure through its required APIs; do not impose a parallel handwritten Markdown run log.
5. Update the existing comparable-metric record, such as `experiments/results.csv`, under the actual project schema.
6. Update the existing evidence/claim record, such as `paper/claims.md`, with supported, weakened, refuted, or missing claims; create no empty records just to follow this sequence.
7. Review unsupported claims, missing experiments, leakage risks, and style issues.

## Local and remote workflow

- Determine the current project's source-of-truth workspace, execution environment, and transfer route from its own documentation and user instructions. Never inherit a donor-machine host or path.
- Before an upload or run, verify the exact host, local source, canonical remote project root, destination, and authorization. Missing or conflicting values stop the operation.
- Use the project's required experiment and transfer APIs. Complete required plan validation, dry run, and confirmation before a live run; do not bypass them with direct SSH or standalone scripts.
- Transfer only stable, scoped files. Never upload secrets, credentials, private keys, environments, caches, checkpoints, or large generated artifacts without explicit need and authorization.

## Research discipline

- Keep changes scoped to the requested experiment or paper section.
- Prefer config driven experiments over hard coded values.
- Keep random seeds, data paths, and hyperparameters explicit.
- Add assertions around tensor shapes, dataset columns, and metric inputs.
- Separate observed facts from hypotheses.
- Do not invent numbers, citations, datasets, baselines, reviewer comments, or implementation details.
- Verify paper, dataset, and library versions when they matter.


## Cross-phase handoffs

This coordinator chooses task scopes; it does not replace narrow scientific skills. Actual manuscript/reply drafting, polishing, logic planning, annotations or acceptance automatically loads `sci-paper-writing` and its global/top/local/state gates, even inside this larger pipeline. Necessary manuscript changes precede replies; supported reply-only clarification does not fabricate manuscript edits. Author decisions, evidence and issue closure remain distinct. Use one canonical review state, not a coordinator mirror.

Route user-focused paper reading/topic onboarding to `sci-paper-reading`, bibliography audits to the canonical `sci-bibliography`, actual discovery/support extraction to `sci-literature-review`, results analysis to `sci-results-analysis`, experiment design to `sci-experiment-planning`, and formal critique to `sci-paper-review`. Load only the current phase and genuine dependencies; this is instruction routing, not delegation to another AI. Experiment/API and project-contract requirements remain unchanged.

The run/results/claims files above belong to an existing research-managed repository under its actual contract. A local paper-only workspace does not acquire new Markdown trackers or an empty evidence pipeline. Keep its global agreements in top comments and local logic before the corresponding prose. For review archive or explicit submission, use the writing skill's conditional module; ordinary Git push is not review-chain backup and submission preparation does not authorize upload.
