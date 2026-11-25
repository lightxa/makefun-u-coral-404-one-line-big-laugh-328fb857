#!/usr/bin/env python3
"""One Line, Big Laugh.

Writes a single funny line of at most 200 characters to /output/entry.txt.
Deterministic, stdlib only, no network at runtime.
"""

from pathlib import Path

LINE = "My AI wrote my wedding vows. It rhymed 'forever' with 'terms and conditions apply'."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
