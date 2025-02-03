import ast
import astor
import os
import shutil
import subprocess
import re

TMP_DIR = "./tmp/consist_classes"
MODIFIED_DIR = "./tmp/modified_consist_classes"
REPORT_FILE = "./tmp/livery_refactor_report.txt"

# Ensure directories exist
os.makedirs(MODIFIED_DIR, exist_ok=True)

def detect_inline_comments(file_path):
    """Scans the file and raises an exception if an inline comment is detected."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Ignore full-line comments, detect inline ones
        if "#" in stripped and not stripped.startswith("#"):
            raise Exception(
                f"❌ INLINE COMMENT DETECTED in {file_path} at line {i}:\n{line.strip()}\n"
                "💡 Remove inline comments manually in train.py before running this script."
            )

def detect_liveries(node):
    """Detects if a class uses liveries."""
    for sub_node in ast.walk(node):
        if isinstance(sub_node, ast.Call):
            for keyword in sub_node.keywords:
                if keyword.arg == "liveries" and isinstance(keyword.value, ast.List):
                    return keyword.value
    return None

def refactor_liveries(class_code):
    """Moves liveries definition to a class attribute while preserving comments and EOF blank lines."""

    # Capture original trailing blank lines
    num_trailing_newlines = len(class_code) - len(class_code.rstrip("\n"))

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

    # Generate modified source code
    modified_code = astor.to_source(tree)

    # Restore trailing blank lines
    modified_code = modified_code.rstrip("\n") + ("\n" * num_trailing_newlines)

    return modified_code

def process_classes():
    """Processes each extracted class file to detect and refactor liveries."""
    report_lines = []

    for file_name in os.listdir(TMP_DIR):
        if not file_name.endswith(".py"):
            continue

        class_file_path = os.path.join(TMP_DIR, file_name)
        modified_file_path = os.path.join(MODIFIED_DIR, file_name)

        # Detect inline comments before parsing the AST
        detect_inline_comments(class_file_path)

        with open(class_file_path, "r", encoding="utf-8") as f:
            class_code = f.read()

        tree = ast.parse(class_code)
        class_def = tree.body[0]  # Expecting a single class per file
        has_liveries = detect_liveries(class_def)

        if not has_liveries:
            shutil.copy(class_file_path, modified_file_path)
            report_lines.append(f"{file_name}: No liveries detected, copied unchanged.")
        else:
            refactored_code = refactor_liveries(class_code)

            with open(modified_file_path, "w", encoding="utf-8") as f:
                f.write(refactored_code)

            report_lines.append(f"{file_name}: Liveries refactored and moved to class attributes.")

        # Auto-format with black
        subprocess.run(["black", "--quiet", modified_file_path])

    # Write report
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"✅ Refactoring complete! Report written to {REPORT_FILE}")

if __name__ == "__main__":
    process_classes()
