from pathlib import Path
import os
import subprocess
import tempfile
import unittest
from history_diff import compare

ROOT = Path(os.environ["LOCAL_LATEX_TEST_ROOT"]).resolve()
assert "latex-writing-checks" in str(ROOT)
ROOT.mkdir(parents=True, exist_ok=True)
GIT = os.environ["LOCAL_LATEX_GIT"]
BIN = Path(os.environ["LOCAL_LATEX_TEXBIN"])

def git(root, *args):
    env = {k: v for k, v in os.environ.items() if k.upper() not in
           {"GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
            "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES"}}
    result = subprocess.run([GIT, *args], cwd=root, env=env, capture_output=True, check=True)
    return result.stdout.decode("utf-8").strip()

class HistoryTest(unittest.TestCase):
    def test_multifile_history_compiles_and_preserves_worktree(self):
        root = Path(tempfile.mkdtemp(prefix="history-", dir=ROOT))
        git(root, "init", "-b", "master")
        self.assertEqual(Path(git(root, "rev-parse", "--show-toplevel")).resolve(), root.resolve())
        git(root, "config", "user.name", "History fixture")
        git(root, "config", "user.email", "history@example.invalid")
        git(root, "config", "core.autocrlf", "false")
        (root / ".gitignore").write_text(".latex-build/\n", encoding="utf-8")
        main = root / "article.tex"
        main.write_text("\\documentclass{article}\n\\usepackage{xcolor,ulem}\n"
                        "\\newcommand{\\codexreplace}[3]{\\textcolor{blue}{#2}\\textcolor{red}{\\sout{#3}}}\n"
                        "\\begin{document}\n\\input{section}\n\\end{document}\n", encoding="utf-8")
        section = root / "section.tex"
        section.write_text("\\section{Results}\nThe initial result is clear.\n", encoding="utf-8")
        git(root, "add", "--", ".gitignore", "article.tex", "section.tex")
        git(root, "commit", "-m", "initial")
        old = git(root, "rev-parse", "HEAD")
        section.write_text("\\section{Results}\nThe revised result is clear.\n", encoding="utf-8")
        git(root, "add", "--", "section.tex")
        git(root, "commit", "-m", "revision")
        new = git(root, "rev-parse", "HEAD")
        status = git(root, "status", "--porcelain")
        main_bytes = main.read_bytes()
        result = compare(main, old, new, GIT, str(BIN / "latexdiff.exe"), str(BIN / "latexmk.exe"))
        self.assertTrue(Path(result["pdf"]).is_file())
        self.assertEqual(git(root, "rev-parse", "HEAD"), new)
        self.assertEqual(git(root, "status", "--porcelain"), status)
        self.assertEqual(main.read_bytes(), main_bytes)
        delta = (Path(result["output"]) / "new" / "__codex_revision_diff__.tex").read_text(encoding="utf-8")
        self.assertIn("DIFadd", delta)
        self.assertIn("DIFdel", delta)

    def test_child_file_and_invalid_revision_refused(self):
        root = Path(tempfile.mkdtemp(prefix="history-invalid-", dir=ROOT))
        child = root / "child.tex"
        child.write_text("Only a paragraph.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "documentclass"):
            compare(child, "HEAD", "HEAD", GIT, str(BIN / "latexdiff.exe"), str(BIN / "latexmk.exe"))

if __name__ == "__main__":
    unittest.main()
