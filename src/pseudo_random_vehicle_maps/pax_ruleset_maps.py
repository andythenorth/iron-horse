from math import floor, ceil
from random import Random

# Constants for coach type codes (adjusted for spriterow logic)
VALUE_STANDARD = 0
VALUE_BRAKE_FRONT = 1
VALUE_BRAKE_REAR = 2
VALUE_SPECIAL = 3

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


def generate_type_a(length: int) -> list[int]:
    if length == 1:
        return [VALUE_BRAKE_FRONT]
    elif length == 2:
        return [VALUE_BRAKE_FRONT, VALUE_BRAKE_REAR]
    else:
        return (
            [VALUE_BRAKE_FRONT] + [VALUE_STANDARD] * (length - 2) + [VALUE_BRAKE_REAR]
        )


def generate_type_b_family(seed_index: int) -> dict[int, list[int]]:
    rng = Random(seed_index)
    family = {}

    for length in range(1, 25):
        formation = [VALUE_STANDARD] * length

        if length <= 5:
            # One brake, placed near center
            pos = min(length // 2, length - 1)
            formation[pos] = VALUE_BRAKE_FRONT
            family[length] = formation
            continue

        # Normal paired-brake logic for length >= 6
        start = floor(length / 3)
        end = max(start, ceil(2 * length / 3) - 1)
        valid_positions = list(range(start, min(end, length - 2) + 1))
        pos1 = rng.choice(valid_positions)

        formation[pos1] = VALUE_BRAKE_FRONT
        formation[pos1 + 1] = VALUE_BRAKE_REAR

        family[length] = formation

    return family


def generate_type_c_family(seed_index: int) -> dict[int, list[int]]:
    rng = Random(seed_index)
    base_first_pos = rng.randint(1, 4)
    second_brake_delta = rng.randint(1, 3)
    family = {}
    for length in range(1, 25):
        formation = [VALUE_STANDARD] * length
        if length < 2:
            formation[0] = VALUE_BRAKE_FRONT
            family[length] = formation
            continue
        first_pos = min(base_first_pos, length - 2)
        formation[first_pos] = VALUE_BRAKE_REAR
        if length >= 4:
            second_pos = min(length - 2, first_pos + second_brake_delta + (length // 8))
            if second_pos != first_pos:
                formation[second_pos] = VALUE_BRAKE_FRONT
        family[length] = formation
    return family


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
                    base = generate_type_a(length)
                elif template_name == "brakes_inner_paired":
                    base = generate_type_b_family(i)[length]
                elif template_name == "brakes_inner_spaced":
                    base = generate_type_c_family(i)[length]
                else:
                    continue
                mod_map = insert_special_variants(base, seed=i)
                maps.append(mod_map)
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
