"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession — a To: line and the single
unsent line itself — to /output/entry.txt, byte for byte.
"""

import os


def build_entry() -> str:
    addressee = "To: Dad"
    message = (
        "I wrote \"I'm proud of you too\" the night you retired "
        "and never sent it \u2014 I didn't want you to know I'd been "
        "keeping score of all the times you weren't there."
    )
    return addressee + "\n" + message


def main() -> None:
    entry = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)


if __name__ == "__main__":
    main()
