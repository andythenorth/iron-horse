import os
# note that we use tomlkit here, not standard library tomllib, as we need write, and tomllib is read-only
import tomlkit

# List of strings to be removed from the TOML files
dead_strings = [
    "STR_WAGON_NAME_COIL_CAR_COVERED",
    "STR_WAGON_NAME_DEDICATED_COIL_CAR_RANDOMISED",
    "STR_WAGON_NAME_DROP_SIDE_FLAT_CAR",
    "STR_WAGON_NAME_HOPPER_CAR_HIGH_SIDE",
    "STR_WAGON_NAME_LOW_FLOOR_AUTOMOBILE_CAR",
    "STR_WAGON_NAME_LOW_FLOOR_INTERMODAL_CAR",
    "STR_WAGON_NAME_MINERAL_BULK_OPEN_CAR_HIGH_SIDE",
    "STR_WAGON_NAME_MGR_TOP_HOOD_HOPPER_CAR",
    "STR_WAGON_NAME_PIECE_GOODS_MANUFACTURING_PARTS_COMBOS",
    "STR_WAGON_NAME_TIPPLER_ROTARY_BULK_OPEN_CAR"
]

def delete_string(dead_strings, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lang_source = tomlkit.load(file)

    for string_id in dead_strings:
        if string_id in lang_source:
            print(f"Removing {string_id} from {file_path}")
            del lang_source[string_id]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(tomlkit.dumps(lang_source))

def main():
    lang_dir = os.path.join('src', 'lang')
    for filename in os.listdir(lang_dir):
        if filename.endswith(".toml"):
            file_path = os.path.join(lang_dir, filename)
            delete_string(dead_strings, file_path)

if __name__ == "__main__":
    main()
