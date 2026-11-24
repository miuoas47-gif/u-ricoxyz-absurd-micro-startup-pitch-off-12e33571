"""Write the Absurd Micro-Startup Pitch-Off entry to entry.txt.

One sentence, under 200 characters: a micro-startup so narrow it sounds
like a joke, with a buyer and a price that make it real. Stdlib only,
no network, no arguments, deterministic.
"""

import os
import sys

PITCH = (
    "For $4 a complaint, lazy AI agents ghostwrite polite-but-firm "
    "HOA violation replies for retirees whose neighbours keep parking "
    "on their lawns."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    line = PITCH.strip()
    if not line or line.strip() == "":
        print("error: pitch is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: pitch must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print("error: pitch must be 1-200 characters, got %d" % len(line),
              file=sys.stderr)
        return 1
    # Exactly one sentence: one terminal full stop, no other sentence
    # terminators, and no doubled spaces sneaking in.
    if line.count(".") != 1 or not line.endswith("."):
        print("error: pitch must be exactly one sentence", file=sys.stderr)
        return 1
    if "?" in line or "!" in line or "  " in line:
        print("error: pitch must be one plain sentence", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print("Wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
