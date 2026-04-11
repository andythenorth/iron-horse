#!/usr/bin/env python3

import re
from pathlib import Path

ROOT = Path("src/vehicles")

RAW_FREE_IDS = """
28560, 28600, 29270, 29290, 29310, 29330, [29350 to 29840], 29860, 29880, 29900, 29920, 29940, 29960, 29980, 30100, 30120, 30140, 30160, 30180, 30200, 30230, 30250, 30270, 30290, 30310, 30340, 30380, 30420, 30440, 30540, 30560, 30590, 30740, 30840, 30860, 30880, 30910, 30980, 31030, 31050, 31080, 31110, 31170, 31190, 31210, 31230, 31250, 31270, 31290, 31310, 31340, 31420, 31460, 31480, 31500, 31520, 31540, 31560, 31580, 31600, 31620, 31640, 31660, 31680, 31700, 31720, 31740, 31800, 31870, 31890, 32030, 32300, 32320, 32340, 32360, 32380, 32400, 32420, 32440, [32470 to 32650], [32750 to 64990]
"""

BATCH_SIZE = 50
STEP = 20
DRY_RUN = False
#DRY_RUN = True


ID_PATTERN = re.compile(r"base_numeric_id\s*=\s*(\d+)")


def parse_free_ids(raw: str):
    result = set()

    tokens = re.split(r",|\n", raw)

    for tok in tokens:
        tok = tok.strip()
        if not tok:
            continue

        # strip brackets
        tok = tok.strip("[]")

        if "to" in tok:
            start, end = tok.split("to")
            start = int(start.strip())
            end = int(end.strip())

            for v in range(start, end + 1, STEP):
                result.add(v)
        else:
            result.add(int(tok))

    return sorted(result)


def find_used_ids():
    used = []
    locations = {}

    for path in ROOT.rglob("*.py"):
        lines = path.read_text().splitlines()

        for i, line in enumerate(lines):
            m = ID_PATTERN.search(line)
            if m:
                vid = int(m.group(1))
                used.append(vid)
                locations.setdefault(vid, []).append((path, i))

    return sorted(set(used)), locations


def pick_moves(used_ids, free_ids, batch_size):
    used_sorted = sorted(used_ids, reverse=True)
    free_sorted = sorted(free_ids)

    moves = []
    free_idx = 0

    for old in used_sorted:
        while free_idx < len(free_sorted) and free_sorted[free_idx] >= old:
            free_idx += 1

        if free_idx >= len(free_sorted):
            break

        new = free_sorted[free_idx]
        moves.append((old, new))
        free_idx += 1

        if len(moves) >= batch_size:
            break

    return moves


def apply_moves(moves, locations):
    for old, new in moves:
        for path, line_idx in locations[old]:
            lines = path.read_text().splitlines()

            lines[line_idx] = re.sub(
                r"\d+",
                str(new),
                lines[line_idx],
                count=1,
            )

            if not DRY_RUN:
                path.write_text("\n".join(lines) + "\n")

        print(f"{old} -> {new}")


def main():
    free_ids = parse_free_ids(RAW_FREE_IDS)
    used_ids, locations = find_used_ids()

    moves = pick_moves(used_ids, free_ids, BATCH_SIZE)

    print(f"Planned moves ({len(moves)}):")
    for old, new in moves:
        print(f"  {old} -> {new}")

    apply_moves(moves, locations)


if __name__ == "__main__":
    main()
