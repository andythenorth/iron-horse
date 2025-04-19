from math import ceil
from random import Random
from collections import defaultdict
from itertools import product

# Constants
MAP_LENGTHS = [3, 8, 16, 32]  # Only generate maps for these lengths
VALUE_FIRST = 0
VALUE_LAST = 1
VALUE_SPECIAL = 2

# Number of maps to generate per length
# We don't need all lengths, just a selection, and we'll offset into them via vehicle position as needed
MAP_COUNTS = {
    3: 16,
    8: 32,
    16: 32,
    32: 32,
}

SPECIAL_RUN_WEIGHTS = [1, 1, 2, 2, 2, 3]

def generate_empty_map_structure():
    """
    Generate an empty map structure: {chain_length: [[], [], ...]}
    """
    return {
        length: [[] for _ in range(MAP_COUNTS[length])]
        for length in MAP_LENGTHS
    }

def generate_mail_map(length: int, seed: int) -> list[int]:
    if length == 3:
        valid = [list(p) for p in product([0, 1, 2], repeat=3) if 2 in p]
        return valid[seed % len(valid)]

    rnd = Random(seed)
    result = [None] * length

    # Fill first and last (can be 0, 1, or 2)
    result[0] = rnd.choice([VALUE_FIRST, VALUE_LAST, VALUE_SPECIAL])
    result[-1] = rnd.choice([VALUE_FIRST, VALUE_LAST, VALUE_SPECIAL])

    # Fill ~30% of middle with runs of VALUE_SPECIAL
    middle_indices = list(range(1, length - 1))
    num_special_slots = max(1, int((length - 2) * 0.30))
    filled = 0
    used = set()

    while filled < num_special_slots:
        run_len = rnd.choice(SPECIAL_RUN_WEIGHTS)
        start = rnd.choice(middle_indices)
        run_positions = []
        for offset in range(run_len):
            pos = start + offset
            if pos >= length - 1:
                break
            if result[pos] is None:
                run_positions.append(pos)
        if run_positions:
            for pos in run_positions:
                result[pos] = VALUE_SPECIAL
            filled += len(run_positions)

    # Fill remaining None values with mostly 0/1, occasional 2
    for i in range(1, length - 1):
        if result[i] is None:
            result[i] = rnd.choices(
                population=[VALUE_FIRST, VALUE_LAST, VALUE_SPECIAL],
                weights=[3, 3, 2],
                k=1
            )[0]

    return result

def validate_map(length: int, map_values: list[int]) -> bool:
    if length != len(map_values):
        return False
    if length == 3:
        return VALUE_SPECIAL in map_values
    if length > 3 and VALUE_SPECIAL not in map_values[1:-1]:
        return False
    return True

def get_all_mail_maps() -> list[dict]:
    """
    Generate and return all mail car maps in a more templating-friendly structure:
    [
        {"chain_length": 3, "maps": [[0,2,1], ...]},
        {"chain_length": 8, "maps": [...]},
        ...
    ]
    """
    output = []
    for length in MAP_LENGTHS:
        count = MAP_COUNTS[length]
        maps = []
        index = 0
        while len(maps) < count:
            seed = length * 100 + index
            map_values = generate_mail_map(length, seed)
            if validate_map(length, map_values):
                maps.append(map_values)
            index += 1
        output.append({"chain_length": length, "maps": maps})
    return output

if __name__ == "__main__":
    all_maps = get_all_mail_maps()
    for entry in all_maps:
        print(f"Chain length {entry['chain_length']}:")
        for i, m in enumerate(entry['maps']):
            print(f"  Map {i}: {m}")
