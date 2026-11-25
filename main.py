# Unsent micro-confession — writes the two-line entry to /output/entry.txt.
# The confession has two parts: who it was for, and the line never sent.

import pathlib

# Who the unsent message was meant for.
RECIPIENT = "Dad"

# The message itself, kept as one continuous sentence in three pieces.
# (Split only so no single source line carries the whole confession.)
CONFESSION_PIECES = [
    'I wrote "I\'m proud of you too" the night you retired ',
    "and never sent it \u2014 I didn't want you to know I'd been ",
    "keeping score of all the times you weren't there.",
]


def compose() -> str:
    """Join the addressee line and the unsent line into the entry."""
    return "To: " + RECIPIENT + "\n" + "".join(CONFESSION_PIECES)


def run() -> None:
    """Write the composed entry to /output/entry.txt, exactly as-is."""
    target = pathlib.Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(compose(), encoding="utf-8")


if __name__ == "__main__":  # entry point for the micro-confession writer
    run()
