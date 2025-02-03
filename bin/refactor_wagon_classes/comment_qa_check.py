import os
import re

ORIGINAL_DIR = "./tmp/consist_classes"
MODIFIED_DIR = "./tmp/modified_consist_classes"
REPORT_FILE = "./tmp/comment_refactor_report.txt"

def extract_comments_from_file(file_path):
    """Extracts all comments from a Python file, normalized."""
    comments = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("#"):  # Capture comments only
                    normalized_comment = re.sub(r'\s+', ' ', stripped)  # Normalize spaces
                    comments.add(normalized_comment)
    except FileNotFoundError:
        print(f"❌ ERROR: File not found: {file_path}")
    return comments

def compare_comments():
    """Compares comments between original and modified files, allowing for flexible placement."""
    missing_comments = {}
    extra_comments = {}

    for file_name in os.listdir(ORIGINAL_DIR):
        if not file_name.endswith(".py"):
            continue

        original_file = os.path.join(ORIGINAL_DIR, file_name)
        modified_file = os.path.join(MODIFIED_DIR, file_name)

        original_comments = extract_comments_from_file(original_file)
        modified_comments = extract_comments_from_file(modified_file)

        missing = original_comments - modified_comments  # Comments that disappeared
        extra = modified_comments - original_comments  # Comments that were added (for debugging)

        if missing:
            missing_comments[file_name] = missing
        if extra:
            extra_comments[file_name] = extra  # Might help debug if comments are duplicated or misplaced

    # Write report
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        if missing_comments:
            f.write(f"⚠️ WARNING: Some comments were lost!\n\n")
            for file, comments in missing_comments.items():
                f.write(f"{file}: {len(comments)} missing comments:\n")
                for comment in comments:
                    f.write(f"  {comment}\n")
                f.write("\n")
        else:
            f.write("✅ All comments successfully preserved!\n")

    print(f"🔍 QA check complete! Report written to {REPORT_FILE}")

if __name__ == "__main__":
    compare_comments()
