# Durable source review mechanics

Load only the needed operation details. [review-round.md](review-round.md) owns workflow; [review-ui.md](review-ui.md) owns current editor/PDF controls.

## Storage and versions

New state uses schema 2 and immutable content-addressed JSON objects under .codex-review/objects. Each stores scoped baseline/source or original/candidate excerpts with contextual anchors. The sole editable state remains the embedded CODEX-REVIEW-DATA line in its actual .tex owner, not a second JSON/Markdown tracker. Object IDs identify exact versions; line numbers are navigation only. Missing/corrupt required objects block operations. Do not fabricate baselines, reuse IDs within a live batch, prune active history outside an explicit new-batch replacement or the approved checkpoint lifecycle or upload private objects automatically.

The fixed round baseline captures actual scoped source, including manual edits. accepted_start and accepted preserve the accepted projection; manual changes after the boundary are not silently accepted. Pending deferred candidates remain outside real prose until the author explicitly accepts. Git/HEAD/index/remote are not required for ongoing review. Normal successful-result checkpoints exclude .codex-review and runtime DATA. After verified push use the [accepted-result lifecycle](local-writing-setup.md#accepted-result-checkpoints) to compact finished state, while retaining all data required by active items. Closed candidate history is not an indefinite retention requirement.

Schema-1 Git-backed records are legacy. While their original objects remain available, migrate --defer-pending converts them to local objects and restores pending original spans using exact matching, retaining session/counters/IDs/requests/history. Do not discard old Git history. Missing objects/manual overlaps stop migration. Compatibility read/display helpers are not the current UI.

## CLI

```text
python -X utf8 <skill>/scripts/source_review.py --project <real-root> --state <relative-owner.tex> status
python -X utf8 <skill>/scripts/source_review.py --project <real-root> --state <relative-owner.tex> begin --round <unique-name> --files <main.tex> <child.tex> <reply.tex>
```

Preview first when determining exact writes. For already-authorized apply add global --apply --expect <current owner SHA256>. Pass UTF-8 JSON through stdin for propose, rework and feedback; do not create a project spec/tracker file. --repo remains an alias; --git is needed only for legacy storage conversion.

- propose: file, kind=manuscript/response, exact before/after, optional left/right anchors, location and deps. New native proposals and CLI proposals require deferred=true; explicit false is rejected, not an alternative writing mode. Existing legacy records remain readable. Original source is not patched.
- New native items receive scope_policy=single-unit. Both preserved original and candidate must satisfy the scope boundary in review-round.md; later rework of those items uses the same check. A rejected oversized proposal consumes no ID. Existing broad records without that policy remain readable and keep history; do not invent a split or renumber them during display.
- inspect --id <ID> [--version <immutable ID>] --source returns immutable original/candidate, token differences, source match, actual source text and Unicode code-point offsets, including owner-header offsets.
- A compacted dependency-only ID returns archived=true and its Git checkpoint locator, not fabricated original/candidate text. Fully retired IDs no longer occur in live state; use successful-source Git history, not the old candidate object, for retrospective reading.
- feedback: id, version, side=original/candidate, start, end, quote, text. Offsets/quote must match that immutable generation.
- rework --id <same ID>: after; add discard_annotations=true when replacing a pending candidate and its disposable old notes for renewed review. No prior accept/reject is required. Preserve first original/ID; never target accepted prose. resolve_requests is an alternative for explicitly retained notes, not a requirement and not combined with discard_annotations.
- link-questions --id <ID> --version <latest version>: UTF-8 stdin {"questions":[{"id":"R1-Q3","file":"reply.tex","quote":"exact full original question"}]}. Default append/deduplicate; explicit --replace replaces the full association set. Same preview/apply/expect and writer lock; only questions changes, never versions/counters/notes/decisions/dependencies/freshness. Exact source and version/concurrency checks must succeed; no automatic pairing or project mapping file.
- feedback-context is read-only and exports the review ID, file, note generation and current generation, complete immutable original/candidate and selected author notes, so Codex need not hunt for their context.
- decide --accept 1 3 --reject b applies only named IDs. GUI also supplies --version to prevent deciding unseen revisions. Acceptance replaces exact live original with candidate; rejection leaves original unchanged. Neither touches staging/commits.
- recover previews the sole state's interrupted transaction; --apply --expect performs exact-byte recovery only.
- migrate --defer-pending previews legacy conversion. Apply only within authorized actual review work and with intact objects/source.
- show --id retains read-only excerpt data for inspection. The old --code window launch is deactivated; use original-editor cards for actual review.

## Source integrity and scope

Exact text plus contextual anchors tolerate unrelated line drift and independent decisions. Preserve other pending work/manual edits and all Git staging. An edited or formatted span/context that no longer matches must be reconciled, not fuzzily replaced. Rework a pending location instead of stacking overlapping IDs.

New/substantively rewritten prose is one sentence per source line. Manual Ctrl+Alt+L only adjusts eligible indentation, retains existing line boundaries, nonleading content, comments/literals/BOM and needs no Git. It never accepts a candidate. Optional separately requested Git checkpoints remain backup operations, not a writing dependency.

Real paper files remain the source of truth. Original/candidate cards review wording; the single full-document positional PDF shows pending changes in context without modifying the real paper. Normal compiled PDF checks actual layout. Do not use Git discard/stage or display artifacts as author acceptance.
