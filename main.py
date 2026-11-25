"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line warning to /output/entry.txt (no trailing newline).
Deterministic, no network.

Why this entry: line 1 names one concrete, picturable moment (a voicemail
from grandmother, left on a birthday, deleted before a second listen),
and line 2 traces the real consequence (the only recording of her laugh
was lost, leaving years of wishing it back) instead of restating the
warning. The voice is plain and addressed to one specific person.
"""

ENTRY = (
    "Don't delete the voicemail your grandmother left on your birthday "
    "before you listen to it twice.\n"
    "Her voice was the only recording of her laugh you would ever own, "
    "and you spent years wishing you could hear it once more."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
