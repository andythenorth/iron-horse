"""
Deterministic entropic formation maps for ruleset-based vehicle rendering.

This module generates fixed-length formations of 64 vehicles, structured into
run-lengths of 1–4. Each run is built with sprite roles:
  0 = single
  1 = first
  2 = last
  3 = inner

Each ruleset defines its own constraints:
  - "max_4_unit_sets": allows inner vehicles, max run length 4
  - "max_2_unit_sets": no inner vehicles, max run length 2

Used in NML rulesets to drive:
  - Sprite role selection
  - Consistent recolor groups per run
  - Consistent base vehicle type per run

All maps are deterministic (seed = index). Run groupings can be derived
via `generate_map_for_random_choices(...)`.

Note: The first and last vehicles in a sliced formation may not be correct.
Consumers must explicitly reassign sprite roles at formation edges.
"""

from random import Random

# Constants for sprite types
VALUE_SINGLE = 0
VALUE_FIRST = 1
VALUE_LAST = 2
VALUE_INNER = 3

DEFAULT_FORMATION_COUNT = 64
DEFAULT_MAX_LENGTH = 64

RULESET_CONFIG = {
    "max_4_unit_sets": {"allow_inner": True, "max_run_length": 4},
    "max_2_unit_sets": {"allow_inner": False, "max_run_length": 2},
}

def generate_entropic_run(run_length: int, allow_inner: bool = True) -> list[int]:
    if run_length == 1:
        return [VALUE_SINGLE]
    elif run_length == 2:
        return [VALUE_FIRST, VALUE_LAST]
    else:
        if allow_inner:
            return [VALUE_FIRST] + [VALUE_INNER] * (run_length - 2) + [VALUE_LAST]
        else:
            raise ValueError("Run length > 2 is not allowed when inners are disabled")

def generate_base_maps_for_ruleset(seed_index: int, config: dict) -> list[int]:
    rng = Random(seed_index)
    remaining = DEFAULT_MAX_LENGTH
    formation = []

    while remaining > 0:
        if config["allow_inner"]:
            if remaining == 1:
                run_len = 1
            elif remaining == 3:
                run_len = 3
            else:
                run_len = rng.choice([1, 2, 3, 4])
                run_len = min(run_len, config["max_run_length"], remaining)
        else:
            run_len = rng.choice([1, 2]) if remaining >= 2 else 1

        run = generate_entropic_run(run_len, allow_inner=config["allow_inner"])
        formation.extend(run)
        remaining -= run_len

    if formation[-1] == VALUE_FIRST:
        formation[-1] = VALUE_SINGLE
    elif formation[-1] == VALUE_INNER:
        formation[-1] = VALUE_LAST

    return formation[:DEFAULT_MAX_LENGTH]

def generate_run_randomization_map(formation: list[int], max_value: int, rng: Random) -> list[int]:
    if max_value < 2:
        raise ValueError("max_value must be at least 2")

    output = []
    i = 0
    while i < len(formation):
        if formation[i] == VALUE_SINGLE:
            run_len = 1
        elif formation[i] == VALUE_FIRST:
            run_len = 1
            while i + run_len < len(formation) and formation[i + run_len] in (VALUE_INNER, VALUE_LAST):
                if formation[i + run_len] == VALUE_LAST:
                    run_len += 1
                    break
                run_len += 1
        else:
            run_len = 1

        value = rng.randint(0, max_value - 1)
        output.extend([value] * run_len)
        i += run_len

    if len(set(output)) == 1:
        print(f"⚠️  All values are the same in run map: {output[0]}")

    return output

def generate_map_for_ruleset() -> dict[str, list[list[int]]]:
    output = {key: [] for key in RULESET_CONFIG}
    for i in range(DEFAULT_FORMATION_COUNT):
        for key, config in RULESET_CONFIG.items():
            formation = generate_base_maps_for_ruleset(i, config)
            output[key].append(formation)
    return output

def generate_map_for_random_choices(max_random_value: int) -> dict[str, list[list[int]]]:
    base_maps = generate_map_for_ruleset()
    output = {key: [] for key in RULESET_CONFIG}
    for category, formations in base_maps.items():
        for i, formation in enumerate(formations):
            rng = Random(i)
            run_map = generate_run_randomization_map(formation, max_random_value, rng)
            output[category].append(run_map)
    return output

# Preview and validation
if __name__ == "__main__":
    all_ok = True
    result = generate_map_for_ruleset()
    for category, formations in result.items():
        print(f"\nValidating {category}...")
        for map_index, formation in enumerate(formations):
            if len(formation) != DEFAULT_MAX_LENGTH:
                print(f"  ❌ Map {map_index} is length {len(formation)}")
                all_ok = False
            elif formation[-1] == VALUE_FIRST:
                print(f"  ❌ Map {map_index} ends in VALUE_FIRST")
                all_ok = False
            else:
                print(f"  ✅ Map {map_index} ok")

    print("\nRun-level randomization preview:")
    run_maps = generate_map_for_random_choices(8)
    for i, category in enumerate(RULESET_CONFIG):
        sample_form = result[category][0]
        sample_runs = run_maps[category][0]
        print(f"  → {category} map 0:")
        print("    Formation:", sample_form)
        print("    Run IDs:  ", sample_runs)

    if all_ok:
        print("\nAll maps are correct ✅")
    else:
        print("\nSome maps are incorrect ❌")
