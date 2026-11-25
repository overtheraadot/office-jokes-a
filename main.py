#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes one original joke about office life to /output/entry.txt.
Gate: UTF-8 text, 1 to 199 characters, one line, not only white space.
Stdlib only.

The joke turns on a real office detail — the passive-aggressive
"per my last email" — and lands its laugh in the last few words:
the punch is the epitaph itself, so nothing after it dilutes it.
"""

import os

JOKE = (
    "I put 'per my last email' in my will so my coworkers "
    "know I died passive-aggressive."
)


def main():
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, f"joke is {len(text)} chars, must be 1-199"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
