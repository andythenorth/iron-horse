#!/usr/bin/env python3

import re
from pathlib import Path

ROOT = Path("src/vehicles")

RAW_FREE_IDS = """
24820, 26390, 26410, 26690, 26710, 26730, 26750, 26770, 26790, 26830, 26850, 26870, 26900, 26920, 27050, 27070, 27200, 27220, 27250, 27270, 27410, 27430, 27450, 27470, 27490, 27510, 27530, 27560, 27580, 27600, 27620, 27640, 27660, 27680, 27700, 27720, 27740, 27760, 27780, 27800, 27840, 27860, 27890, 28000, 28020, 28040, 28060, 28080, 28100, 28140, 28160, 28210, 28230, 28330, 28360, 28380, 28400, 28420, 28460, 28540, 28560, 28580, 28600, 28620, 28640, 28660, 28720, 28740, 28760, 28780, 28800, 28820, 28840, 28860, 28880, 28900, 28920, 28940, 28960, 28980, 29010, 29030, 29050, 29070, 29120, 29140, 29160, 29180, 29200, 29220, 29240, [29260 to 29840], 29860, 29880, 29900, 29920, 29940, 29960, 29980, 30100, 30120, 30140, 30160, 30180, 30200, 30230, 30250, 30270, 30290, 30310, 30340, 30380, 30420, 30440, 30540, 30560, 30590, 30740, 30840, 30860, 30880, 30910, 30980, 31030, 31050, 31080, 31110, 31170, 31190, 31210, 31230, 31250, 31270, 31290, 31310, 31340, 31420, 31460, 31480, 31500, 31520, 31540, 31560, 31580, 31600, 31620, 31640, 31660, 31680, 31700, 31720, 31740, 31800, 31870, 31890, 32030, 32300, 32320, 32340, 32360, 32380, 32400, 32420, 32440, [32470 to 32650], 33080, 33100, 33300, 33320, 33340, 33360, [33470 to 33710], 33730, 33750, 33770, 33790, 33810, 33830, 33850, 33870, 33890, 33910, 33930, 33950, 33970, 33990, 34010, 34030, 34050, 34070, 34090, 34110, 34130, 34150, 34170, 34200, 34220, 34240, [34260 to 64990]
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
