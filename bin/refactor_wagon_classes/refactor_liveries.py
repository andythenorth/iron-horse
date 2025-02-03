import ast
import astor
import os
import shutil
import subprocess

TMP_DIR = "./tmp/consist_classes"
MODIFIED_DIR = "./tmp/modified_consist_classes"
REPORT_FILE = "./tmp/livery_refactor_report.txt"

# Ensure directories exist
os.makedirs(MODIFIED_DIR, exist_ok=True)

def detect_liveries(node):
    """Detects if a class uses liveries, even if inside another function argument."""
    for sub_node in ast.walk(node):
        if isinstance(sub_node, ast.Call):  # Check function calls
            for keyword in sub_node.keywords:
                if keyword.arg == "liveries" and isinstance(keyword.value, ast.List):
                    return keyword.value  # Return the livery list AST node
    return None

def count_trailing_blank_lines(file_path):
    """Counts the number of blank lines at the end of a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    trailing_blank_lines = 0
    for line in reversed(lines):
        if line.strip() == "":
            trailing_blank_lines += 1
        else:
            break

    return trailing_blank_lines

def refactor_liveries(class_code):
    """Moves liveries definition to a class attribute while preserving comments."""

    tree = ast.parse(class_code)
    class_def = tree.body[0]  # Expecting a single class per file

    livery_list = detect_liveries(class_def)

    if livery_list:
        # Create a new class-level attribute
        livery_assignment = ast.Assign(
            targets=[ast.Name(id="liveries", ctx=ast.Store())], value=livery_list
        )

        # Insert after docstring (if present)
        class_def.body.insert(1, livery_assignment)

        # Replace function call arguments with self.liveries
        for sub_node in ast.walk(class_def):
            if isinstance(sub_node, ast.Call):
                for keyword in sub_node.keywords:
                    if keyword.arg == "liveries":
                        keyword.value = ast.Attribute(
                            value=ast.Name(id="self", ctx=ast.Load()),
                            attr="liveries",
                            ctx=ast.Load(),
                        )

    return astor.to_source(tree)

def process_classes():
    """Processes each extracted class file to detect and refactor liveries."""
    report_lines = []

    for file_name in os.listdir(TMP_DIR):
        if not file_name.endswith(".py"):
            continue

        class_file_path = os.path.join(TMP_DIR, file_name)
        modified_file_path = os.path.join(MODIFIED_DIR, file_name)

        with open(class_file_path, "r", encoding="utf-8") as f:
            class_code = f.read()

        tree = ast.parse(class_code)
        class_def = tree.body[0]  # Expecting a single class per file
        has_liveries = detect_liveries(class_def)

        trailing_blank_lines = count_trailing_blank_lines(class_file_path)  # Preserve blank lines

        if not has_liveries:
            shutil.copy(class_file_path, modified_file_path)
            report_lines.append(f"{file_name}: No liveries detected, copied unchanged.")
        else:
            refactored_code = refactor_liveries(class_code)

            # Write initially modified file (before Black)
            with open(modified_file_path, "w", encoding="utf-8") as f:
                f.write(refactored_code)

            # Auto-format with Black
            subprocess.run(["black", "--quiet", modified_file_path])

            # Re-read formatted file and reapply blank lines
            with open(modified_file_path, "r", encoding="utf-8") as f:
                formatted_code = f.read()

            # Preserve trailing blank lines **after** Black formatting
            formatted_code = formatted_code.rstrip("\n") + ("\n" * trailing_blank_lines)

            with open(modified_file_path, "w", encoding="utf-8") as f:
                f.write(formatted_code)

            report_lines.append(f"{file_name}: Liveries refactored and moved to class attributes.")

    # Write report
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"✅ Refactoring complete! Report written to {REPORT_FILE}")

if __name__ == "__main__":
    process_classes()
