from random import Random

# Constants for coach type codes (adjusted for spriterow logic)
VALUE_STANDARD = 0
VALUE_BRAKE_FRONT = 1
VALUE_BRAKE_REAR = 2
VALUE_SPECIAL = 3

FORMATION_CLASSES = {
    "brakes_outer_ends": {"count": 8, "lengths": list(range(1, 17))},
    "brakes_inner_paired": {"count": 8, "lengths": list(range(1, 17))},
    "brakes_inner_spaced": {"count": 8, "lengths": list(range(1, 17))},
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
    attempted_positions = set()

    for _ in range(num_special):
        valid_positions = [
            i
            for i in range(1, length - 1)
            if mod_map[i] == VALUE_STANDARD and i not in attempted_positions
        ]
        if not valid_positions:
            break

        idx = rng.choice(valid_positions)
        attempted_positions.add(idx)

        if mod_map[idx] == VALUE_STANDARD:
            mod_map[idx] = VALUE_SPECIAL
            special_inserted += 1
        else:
            # walk forwards until standard is found
            for j in range(idx + 1, length - 1):
                if mod_map[j] == VALUE_STANDARD:
                    mod_map[j] = VALUE_SPECIAL
                    special_inserted += 1
                    break

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
    base_offset = seed_index - 4  # bias middle slightly left or right
    family = {}
    for length in range(1, 17):
        if length < 3:
            family[length] = [VALUE_STANDARD] * length
            continue
        formation = [VALUE_STANDARD] * length
        mid = length // 2
        offset = max(-mid + 1, min(base_offset, length - 3 - mid))
        pos1 = max(1, min(length - 3, mid + offset))
        formation[pos1] = VALUE_BRAKE_FRONT
        formation[pos1 + 1] = VALUE_BRAKE_REAR
        family[length] = formation
    return family


def generate_type_c_family(seed_index: int) -> dict[int, list[int]]:
    rng = Random(seed_index)
    base_first_pos = rng.randint(1, 4)
    second_brake_delta = rng.randint(1, 3)
    family = {}
    for length in range(1, 17):
        formation = [VALUE_STANDARD] * length
        if length < 2:
            formation[0] = VALUE_BRAKE_REAR
            family[length] = formation
            continue
        first_pos = min(base_first_pos, length - 2)
        formation[first_pos] = VALUE_BRAKE_FRONT
        if length >= 4:
            second_pos = min(length - 2, first_pos + second_brake_delta + (length // 8))
            if second_pos != first_pos:
                formation[second_pos] = VALUE_BRAKE_REAR
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
