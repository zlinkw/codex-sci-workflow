---
name: sci-literature-review
description: Discover papers, trace original and recent sources, synthesize related literature and retrieve specific source facts. Use for paper search, citation support and cross-paper research synthesis. User-focused reading of a supplied paper or learning a new topic uses sci-paper-reading; manuscript drafting, bibliography audits and local result analysis retain their own skills.
---

## Execution constraints

Follow the active global progress/remaining-time, evidence and authorization requirements. Keep updates concise and parallelize independent reads/checks; serialize shared state, dependent writes and live operations. Do not expose hidden reasoning, automatically delegate to another AI, or trade required verification for speed.

# SCI Literature Review

Search the web when exact or current paper information is needed. Prefer primary sources.

For “读这篇论文 / 只看创新点 / 了解一个新课题”, use `sci-paper-reading` as the primary instruction set; this skill handles only actual discovery/support-retrieval subtasks as needed. Do not reroute back recursively once the reading purpose is established. Existing extraction/source/citation rules remain available for a specific factual lookup or cross-paper synthesis. Reading does not automatically load the manuscript writing or formal peer-review workflow.

## Source priority

1. Paper page, arXiv, publisher page, PubMed, IEEE, ACM, Springer, Elsevier, MICCAI, CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML, or journal page.
2. Official code repository, project page, model card, dataset page, or benchmark page.
3. Secondary summaries only when primary sources are unavailable, and mark them as secondary.

## Extraction rules

Extract only what the user asks for. Do not produce a generic full paper summary unless requested.

Common focus types:

- Innovation point
- Network structure
- Loss function
- Training setting
- Dataset and split
- Baselines
- Metrics
- Tables and figures
- Ablation studies
- Efficiency results
- Failure cases
- Limitations
- Implementation details

## Evidence rules

- Include source links for factual paper claims.
- Mark inaccessible PDFs, abstract only findings, and uncertain details clearly.
- Do not invent citations, numbers, datasets, baselines, or architecture details.
- If a claim is inferred from a figure, table, or code rather than explicitly stated, label it as inference.

## Author-approved AI literature search and citation rules

Apply the following fourteen rules proportionately to the actual request. They guide discovery and scientific-content verification; `sci-bibliography` owns authoritative field checks, LaTeX/Typst styles and approved library changes, while `sci-paper-writing` owns placement in the argument and its canonical paragraph comments. Do not require the author to name skills or expand a narrow citation search into a systematic review.

1. **确定用途。** Establish whether the citation supports a background fact, original method, prior limitation, comparator or another specific role. Choose papers for that role rather than keyword resemblance.
2. **医学与通用方法两路检索。** For medical AI, combine relevant biomedical/imaging sources (such as PubMed, TMI, MedIA and MICCAI) with appropriate AI/CV original proceedings and indexes. PubMed alone can miss computing literature; choose complementary available databases rather than requiring a particular paid service.
3. **构造概念与同义词。** Break the question into task, problem, mechanism and application conditions; combine synonyms, abbreviations and alternate terms. Do not search only a proposed module's name. Record useful queries and scope compactly.
4. **兼顾近期与原始来源。** State the search cutoff/date and temporal scope; check recent developments while tracing foundational mechanisms to their originals. Publication age, citations and venue prestige do not establish relevance or truth; do not impose a fixed recent-paper quota.
5. **前后向追踪。** Inspect the references and citing follow-ups of strong seeds for foundations, improvements, challenges and alternatives. Distinguish discovered candidates from papers actually inspected.
6. **交叉核验身份。** Confirm title, authors, year and identity/version through the official publisher/proceedings and DOI registration or another authoritative record as available. Repeated copies of one metadata error are not independent confirmation; unresolved conflicts remain `needs verification`.
7. **核验支持关系。** Check that the cited proposition actually appears in the inspected source and under compatible conditions. Keep section/paragraph/table/figure locators and qualifiers. DOI resolution establishes neither correct citation meaning nor experimental support.
8. **关键判断读全文。** Read relevant full text for methodological limitations, architecture and experimental/comparison claims. Identify inaccessible or truncated content and abstract-only findings; narrow or defer the proposed claim instead of implying full-text review.
9. **准确描述局限。** Distinguish an author's stated limitation, an experimental observation and our own analysis. Do not make competing methods appear necessarily defective merely to motivate novelty; preserve their setting and the scope of available evidence.
10. **检查版本与状态。** Look for the corresponding formal publication, substantive version changes, corrections and retraction notices. Verify that replacement content still supports the claim; pass metadata changes to `sci-bibliography` without silently changing stable keys or mixing version fields. Report unchecked status as unchecked, not clean.
11. **获取元数据而非凭记忆拼写。** Retrieve publisher/conference/identifier records, then use `sci-bibliography` for type/style normalization. Never guess DOI, author order, year, volume, issue or locator; distinguish missing, unassigned and inapplicable fields.
12. **候选与正式引用分开。** Present candidates with intended role, source/identifier, publication version and verification scope/status. Integrate only within the author's authorized writing/library scope and bibliography audit/edit procedure. Unverified candidates remain explicit gaps, not fabricated BibTeX or unresolved fake citation keys in final prose.
13. **保留不利证据。** Include relevant contradictory findings, alternatives and limitations. Ranked search results do not establish exhaustive coverage. Use systematic-review search/screening requirements only when that review type is requested; report unavailable coverage honestly.
14. **原位保存必要核验信息。** During authorized manuscript work, preserve claim/key, citation purpose, inspected source/locator, support boundary and verification gap/status in the existing `CODEX-PARAGRAPH-PLAN` immediately before the citing paragraph, using the writing skill's embedded template and TeX `%` comments. Only an explicitly requested legacy Typst audit uses its existing `//` comments; new writing follows the LaTeX workflow. Keep stable venue/style rules only in the main header and full metadata in the library; no duplicate global citation ledger, new project Markdown tracker or header full of paragraph-level records. Read the local comments after context loss and update in place. Read-only search or global skill maintenance alone does not authorize manuscript writes.

## Output shape

Use a compact table when comparing multiple papers. Use short prose when analyzing one paper. Keep the focus aligned with the requested information.

For a reference-candidate task, include each candidate's intended citation role and verification scope (identity checked, abstract/full passage inspected, claim support, metadata/style gaps) as applicable. Do not collapse these independent checks into a single unexplained verified label. Report only the coverage actually searched and inspected.

## Sources informing this workflow

- [K-Dense literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md): scoped, multi-source retrieval and screening; ranked web results are not exhaustive coverage or full-text assessment.
- [K-Dense citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md): identifier-based retrieval and metadata validation; metadata existence and claim support require separate checks.
- [Orchestra ML paper writing, citation workflow](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/20-ml-paper-writing/ml-paper-writing/SKILL.md#citation-workflow-hallucination-prevention): retrieved citations, cross-checking and checking the actual attributed claim. Do not inherit unsupported numerical hallucination-rate claims, compulsory APIs, fabricated placeholder citation keys, automatic rekeying or extra project reports. Use this author's existing tools and authorization rules.

