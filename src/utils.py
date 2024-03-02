import argparse
import os.path
import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output
from polar_fox.utils import split_nml_string_lines as split_nml_string_lines
from polar_fox.utils import (
    unwrap_nml_string_declaration as unwrap_nml_string_declaration,
)


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


def get_docs_url():
    # not convinced this belongs in utils, but I can't find anywhere better to put it
    # could be in polar fox - method will be common to all grfs? - pass the project name as a var?
    # not convinced it's big enough to bother centralising TBH, too much close coupling has costs
    result = [global_constants.metadata["docs_url"]]
    if git_info.get_tag_exact_match() != "undefined":
        result.append(git_info.get_monorepo_tag_parts()[1])
    result.append("index.html")
    return "/".join(result)


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


def extend_list_to_power_of_2_length(list_to_extend):
    # length of random choices needs to be power of 2 as random choice can only be picked from powers of 2s (1 bit = 2 options, 2 bits = 4 options, 3 bits = 8 options, 4 bits = 16 options, 5 bits = 32 options)
    # so just do a clunky manual append here, JFDI, not figuring out a power of 2 detector at this time of night :P
    # this will cause uneven probabilities, but eh, life is not perfect
    if len(list_to_extend) == 3:
        list_to_extend.append(list_to_extend[0])
    if len(list_to_extend) >= 5 and len(list_to_extend) < 9:
        list_to_extend.extend(list_to_extend[: 8 - len(list_to_extend)])
    if len(list_to_extend) >= 9 and len(list_to_extend) < 17:
        list_to_extend.extend(list_to_extend[: 16 - len(list_to_extend)])
    if len(list_to_extend) >= 17 and len(list_to_extend) < 33:
        list_to_extend.extend(list_to_extend[: 32 - len(list_to_extend)])
    if len(list_to_extend) >= 33:
        list_to_extend.extend(list_to_extend[: 64 - len(list_to_extend)])
    return list_to_extend


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
