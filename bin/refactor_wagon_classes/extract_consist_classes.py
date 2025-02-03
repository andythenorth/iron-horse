import os
import re

TRAIN_FILE = "src/train.py"
OUTPUT_DIR = "./tmp/consist_classes"
CLASS_LIST_FILE = "./tmp/consist_classes_list.txt"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_class_names():
    """Loads the list of class names from the class name file."""
    with open(CLASS_LIST_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def extract_and_save_classes():
    """Extracts classes from the source file based on the class name list."""
    with open(TRAIN_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    class_names = load_class_names()
    current_class = []
    inside_class = False
    class_name = None

    for i, line in enumerate(lines):
        # Detect class definitions
        class_match = re.match(r"class (\w+)\(", line)
        if class_match:
            detected_class_name = class_match.group(1)

            # If we were processing a class, save it before starting the next
            if inside_class and class_name in class_names:
                save_class_to_file(class_name, current_class)

            # Start processing the new class
            inside_class = detected_class_name in class_names
            class_name = detected_class_name if inside_class else None
            current_class = [line] if inside_class else []

        elif inside_class:
            # Continue capturing the class body
            current_class.append(line)

            # Detect the end of the class at a new class definition or EOF
            is_last_line = i == len(lines) - 1
            next_line_is_class = (
                i + 1 < len(lines) and re.match(r"class (\w+)\(", lines[i + 1])
            )

            if is_last_line or next_line_is_class:
                save_class_to_file(class_name, current_class)
                inside_class = False

    # Save the last class if needed
    if inside_class and class_name in class_names:
        save_class_to_file(class_name, current_class)

    print(f"✅ Extraction complete. Classes saved to {OUTPUT_DIR}")

def save_class_to_file(class_name, class_lines):
    """Writes a single class definition to a separate file, preserving comments and blank lines."""
    output_path = os.path.join(OUTPUT_DIR, f"{class_name}.py")

    # Ensure extracted class ends with at least one blank line
    if class_lines[-1].strip():  # Last line is not blank
        class_lines.append("\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(class_lines)

    print(f"✅ Extracted {class_name} to {output_path}")

if __name__ == "__main__":
    extract_and_save_classes()
