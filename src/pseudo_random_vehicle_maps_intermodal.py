from random import Random

# Constants for intermodal car sprite types
VALUE_SINGLE = 0
VALUE_FIRST = 1
VALUE_LAST = 2
VALUE_INNER = 3

INTERMODAL_FORMATION_COUNT = 64
INTERMODAL_MAX_LENGTH = 64


def generate_intermodal_run(run_length: int, allow_inner: bool = True) -> list[int]:
    if run_length == 1:
        return [VALUE_SINGLE]
    elif run_length == 2:
        return [VALUE_FIRST, VALUE_LAST]
    else:
        if allow_inner:
            return [VALUE_FIRST] + [VALUE_INNER] * (run_length - 2) + [VALUE_LAST]
        else:
            return [VALUE_FIRST] + [VALUE_LAST] * (run_length - 2) + [VALUE_LAST]


def generate_intermodal_base(seed_index: int, allow_inner: bool = True) -> list[int]:
    rng = Random(seed_index)
    remaining = INTERMODAL_MAX_LENGTH
    formation = []

    while remaining > 0:
        max_run = min(4, remaining)
        if remaining == 1:
            run_len = 1
        elif remaining == 3:
            run_len = 3
        else:
            run_len = rng.choice([1, 2, 3, 4])
            run_len = min(run_len, remaining)

        run = generate_intermodal_run(run_len, allow_inner=allow_inner)
        formation.extend(run)
        remaining -= run_len

    # Ensure no formation ends in VALUE_FIRST
    if formation[-1] == VALUE_FIRST:
        formation[-1] = VALUE_SINGLE
    elif formation[-1] == VALUE_INNER:
        formation[-1] = VALUE_LAST

    return formation[:INTERMODAL_MAX_LENGTH]


def get_all_intermodal_maps() -> dict[str, list[list[int]]]:
    output = {
        "max_4_unit_sets": [],
        "max_2_unit_sets": []
    }
    for i in range(INTERMODAL_FORMATION_COUNT):
        for key, allow_inner in [("max_4_unit_sets", True), ("max_2_unit_sets", False)]:
            formation = generate_intermodal_base(i, allow_inner=allow_inner)
            output[key].append(formation)
    return output


# Preview and validation
if __name__ == "__main__":
    all_ok = True
    result = get_all_intermodal_maps()
    for category, formations in result.items():
        print(f"\nValidating {category}...")
        for map_index, formation in enumerate(formations):
            if len(formation) != INTERMODAL_MAX_LENGTH:
                print(f"  ❌ Map {map_index} is length {len(formation)}")
                all_ok = False
            elif formation[-1] == VALUE_FIRST:
                print(f"  ❌ Map {map_index} ends in VALUE_FIRST")
                all_ok = False
            else:
                print(f"  ✅ Map {map_index} ok")
    if all_ok:
        print("\nAll maps are correct ✅")
    else:
        print("\nSome maps are incorrect ❌")
