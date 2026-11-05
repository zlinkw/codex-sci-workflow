# Medical imaging AI reporting review

Use for requested medical-imaging manuscript self-review, formal assessment or submission completeness, not every wording edit. Source: [CLAIM 2024 official checklist](https://rsna.github.io/claim/checklist.html), [RSNA explanation and examples](https://rsna.github.io/claim/), [official LLM skill](https://rsna.github.io/claim/llm-skill.html). Checked 2026-11-02: the checklist is the 44-item 2024 version; the 2026 explanation is not a new checklist version. Do not reuse 2020's 42-item numbering. Verify a journal's actual requirement before treating CLAIM as mandatory for TMI/MedIA or using an older requested edition.

This is an original application guide, not a reproduction of the copyrighted checklist. For a complete item-level assessment consult the official current table and relevant item explanations. Do not copy its published examples or treat them as this project's evidence.

## Apply proportionately

For a focused question, inspect its relevant item groups. For an explicitly full CLAIM assessment cover all 44 official items, preserving their real IDs. Read the manuscript, captions, tables and supplied supplements; unavailable material stays unchecked rather than silently No. Do not infer consent, acquisition, patient-level disjointness or clinical registration from common practice.

Compact navigation, not replacement item wording:

| Official items | Inspect in this study |
| --- | --- |
| 1–4 | AI task identification, abstract coverage, clinical/scientific purpose, aims |
| 5–6 | Study design and intended study role |
| 7–13 | Data provenance/selection, preprocessing/subsets, de-identification, missingness, acquisition |
| 14–18 | Reference-standard construction, rationale, annotator/source details, testing annotations and agreement |
| 19–21 | Split assignment and disjoint unit; justification of testing size |
| 22–27 | Architecture, software, initialization, training, checkpoint choice and any ensemble |
| 28–34 | Metrics, uncertainty/significance, robustness, explainability, internal/external testing and trial registration |
| 35–39 | Participant/exam flow, partition characteristics, results/uncertainty, diagnostic estimates where applicable and errors |
| 40–44 | Limits/intended use, technical details/protocol, code/model/data availability and support |

For segmentation/UDA pay attention to patient/site separation, target-label access at training/tuning/testing, slice-versus-volume aggregation, preprocessing fitted on testing data, pretrained model provenance, final-checkpoint selection, reference-label provenance and failure conditions. A public benchmark is not automatically a clinical trial. A reused annotated dataset still needs its annotation source described. Separate missing reporting from an actual design defect and from missing accessible evidence.

## Answer and record

- Yes requires an inspected passage/display/supplement and exact location covering the actual requirement. Reporting a value is not evidence that the estimator/design is appropriate.
- No means applicable but absent after checking the available complete material. NA needs a study-specific reason that the activity genuinely does not apply, not a way to excuse absent testing, sensitivity or sample-size justification. Use the official item explanation for borderline calls; do not infer an ensemble or a trial just to fill the checklist.
- Unchecked means unavailable or unresolved material. Keep it distinct from No/NA. Do not invent page/line numbers; use section, label and passage location until final pagination is available.
- Present item → inspected location/evidence → Yes/No/NA/unchecked → narrow gap/action. No percentage or checklist total is a scientific quality/acceptance score. Examples in the elaboration are not all obligatory subrequirements.
- Keep concise unresolved findings and manuscript/reply dependencies in the existing canonical review-state comments when maintaining that state is already authorized. No extra Markdown tracker. Do not run experiments or change prose merely to complete a checklist. Submit/export a filled official form only on request, without automatic upload.

Prefer reference-standard and unambiguous tuning/internal-testing/external-testing descriptions where they accurately reflect the study. Do not globally replace technical terms or claim compliance from a terminology change alone.
