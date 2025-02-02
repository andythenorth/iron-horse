import ast
import astor
import os
import shutil
import subprocess
import re
from .find_consist_classes import find_consist_classes
from .extract_consist_classes import extract_and_save_classes
from .refactor_liveries import process_classes

TMP_DIR = "./tmp/consist_classes"
MODIFIED_DIR = "./tmp/modified_consist_classes"
REPORT_FILE = "./tmp/livery_refactor_report.txt"
SOURCE_FILE = "src/train.py"

# Ensure directories exist
os.makedirs(MODIFIED_DIR, exist_ok=True)

def count_livery_occurrences(file_path=SOURCE_FILE):
    """Counts the number of times 'liveries =' appears in the source file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return len(re.findall(r"\bliveries\s*=", content))

def count_livery_occurrences_in_dir(directory):
    """Counts all occurrences of 'liveries =' in a directory of Python files."""
    count = 0
    for file_name in os.listdir(directory):
        if file_name.endswith(".py"):
            with open(os.path.join(directory, file_name), "r", encoding="utf-8") as f:
                count += len(re.findall(r"\bliveries\s*=", f.read()))
    return count

def main():
    """Runs the refactoring pipeline in sequence, including QA checks."""
    print("🚀 Step 1: Finding all Consist subclasses...")
    find_consist_classes()

    print("🚀 Step 2: Extracting class definitions...")
    extract_and_save_classes()

    print("🚀 Step 3: Refactoring liveries...")
    process_classes()

    # QA check: count occurrences of 'liveries =' before and after refactor
    original_livery_count = count_livery_occurrences(SOURCE_FILE)  # Check original
    modified_livery_count = count_livery_occurrences_in_dir(MODIFIED_DIR)  # Check refactored files

    print(f"🔍 QA Check: Found {original_livery_count} instances of 'liveries =' in the original file.")
    print(f"🔍 QA Check: Found {modified_livery_count} instances of 'liveries =' after refactor.")

    if modified_livery_count < original_livery_count:
        print("⚠️ WARNING: Some liveries may not have been properly refactored!")
    else:
        print("✅ QA Passed: All liveries successfully refactored.")

    print(f"✅ Refactoring sequence complete! Report written to {REPORT_FILE}")

if __name__ == "__main__":
    main()
