# Opt-in colored and legacy review

Load only on explicit author/verified venue request or preserving/migrating existing marks. Clean review is the default. Apply the kernel once.

This module concerns optional legacy author-review markup, not final revised-manuscript highlighting. The author's final delivery requires additions/replacements in red against a fixed original baseline under [submission.md](submission.md#final-revision-highlighting); do not use the blue-new/red-deleted convention below for that deliverable or add per-acceptance coloring to the plugin.

## Optional colored or legacy review

Activate only for the author's explicit request, an actual venue requirement, or preserving an existing unmigrated project's pending marks. It is not the default for new clean revisions. The existing macro helper remains available; no legacy marks or preamble are automatically removed. Removing colors or using final mode is never acceptance.

Reuse an equivalent compatible revision system. Otherwise insert only the needed embedded preamble below after checking packages/macros, after documentclass and before begin-document in each actual independently compiled root. Do not load/define twice, overwrite author commands, add external skill-file inputs, or initialize it during read-only checks. The changes package renders revisions; it does not establish author decisions.

The source forms are:

```latex
\codexreplace{1}{new text}{original text}
\codexadd{2}{new text}
\codexdelete{3}{original text}
% In the response letter:
\codexreplace{a}{new reply}{original reply}
```

New text is blue. Original removed text is red with a strike-through. IDs identify review decisions and remain stable when reworking an unsatisfied change. Use one ID per independently reviewable prose edit; do not create one giant replacement for a section with unrelated edits.

The markup package has limits. Do not wrap entire figures, tables, headings, environments, verbatim text, or multiple paragraphs in one change command. For formulas and structural changes, use a template-compatible per-element presentation, avoid duplicate labels/numbering, and explain any item that cannot safely use a strike-through. Never silently force broken LaTeX through the text markup. Existing labels and commands must remain functional.

### Legacy macro decisions only

Resolve [review_marks.py](../scripts/review_marks.py) relative to this skill package, not the paper root. Use it to list changes and prepare selective resolutions with exact `--ids 1,3` or `--ids a,c` when useful. Map IDs to the verified files before invoking it; it acts on one specified file, not a whole project or round. Its default is a dry run; `--apply` and the exact expected SHA256 are required to write. Read the proposed ID/content mapping before applying the user's already-authorized decision. Do not request a second approval for the exact accepted IDs. Partial acceptance leaves other marks intact. The helper resolves selected source marks only; the agent must reconcile version, dependency and issue state under this guide. It neither changes those records automatically nor compiles/pushes.

After acceptance, rejection or rework, apply the version/freshness protocol above before reporting affected replies current: mark stale dependencies, prepare the necessary candidate correction and update coverage/evidence separately from author acceptance. Preserve unrelated pending marks. Do not use package final mode to disguise unresolved revisions.

### Colored revision preamble

For the first colored revision, reuse an existing equivalent system or insert compatible definitions from this block after `\documentclass` and before `\begin{document}` in the independently compiled document that needs them. Do not load packages or redefine author macros twice. These are executable preamble commands, not comments to put before the document class.

```latex
% CODEX-REVIEW-PREAMBLE-BEGIN
% Insert in the main preamble only after checking existing revision packages/macros.
% Review IDs are source identifiers; they do not add author labels to the PDF.
\usepackage{xcolor}
\usepackage[normalem]{ulem}
\usepackage[authormarkup=none]{changes}
\setaddedmarkup{\textcolor{blue}{#1}}
\setdeletedmarkup{\textcolor{red}{\sout{#1}}}
\newcommand{\codexreplace}[3]{\replaced{#2}{#3}}
\newcommand{\codexadd}[2]{\added{#2}}
\newcommand{\codexdelete}[2]{\deleted{#2}}
% CODEX-REVIEW-PREAMBLE-END
```
Read the response-writing module only when drafting or substantively changing a reply, not for a bare accept/reject command.
