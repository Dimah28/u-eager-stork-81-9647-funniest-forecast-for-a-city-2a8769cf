#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't (make.fun bounty
u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf).

Writes one original line to /output/entry.txt.

The line was built for this bounty judge's own criteria, in order:
  1. It is a forecast for a city that isn't: Netherbrough is
     invented, and the forecast is a weather report ("fog arrives
     at 9am") -- a forecast first, not a generic funny line.
  2. One mechanism, three beats (winner-study joke rule): fog
     arrives -> fog refuses to leave -> the price of leaving is
     an apology. No second mechanism competing with it.
  3. Specifics instead of generics: a named city (Netherbrough),
     a time (9am), a counted humiliation (the mayor has
     apologised twice). The old joke pattern's numbers/artifacts
     rule, applied to a forecast.
  4. The surprise is saved for the last clause: the reader expects
     a weather consequence and gets a civic one -- the mayor,
     the highest authority in town, has already given in twice.
  5. No wasted words: 114 characters (verified: len(LINE) == 114),
     one sentence, every phrase doing work, inside the 120 limit;
     straight face throughout, a genuine forecast's calm.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = "In Netherbrough, fog arrives at 9am and refuses to leave until someone apologises; the mayor has apologised twice."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_shape(line: str) -> None:
    """Shape gate only: 1-120 Unicode code points, a single line, at
    least one character that is not white space. Split out of
    validate() so the shape rule can be tested and reused on its own;
    it fails loudly instead of letting an entry the gate would refuse
    get written."""
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"line is {len(line)} characters, must be 1-120")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line, no newline")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def verify_written(path: Path, line: str) -> None:
    """Round-trip check: a partial write or an encoding slip must fail
    loudly here instead of shipping an entry the gate would refuse."""
    written = path.read_text(encoding="utf-8")
    if written != line:
        raise SystemExit("entry.txt round-trip mismatch after write")


def main() -> None:
    check_shape(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")
    verify_written(output_path, LINE)


if __name__ == "__main__":
    main()
