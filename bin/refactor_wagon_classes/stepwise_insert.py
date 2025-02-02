import os
import re
import shutil

TRAIN_FILE = "src/train.py"
INSERTION_QUEUE = "./tmp/insertion_queue"
BACKUP_FILE = "src/train_backup.py"

def ensure_dirs():
    """Ensure the insertion queue directory exists."""
    os.makedirs(INSERTION_QUEUE, exist_ok=True)

def prompt_for_files():
    """Prompt user to place files in the queue and hit Enter to continue."""
    input(f"📝 Place the modified class files in {INSERTION_QUEUE}, then press Enter to continue...")

def load_modified_classes():
    """Loads modified classes from the insertion queue."""
    modified_classes = {}
    for file_name in os.listdir(INSERTION_QUEUE):
        if file_name.endswith(".py"):
            class_name = file_name.replace(".py", "")
            with open(os.path.join(INSERTION_QUEUE, file_name), "r", encoding="utf-8") as f:
                modified_classes[class_name] = f.readlines()
    return modified_classes

def replace_class_in_train(class_name, modified_lines):
    """Replaces the specified class definition in train.py using the unmodified version as a reference."""
    unmodified_class_path = os.path.join("./tmp/consist_classes", f"{class_name}.py")

    if not os.path.exists(unmodified_class_path):
        print(f"❌ ERROR: Unmodified class file {unmodified_class_path} not found. Skipping.")
        return

    # Read the original (unmodified) class definition
    with open(unmodified_class_path, "r", encoding="utf-8") as f:
        original_class_lines = f.readlines()

    # Read the full train.py content
    with open(TRAIN_FILE, "r", encoding="utf-8") as f:
        train_lines = f.readlines()

    # Find the exact slice of train.py that matches the original class
    try:
        start_index = train_lines.index(original_class_lines[0])
        end_index = start_index + len(original_class_lines)
    except ValueError:
        print(f"⚠️ WARNING: Class {class_name} not found in train.py! Appending at the end.")
        train_lines.append("\n".join(modified_lines) + "\n")
    else:
        # Replace the exact matching slice with the modified class
        train_lines[start_index:end_index] = modified_lines

    # Ensure only one instance of the class exists
    class_count = sum(1 for line in train_lines if line.strip().startswith(f"class {class_name}("))
    assert class_count == 1, f"❌ Duplicate class {class_name} found after insertion!"

    # Write back to train.py
    with open(TRAIN_FILE, "w", encoding="utf-8") as f:
        f.writelines(train_lines)

    print(f"✅ Successfully replaced class {class_name} in {TRAIN_FILE}")

def stepwise_insert():
    """Stepwise class insertion with review between steps."""
    ensure_dirs()
    prompt_for_files()

    # Backup train.py before modifications
    if not os.path.exists(BACKUP_FILE):
        shutil.copyfile(TRAIN_FILE, BACKUP_FILE)
        print(f"✅ Backup created at {BACKUP_FILE}")

    modified_classes = load_modified_classes()

    for class_name, modified_lines in modified_classes.items():
        replace_class_in_train(class_name, modified_lines)

        # Prompt user to review changes before proceeding
        print(f"🔍 Review the changes in {TRAIN_FILE}.")
        input("📝 Press Enter to continue with the next file, or Ctrl+C to stop...")

    print("✅ Stepwise insertions complete!")

if __name__ == "__main__":
    stepwise_insert()
