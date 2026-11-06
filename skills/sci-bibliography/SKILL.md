---
name: sci-bibliography
description: Audit bibliography metadata, .bib entries and rendered reference styles for LaTeX and Typst, including TMI/MedIA formatting, capitalization, authors, venues, DOI, versions, duplicates and citation integrity. Use for reference-format questions and approved bibliography changes; route paper discovery and scientific-content verification to sci-literature-review, and prose drafting to sci-paper-writing.
---

## Execution constraints

- Never expose hidden reasoning, scratch notes, or step-by-step internal thought.
- Follow the active global progress/remaining-time requirement; keep routine output concise.
- Parallelize independent file reads, metadata checks, and validations when they do not share mutable state.

# SCI Bibliography

Audit bibliography data from the actual project sources. Never infer an entry from memory or from the rendered reference list alone.

## Routing and reference data

- Use this skill for bibliography metadata, `.bib` maintenance, venue normalization, LaTeX/Typst citation integrity and rendered reference styles. Distinguish metadata accuracy, support for the cited claim, and presentation compliance; a valid DOI or successful build establishes none of the other checks.
- Use `sci-literature-review` instead when the task is to discover papers or extract their scientific content.
- Read [references/venue-names.md](references/venue-names.md) only when journal, conference, publisher, organization, institution, venue acronym, or venue capitalization must be checked.

New manuscript work uses LaTeX only. Typst material below is compatibility reference for an explicitly requested legacy audit; do not migrate configuration or route new writing to it.

## Grounding workflow

1. Resolve the actual current manuscript and target venue. For LaTeX inspect the entry point, `latexmkrc`, build scripts, bibliography packages, `\bibliographystyle`, bst/bbx/cbx and template examples. For Typst inspect the main `.typ`, imported template functions, actual `bibliography` calls and built-in or custom CSL styles. Do not reuse a historical project path as the current project.
2. Determine the engine, data format and encoding: BibTeX, biber or Typst/Hayagriva; LaTeX escapes or supported UTF-8. Resolve style overrides before proposing metadata changes.
3. Resolve the bibliography resources and style needed for the request, including imported macros and cross-reference dependencies. A whole-library audit reads each active library completely. A specific entry/field question inspects that entry and necessary dependencies without expanding into unrelated metadata corrections. Handle an existing Hayagriva YAML library in its own format.
4. Audit every library in the agreed scope, reporting its coverage and material unavailable dependencies. A full bibliography audit covers all active libraries. Inactive resources remain unchanged. Prefer one existing compatible source rather than duplicate libraries.
5. Use a structured parser appropriate to the actual format. Preserve nested braces, supported markup, concatenated values, macros and comments. Never run executable TeX to inspect bibliography data or assume arbitrary LaTeX commands work in Typst.

## LaTeX and Typst citation mechanisms

Keep citation keys stable and let the active style generate numbering, ordering, name initials, author truncation, punctuation and displayed fields. Do not type rendered references or citation numbers into manuscript prose.

| Purpose | LaTeX | Typst |
|---|---|---|
| Cite an entry | `\cite{key}`; template-supported narrative/parenthetical commands when applicable | `@key` or `#cite(<key>)` |
| Load a library | Existing template's `\bibliography{references}` or `\addbibresource{references.bib}` and bibliography output | `#bibliography("references.bib", style: "ieee")` |
| Choose presentation | Template's `.bst` or biblatex configuration; do not mix engines | Built-in style or an independent CSL file |

Typst also supports Hayagriva YAML; `.bib` can remain the shared source and does not require a second library. For a MedIA-oriented starting point use `#bibliography("references.bib", style: "elsevier-harvard")`, then compare the rendered result with the actual journal/template requirements. A generic APA style is not a substitute. A dependent CSL stub that points to another style is not automatically a self-contained custom CSL; resolve the independent parent when needed. Verify the installed Typst version's support rather than assuming current online documentation matches it. Test special terms, math, accented names, multi-author entries and article numbers in rendered output only when compilation is authorized.

## Venue presentation profiles

Treat the active journal-specific instructions and verified template as authoritative, not a universal formatting rule. Retrieve current requirements when selecting or changing a journal; record the source, verification date and limitations. The following profiles are reusable starting points, not a claim that a generic style guarantees submission compliance.

| Feature | TMI | MedIA |
|---|---|---|
| In-text citation and ordering | IEEE numeric citations in first-citation order | Author–year citations; author-alphabetical bibliography with year disambiguation as needed |
| Displayed author names | Initials before surname | Surname before initials |
| Author truncation | TMI explicitly lists all authors up to six; above six, first author plus et al. | In-text three or more authors use et al.; bibliography follows its actual style, not the TMI cutoff |
| Article/conference-paper title | Sentence-style capitalization with correct proper names and acronyms | Sentence-style capitalization with correct proper names and acronyms |
| Container title | Required official abbreviation, e.g. `IEEE Trans. Med. Imaging` | Required standard abbreviation, e.g. `Med. Image Anal.` |
| Publication locator | Verified volume, issue if assigned, pages or the real article number | Verified volume and pages/article number, with other fields displayed as required by the style |
| DOI | Retrieve and verify when assigned; display through the template | Retrieve and verify when assigned; display through the template |

TMI's author-count rule and completeness requirement come from its [author instructions](https://ieeetmi.org/authors-instructions/); article/container casing is supported by [IEEE reference guidance](https://procomm.ieee.org/transactions-of-professional-communication/for-prospective-authors/guidelines-to-follow/guidelines-for-preparing-references/). For MedIA, the 2026-10-30 inspection could not access the [current author guide](https://www.sciencedirect.com/journal/medical-image-analysis/publish/guide-for-authors), which returned 403. The provisional profile was cross-checked against the journal's [historical official guide](https://citeseerx.ist.psu.edu/document?doi=6829856a637b5aa870afd5d9f478da8a9d66ab45&repid=rep1&type=pdf) and the [CSL journal definition](https://github.com/citation-style-language/styles/blob/master/dependent/medical-image-analysis.csl), which points to Elsevier Harvard. Do not treat those as confirmation of every current requirement; recheck at submission and preserve unresolved differences.

Keep a compact venue/style profile in the existing main manuscript's header comments during authorized work: target venue, actual engine and library/style paths, authoritative source and check date, confirmed rules versus provisional items. Use `%` in TeX and `//` in Typst. Claim-specific verification belongs before its citing paragraph using the writing skill's local comment template, not in the header or a new Markdown tracker. Global skill maintenance does not authorize changing a live manuscript.

## Metadata authority

- Verify metadata in this order: official publisher or conference page, DOI/Crossref, DBLP, then the existing BibTeX entry.
- Check authors, title, year, journal or booktitle, volume, number, pages, DOI, URL, publisher, organization, institution, entry type, publication version, and required missing fields.
- Preserve source locators and verification status so the author can inspect disputed changes. Keep the audit table compact; put authoritative links in its explanation or an adjacent source note rather than hiding them. Persist claim-level evidence in paragraph comments, with stable venue rules only in the header.
- Never invent metadata. If authoritative sources are unavailable or disagree, mark the field `needs verification`, retain the current value, and show the plausible candidates to the user.

## Mandatory no-edit audit gate

- Do not modify active bibliography, `.tex`, `.typ` or style files during the audit phase, even when a correction appears certain. Read-only style advice and global skill maintenance do not trigger a manuscript-edit request.
- Complete the audit within the requested scope before requesting approval, using one complete table for those mappings. A narrow field question does not require a full-library audit. A general request such as "fix the bibliography" is not approval for mappings that have not yet appeared in the table.
- Submit one complete mapping table with these columns: citation key, entry type, field, current value, proposed value, necessary explanation, change reason, and status.
- Represent a missing field as `missing` in the current-value column. Include every proposed addition, deletion, type correction, capitalization change, formatting change, and publication-version replacement.
- Report duplicate keys, duplicate DOI values, duplicate normalized titles, and likely duplicate publications separately. Do not merge duplicates or rename citation keys.
- Require explicit user confirmation of the proposed mappings unless the same exact mappings are already authorized in the current session. If a mapping materially changes during review, show the revised complete table for context and request confirmation only for the changed or still-unapproved mappings; preserve authorization for unchanged accepted rows.
- After approval, apply only accepted mappings. Preserve citation keys, entry order, field order, indentation, comments, and unrelated content.

## Title rules

- Identify the field, publication type and target style before adjusting capitalization. English article and conference-paper titles in the TMI/MedIA profiles use sentence-style casing; journal names, proceedings titles and book titles follow their own official/style conventions, not this article-title transformation.
- Capitalize the article title's first word and preserve proper names. Follow the verified style for the first word after a colon; do not impose one colon rule on all venues. Record an unresolved convention instead of silently guessing.
- Preserve official capitalization for acronyms, initialisms, models, algorithms, datasets, benchmarks, software, programming languages, frameworks, hardware, companies, products, geographic names, personal names, chemical formulas, gene or protein symbols, and case-sensitive technical terms such as `2D`, `3D`, `U-Net`, `ImageNet`, `LiDAR`, `MRI`, `CT`, and `COVID-19`.
- Preserve valid title math and supported markup under the actual engine. For a shared library, inspect compatibility instead of blindly transferring LaTeX-only commands to Typst.
- Prefer local case protection for necessary terms, e.g. `{MRI}`, `{CT}`, `{U-Net}` and `{DINOv3}`. Do not require `title = {{...}}` for every entry: whole-title protection is appropriate only when preserving the verified literal casing is intended and compatible with the style. Existing valid whole-title braces are not automatically errors and must not be rewritten outside the approved mapping.
- Some styles output stored titles without normalizing case. Judge the actual rendered list as well as parsed source data; a style switch alone may not correct source casing.
- Preserve the official language-specific casing of non-English titles; do not impose English sentence case on them.

## Author and encoding rules

- Preserve official author order, full names, spelling, hyphenation, particles, suffixes, and compound family names. Do not manually reduce given names to initials.
- Protect corporate or consortium authors with double braces.
- For BibTeX projects use the actual engine's supported spelling/escapes; for biber, Typst or confirmed UTF-8 projects prefer supported official Unicode spelling. Check name particles, compound surnames, accents and corporate authors across both renderers before declaring a shared library compatible.
- Do not change author identity or ordering based only on inconsistent secondary metadata. Mark unresolved differences `needs verification`.

## Venue rules

- Prefer venue macros already provided by the template or active `.bib` files when their expansion is correct.
- BibTeX brace/escape syntax in these rules applies to `.bib` values, not literal Hayagriva YAML. Use the existing native format's own protection and field conventions when that is the active library.
- When the template requires full names, use the canonical official venue name. When it requires abbreviations, use IEEE official abbreviations, publisher or ISO 4 journal abbreviations, and official conference acronyms.
- Use the year-specific official branding for historical entries. Do not retroactively change `NIPS` to `NeurIPS`, `IEEE` to `IEEE/CVF`, or another organization name when the publication year used the earlier form.
- Protect fixed organization names and acronyms in literal values, including `{IEEE}`, `{CVF}`, `{ACM}`, `{AAAI}`, and `{ISPRS}`.
- Normalize `publisher`, `organization`, and `institution` to official casing, including `{IEEE}`, `{ACM}`, `Springer Nature`, `Elsevier`, `Wiley`, and `Taylor & Francis`.
- Use the venue reference table as a casing and alias dictionary, not as permission to overwrite year-specific proceedings titles or template macros.

## Field and entry rules

- Keep authoritative metadata as complete as appropriate; let the style decide which fields are printed. Do not delete a true issue, DOI or other field simply because one style omits it. Distinguish `missing`, `not yet assigned` and `not applicable`; never invent volume, issue, pages or article numbers for early-online work.
- Retrieve journal-article authors, title, journal, year, volume/issue when assigned, pages/article number and DOI. For proceedings retrieve the year-specific proceedings title, pages, DOI and applicable series, volume, editors/publisher. For preprints retain the platform, identifier, year/version and stable locator; for datasets/software retain creators, title, version, date, repository/publisher and persistent ID; for webpages retain author/organization, title, URL and publication/access dates where applicable.
- Store DOI values without `https://doi.org/` or `doi:` prefixes. Preserve the canonical DOI value.
- A verified DOI landing URL need not be printed redundantly; retain useful source metadata unless a justified, approved field change is needed. Include any proposed URL deletion in the audit table.
- Use `--` for page ranges in `.bib`, or the native range representation in an existing Hayagriva library. Validate year, volume, number, month, pages, article number, publisher, organization, institution, series, and edition against the entry type and template.
- Prefer a formal publication when it is the same work and supports the actual cited content; check substantive/version differences, corrections and retraction notices. Do not combine authors/year/locators from different versions. Keep the citation key stable and include each version-related field replacement in the audit table; route scientific claim verification to `sci-literature-review`.
- For preprint-only work, follow the active BibTeX or biblatex template for `eprint`, `archivePrefix`, `primaryClass`, `note`, and URL fields.
- Validate `@article`, `@inproceedings`, `@proceedings`, `@book`, `@incollection`, `@misc`, `@techreport`, `@phdthesis`, and `@mastersthesis` against their required and appropriate fields.
- Add authoritative missing fields only after approval. Remove only invalid, duplicated, or template-rejected fields listed in the approved table.

## Citation integrity

- Scan the actual manuscript and imported sections for LaTeX citation commands or Typst `@key`/`cite(...)`, comparing with active library keys. In Typst distinguish label cross-references such as `@fig-model` from bibliography citations; do not report every `@` reference as a missing paper.
- Report undefined citations, duplicate keys, unused entries, broken `crossref` targets, malformed key lists, and references to a preprint when a formal replacement is proposed.
- Never rename a citation key automatically. Duplicate entries with different keys require a separate user decision before any merge or citation rewrite.

## Approved edit workflow

1. Re-read the approved table and active files immediately before editing.
2. Apply field-level changes with the smallest possible diff. Do not reformat the full `.bib` file.
3. Update `.tex`/`.typ` citation keys only when the user separately approves a duplicate merge or key change. Style-switch changes require an explicit scoped proposal, not a metadata-only correction.
4. Reparse active bibliography resources and rerun engine-appropriate citation-integrity checks.
5. Compile/render through the project's local workflow only when requested or already authorized; do not change editor auto-build settings. If no render was authorized, report source checks separately from unverified output compliance.
6. Report only the applied changes, validation result, unresolved `needs verification` items, and any required user action.

## Validation checklist

- Confirm type/style-specific casing, the verified colon convention, necessary case protection and supported special terms; do not require whole-title braces universally.
- Confirm author spelling and encoding under the detected engine.
- Confirm venue full names or abbreviations against the template and venue dictionary.
- Confirm DOI format, page ranges, entry types, required fields, formal-version preference, and citation integrity.
- Confirm no unapproved field changed and no unrelated formatting churn occurred.
- Distinguish metadata verification, scientific claim support and rendered-style verification in the result; preserve gaps and the relevant local comments rather than declaring all three passed from one check.

## Mechanism sources

- [Typst bibliography documentation](https://typst.app/docs/reference/model/bibliography/) and [citation documentation](https://typst.app/docs/reference/model/cite/): supported library formats, citation syntax and built-in/custom styles. Check installed-version behavior.
- [K-Dense citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md): identifier-based metadata retrieval and validation inform this workflow. Its automatic rekeying/deduplication or tool dependencies are not authorization to alter this author's library.
