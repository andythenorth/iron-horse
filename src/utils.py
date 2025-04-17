import argparse
import os.path
from functools import lru_cache

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


@lru_cache(maxsize=None)
def get_git_tag_or_version():
    # expensive if repeated due to git lookup, pre-compute and cache it
    return git_info.get_monorepo_tag_parts()[1]


@lru_cache(maxsize=None)
def get_docs_base_url():
    # not convinced this belongs in utils, but I can't find anywhere better to put it
    # could be in polar fox - method will be common to all grfs? - pass the project name as a var?
    # not convinced it's big enough to bother centralising TBH, too much close coupling has costs
    result = [global_constants.metadata["docs_url"]]
    if git_info.get_tag_exact_match() != "undefined":
        result.append(get_git_tag_or_version())
    return "/".join(result)


@lru_cache(maxsize=None)
def get_docs_url():
    return get_docs_base_url() + "/index.html"


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


def nml_safe_id(s: str) -> str:
    NML_SAFE_REPLACEMENTS = {
        "/": "_",
        "-": "_minus_",
        "!": "_shebang_",
        # add more here as needed
    }
    for bad_char, replacement in NML_SAFE_REPLACEMENTS.items():
        s = s.replace(bad_char, replacement)
    return s


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
    byte_values = [
        ord(parts[0][0]),
        ord(parts[0][1]),
        int(parts[1], 16),
        int(parts[2], 16),
    ]
    # Combine into a single DWORD using big-endian order
    dword = (
        (byte_values[0] << 24)
        | (byte_values[1] << 16)
        | (byte_values[2] << 8)
        | byte_values[3]
    )
    # Return as hexadecimal string
    return f"{dword:08X}"


# move logger to Polar Fox?
import logging
import os
import sys
import re

# ANSI escape codes
COLOR_CODES = {
    "reset": "\033[0m",
    "cyan": "\033[96m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "aquamarine": "\033[38;5;122m",
    # Add more as needed
}

ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")


class ColoredLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
        self._current_colour = None

    def set_colour(self, colour_name):
        if colour_name in COLOR_CODES:
            self._current_colour = COLOR_CODES[colour_name]
        else:
            raise ValueError(f"Unknown colour: {colour_name}")

    def reset_colour(self):
        self._current_colour = None

    def get_colour(self):
        return self._current_colour


class ColorizingFormatter(logging.Formatter):
    """Applies colour only in console formatter, not in log files."""

    def __init__(self, get_colour_fn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._get_colour = get_colour_fn

    def format(self, record):
        msg = super().format(record)
        colour = self._get_colour()
        if colour:
            return f"{colour}{msg}{COLOR_CODES['reset']}"
        return msg


class StrippingFormatter(logging.Formatter):
    """Strips ANSI codes from log file output."""

    def format(self, record):
        msg = super().format(record)
        return ANSI_ESCAPE_RE.sub("", msg)


def get_logger(module_name):
    logging.setLoggerClass(ColoredLogger)
    logger = logging.getLogger(module_name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Ensure log dir exists
        os.makedirs("build_logs", exist_ok=True)
        log_filename = os.path.join(
            "build_logs", os.path.basename(module_name) + ".log"
        )

        # File handler — strip ANSI
        file_handler = logging.FileHandler(log_filename, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = StrippingFormatter(
            "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler — apply ANSI
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = ColorizingFormatter(logger.get_colour, "%(message)s")
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
