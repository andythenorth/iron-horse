#!/usr/bin/env python3
import subprocess, sys

# Default file paths
file1 = "generated copy/iron-horse.nml"
file2 = "generated/iron-horse.nml"

if len(sys.argv) >= 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

# List of exclusion patterns (noise differences)
excludes = [
    "colour_mapping",
    "No newline at end of file",
    "intermodal_containers",
    "spriteset_template",
    "ih_ruleset_flags",
    "additional_text",
    "mineral_bulk_open_car_low_side_pony_gen_5B_switch_cargo_capacity",
    "_switch_cargo_capacity",
]

# Run diff with zero context lines so only changed lines (and hunk headers) are shown
proc = subprocess.Popen(
    ["diff", "-U0", file1, file2],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)


def process_hunk(hunk):
    """
    Given a hunk (list of lines starting with @@ header, then diff lines),
    return a filtered hunk if it contains at least one changed line that does not
    include any exclusion pattern. Otherwise, return None.
    """
    significant = False
    filtered = []
    for line in hunk:
        if line.startswith("@@"):
            filtered.append(line)
        elif line.startswith("+") or line.startswith("-"):
            if any(pattern in line for pattern in excludes):
                # skip this noise line
                continue
            else:
                significant = True
                filtered.append(line)
    return filtered if significant else None


# Group diff output into hunks
current_hunk = []
output_lines = []

for line in proc.stdout:
    if line.startswith("@@"):
        # Process previous hunk if any
        if current_hunk:
            filtered = process_hunk(current_hunk)
            if filtered:
                output_lines.extend(filtered)
            current_hunk = []
    current_hunk.append(line)
# Process the last hunk
if current_hunk:
    filtered = process_hunk(current_hunk)
    if filtered:
        output_lines.extend(filtered)

# Print only significant hunks
for line in output_lines:
    sys.stdout.write(line)

proc.wait()
