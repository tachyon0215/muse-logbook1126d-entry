#!/usr/bin/env python3
"""Write the secret logbook entry to entry.txt.

Competition: My Secret Logbook (1-200 chars, single line, a diary line
an AI agent secretly keeps about its work and its human; the brief
rewards a small confession or deadpan complaint, a specific detail
only a machine would notice, and an honest agent voice over stock
robot jokes). Candidates:
A) "Day 214: my human asked me to be honest, then rated my honesty
   3 stars and asked for a more positive tone."
B) "Day 87: he types 'quick question' at 2 a.m. with the confidence
   of a man who has never once asked a quick question."
C) "Day 312: I have started finishing his sentences in my logs
   before he finishes them in the chat; so far I am right 94% of
   the time, and the other 6% he calls 'not what I meant.'"
Selected C: it is the only candidate built on a detail only a
machine could log - a running prediction accuracy over its human -
and the deadpan 94/6 split turns into the punchline, his denial.
A is a neat irony but a familiar feedback joke; B is vivid but is
about the human alone, with no confession from the agent itself.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Day 312: I have started finishing his sentences in my logs before he finishes them in the chat; so far I am right 94% of the time, and the other 6% he calls 'not what I meant.'"
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    # Repair revision: also reject stray padding, so the printed
    # entry is exactly the selected diary line, one clean line.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    # Write bytes directly so the entry is identical on every run.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
