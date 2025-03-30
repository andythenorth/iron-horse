import os
# note that we use tomlkit here, not standard library tomllib, as we need write, and tomllib is read-only
import tomlkit

# List of strings to be removed from the TOML files
dead_strings = [
    "STR_COLOUR_NAME_COLOUR_DARK_BLUE",
    "STR_COLOUR_NAME_COLOUR_PALE_GREEN",
    "STR_COLOUR_NAME_COLOUR_PINK",
    "STR_COLOUR_NAME_COLOUR_YELLOW",
    "STR_COLOUR_NAME_COLOUR_RED",
    "STR_COLOUR_NAME_COLOUR_LIGHT_BLUE",
    "STR_COLOUR_NAME_COLOUR_GREEN",
    "STR_COLOUR_NAME_COLOUR_DARK_GREEN",
    "STR_COLOUR_NAME_COLOUR_BLUE",
    "STR_COLOUR_NAME_COLOUR_CREAM",
    "STR_COLOUR_NAME_COLOUR_MAUVE",
    "STR_COLOUR_NAME_COLOUR_PURPLE",
    "STR_COLOUR_NAME_COLOUR_ORANGE",
    "STR_COLOUR_NAME_COLOUR_BROWN",
    "STR_COLOUR_NAME_COLOUR_GREY",
    "STR_COLOUR_NAME_COLOUR_WHITE",
    "STR_COLOUR_NAME_CUSTOM_BAUXITE",
    "STR_COLOUR_NAME_CUSTOM_DARK_GREY",
    "STR_COLOUR_NAME_CUSTOM_GREMLIN_GREEN",
    "STR_COLOUR_NAME_CUSTOM_NIGHTSHADE",
    "STR_COLOUR_NAME_CUSTOM_OCHRE",
    "STR_COLOUR_NAME_CUSTOM_OIL_BLACK",
    "STR_COLOUR_NAME_CUSTOM_PEWTER",
    "STR_COLOUR_NAME_CUSTOM_RUBY",
    "STR_COLOUR_NAME_CUSTOM_SILVER",
    "STR_COLOUR_NAME_CUSTOM_SULPHUR",
    "STR_COLOUR_NAME_CUSTOM_TEAL",
    "STR_COLOUR_NAME_CUSTOM_VIOLET",
    "STR_NAME_SUFFIX_LIVERY_MIX_COMPLEMENT_COMPANY_COLOUR",
    "STR_NAME_SUFFIX_LIVERY_MIX_VARIETY",
    "STR_NAME_SUFFIX_LIVERY_MIX_BAUXITE_GREY_NIGHTSHADE",
    "STR_NAME_SUFFIX_LIVERY_MIX_TEAL_VIOLET",
    "STR_NAME_SUFFIX_LIVERY_MIX_SILVER_PEWTER",
    "STR_NAME_SUFFIX_LIVERY_MIX_SULPHUR_OCHRE",
    "STR_NAME_SUFFIX_LIVERY_MIX_RUBY_BAUXITE",
    "STR_NAME_SUFFIX_LIVERY_MIX_OIL_BLACK_NIGHTSHADE",
    "STR_NAME_SUFFIX_LIVERY_MIX_OCHRE_SAND",
    "STR_NAME_SUFFIX_LIVERY_MIX_GREMLIN_GREEN_SILVER",
    "STR_NAME_SUFFIX_LIVERY_MIX_SULPHUR_STRAW",
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
