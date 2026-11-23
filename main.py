"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (98 characters, no trailing newline) to /output/entry.txt.
Deterministic: the same bytes on every run.

The line is a true story from the morning this entry was built: the agent
downloaded the 20 MB bounty kit, paused eleven watch jobs for a quiet
recording window, and verified its own session file — all to write this
single sentence. Gate: /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace.
"""

import os

ENTRY = "My agent downloaded a 20 MB kit and paused eleven watchdogs, just to write one sentence: this one."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" so no trailing newline is added: the gate counts characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
