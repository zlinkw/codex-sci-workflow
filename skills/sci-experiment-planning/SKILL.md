---
name: sci-experiment-planning
description: SCI experiment and reproduction planning. Use ONLY when the user asks to design experiments, reproduce a baseline, plan ablations, plan sensitivity analysis, define metrics, choose statistical tests, prepare commands configs seeds datasets hardware or acceptance criteria. Do not use for analyzing already completed results unless new experiments must be planned.
---

## Execution constraints

Follow the active global progress/remaining-time, evidence and authorization requirements. Keep updates concise and parallelize independent reads/checks; serialize shared state, dependent writes and live operations. Do not expose hidden reasoning, automatically delegate to another AI, or trade required verification for speed.

# SCI Experiment Planning

Plan experiments so they can be reproduced, audited, and converted into paper evidence. Resolve the actual project root and documented contract first; a paper-only request does not initialize a research repository or new Markdown trackers.

## Planning checklist

Define:

- Goal
- Hypothesis
- Dataset and split
- Baselines
- Metrics
- Config path
- Command
- Hardware
- Available GPU count, memory per GPU, expected GPU memory per job, and the maximum safe concurrent job count
- Planned job count after expanding cases and seeds; identify serial preparation, parallel branches, and final aggregation
- Random seed
- Expected outputs
- Acceptance criteria
- Failure risks
- Evidence files to update
- Result destinations and publication format from the actual project contract. Use paired `<family>.csv`/`<family>.md` reports and baseline/final/model names only when that project requires them, not as a universal writing rule.
- In research-managed projects, write official run plans under `experiments/plans/**/*.yaml` with the required config before API validation, dry run and execution. A project's documented `tmp/` draft buffer or promotion approval remains applicable where actually required; it does not replace the official plan location or invent new approval steps.
- Reuse existing code, preprocessing entrypoints, configs, and plans; express fine-grained variants through parameters, overrides, or cases. Planning does not authorize cleanup; use the separately applicable exact-scope cleanup rules for a requested cleanup.

## GPU scheduling and dependent phases

- Before publishing a PLAN, expand its cases and seeds and compare runnable jobs with the available GPUs. If a single case trains independent variants sequentially, first look for a faithful split into concurrently schedulable jobs. Maximize safe GPU occupancy without changing data access, random seeds, metrics, physical batch size, or selection rules merely to create jobs.
- Draw the dependency boundary explicitly. Shared data preparation, classifier fitting, or candidate selection runs once; independent method branches consume immutable, fingerprinted preparation artifacts; aggregation starts only after all required branches succeed. Use separate phase PLANs when the scheduler has no verified cross-case dependency support. Never assume that adding cases establishes a dependency or that a downstream job can safely read partially written outputs.
- Give each parallel job its own checkpoint, logs, result files, and writable directory. Share only read-only artifacts and stable inputs. Record input fingerprints, branch identity, seed, split, configuration, and code version; fail on missing, stale, mismatched, or incomplete dependencies. Publish a completion marker only after an artifact set is fully written and checked.
- Estimate GPU memory with the configured physical batch and actual model variants before scheduling concurrency. A free GPU is not a reason to lower batch size, add gradient accumulation, train unused variants, or duplicate shared work. Document any unavoidable idle phase and the expected number of simultaneous GPU jobs.
- Require the SimpleExperiment plan validation and dry run before execution. For dependent phases, validate each PLAN and explicitly state their order and expected artifacts. Report observed scheduler concurrency separately from planned job count; if fewer GPUs run than expected, inspect the plugin's worker/GPU assignment rather than inventing extra experimental seeds.

## Required experiments for all papers

Before treating any experimental section as complete, check:

- Mean and standard deviation when repeated runs, folds, or cases exist.
- p value or another justified statistical analysis for key comparisons.
- Hyperparameter sensitivity analysis for important tunable parameters.
- Failure case analysis with concrete examples and likely causes.
- Limitations, even if brief.
- Efficiency results when relevant, including inference time, GFLOPs, parameter count, memory use, or throughput.

If any item is missing, record `missing experiment` or `missing analysis` in the existing project evidence record under its actual contract. In a paper-only workspace, use the existing canonical review state or relevant paragraph comments; do not create `paper/claims.md`, `reviews/self-review.md` or another tracker merely to satisfy this checklist. Planning does not establish evidence or authorize execution; use the required SimpleExperiment/SimpleSFTP skills and live APIs for actual runs/transfers.

## Reproduction rules

- Prefer exact paper settings before improving them.
- Record deviations from the original paper.
- Separate reproduction failure from method failure.
- Keep environment, dependency, checkpoint, and dataset assumptions explicit.

