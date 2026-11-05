# Reading workflow sources and MVP options

Setup/provenance only; do not load for every paper. Sources inspected 2026-10-30. Counts/features may change; repository popularity is discovery evidence, not a quality or compatibility guarantee. No external skill/package/connector below was installed as part of creating this skill.

## Practices inspected

- [K-Dense literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md) and [scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md): borrow question-specific retrieval, extract-before-judge, claim/evidence separation and bounded conclusions. Its repository showed about 55.3k stars at inspection. Do not impose PRISMA, full reports, clinical evidence hierarchies, paid generation or other AI on ordinary concept reading.
- [UCL-ERL paper-reading-card](https://github.com/UCL-ERL/skills/blob/main/skills/research/paper-reading-card/SKILL.md): borrow stable identity, source-grounded contribution/evidence/reuse separation and explicit missing information. The author's familiar-topic mode intentionally omits irrelevant full-card fields. Repository adoption was not independently measured; treat it as an inspected design example, not an adoption-based recommendation.
- [Charles-Donne Research-Paper-Skills](https://github.com/Charles-Donne/Research-Paper-Skills): metadata/version-first and Zotero attachment-in-place are useful. Small inspected repository, about 7 stars; not selected as an installed dependency. Reject its mandatory new subagent per paper, hard stop without delegation and multiple note/index outputs, which conflict with this user's single-assistant/lightweight workflow.
- [Zotero Obsidian Paper Reader](https://github.com/zyf4321/zotero-obsidian-paper-reader-skill): useful explicit PDF/figure access and novice explanations, but a full bilingual per-figure vault is excessive for this author's familiar-topic reading. No Obsidian dependency or bulk copying is inherited; adoption not verified.

## Candidate tool routes

| Route | Verified advertised role | MVP judgment |
|---|---|---|
| [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp), [agent/CLI guide](https://github.com/54yyyu/zotero-mcp/blob/main/docs/for-agents.md) | Search/read/notes/annotations via CLI or MCP, local and optional local-write modes; repository about 5.6k stars | Preferred connector candidate for a later small setup. Prefer on-demand CLI/API and no embeddings; inspect the actual installed schema/version. Documentation inspected, not live-tested here |
| [ResearchRabbit importer](https://learn.researchrabbit.ai/en/articles/12796541-using-the-zotero-importer-in-researchrabbit) | Selectively import Zotero collection papers for related-work discovery; export BibTeX back | Optional quick citation-discovery map. The inspected official guide says two-way sync is being developed, so do not promise it already works |
| [Litmaps Zotero sync](https://docs.litmaps.com/en/articles/9421968-sync-zotero-with-litmaps) | Bidirectional selected collection/tag synchronization, Pro feature | Consider only if author wants automatic synchronization and accepts the plan/access requirements; not needed for first MVP |
| [Connected Papers](https://www.connectedpapers.com/about) | Similarity graph based on co-citation/bibliographic coupling; not a citation tree | Useful seed discovery, not an automatic concept/contradiction graph |
| [alisoroushmd/zotero-mcp](https://github.com/alisoroushmd/zotero-mcp) | Citation graph/NetworkX analysis and HTML export, plus separate full-text/entity functions; graph tooling requires OpenAlex key and package extras | More experimental candidate, about 4 stars at inspection. API credentials/dependencies are heavier; its graph/abstract-entity tools do not prove concept-level idea relationships. Do not select as first default |
| [Thrillcrazyer/Zotero-Citation-Graph](https://github.com/Thrillcrazyer/Zotero-Citation-Graph) | In-Zotero citation visualization advertised | Small inspected project, about 8 stars and three commits; not compatibility-tested. Do not equate “inside Zotero” with a proven stable MVP |

The [official Zotero local API](https://www.zotero.org/support/dev/web_api/v3/local_api) documents local reads and Zotero 10+ authorized writes. Older “local API is always read-only” advice is version-dependent. The [54yyyu configuration guide](https://github.com/54yyyu/zotero-mcp/blob/main/docs/configuration.md) describes an API backend and a default SQLite snapshot backend: choose deliberately rather than treating all local modes as identical. A third-party capability claim remains unverified until an actual selected-library test.

## Recommended first delivery

Use **this custom reading skill + existing Zotero PDF/notes + optional small derived concept map**. It supports local PDFs even before a connector is configured. A later connection test should read one selected item/PDF, retrieve a real annotation, and only with authorization save/reopen one child note without altering another author note. Then map 5–10 selected papers with separate citation/retrieval/content-inference edges. Avoid installing a graph database, all-library embedding search, multiple overlapping Zotero MCPs or a second assistant to validate a small personal workflow.

If the author prioritizes ready-made global discovery maps, add ResearchRabbit as an explicitly selected external workflow; if ongoing two-way sync is essential, evaluate Litmaps Pro. Neither replaces the evidence-grounded concept map. No financial commitment, Zotero write authorization, external sharing or plugin installation is granted just by choosing to discuss the MVP.
