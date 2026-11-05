"""Small native-Git/LaTeX workflow regressions, not independent model evaluations.

Existing backend fixtures supply real staging/manual edits. Artifacts are retained.
"""
import json
import os
from pathlib import Path
import unittest
import zipfile

import source_review_test as fixtures
from source_review import Conflict, digest
import review_archive as archive
import submission

GIT, ROOT = fixtures.GIT, fixtures.ROOT


class Workflow(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.Flow("test_cross_file_partial_accept_reject_rework")
        self.f._testMethodName = self._testMethodName
        self.f.setUp()

    def test_review_backup_restore_and_continue(self):
        f = self.f
        f.write("index-removed.txt", "tracked in HEAD, removed only from the index\n")
        f.g("add", "index-removed.txt")
        f.g("commit", "--only", "-m", "fixture tracked asset", "--", "index-removed.txt")
        f.g("update-index", "--force-remove", "--", "index-removed.txt")
        f.edit("main.tex", "The model improves performance.", "The model may improve performance.")
        f.edit("section.tex", "The estimator is robust.", "The estimator may be robust.")
        f.edit("reply.tex", "Thank you for the comment.", "Thank you for the suggestion.", deps=["2"])
        e = f.review().inspect("2")
        f.runop("feedback", {"id": "2", "version": e["edit"]["versions"][-1], "side": "candidate", "start": 0,
                             "end": len(e["candidate"]), "quote": e["candidate"], "text": "语气弱一点，保留条件。"})
        f.runop("decide", ["1"], [])
        f.write("extra.bib", "@article{extra, title={Untracked source}}\n")
        before = {n: (f.root / n).read_bytes() for n in ("main.tex", "reply.tex", "section.tex", "other.txt", ".git/index")}
        out = ROOT / (self._testMethodName + ".zip")
        b = archive.backup(f.root, "reply.tex", out, GIT, ["extra.bib"])
        self.assertEqual(b["omitted_untracked"], [])
        for n, data in before.items():
            self.assertEqual((f.root / n).read_bytes(), data)
        restored = ROOT / (self._testMethodName + "-restored")
        archive.restore(out, restored, GIT)
        # No original repository access is used by these subsequent actions.
        r = archive.Review(restored, "reply.tex", GIT)
        self.assertEqual(r.state, f.review().state)
        self.assertEqual(r.git("ls-files", "--stage", "-z"), f.review().git("ls-files", "--stage", "-z"))
        self.assertEqual((restored / "other.txt").read_text(encoding="utf-8"), "unstaged author content\n")
        self.assertEqual((restored / "extra.bib").read_bytes(), (f.root / "extra.bib").read_bytes())
        self.assertEqual((restored / "index-removed.txt").read_bytes(), (f.root / "index-removed.txt").read_bytes())
        self.assertIn("语气弱一点", r.state["edits"]["2"]["requests"][0]["text"])
        updates, _ = r.propose({"after": "The estimator may be robust under the tested conditions.", "resolve_requests": [r.state["edits"]["2"]["requests"][0]["id"]]}, "2")
        r.persist(updates, digest(r.raw))
        r = archive.Review(restored, "reply.tex", GIT)
        self.assertEqual(r.state["edits"]["a"]["freshness"], "needs-recheck")
        updates, _ = r.decide([], ["a"])
        r.persist(updates, digest(r.raw))
        self.assertIn("Thank you for the comment.", (restored / "reply.tex").read_text(encoding="utf-8"))
        with self.assertRaises(Conflict):
            archive.restore(out, restored, GIT)

    def test_backup_reports_omissions_and_rejects_corruption(self):
        f = self.f
        f.write("untracked.bib", "omitted\n")
        out = ROOT / (self._testMethodName + ".zip")
        result = archive.backup(f.root, "reply.tex", out, GIT)
        self.assertEqual(result["omitted_untracked"], ["untracked.bib"])
        bad = ROOT / (self._testMethodName + "-corrupt.zip")
        with zipfile.ZipFile(out) as src, zipfile.ZipFile(bad, "x") as dst:
            for n in src.namelist():
                dst.writestr(n, b"changed" if n == "working/main.tex" else src.read(n))
        target = ROOT / (self._testMethodName + "-blocked")
        with self.assertRaises(Conflict):
            archive.restore(bad, target, GIT)
        self.assertFalse(target.exists())
        f.check_index()

    def test_gui_rejection_continuation_and_reply_only(self):
        f = self.f
        f.edit("main.tex", "The model improves performance.", "The model always improves performance.")
        f.edit("reply.tex", "Thank you for the comment.", "Thank you for the clarification.", deps=["1"])
        f.runop("decide", [], ["1"])
        # Fresh instance represents context recovery; rejected prose must remain absent.
        state = f.review().status()
        self.assertEqual(state["edits"]["1"]["status"], "rejected")
        self.assertEqual(state["edits"]["a"]["freshness"], "needs-recheck")
        original_main = (f.root / "main.tex").read_bytes()
        f.runop("propose", {"after": "Thank you for the clarification. The supported scope is unchanged."}, "a")
        self.assertEqual((f.root / "main.tex").read_bytes(), original_main)
        self.assertEqual(f.review().state["next"], [2, 2])
        f.check_index()

    def test_manual_overlap_blocks_and_pending_submission_stops(self):
        f = self.f
        f.edit("section.tex", "The estimator is robust.", "The estimator may be robust.")
        report = submission.preflight(f.root, "reply.tex", "main.tex", ["main.tex", "section.tex"], GIT)[-1]
        self.assertTrue(report["machine_blockers"])
        f.write("section.tex", f.read("section.tex").replace("may be robust", "has author revisions"))
        actual = (f.root / "section.tex").read_bytes()
        with self.assertRaises(fixtures.m.Conflict):
            f.runop("decide", [], ["1"])
        self.assertEqual((f.root / "section.tex").read_bytes(), actual)
        self.assertEqual(f.review().state["edits"]["1"]["status"], "pending")
        f.check_index()

    def test_submission_bibliography_is_derived_and_opt_in(self):
        f = self.f
        f.write("main.tex", f.read("main.tex").replace("\\end{document}",
                "A synthetic citation~\\cite{fixture}.\n\\bibliographystyle{plain}\n\\bibliography{refs}\n\\end{document}"))
        f.write("refs.bib", "@article{fixture, author={Example, A.}, title={Synthetic bibliography fixture}, journal={Test Fixture}, year={2026}}\n")
        originals = {n: (f.root / n).read_bytes() for n in ("main.tex", "section.tex", "reply.tex", "refs.bib", ".git/index")}
        checks = {k: {"verified": True, "evidence": "Synthetic bibliography/export correctness fixture only; not scientific or journal evidence."} for k in submission.CHECKS}
        latexmk = str(Path(os.environ["LOCAL_LATEX_TEXBIN"]) / "latexmk.exe")
        files = ["main.tex", "section.tex", "refs.bib"]
        for include in (False, True):
            dest = ROOT / (self._testMethodName + ("-with-bbl" if include else "-without-bbl"))
            result = submission.export(f.root, "reply.tex", "main.tex", files, dest, checks, latexmk, git=GIT, include_bbl=include)
            self.assertIn("\\bibcite{fixture}", (dest / "source/build/main.aux").read_text(encoding="utf-8"))
            with zipfile.ZipFile(result["source_zip"]) as z:
                self.assertEqual("main.bbl" in z.namelist(), include)
                self.assertFalse(any(n.startswith("build/") or n.endswith((".aux", ".log")) for n in z.namelist()))
                if include:
                    bbl = (dest / "source/build/main.bbl").read_bytes()
                    self.assertEqual(z.read("main.bbl"), bbl)
                    self.assertIn(b"\\bibitem{fixture}", bbl)
                    report = json.loads(Path(result["report"]).read_text(encoding="utf-8"))
                    self.assertEqual(report["generated_files"], {"main.bbl": digest(bbl)})
        for n, raw in originals.items():
            self.assertEqual((f.root / n).read_bytes(), raw)
        invalid = f.read("main.tex").replace("\\cite{fixture}", "\\cite{not_in_library}")
        f.write("main.tex", invalid)
        blocked = ROOT / (self._testMethodName + "-unresolved")
        with self.assertRaises(Conflict):
            submission.export(f.root, "reply.tex", "main.tex", files, blocked, checks, latexmk, git=GIT, include_bbl=True)
        self.assertFalse((blocked / "submission.zip").exists())
        self.assertEqual(f.read("main.tex"), invalid)
        f.check_index()

    def test_submission_strips_only_derived_comments_and_builds(self):
        f = self.f
        main = f.read("main.tex")
        f.write("main.tex", "% CODEX-RULES-BEGIN\n% 中文全局约定\n% CODEX-RULES-END\n% Scientific comment retained.\n" + main)
        originals = {n: (f.root / n).read_bytes() for n in ("main.tex", "section.tex", "reply.tex", ".git/index")}
        checks = {k: {"verified": True, "evidence": "Independent synthetic article; no scientific results or citations; fixture source and rendered build are the scoped checks, not a journal paper."} for k in submission.CHECKS}
        dest = ROOT / (self._testMethodName + "-export")
        texbin = Path(os.environ["LOCAL_LATEX_TEXBIN"])
        result = submission.export(f.root, "reply.tex", "main.tex", ["main.tex", "section.tex"], dest, checks, str(texbin / "latexmk.exe"), git=GIT)
        self.assertTrue(Path(result["pdf"]).is_file())
        with zipfile.ZipFile(result["source_zip"]) as z:
            clean = z.read("main.tex").decode("utf-8")
            self.assertNotIn("CODEX-", clean)
            self.assertIn("Scientific comment retained.", clean)
            self.assertIn("The model improves performance.", clean)
        blocked = ROOT / (self._testMethodName + "-missing-bbl")
        with self.assertRaises(Conflict):
            submission.export(f.root, "reply.tex", "main.tex", ["main.tex", "section.tex"], blocked, checks, str(texbin / "latexmk.exe"), git=GIT, include_bbl=True)
        self.assertFalse((blocked / "submission.zip").exists())
        for n, data in originals.items():
            self.assertEqual((f.root / n).read_bytes(), data)
        with self.assertRaises(Conflict):
            submission.strip_internal(b"% CODEX-RULES-BEGIN\n\\danger\n% CODEX-RULES-END\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
