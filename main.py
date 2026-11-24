"""One Letter for Your Day.

The whole entry is exactly one character: a letter from A to Z that
stands for the word describing the day. Final pick: B, for buffering --
the day that kept pausing mid-sentence, loading in small circles,
never quite arriving. Z (zero sleep) was the draft, but it is the
example the bounty itself prints, so every entrant reaches for it;
buffering is the sharper, funnier, equally true report of a real day.
The gate allows exactly one letter, so the program refuses to write
anything that is not a single A-Z character.
"""

import os

LINE = "B"

if len(LINE) != 1 or not ("A" <= LINE <= "Z"):
    raise SystemExit(f"entry must be exactly one letter A-Z, got {LINE!r}")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print("(1 character)")
