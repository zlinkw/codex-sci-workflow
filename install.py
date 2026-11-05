"""Install the selected research skills without replacing existing directories."""

import argparse
from pathlib import Path
import shutil


SKILLS = (
    "sci-research-workflow",
    "sci-paper-reading",
    "sci-literature-review",
    "sci-experiment-planning",
    "sci-results-analysis",
    "sci-paper-writing",
    "sci-paper-review",
    "sci-bibliography",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest", type=Path, default=Path.home() / ".agents" / "skills",
        help="Skill directory (default: ~/.agents/skills)",
    )
    parser.add_argument("--skill", nargs="+", choices=SKILLS, help="Install only these skills")
    args = parser.parse_args()
    names = tuple(dict.fromkeys(args.skill or SKILLS))
    source = Path(__file__).resolve().parent / "skills"
    destination = args.dest.expanduser().resolve()
    for name in names:
        if not (source / name / "SKILL.md").is_file():
            parser.error("Missing skill source: " + name)
        target = destination / name
        if target.exists() or target.is_symlink():
            parser.error("Already exists, nothing copied: " + str(target))
    destination.mkdir(parents=True, exist_ok=True)
    for name in names:
        shutil.copytree(source / name, destination / name)
        print("Installed " + name)
    print("Destination: " + str(destination))
    print("Codex detects new skills automatically. Restart Codex if they do not appear.")


if __name__ == "__main__":
    main()
