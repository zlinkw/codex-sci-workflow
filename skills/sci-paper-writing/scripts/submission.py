#!/usr/bin/env python3
"""Explicit local submission preflight and derived-source export; never accepts edits.

Pass an inspected, explicit dependency file list. This is not a general TeX parser or
journal/scientific compliance engine. Scientific, venue, bibliography and visual
checks require evidence-bearing human/agent attestations, recorded in the report.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

from source_review import Review, Conflict, digest, PENDING
from review_archive import plain_file, safe_name

ALLOWED = {".tex", ".bib", ".bbl", ".bst", ".sty", ".cls", ".clo", ".def",
           ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg", ".csv", ".dat", ".txt"}
BLOCK = re.compile(r"^%\s*CODEX-([A-Z][A-Z0-9-]*)-(BEGIN|END)\s*$")
SINGLE = re.compile(r"^%\s*CODEX-[A-Z][A-Z0-9-]*(?::|\s|$)")
CHECKS = ("venue", "scientific_evidence", "reply_consistency", "bibliography", "visual_pdf")


def strip_internal(raw):
    text = raw.decode("utf-8-sig")
    result, active = [], None
    for line in text.splitlines(keepends=True):
        marker = BLOCK.fullmatch(line.rstrip("\r\n"))
        if marker:
            name, edge = marker.groups()
            if edge == "BEGIN":
                if active:
                    raise Conflict("Nested internal comment blocks")
                active = name
            else:
                if active != name:
                    raise Conflict("Unmatched internal comment block")
                active = None
        elif active:
            if line.strip() and not line.lstrip().startswith("%"):
                raise Conflict("Executable/noncomment content inside CODEX block; preserve it for manual review")
        elif not SINGLE.match(line):
            result.append(line)
    if active:
        raise Conflict("Unclosed internal comment block")
    return (b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b"") + "".join(result).encode("utf-8")


def preflight(repo, owner, main, files, git="git"):
    r = Review(repo, owner, git)
    r.assert_ready()
    s = r.status()
    blockers = []
    for id_, e in s["edits"].items():
        if e["status"] in PENDING:
            blockers.append(f"{id_}: author decision pending")
        if e.get("freshness") == "needs-recheck":
            blockers.append(f"{id_}: dependency needs recheck")
        if any(q.get("status") in ("open", "addressed-pending-review") for q in e.get("requests", [])):
            blockers.append(f"{id_}: unresolved author annotation")
    names = sorted(set(files))
    if main not in names:
        raise Conflict("Include the verified main root in explicit export files")
    contents, cleaned = {}, {}
    for n in names:
        safe_name(n)
        if Path(n).suffix.lower() not in ALLOWED or any(x.startswith(".") or x == "clean_dir" for x in n.lower().split("/")):
            raise Conflict("Unsupported/non-submission file: " + n)
        p = plain_file(r.repo, n)
        raw = p.read_bytes()
        contents[n] = raw
        cleaned[n] = strip_internal(raw) if p.suffix.lower() == ".tex" else raw
        if p.suffix.lower() == ".tex":
            t = cleaned[n].decode("utf-8-sig")
            if re.search(r"\\(?:codex(?:add|delete|replace)|revall|revadd)\s*\{", t):
                blockers.append(n + ": revision syntax requires explicit legacy review, not automatic stripping")
            # Static literal dependencies only; generated/macro paths require separate inspection.
            for path in re.findall(r"\\(?:input|include|includegraphics)(?:\[[^\]]*\])?\s*\{([^{}]+)\}", t):
                if path.startswith(("/", "\\")) or ":" in path or ".." in path.replace("\\", "/").split("/"):
                    blockers.append(n + ": external/traversing literal dependency " + path)
    report = {"main": main, "owner": owner, "owner_sha256": digest(r.raw), "machine_blockers": blockers,
              "files": {n: digest(b) for n, b in contents.items()}, "checks_required": list(CHECKS),
              "boundary": "Machine checks do not verify scientific truth, journal compliance, dependency closure or visual layout. No edits accepted or working files stripped."}
    return r, contents, cleaned, report


def export(repo, owner, main, files, destination, checks, latexmk, engine="pdflatex", git="git", include_bbl=False):
    r, originals, cleaned, report = preflight(repo, owner, main, files, git)
    if report["machine_blockers"]:
        raise Conflict("Submission blocked: " + "; ".join(report["machine_blockers"]))
    if any(not isinstance(checks.get(k), dict) or checks[k].get("verified") is not True or
           not str(checks[k].get("evidence", "")).strip() for k in CHECKS):
        raise Conflict("Each required check needs verified=true and actual evidence/inspection locator; unknown is not pass")
    dest = Path(destination).resolve()
    if dest.exists() or dest.is_relative_to(r.repo):
        raise Conflict("Use an absent derived export directory outside the project")
    # Fresh state/source guard before materializing this immutable candidate export.
    if r.state_path.read_bytes() != r.raw or any(plain_file(r.repo, n).read_bytes() != b for n, b in originals.items()):
        raise Conflict("Source/state changed since preflight")
    dest.mkdir(parents=True, exist_ok=False)
    payload = dest / "source"
    payload.mkdir()
    for n, raw in cleaned.items():
        p = payload / n
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(raw)
    engines = {"pdflatex": "-pdf", "xelatex": "-xelatex", "lualatex": "-lualatex"}
    if engine not in engines:
        raise Conflict("Select the verified project engine")
    argv = [latexmk, engines[engine], "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-recorder", "-outdir=build", "./" + main]
    run = subprocess.run(argv, cwd=payload, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (dest / "build.log").write_bytes(run.stdout)
    # latexmk stdout retains expected first-pass citation warnings even when
    # later passes resolve them. Judge unresolved references from the final
    # engine log; keep the full multi-pass stdout in build.log as evidence.
    final_log = payload / "build" / (Path(main).stem + ".log")
    logs = final_log.read_text(encoding="utf-8", errors="replace") if final_log.is_file() else ""
    pdf = payload / "build" / (Path(main).stem + ".pdf")
    if run.returncode or not pdf.is_file() or not final_log.is_file() or re.search(r"(?i)(undefined (?:references|citations)|(?:citation|reference) [`'][^\n]+undefined|label\(s\) may have changed|multiply[- ]defined labels)", logs):
        raise Conflict("Derived build failed or unresolved references/citations; retained export/build.log, no ready ZIP")
    if r.state_path.read_bytes() != r.raw or any(plain_file(r.repo, n).read_bytes() != b for n, b in originals.items()):
        raise Conflict("Source changed during export; derived files retained, no ready ZIP")
    generated = {}
    if include_bbl:
        bbl_name = Path(main).stem + ".bbl"
        bbl = plain_file(payload, "build/" + bbl_name).read_bytes()
        if not bbl.strip():
            raise Conflict("Requested generated bibliography is empty; no ready ZIP")
        if bbl_name in cleaned and cleaned[bbl_name] != bbl:
            raise Conflict("Selected bibliography differs from the derived build; no ready ZIP")
        if bbl_name not in cleaned:
            generated[bbl_name] = bbl
    report.update({"checks": checks, "build": {"argv": argv, "exit_code": run.returncode},
                   "derived_files": {n: digest(b) for n, b in cleaned.items()}, "pdf_sha256": digest(pdf.read_bytes()),
                   "generated_files": {n: digest(b) for n, b in generated.items()},
                   "uploaded": False, "author_decisions_changed": False})
    (dest / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    with zipfile.ZipFile(dest / "submission.zip", "x", zipfile.ZIP_DEFLATED) as z:
        for n in cleaned:
            z.write(payload / n, n)
        for n, raw in generated.items():
            z.writestr(n, raw)
        # The normal PDF remains available separately.
    return {"source_zip": str(dest / "submission.zip"), "pdf": str(pdf), "report": str(dest / "verification.json"),
            "note": "Explicit source selection and evidence attestations still require author/venue judgment. No upload or author acceptance."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("preflight", "export"))
    p.add_argument("--repo", required=True)
    p.add_argument("--state", required=True)
    p.add_argument("--main", required=True)
    p.add_argument("--files", nargs="+", required=True)
    p.add_argument("--git", default="git")
    p.add_argument("--destination")
    p.add_argument("--checks", help="UTF-8 evidence-bearing checks JSON outside the working paper")
    p.add_argument("--latexmk")
    p.add_argument("--engine", choices=("pdflatex", "xelatex", "lualatex"), default="pdflatex")
    p.add_argument("--include-bbl", action="store_true", help="Include the bibliography generated by this derived build when the verified venue requires it")
    a = p.parse_args()
    if a.action == "preflight":
        result = preflight(a.repo, a.state, a.main, a.files, a.git)[-1]
    else:
        if not all((a.destination, a.checks, a.latexmk)):
            raise Conflict("Export needs destination, checks and verified latexmk")
        result = export(a.repo, a.state, a.main, a.files, a.destination,
                        json.loads(Path(a.checks).read_text(encoding="utf-8-sig")), a.latexmk, a.engine, a.git, a.include_bbl)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (Conflict, KeyError, ValueError, OSError) as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
