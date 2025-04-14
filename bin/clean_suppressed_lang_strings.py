# remove any suppression strings where there is no matching node in any lang file
# this is just to keep suppression strings up to date and manageable

import os
from tomlkit import parse, dumps
from tomlkit.toml_file import TOMLFile

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lang_dir = os.path.join(base_dir, "src", "lang")
    suppressed_path = os.path.join(lang_dir, "suppressed_strings.toml")

    # Load suppressed_strings.toml (preserve formatting/comments)
    suppressed_file = TOMLFile(suppressed_path)
    suppressed_doc = suppressed_file.read()
    suppressed_keys = set(suppressed_doc.keys())

    # Collect all keys from other TOML files
    all_lang_keys = set()
    for filename in os.listdir(lang_dir):
        if not filename.endswith(".toml") or filename == "suppressed_strings.toml":
            continue

        filepath = os.path.join(lang_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                parsed = parse(f.read())
                all_lang_keys.update(parsed.keys())
        except Exception as e:
            print(f"[warn] Failed to parse {filename}: {e}")

    # Identify and remove unused keys
    unused_keys = suppressed_keys - all_lang_keys
    if unused_keys:
        for key in unused_keys:
            suppressed_doc.pop(key, None)

        suppressed_file.write(suppressed_doc)

        print("Removed unused keys:")
        for key in sorted(unused_keys):
            print(f"  {key}")
    else:
        print("No unused keys found.")

if __name__ == "__main__":
    main()
