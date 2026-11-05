# Review versions and manuscript/reply synchronization

Load when support changes, issue closure is assessed or dependent replies/quotes/locations need rechecking. Reuse the already-read kernel/state and review-round rules; links do not recursively reload modules.

## Versions, state and issue closure

Resolve and preserve the one existing CODEX-REVIEW-STATE owner before considering initialization. Other roots point to it. Only when no state exists, initialize at the existing reply top or otherwise manuscript top within authorized writing. A subsequently created reply does not acquire a fresh state: if relocation is authorized, preserve the session, rounds, immutable object identities, all issued IDs/counters, author decisions, requests and unresolved dependencies, then redirect the other roots to that single owner. Do not leave a second live block. If an old counter resides in CODEX-RULES, reconcile its actual values and issued IDs before moving it into that state; never reset history.

For active reviewer work record:
- **审稿基线:** the actual version submitted for this review, using an existing verified Git commit or real source identity. Missing provenance stays unverified; do not infer “original text” from the latest commit or candidate.
- **已接收基准:** the author's current accepted reading.
- **候选:** the pending revision's proposed reading and exact current-round ID sets.

A clean-source original/candidate diff, or an explicitly selected legacy marked pair, preserves alternatives intentionally. Judge accepted and candidate readings separately, and compare “already present/newly added” claims with the submitted baseline. For a new paper without submitted review, mark the submitted-review baseline inapplicable; do not invent a submission version. Actual pre-round baselines still apply to tracked clean-source revisions.

Each actual issue/subquestion keeps manuscript numeric IDs/locations, reply letter IDs/locations, source/evidence gaps and these separate fields in the same record:
**作者决定（待审/接收/拒绝/返修）｜问题处理（待处理/部分回应/已答复待核对/已解决/有依据不改）｜证据（已核验/待核验/待实验/不适用）｜依赖及核对状态**.
Preserve full reviewer wording in the response body; the state is a compact association, not a second transcript.

In clean mode the per-ID author decision is authoritative in CODEX-REVIEW-DATA; issue records reference those IDs and add issue/evidence/semantic-dependency status rather than copy a second decision table. The next-ID counter is stored once in CODEX-REVIEW-NEXT, not duplicated in that JSON. Preserve the legacy record scheme in an unmigrated colored project.

Accepting wording does not establish scientific resolution. Mark an issue resolved only when every subquestion has an adequate answer or justified non-change, required evidence is valid, linked manuscript changes are in the intended current version, and the response/locations are current. If the intended resolution still depends on unaccepted manuscript/reply edits, keep it answered-pending-check rather than fully resolved. A candidate edit, commit, fluent reply or passed syntax check alone is insufficient.

### Manuscript/reply synchronization

When supporting definitions, passages, results or conclusions change/revert, mark affected replies, excerpts and locations **待重新核对** through actual shared/transitive issue dependencies. Reconcile GUI decisions on the next ordinary writing turn even when no annotation remains open; inspect `freshness=needs-recheck` and actual related source, not only the request queue. A decision button records author choice and registered dependency flags, not an AI check of scientific consistency.

Check the reply's answer, quoted manuscript text and source locations against the exact manuscript ID/generation/accepted-or-candidate reading it describes. Keep the previous author decisions, but do not describe stale accepted reply wording as current. Repair pending reply prose under its existing letter ID; a substantive change to an accepted reply gets a new letter ID and remains pending. Apply the same numeric-ID rule to manuscript repairs. Resolve needed manuscript changes first; a supported response-only clarification or justified non-change needs no artificial manuscript edit. If a narrow scope excludes the required reply repair, retain its stale state and report the specific dependency rather than silently rewriting it or declaring it synchronized.

After actual checks, reconcile the existing canonical dependency fields and record the checked manuscript/reply versions in the same issue record; do not create a second table. A `needs-recheck` flag may become `checked` only through a fresh, scoped metadata update after verification, preserving all author decisions, counters, objects, requests and unrelated records. No active transaction or unknown concurrent change may be overwritten. New source/support changes invalidate that check. Preserve historical records when a new pending ID supersedes an accepted passage; evaluate the current issue-to-ID mapping instead of repeatedly rewriting obsolete versions. Matching the quote alone does not establish evidence sufficiency or issue closure. Formatting-only location changes require relevant locator checks, not an invented change in scientific evidence.

Before each round/context recovery, reconcile state, counters, clean-source records, any legacy marks and current manual edits. Merge/update actual issue rows in place, preserving unresolved dependencies and decisions; distinguish source reviewer numbering from simple edit IDs. Do not prune unresolved issues to save space or duplicate state in multiple roots.

## Checks relevant to the revision

Apply the canonical impact rules to actual changed meaning. Check the affected terminology/symbol definitions, capability/claim strength, source data/statistical context, figure/table labels, exact quotations and manuscript/reply agreement. Keep legitimate differences in populations, subsets and units explicit instead of forcing every repeated number to match.

Mechanical checks of syntax, IDs, quoted text and locations do not establish claim support, experimental sufficiency, author acceptance, a reviewed PDF or submission readiness. Inspect actual evidence for scientific claims; disclose inaccessible sources and unrun rendering. A courtesy edit needs no unrelated equation audit.

