import argparse
import os.path
from functools import cached_property

import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output

def get_command_line_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-pw",
        "--pool_workers",
        type=int,
        default=0,
        dest="num_pool_workers",
        help="The number of pool workers to use in multiprocessing pools [default: 0] (multiprocessing disabled unless explicitly enabled)",
    )
    argparser.add_argument(
        "-gn",
        "--grf-name",
        dest="grf_name",
        required=True,
        help="The grf to build",
        # manually extend the list if more rosters are added
        choices=["iron-horse", "iron-moose", "iron-ibex", "id-report-only"],
    )
    argparser.add_argument(
        "-sd",
        "--suppress-docs",
        action=argparse.BooleanOptionalAction,
        dest="suppress_docs",
        help="Optionally suppress docs, can save some compile time",
    )
    return argparser.parse_args()

@cached_property
def git_tag_or_version():
    # expensive if repeated due to git lookup, pre-compute and cache it
    return git_info.get_monorepo_tag_parts()[1]

@cached_property
def docs_base_url():
    # not convinced this belongs in utils, but I can't find anywhere better to put it
    # could be in polar fox - method will be common to all grfs? - pass the project name as a var?
    # not convinced it's big enough to bother centralising TBH, too much close coupling has costs
    result = [global_constants.metadata["docs_url"]]
    if git_info.get_tag_exact_match() != "undefined":
        result.append(git_tag_or_version)
    return "/".join(result)


@cached_property
def docs_url():
    return docs_base_url + "/index.html"


def get_offsets(length):
    return global_constants.default_spritesheet_offsets[str(length)]


def unpack_colour(colour_name, cc_to_remap):
    # seems utils is the best place to keep this, but eh
    if "COLOUR_" in colour_name:
        # assume it's a default CC name constant
        if cc_to_remap == 1:
            return "palette_2cc(" + colour_name + ", company_colour2)"
        if cc_to_remap == 2:
            return "palette_2cc(company_colour1, " + colour_name + ")"
    else:
        # assume custom colour
        colour_name_offset = 2 * list(
            global_constants.custom_wagon_recolour_sprite_maps.keys()
        ).index(colour_name)
        remap_index = colour_name_offset + cc_to_remap - 1
        # return an nml fragment: custom_ship_recolour_sprites + index into recolour sprite + [company_colour1 or company_colour2]
        return (
            "custom_wagon_recolour_sprites + "
            + str(16 * remap_index)
            + " + company_colour"
            + str(1 if cc_to_remap == 2 else 2)
        )


def convert_flat_list_to_pairs_of_tuples(flat_list):
    # used to create a list suitable for iterating over and pushing values to the text stack
    # parse a flat list [a, b, c] into a list of 2 tuples [(a, b), (c, 0)] as we need to push 2 WORD values into each DWORD text stack register
    pairs = [
        (
            flat_list[i],
            flat_list[i + 1] if i + 1 < len(flat_list) else "0",
        )
        for i in range(0, len(flat_list), 2)
    ]
    return pairs

def string_format_compile_time_deltas(time_start, time_later):
    return format((time_later - time_start), ".2f") + " s"


def grfid_to_dword(grfid: str) -> str:
    """
    Convert a GRF ID string like "CA\\12\\22" into a DWORD in hexadecimal format.

    Args:
        grfid (str): The GRF ID string, e.g., "CA\\12\\22".

    Returns:
        str: The DWORD representation in hexadecimal (e.g., "0x43411222").
    """
    # Remove backslashes and split into parts
    parts = grfid.split("\\")
    # Convert the parts into bytes
    byte_values = [ord(parts[0][0]), ord(parts[0][1]), int(parts[1], 16), int(parts[2], 16)]
    # Combine into a single DWORD using big-endian order
    dword = (byte_values[0] << 24) | (byte_values[1] << 16) | (byte_values[2] << 8) | byte_values[3]
    # Return as hexadecimal string
    return f"{dword:08X}"

# move logger to Polar Fox?
import logging
import os
import sys

def get_logger(module_name):
    """Return a logger configured to write to a file named after the module (with timestamp and level)
    and to stdout (with plain message)."""
    logger = logging.getLogger(module_name)
    if not logger.handlers:  # Prevent duplicate handlers if the logger is already configured
        logger.setLevel(logging.DEBUG)

        # Ensure the log directory exists
        os.makedirs("build_logs", exist_ok=True)
        log_filename = os.path.join("build_logs", os.path.basename(module_name) + ".log")

        # File handler: timestamp truncated to seconds and log level included
        file_handler = logging.FileHandler(log_filename, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(message)s', datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler: plain message only
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger

# move timing decorator to Polar Fox?
import time
import functools

def timing(func):
    """Decorator that reports the execution time of the wrapped function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper
