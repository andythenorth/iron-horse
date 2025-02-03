import ast
import astor
import os
import shutil
import subprocess
import re

TMP_DIR = "./tmp/consist_classes"
MODIFIED_DIR = "./tmp/modified_consist_classes"
REPORT_FILE = "./tmp/livery_refactor_report.txt"
WRAPPED_DIR = "./tmp/wrapped_comments"

os.makedirs(WRAPPED_DIR, exist_ok=True)
os.makedirs(MODIFIED_DIR, exist_ok=True)

def extract_comments_and_code(class_code):
    """Extracts comments and associates them with the first token of the next valid code line."""
    lines = class_code.splitlines()
    comments_dict = {}
    comment_buffer = []
    processed_lines = []

    for line in lines:
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]  # Preserve leading whitespace

        if stripped.startswith("#"):
            comment_buffer.append(line)  # Store full line, keeping indentation
        else:
            if comment_buffer:
                first_token = stripped.split()[0] if stripped else None
                if first_token:
                    if first_token in comments_dict:
                        comments_dict[first_token].extend(comment_buffer)
                    else:
                        comments_dict[first_token] = comment_buffer
                else:
                    comments_dict["__MISC__"] = comment_buffer
                comment_buffer = []
            processed_lines.append(line)

    # Handle any remaining floating comments
    if comment_buffer:
        comments_dict["__UNMATCHED__"] = comment_buffer

    return comments_dict, "\n".join(processed_lines)

def reinsert_comments(refactored_code, comments_dict):
    """Reinserts extracted comments into the refactored code using first-token matching."""
    refactored_lines = refactored_code.splitlines()
    final_code = []
    unmatched_comments = []

    for line in refactored_lines:
        stripped = line.lstrip()
        first_token = stripped.split()[0] if stripped else None

        if first_token in comments_dict:
            final_code.extend(comments_dict[first_token])  # Insert stored comments
            del comments_dict[first_token]  # Remove from dict to avoid duplicates

        final_code.append(line)

    # Handle unmatched comments at the end
    unmatched_comments.extend(comments_dict.get("__UNMATCHED__", []))
    unmatched_comments.extend(comments_dict.get("__MISC__", []))

    if unmatched_comments:
        final_code.append('""" Unmatched Comments:')
        final_code.extend(unmatched_comments)
        final_code.append('"""')

    return "\n".join(final_code)

def detect_liveries(node):
    """Detects if a class uses liveries, even if inside another function argument."""
    for sub_node in ast.walk(node):
        if isinstance(sub_node, ast.Call):
            for keyword in sub_node.keywords:
                if keyword.arg == "liveries" and isinstance(keyword.value, ast.List):
                    return keyword.value
    return None

def refactor_liveries(class_code, file_name):
    """Moves liveries definition to a class attribute while preserving comments."""
    comments_dict, cleaned_code = extract_comments_and_code(class_code)

    tree = ast.parse(cleaned_code)
    class_def = tree.body[0]  # Expecting a single class per file
    livery_list = detect_liveries(class_def)

    if livery_list:
        livery_assignment = ast.Assign(
            targets=[ast.Name(id="liveries", ctx=ast.Store())], value=livery_list
        )
        class_def.body.insert(1, livery_assignment)

        for sub_node in ast.walk(class_def):
            if isinstance(sub_node, ast.Call):
                for keyword in sub_node.keywords:
                    if keyword.arg == "liveries":
                        keyword.value = ast.Attribute(
                            value=ast.Name(id="self", ctx=ast.Load()),
                            attr="liveries",
                            ctx=ast.Load(),
                        )

    refactored_code = astor.to_source(tree)
    final_code = reinsert_comments(refactored_code, comments_dict)

    # Debugging: Dump wrapped comments and processed output
    debug_path = os.path.join(WRAPPED_DIR, file_name + ".txt")
    with open(debug_path, "w", encoding="utf-8") as debug_file:
        debug_file.write("### Extracted Comments ###\n")
        for key, value in comments_dict.items():
            debug_file.write(f"{key}: {value}\n")
        debug_file.write("\n### Final Refactored Code ###\n")
        debug_file.write(final_code)

    return final_code

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
        class_def = tree.body[0]
        has_liveries = detect_liveries(class_def)

        if not has_liveries:
            shutil.copy(class_file_path, modified_file_path)
            report_lines.append(f"{file_name}: No liveries detected, copied unchanged.")
        else:
            refactored_code = refactor_liveries(class_code, file_name)

            with open(modified_file_path, "w", encoding="utf-8") as f:
                f.write(refactored_code)

            report_lines.append(f"{file_name}: Liveries refactored and moved to class attributes.")

        subprocess.run(["black", "--quiet", modified_file_path])

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"✅ Refactoring complete! Report written to {REPORT_FILE}")

if __name__ == "__main__":
    process_classes()
