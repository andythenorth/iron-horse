import os
# note that we use tomlkit here, not standard library tomllib, as we need write, and tomllib is read-only
import tomlkit

# List of strings to be removed from the TOML files
dead_strings = [
    "STR_WAGON_GROUP_BOX_CARS_RANDOMISED",
    "STR_WAGON_GROUP_COVERED_HOPPER_CARS_RANDOMISED",
    "STR_WAGON_GROUP_DROP_SIDE_FLAT_CARS",
    "STR_WAGON_GROUP_FLAT_CARS_RANDOMISED",
    "STR_WAGON_GROUP_HOPPER_CARS_RANDOMISED",
    "STR_WAGON_GROUP_MINERAL_BULK_OPEN_CARS_RANDOMISED",
    "STR_WAGON_GROUP_OPEN_CARS_RANDOMISED",
    "STR_WAGON_GROUP_SALT_SWING_ROOF_HOPPER_CARS",
    "STR_NAME_SUFFIX_GOODS_BOX_CAR",
    "STR_WAGON_GROUP_EXPRESS_FOOD_CARS_RANDOMISED",
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
