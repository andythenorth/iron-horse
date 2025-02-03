import os
import shutil
import subprocess

TRAIN_FILE = "src/train.py"
INSERTION_QUEUE = "./tmp/insertion_queue"
BACKUP_FILE = "src/train_backup.py"

def ensure_dirs():
    """Ensure required directories exist."""
    os.makedirs(INSERTION_QUEUE, exist_ok=True)

def prompt_for_files():
    """Prompt user to place files in the queue and hit Enter to continue."""
    input(f"📝 Place the modified class files in {INSERTION_QUEUE}, then press Enter to continue...")

def load_modified_classes():
    """Loads modified classes from the insertion queue, sorted lexically."""
    modified_classes = {}

    # Ensure we process files in sorted order
    for file_name in sorted(os.listdir(INSERTION_QUEUE)):
        if file_name.endswith(".py"):
            class_name = file_name.replace(".py", "")
            with open(os.path.join(INSERTION_QUEUE, file_name), "r", encoding="utf-8") as f:
                modified_classes[class_name] = f.readlines()

    return modified_classes

def find_class_indexes(train_lines, class_name):
    """Finds the start and end indexes of a class definition in train.py."""
    class_def_line = f"class {class_name}("
    start_index, end_index = None, None

    # Find the class start
    for i, line in enumerate(train_lines):
        if line.strip().startswith(class_def_line):
            start_index = i
            break

    if start_index is None:
        return None, None

    # Find where the class ends
    for i in range(start_index + 1, len(train_lines)):
        if train_lines[i].strip().startswith("class "):  # Next class detected
            end_index = i
            break

    if end_index is None:
        end_index = len(train_lines)  # If it's the last class in the file

    return start_index, end_index

def replace_class_in_train(class_name, modified_lines):
    """Replaces the specified class definition in train.py using the unmodified version as a reference."""
    unmodified_class_path = os.path.join("./tmp/consist_classes", f"{class_name}.py")

    if not os.path.exists(unmodified_class_path):
        print(f"❌ ERROR: Unmodified class file {unmodified_class_path} not found. Skipping.")
        return

    # Read the full train.py content
    with open(TRAIN_FILE, "r", encoding="utf-8") as f:
        train_lines = f.readlines()

    # Find class location in train.py
    start_index, end_index = find_class_indexes(train_lines, class_name)

    if start_index is None:
        print(f"⚠️ WARNING: Class {class_name} not found in train.py! Appending at the end.")
        train_lines.append("\n".join(modified_lines) + "\n")
    else:
        # Preserve trailing blank lines (formatting)
        while end_index < len(train_lines) and train_lines[end_index].strip() == "":
            end_index += 1  # Move forward, keeping blank lines

        # Ensure at least one blank line after replacement
        if not modified_lines[-1].strip():  # Already ends with blank line
            train_lines[start_index:end_index] = modified_lines
        else:  # Add a blank line for formatting
            train_lines[start_index:end_index] = modified_lines + ["\n"]

    # Ensure no duplicate class definitions
    class_count = sum(1 for line in train_lines if line.strip().startswith(f"class {class_name}("))
    assert class_count == 1, f"❌ Duplicate class {class_name} found after insertion!"

    # Write back to train.py
    with open(TRAIN_FILE, "w", encoding="utf-8") as f:
        f.writelines(train_lines)

    print(f"✅ Successfully replaced class {class_name} in {TRAIN_FILE}")

def run_git_command(args, error_message):
    """Executes a git command safely, capturing errors."""
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        print(f"⚠️ WARNING: {error_message}")

def stepwise_insert():
    """Stepwise class insertion with review and lexical ordering."""
    ensure_dirs()
    prompt_for_files()

    # Backup train.py before modifications
    if not os.path.exists(BACKUP_FILE):
        shutil.copyfile(TRAIN_FILE, BACKUP_FILE)
        print(f"✅ Backup created at {BACKUP_FILE}")

    modified_classes = load_modified_classes()

    for class_name, modified_lines in modified_classes.items():
        replace_class_in_train(class_name, modified_lines)

        # Show the git diff properly
        run_git_command(["git", "diff", "--", TRAIN_FILE], "Failed to show git diff.")

        # Prompt user to review changes before proceeding
        while True:
            user_input = input("Do you want to stage this change? (y/n) ").strip().lower()
            if user_input == "y":
                run_git_command(["git", "add", "--", TRAIN_FILE], "Failed to stage changes.")
                print("✅ Change staged.")
                break
            elif user_input == "n":
                print("❌ Skipping staging for now.")
                break
            else:
                print("❓ Invalid input. Please enter 'y' or 'n'.")

        # Ask if the user wants to continue
        user_input = input("Continue with next class? (y/n) ").strip().lower()
        if user_input != "y":
            print("🚪 Exiting stepwise insert.")
            break

    print("✅ Stepwise insertions complete!")

if __name__ == "__main__":
    stepwise_insert()
