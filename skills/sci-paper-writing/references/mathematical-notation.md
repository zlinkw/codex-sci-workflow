# Mathematical notation and approval

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

- Write inline math as `$...$`, with one dollar delimiter on each side. Do not use `\(...\)` for inline math.
- Write every display equation with a numbered `\begin{equation}...\end{equation}` environment. Do not use `equation*`, `$$...$$`, or `\[...\]`.
- Give every display equation a unique `\label{eq:...}`, including equations not currently referenced in prose. Nest `aligned` inside `equation` for multiline formulas.
- Refer to equations as `Eq.~\eqref{...}`.
- When a display equation ends with a period, place exactly one empty source line between the closing `\end{equation}` and the following prose so that the prose begins a new paragraph.
- When a display equation ends with a comma, place no empty source line between `\end{equation}` and the following prose; they continue the same sentence and paragraph.
- Determine this from the display's final sentence punctuation, not a decimal point, label or intermediate equation row. For nested `aligned`, apply the spacing after the outer `\end{equation}`, not inside the math environment. A comment-only line does not replace the empty line needed to start a paragraph. Preserve the intended sentence punctuation rather than changing it just to obtain a preferred layout.

Period followed by a new paragraph:

```latex
\begin{equation}
a = b.
\label{eq:example-period}
\end{equation}

The next paragraph starts here.
```

Comma followed by a continuation:

```latex
\begin{equation}
a = b,
\label{eq:example-comma}
\end{equation}
where $a$ and $b$ denote the defined quantities.
```

## Mathematical notation rules

- Use italic mathematical letters for scalars. Use bold lowercase letters for vectors, bold uppercase letters for matrices, bold calligraphic uppercase letters for tensors of order three or higher, and ordinary calligraphic uppercase letters for sets, datasets, and domains.
- Use blackboard bold for number systems. Write loss functions as `\mathcal{L}`. Use blackboard bold for probability measures, expectations, and indicator functions; use italic lowercase letters for probability mass or density functions.
- Use italic uppercase letters for random variables and corresponding italic lowercase letters for observations. Use calligraphic uppercase letters for distribution families.
- Keep scalar Greek letters italic and write Greek vectors with `\boldsymbol{...}`.
- Write custom mathematical functions as italic function symbols. Write named and standard operators with `\operatorname{...}` or `\mathrm{...}`.
- Write running indices such as `i`, `j`, and `k` in italics. Write semantic subscripts and superscripts such as `src`, `tgt`, `pred`, and `cls` in upright roman type.
- Assign one stable meaning to every hat, tilde, bar, prime, subscript, superscript, case distinction, and font change. Do not let these meanings drift across sections.
- Use one consistent notation for transpose, inverse, norm, inner product, gradient, differential, expectation, probability, conditional probability, summation, concatenation, normalization, and set cardinality.
- Give each symbol exactly one meaning across the manuscript, and do not switch symbols for the same object without a stated mathematical reason.
- Explain every new symbol and operator at first occurrence, including common operators. Place the explanation immediately before or after the first formula and state its meaning, index range, and every dimension needed to understand or validate the operation.
- Recover consequential symbol meanings/scopes from the compact top-profile agreement and relevant local definitions; update the internal ledger only for affected notation. Persist only what context recovery needs, not a visible notation table unless requested.
- If a symbol's meaning cannot be determined from the manuscript, code, or local context, stop and ask the user. Present the conflicting locations and candidate meanings; do not guess or normalize it silently.

## Symbol refactoring approval gate

- Before any manuscript-wide symbol normalization, inspect the full manuscript and prepare a proposed mapping table without changing manuscript content.
- Include these columns: current symbol, proposed symbol, meaning, mathematical type, shape or dimension when relevant, scope and affected locations, detected conflict, proposed change, and replacement reason.
- Add the necessary symbol explanations and identify every planned font, case, accent, subscript, superscript, or naming change.
- For this manuscript-wide normalization, ask the user to confirm the proposed mapping table before applying it. Already-authorized exact mappings need no second approval; this gate does not turn a scoped equation edit or the approved manual indentation formatter into a new whole-paper approval process.
- If the user changes or rejects an entry, revise the complete table for context and request confirmation only for materially changed or still-unapproved mappings; preserve unchanged accepted rows and respect rejected ones.
- After approval, apply the accepted mapping consistently across prose, equations, captions, tables, and cross references, then verify that no obsolete or conflicting notation remains.
