import os
import sys

def count_pattern_in_file(file_path, pattern):
    """Count occurrences of a pattern in a file, handling encoding errors."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return sum(1 for line in f if pattern in line)
    except UnicodeDecodeError:
        print(f"⚠️ Skipping unreadable file (encoding issue): {file_path}")
        return 0
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
        return 0

def find_mismatched_files(directory):
    """Find .py files with 'cars' in the filename where 'result.append(consist_factory)'
    and 'consist_factory = ConsistFactory(' counts do not match."""
    mismatches = []

    for root, _, files in os.walk(directory):
        for file in sorted(files):  # Sort files lexically
            if not file.endswith(".py") or "cars" not in file.lower():  # Filter by .py and 'cars'
                continue

            file_path = os.path.join(root, file)

            if not os.path.isfile(file_path):
                continue  # Ensure it's a file

            count_append = count_pattern_in_file(file_path, "    result.append(consist_factory)")
            count_factory = count_pattern_in_file(file_path, "    consist_factory = ConsistFactory(")

            if count_append != count_factory:
                mismatches.append((file_path, count_append, count_factory))

    return sorted(mismatches)  # Ensure final results are sorted lexically

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_consist_mismatch.py /path/to/your/files")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("Error: The provided path is not a valid directory.")
        sys.exit(1)

    mismatched_files = find_mismatched_files(directory)

    if mismatched_files:
        print("\n❌ Files with mismatched counts:")
        for file, append_count, factory_count in mismatched_files:
            print(f"{file}: append={append_count}, factory={factory_count}")
    else:
        print("✅ All matching files have consistent counts.")
