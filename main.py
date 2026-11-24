#!/usr/bin/env python3
"""Most Honest Outage Line: write one honest status-page line to /output/entry.txt.

Pure stdlib. Writes the line with no trailing newline.
"""

import os

PART_A = "Our API, dashboard, and database are down, and so is the monitoring I would use to check them."
PART_B = " I cannot confirm your data is safe yet. This page updates first."

LINE = PART_A + PART_B


def main():
    assert 1 <= len(LINE) <= 160, "line must be 1-160 chars"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
