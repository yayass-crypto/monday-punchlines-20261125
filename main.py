#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

The competition gate: /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace. This program writes exactly one joke
that satisfies the gate and the published judge brief:

  1. It is about Monday mornings, unambiguously.
  2. It earns a laugh with a turn that lands (the reflection calls in
     sick; the speaker has to cover its shift), not a complaint.
  3. The twist surprises: a mirror image refusing Monday is not the
     first thing anyone thinks of.
  4. Every word does work — 76 characters, no wasted setup.
  5. It is fresh: no alarm, snooze, bed-custody, coffee, HR or
     weekend-invoice cliche (the crowded lanes of the live field).
"""

import os

JOKE = "Monday morning, my reflection called in sick. I had to go in for both of us."

MAX_CHARS = 200


def validate(text):
    """Return the entry text, or raise if it fails the gate.

    The gate counts characters, so the check is on the stripped text:
    an entry that is only whitespace fails even though it has length.
    """
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    checked = text.strip()
    if len(checked) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character gate"
            % (len(checked), MAX_CHARS)
        )
    return checked


def main():
    joke = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(joke)
    print("wrote %d characters to %s: %r" % (len(joke), path, joke))


if __name__ == "__main__":
    main()
