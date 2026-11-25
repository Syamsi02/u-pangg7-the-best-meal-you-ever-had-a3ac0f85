"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal
ever had to /output/entry.txt. Pure standard library, deterministic:
the same sentence on every run.
"""

import os

ENTRY = (
    "My grandmother's rendang in Bandung \u2014 beef so dark and slow "
    "it fell apart on the rice, coconut gravy on my chin, and me "
    "licking the spoon while the whole table pretended not to notice."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1, "entry must be a single sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
