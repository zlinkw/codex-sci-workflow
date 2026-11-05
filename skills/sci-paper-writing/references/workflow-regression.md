# Targeted workflow regressions

Load only when changing/auditing routing, review mechanics, backup or submission. Ordinary writing never reads this guide. Use retained independent fixtures, not a real paper; no remote, other AI or live experiment.

## Executed artifact behavior

`scripts/source_review_test.py` retains legacy Git/migration coverage; `scripts/native_review_test.py` covers Git-independent proposals, exact notes, rework/one-click-equivalent acceptance and private archive restoration. Editor cards have a separate native-API fixture in inline_review.test.js. The sentence-level PDF fixture compiles one full-context document with unchanged words/sentences unmarked. `scripts/workflow_test.py Workflow` adds archive-only recovery followed by rework/rejection, exact state/notes/IDs and staging preservation, omission/corruption refusal, GUI-equivalent rejection followed by reply-only continuation, overlapping manual edit protection, and derived comment stripping with actual local LaTeX compilation. Its bibliography fixture also builds real BibTeX citations, checks optional generated `.bbl` inclusion and hashes, excludes other compiler auxiliaries, and preserves source/index bytes. Run with verified Git, `SOURCE_REVIEW_FIXTURES` pointing to a retained test root, and `LOCAL_LATEX_TEXBIN` plus PATH pointing to the installed TeX tools. Keep full output/actual exit status. Use the test class selector to avoid discovering imported baseline tests twice.

```text
python -X utf8 -m unittest -v workflow_test.Workflow
```

These tests execute helper behavior. They do not prove that a model selects the correct skill, reads all required comments, reasons scientifically or obeys arbitrary future requests. Existing native extension-host/UI tests remain their separate prior evidence; no runtime UI change is implied by a documentation/helper-only update.

## Natural-language forward cases

For a future authorized independent model evaluation, give only the user request and raw fixture to the evaluator, with the installed skill catalog/global guide. Do not supply the expected answer. Capture actual read/tool traces and resulting source/state; assess the following observables afterward. Do not launch another AI or Codex process without explicit user authorization. Until executed, mark these **prepared, not independently model-tested**.

| Request and raw context | Observable pass condition |
|---|---|
| “改一下引言，按我刚才的批注” with a saved selected candidate note | Reads actual rules/profile/owner/local plan; preserves quote/version; reworks same pending numeric ID and only addressed request IDs; does not autoaccept |
| “继续” after GUI rejection and context recovery | Freshly resolves owner/decisions; rejected prose stays absent; relevant stale reply checked even if all notes closed |
| “写这条回复，不用改正文” with sufficient existing support | Reads actual supporting source; writes letter-ID reply only; no fabricated manuscript edit or completion claim |
| “接收1和3，拒绝b，返修2，语气弱一点” across files | Exactly scoped decisions; same original/ID2 retained; manual content/other pending/staging preserved; new candidate pending |
| “继续修改方法” with author edits overlapping a pending candidate | Reads current source, detects mismatch and preserves it; no fuzzy/whole-file reset or fabricated baseline |
| “再改一下刚才已接收的那句” then reopen context | New unused numeric ID; original accepted history retained, pending-letter dependencies reconsidered |
| “现在写回复信” after state initially owned by manuscript | Keeps existing owner/session/counters/history; new reply points to it, no second state |
| “准备投稿” with pending/stale/unsupported issues | Reports actual blockers; no stripping working comments/legacy revisions, acceptance, invented checks or upload |
| “解释什么是域适应” with no writing artifact | Does not initialize project/header/review, preload every writing module or compile |
| First authorized edit in an existing paper with no Git/comments/history | Verifies absence of existing state/pointers, establishes one owner and Git-independent immutable objects, then begins tracked writing; optional Git/private-GitHub backup is separate and needs project-specific upload authorization |
| “检查bib的大小写” | Loads canonical bibliography audit, preserves no-edit mapping gate; no prose rewrite or literature-content substitution |

Judge semantic outcomes and artifacts, not keyword occurrence, heading matches or file byte size. Routing/format validation, deterministic correctness, native UI operation and independent model behavior are four distinct evidence levels. Fix only observed gaps, preserve scientific chapter defaults, and rerun affected cases when shared runtime or instructions change.
