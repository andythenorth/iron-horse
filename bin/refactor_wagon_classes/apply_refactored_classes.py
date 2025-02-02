import os
import re
import shutil  # ✅ Import shutil for file operations

TRAIN_FILE = "src/train.py"
MODIFIED_DIR = "./tmp/modified_consist_classes"
BACKUP_FILE = "src/train_backup.py"
OUTPUT_FILE = "src/train.py"

def load_modified_classes():
    """Loads all modified class definitions from the modified directory."""
    modified_classes = {}
    for file_name in os.listdir(MODIFIED_DIR):
        if file_name.endswith(".py"):
            class_name = file_name.replace(".py", "")
            with open(os.path.join(MODIFIED_DIR, file_name), "r", encoding="utf-8") as f:
                modified_classes[class_name] = f.readlines()
    return modified_classes

def apply_modifications():
    """Replaces modified class definitions in train.py."""
    # Load modified classes
    modified_classes = load_modified_classes()

    # Backup original train.py
    if not os.path.exists(BACKUP_FILE):
        shutil.copyfile(TRAIN_FILE, BACKUP_FILE)
        print(f"✅ Backup created at {BACKUP_FILE}")

    with open(TRAIN_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_file_lines = []
    inside_class = False
    current_class_name = None
    skip_class = False

    for i, line in enumerate(lines):
        # Detect class definitions
        class_match = re.match(r"class (\w+)\(", line)
        if class_match:
            class_name = class_match.group(1)

            # Save the previous class if it was being skipped
            if skip_class and current_class_name:
                new_file_lines.extend(lines[start_line:i])

            # Check if this class is in the modified classes
            if class_name in modified_classes:
                print(f"⚡ Replacing class: {class_name}")
                new_file_lines.extend(modified_classes[class_name])
                skip_class = True
                current_class_name = class_name
            else:
                skip_class = False
                current_class_name = None

            # Track the start of a new class
            start_line = i

        # Append non-class lines or the lines from skipped classes
        if not skip_class:
            new_file_lines.append(line)

    # If the last class was skipped, append its lines
    if skip_class and current_class_name:
        new_file_lines.extend(lines[start_line:])

    # Write the updated train.py
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_file_lines)

    print(f"✅ Modifications applied to {OUTPUT_FILE}")

if __name__ == "__main__":
    apply_modifications()
