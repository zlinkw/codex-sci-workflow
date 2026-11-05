"""Create an isolated PDF comparison of two committed LaTeX project versions."""
# Retired source: Git-history PDF command disabled; this file is no longer shipped.
from pathlib import Path, PurePosixPath
import argparse
import datetime
import json
import os
import re
import subprocess
import tarfile
import tempfile

LOCATORS = {"GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
            "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES"}

def execute(args, cwd, *, stdout=None):
    env = {k: v for k, v in os.environ.items() if k.upper() not in LOCATORS}
    env.update(LC_ALL="C", LC_CTYPE="C", LANG="C")
    result = subprocess.run(args, cwd=cwd, env=env, stdout=stdout or subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=180)
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace")[-4000:]
                           or f"Tool failed with exit code {result.returncode}")
    return result.stdout

def render_comparison(old_doc, new_doc, out, latexdiff, latexmk):
    """Render a derived, word-level comparison; never modify either source."""
    diff_tex = new_doc.parent / "__codex_revision_diff__.tex"
    if diff_tex.exists():
        raise ValueError("历史项目已有同名差异文件，停止避免覆盖。")
    pdf_dir = out / "pdf"
    pdf_dir.mkdir()
    try:
        delta = execute([latexdiff, "--encoding=utf8", "--flatten", "--config", "MINWORDSBLOCK=0",
                         str(old_doc), str(new_doc)], new_doc.parent)
        diff_tex.write_bytes(b"\\PassOptionsToPackage{normalem}{ulem}\n" + delta)
        env = {k: v for k, v in os.environ.items() if k.upper() not in LOCATORS}
        env.update(LC_ALL="C", LC_CTYPE="C", LANG="C")
        build = subprocess.run([latexmk, "-pdf", "-synctex=1", "-interaction=nonstopmode",
                                "-file-line-error", "-jobname=revision-diff", f"-outdir={pdf_dir}", str(diff_tex)],
                               cwd=new_doc.parent, env=env, capture_output=True)
        (out / "compile.stdout.log").write_bytes(build.stdout)
        (out / "compile.stderr.log").write_bytes(build.stderr)
        if build.returncode:
            raise RuntimeError(f"差异稿编译失败；请查看 {out / 'compile.stdout.log'}。未修改原手稿。")
    except Exception as error:
        (out / "failure.txt").write_text(str(error), encoding="utf-8")
        raise
    pdf = pdf_dir / "revision-diff.pdf"
    if not pdf.is_file():
        raise RuntimeError("工具没有生成 PDF。")
    return pdf


def compare(document, old, new, git, latexdiff, latexmk):
    document = Path(document).resolve(strict=True)
    if document.suffix.lower() != ".tex":
        raise ValueError("请选择实际主文档 .tex。")
    if not re.search(r"\\documentclass\b", document.read_text(encoding="utf-8-sig")):
        raise ValueError("请先打开含 documentclass 的实际主文档，再比较历史。")
    root = Path(execute([git, "rev-parse", "--show-toplevel"], document.parent).decode("utf-8").strip()).resolve(strict=True)
    relative = document.relative_to(root)
    for revision in (old, new):
        if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
            raise ValueError("版本必须是已选择提交的完整 SHA。")
    output_parent = document.parent / ".latex-build" / "history-diff"
    output_parent.mkdir(parents=True, exist_ok=True)
    out = Path(tempfile.mkdtemp(prefix=datetime.datetime.now().strftime("%Y%m%d-%H%M%S-"), dir=output_parent))
    for label, revision in (("old", old), ("new", new)):
        archive = out / f"{label}.tar"
        with archive.open("wb") as sink:
            execute([git, "archive", "--format=tar", revision], root, stdout=sink)
        destination = out / label
        destination.mkdir()
        with tarfile.open(archive) as tar:
            for member in tar.getmembers():
                name = PurePosixPath(member.name)
                if name.is_absolute() or ".." in name.parts or any(":" in s or "\\" in s or s == ".git" for s in name.parts):
                    raise ValueError("历史归档存在不安全路径。")
                if not (member.isfile() or member.isdir()):
                    raise ValueError("历史归档包含链接或特殊文件，已停止。")
                if not (destination / member.name).resolve().is_relative_to(destination.resolve()):
                    raise ValueError("历史归档路径越界。")
            tar.extractall(destination, filter="data")
        if not (destination / relative).is_file():
            raise ValueError(f"{label} 版本没有当前主文档。")
    old_doc = out / "old" / relative
    new_doc = out / "new" / relative
    pdf = render_comparison(old_doc, new_doc, out, latexdiff, latexmk)
    (out / "comparison.json").write_text(json.dumps({"document": str(document), "old": old, "new": new,
                                                    "engine": "pdfLaTeX", "pdf": str(pdf)}, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"pdf": str(pdf), "output": str(out)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for name in ("document", "old", "new", "git", "latexdiff", "latexmk"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    print(json.dumps(compare(args.document, args.old, args.new, args.git, args.latexdiff, args.latexmk), ensure_ascii=False))
