import argparse
import os.path
import codecs  # used for writing files - more unicode friendly than standard open() module
import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output
from polar_fox.utils import split_nml_string_lines as split_nml_string_lines
from polar_fox.utils import unwrap_nml_string_declaration as unwrap_nml_string_declaration


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
        "-sc",
        "--suppress-cargo-sprites",
        action=argparse.BooleanOptionalAction,
        dest="suppress_cargo_sprites",
        help="Optionally suppress visible cargo sprites in the grf output, can save substantial compile time",
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


def parse_base_lang():
    # expose base lang strings to python - for reuse in docs
    base_lang_file = codecs.open(
        os.path.join(
            "generated", "lang", get_command_line_args().grf_name, "english.lng"
        ),
        "r",
        "utf8",
    )
    text = base_lang_file.readlines()
    # this is fragile, playing one line python is silly :)
    strings = dict(
        (line.split(":", 1)[0].strip(), line.split(":", 1)[1].strip())
        for line in text
        if ":" in line
    )
    return strings


def get_offsets(length, flipped=False):
    # offsets can also be over-ridden on a per-model basis by providing this property in the model class
    base_offsets = global_constants.default_spritesheet_offsets[str(length)]
    if flipped:
        flipped_offsets = list(base_offsets[4:8])
        flipped_offsets.extend(base_offsets[0:4])
        return flipped_offsets
    else:
        return base_offsets


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
        remap_index = (
            (
                2
                * list(global_constants.custom_wagon_recolour_sprite_maps.keys()).index(
                    colour_name
                )
            )
            + cc_to_remap
            - 1
        )
        # return an nml fragment in format "custom_wagon_recolour_sprites + 16 * 0 /* recolour set */ + company_colour1 /* or company_colour2 */"
        return (
            "custom_wagon_recolour_sprites + 16 * "
            + str(remap_index)
            + " + company_colour"
            + str(1 if cc_to_remap == 2 else 2)
        )
