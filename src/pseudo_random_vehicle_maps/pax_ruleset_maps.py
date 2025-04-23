from math import floor, ceil
from random import Random

# Constants for coach type codes (adjusted for spriterow logic)
VALUE_STANDARD = 0
VALUE_BRAKE_FRONT = 1
VALUE_BRAKE_REAR = 2
VALUE_SPECIAL = 3
VALUE_CONDITIONAL_BRAKE_BEFORE = 4  # Shows brake if one of the previous 2 vehicles is a restaurant car
VALUE_CONDITIONAL_BRAKE_AFTER = 5  # Shows brake if one of the following 2 vehicles is a restaurant car

# 25 relates to map max length of 24 vehicles, to get wrap around on formations of 4/8, to get more brakes, without editing the generation logic
FORMATION_CLASSES = {
    "brakes_outer_ends": {"count": 8, "lengths": list(range(1, 25))},
    "brakes_inner_paired": {"count": 8, "lengths": list(range(1, 25))},
    "brakes_inner_spaced": {"count": 8, "lengths": list(range(1, 25))},
}

def insert_special_variants(base_map: list[int], seed: int = 0) -> list[int]:
    length = len(base_map)
    if length < 5:
        return base_map[:]
    elif length < 9:
        num_special = 1
    else:
        num_special = 2

    rng = Random(seed)
    mod_map = base_map[:]
    special_inserted = 0

    # Exclude ends and any position with brakes
    candidate_indexes = [
        i for i in range(1, length - 1)
        if base_map[i] == VALUE_STANDARD
    ]

    rng.shuffle(candidate_indexes)

    for idx in candidate_indexes:
        if special_inserted >= num_special:
            break
        mod_map[idx] = VALUE_SPECIAL
        special_inserted += 1

    return mod_map

def apply_family_offset(family: dict[int, list[int]], offset: int) -> dict[int, list[int]]:
    return {
        length: [value + offset for value in formation]
        for length, formation in family.items()
    }

def generate_type_a(length: int) -> dict[int, list[int]]:
    if length == 1:
        family = {1: [VALUE_BRAKE_FRONT]}
    elif length == 2:
        family = {2: [VALUE_BRAKE_FRONT, VALUE_BRAKE_REAR]}
    else:
        base = [VALUE_BRAKE_FRONT] + [VALUE_STANDARD] * (length - 2) + [VALUE_BRAKE_REAR]
        family = {length: insert_special_variants(base)}
    return apply_family_offset(family, 100)

def generate_type_b_family(seed_index: int) -> dict[int, list[int]]:
    rng = Random(seed_index)
    family = {}

    for length in range(1, 25):
        formation = [VALUE_STANDARD] * length

        if length <= 5:
            pos = min(length // 2, length - 1)
            formation[pos] = VALUE_BRAKE_FRONT
            family[length] = insert_special_variants(formation, seed_index)
            continue

        # Brake placement: fixed front+rear with one fallback
        mid_start = floor(length / 3)
        mid_end = ceil(2 * length / 3)
        valid_positions = [i for i in range(mid_start, mid_end - 2) if i < length - 2]

        if not valid_positions:
            pos1 = min(length - 3, mid_start)
        else:
            pos1 = rng.choice(valid_positions)

        formation[pos1] = VALUE_BRAKE_FRONT
        formation[pos1 + 1] = VALUE_BRAKE_REAR
        formation[pos1 + 2] = VALUE_CONDITIONAL_BRAKE_BEFORE

        family[length] = insert_special_variants(formation, seed_index)

    return apply_family_offset(family, 200)

def generate_type_c_family(seed_index: int) -> dict[int, list[int]]:
    rng = Random(seed_index)
    family = {}

    for length in range(1, 25):
        formation = [VALUE_STANDARD] * length

        if length < 5:
            mid = length // 2
            formation[mid] = VALUE_BRAKE_REAR
            family[length] = insert_special_variants(formation, seed_index)
            continue

        if length <= 6:
            mid = (length - 2) // 2
            formation[mid] = VALUE_CONDITIONAL_BRAKE_AFTER
            formation[mid + 1] = VALUE_BRAKE_REAR
            family[length] = insert_special_variants(formation, seed_index)
            continue

        start_range = 1
        end_range = length - 6
        if end_range < start_range:
            family[length] = insert_special_variants(formation, seed_index)
            continue

        pos1 = rng.randint(start_range, end_range)
        pos2_min = pos1 + 3
        pos2_max = length - 3
        if pos2_min > pos2_max:
            family[length] = insert_special_variants(formation, seed_index)
            continue

        pos2 = rng.randint(pos2_min, pos2_max)

        formation[pos1] = VALUE_CONDITIONAL_BRAKE_AFTER
        formation[pos1 + 1] = VALUE_BRAKE_REAR
        formation[pos2] = VALUE_BRAKE_FRONT
        formation[pos2 + 1] = VALUE_CONDITIONAL_BRAKE_BEFORE

        family[length] = insert_special_variants(formation, seed_index)

    return apply_family_offset(family, 300)

def get_all_pax_maps() -> dict[str, list[dict]]:
    output = {
        "brakes_outer_ends": [],
        "brakes_inner_paired": [],
        "brakes_inner_spaced": [],
    }
    for template_name, meta in FORMATION_CLASSES.items():
        for length in meta["lengths"]:
            maps = []
            for i in range(meta["count"]):
                if template_name == "brakes_outer_ends":
                    base = generate_type_a(length)[length]
                elif template_name == "brakes_inner_paired":
                    base = generate_type_b_family(i)[length]
                elif template_name == "brakes_inner_spaced":
                    base = generate_type_c_family(i)[length]
                else:
                    continue
                maps.append(base)
            output[template_name].append({"chain_length": length, "maps": maps})
    return output

# Preview and validation
if __name__ == "__main__":
    all_ok = True
    result = get_all_pax_maps()
    for template, entries in result.items():
        for entry in entries:
            expected_len = entry["chain_length"]
            print(f"Template {template} – Chain length {expected_len}:")
            for i, m in enumerate(entry["maps"]):
                if len(m) != expected_len:
                    print(f"  ❌ Map {i} has length {len(m)}")
                    all_ok = False
                else:
                    print(f"  ✅ Map {i} ok")
    if all_ok:
        print("\nAll map lengths are correct ✅")
    else:
        print("\nSome map lengths are incorrect ❌")
