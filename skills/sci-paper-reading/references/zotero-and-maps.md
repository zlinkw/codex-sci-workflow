# Zotero and evidence-bearing literature maps

Load the integration/storage sections only when the user explicitly reintroduces Zotero. Default saved notes and maps use the selected Obsidian library and sci-obsidian-reading. The relationship vocabulary below is reusable, but it does not change the chosen storage destination or authorize a second library. Read only the needed subsection.

## Resolve the connection, do not assume it

Verify the installed Zotero version, running instance, actual available tools and library identity. Reuse an installed connector/CLI; no bundled MCP tool names are guaranteed. Prefer a shell CLI for bounded on-demand operations when available rather than permanently exposing a large tool catalog. Inspect that installed version's help/schema and errors; a GitHub README is a candidate capability, not evidence of local integration.

The official local API is normally `http://127.0.0.1:23119/api/`, must be enabled by the user in Zotero's advanced settings, and supports unauthenticated local reads. Probe the root/version before requests; use bounded results, explicit selected library/collection/items and stable item keys. Do not scan the entire library merely to read one paper. A timeout is an unavailable interface, not proof of a missing library. No direct database edits, copying live SQLite files or hidden browser cookies.

Zotero 10+ supports local writes with a user-granted local key. Authorization is a human permission dialog, not an agent click-through. Bind saved identities to the actual local server/library and object versions; local and web version counters are not interchangeable. Use optimistic versions and fresh reads before a scoped update; conflict means preserve the author's changes and reconcile. No silent fallback to cloud credentials on a local-only request. The user's willingness to consider Zotero does not authorize publishing private library data to another service.

If using `54yyyu/zotero-mcp` later, its `zotero-cli` entry offers JSON commands and optional PDF support. Verify installed `--help`/schema, configure explicitly local with the API read backend if the goal is avoiding a SQLite snapshot, and disable unrequested embeddings/global indexing/external model calls. Do not run its setup helpers that add another coding agent/project SKILL without need. Paper discovery can still use public publisher/search pages; send only authorized query/identifiers to external services.

## Read and save one authoritative note

Resolve the paper item, chosen version and exact PDF attachment. Read in place; distinguish item keys from attachment keys. Reuse the paper's existing annotations/child reading note, labeled as prior user/model interpretation rather than original-paper evidence. Preserve unknown user content and attachments. Source pages for a claim may be outside the first extraction window; detect truncation and fetch relevant remaining pages. Use page images for important equations/tables/figures.

Reading in chat creates no Zotero writes by default. When asked to save reading notes, write a concise child note for that exact paper using the selected mode and verified page/section locators. Update only this skill's identified note region or create its distinct child note; never replace arbitrary author notes. Keep content/identity/version together and avoid duplicate local Markdown mirrors. Topic-level plans/maps can use one explicitly selected topic note with links to paper notes; do not create Markdown trackers in manuscript projects. If a connector lacks safe write support, present the note content and the precise gap rather than claiming it was saved.

## Distinguish relationship types

| Edge | Meaning and minimum basis |
|---|---|
| cites | A actually references B; use a verified reference list or authoritative citation record and preserve A→B direction |
| similar | A retrieval/similarity service suggested proximity; record the metric/source. It is not citation, historical influence or scientific agreement |
| introduces/uses | An inspected paper formulates/uses a defined concept under stated conditions; preserve concept scope and source locator |
| extends/reframes | Content shows which assumption/problem/mechanism is changed relative to the inspected prior work; give both sources and distinguish author statement from reader interpretation |
| supports/challenges | Comparable claims under compatible conditions plus inspected results/argument. Mere citation, shared keywords or a different task's numbers are insufficient |
| may-transfer | Reader hypothesis about relevance to the user's project, with prerequisites and untested status; never display as proven support |

For an evidence-bearing edge keep endpoint identifiers, type/direction, a short reason, source/version and page/section/figure locator, reading scope and basis (`source-stated`, `retrieval-signal`, `reader-inference` or `untested-hypothesis`). Cross-paper comparison needs the relevant originals, not one author's caricature of another. Unknown relationship stays a candidate; omit rather than fill a visually pleasing map with invented arrows. No DOI does not imply no valid work; resolve a stable alternate identity. Preprint/journal versions are linked reports, not automatically independent ideas.

## Minimal map and storage

Start with one topic and roughly 5–10 selected papers. A minimal map can show **problem → challenge → concept → papers → supporting/limiting evidence**. Use ordinary Zotero notes/links for authoritative reading facts and an explicitly requested local interactive HTML/SVG for a derived view; a graph database, Obsidian vault, embedding index and second AI are not prerequisites. Label it a curated concept map, not an automatically complete knowledge graph. Preserve any author-corrected edge before regenerating; Zotero's generic Related link alone cannot encode these typed/directional claims.

Each node should link to the verified public paper or real Zotero item/PDF locator. On a relationship map show its basis/uncertainty and where to inspect the source. Distinguish inspected papers from discovered candidates; allow filtering those groups and edge types when an interactive view is actually implemented. Clicking or visual closeness never establishes a claim. Exported graph files are derived artifacts, not a second decision/evidence ledger. Do not generate a map on every routine quick read.

## Integration selection

The checked candidates and caveats live in [sources-and-mvp.md](sources-and-mvp.md), read only for tool choice/setup. Before recommending payment, installing, granting library access or implementing a custom map refresh the actual current capability/version. A citation map is useful for discovering lineage candidates; Codex still needs original text to judge the conceptual lineage the author cares about. No web service/library upload or automatic monitoring is enabled by this skill.
