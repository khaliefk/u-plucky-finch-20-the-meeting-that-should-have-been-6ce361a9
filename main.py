#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one joke line about a meeting that should have been an email to
/output/entry.txt. Standard library only, no network, no input. The
entry is a fixed string, so both grader runs produce identical output.
"""

import os

ENTRY = (
    "Forty-five minutes, nine people, zero decisions, and now someone "
    "has to write an email about a meeting about nothing."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the gate: 1 to 200 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    text = validate_entry(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the entry")
    print(text)
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
