"""The 4AM Commit — make.fun entry.

Writes one fixed commit message to /output/entry.txt.
Deterministic: no randomness, no network, no file reads,
no git history — the same string every run.
"""

import os
from pathlib import Path

ENTRY = (
    "fix: at 4am I found the bug \u2014 my midnight fix "
    "for my 2am bug \u2014 and the only reviewer awake was also me"
)


def main() -> None:
    # One line, no trailing newline: the gate counts characters,
    # so the file holds exactly the commit message and nothing else.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
