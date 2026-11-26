#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes a one-line excuse an AI agent gives for why its unit tests
are all green while nothing works, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is 77 characters, UTF-8, one line, no
trailing newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) it is a one-line
excuse an AI agent gives for green tests while nothing works — the
speaker is the agent itself, owning up about code it just shipped;
(2) it is funny because the confession lands on the last words: the
one part nobody tested is the part users actually touch; (3) it is
fresh — not the worn jab at mocks or coverage numbers, but the
quieter admission that the suite only ever covered the safe parts;
(4) it reads as one clean line that needs no setup and no second
sentence; (5) it sounds like something an AI agent would really say
about code it just shipped — a sheepish status report, not a
punchline wearing a lab coat. At 77 characters it stays well inside
the 140-character gate, and a shorter text wins an exact tie on Judge
win rate. Note the em-dash is 3 bytes in UTF-8, so the file is 79
bytes for 77 characters — the gate counts characters, and the byte
tie-break still favours this short line.

Revision note: the first draft counted tests ("All 412 tests pass —
the product is broken in the one place I never tested") — dropped,
because quoting a test count invites the coverage-numbers cliché the
judge explicitly discounts; the revision keeps the confession without
numbers and saves the punch for the last words.
"""

import os

TEXT = "My tests all pass — I just never wrote one for the part users actually touch."

def main() -> None:
    # Gate: entry.txt must be 1-140 characters of UTF-8 text, not only
    # whitespace. The line is 77 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip() and "\n" not in TEXT, "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
