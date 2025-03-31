import codecs  # used for writing files - more unicode friendly than standard open() module

import sys
import os

currentdir = os.curdir
from time import time

import iron_horse
import utils
import global_constants
import pseudo_random_vehicle_maps
from polar_fox import git_info

# get args passed by makefile
command_line_args = utils.get_command_line_args()

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(
    currentdir, global_constants.chameleon_cache_dir
)
# exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
os.makedirs(chameleon_cache_path, exist_ok=True)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

# setup the places we look for templates
from chameleon import PageTemplateLoader
templates = PageTemplateLoader(os.path.join(currentdir, "src", "templates"), format="text")

generated_files_path = iron_horse.generated_files_path

def render_header_item_nml(header_item, roster, graphics_path, pseudo_random_vehicle_maps, git_revision):
    template = templates[header_item + ".pynml"]
    return utils.unescape_chameleon_output(
        template(
            roster=roster,
            global_constants=global_constants,
            temp_storage_ids=global_constants.temp_storage_ids,  # convenience measure
            utils=utils,
            livery_supplier=iron_horse.livery_supplier,
            badge_manager=iron_horse.badge_manager,
            railtype_manager=iron_horse.railtype_manager,
            roster_manager=iron_horse.roster_manager,
            graphics_path=graphics_path,
            git_revision=git_revision,
            pseudo_random_vehicle_maps=pseudo_random_vehicle_maps,
        )
    )


def render_item_nml(item, graphics_path):
    result = utils.unescape_chameleon_output(item.render(templates, graphics_path))
    # write the nml per item to disk, it aids debugging
    item_nml = codecs.open(
        os.path.join(generated_files_path, "nml", item.id + ".nml"), "w", "utf8"
    )
    item_nml.write(result)
    item_nml.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result


def main():
    globals()['logger'] = utils.get_logger(__file__)
    logger.info(f"[RENDER NML] {' '.join(sys.argv)}")
    start = time()
    iron_horse.main(run_post_validation_steps=True)

    roster = iron_horse.roster_manager.active_roster
    # expect Exception failures if there is no active roster, don't bother explicitly handling that case

    # we don't need to user os.path.join here, this is an nml path (and we want the explicit trailing slash also)
    graphics_path = "generated/graphics/" + roster.grf_name + "/"
    generated_nml_path = os.path.join(generated_files_path, "nml")
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(generated_nml_path, exist_ok=True)
    grf_nml = codecs.open(
        os.path.join(generated_files_path, command_line_args.grf_name + ".nml"),
        "w",
        "utf8",
    )

    spritelayer_cargos = iron_horse.registered_spritelayer_cargos

    # expensive if repeatedly computed
    git_revision = git_info.get_revision()

    header_items = [
        "header",
        "cargo_table",
        "signals",
        "railtypes",
        "badges",
        "spriteset_templates",
        "spritelayer_cargo_empty_ss",
        "tail_lights",
        "recolour_sprites",
        "procedures_var_41_but_badges_not_ids",
        "procedures_alternative_var_random_bits",
        "procedures_capacity",
        "procedures_cargo_subtypes",
        "procedures_colour_names",
        "procedures_haulage_bonus",
        "procedures_opening_doors",
        "procedures_powered_by_railtype",
        "procedures_rulesets",
        "procedures_visible_cargo",
        "procedures_wagon_recolour_strategies",
        "pseudo_random_vehicle_maps",
    ]

    for header_item in header_items:
        grf_nml.write(
            render_header_item_nml(header_item, roster, graphics_path, pseudo_random_vehicle_maps, git_revision)
        )

    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    # also multiprocessing failed on fiddly internal deps as of March 2025
    for spritelayercargo in spritelayer_cargos:
        grf_nml.write(render_item_nml(spritelayercargo, graphics_path))

    model_variant_timings = []
    for model_variant in roster.model_variants_in_order_optimised_for_action_2_ids:
        start_time = time()
        rendered_nml = render_item_nml(model_variant, graphics_path)
        grf_nml.write(rendered_nml)
        end_time = time()
        elapsed_time = end_time - start_time
        model_variant_timings.append((model_variant, elapsed_time))
    """
    # Sort timings by elapsed time in descending order (longest first)
    timings_sorted = sorted(model_variant_timings, key=lambda x: x[1], reverse=True)
    # Dump all timing information to a file after the loop
    with open('render_timings.txt', 'w') as f:
        for variant, duration in timings_sorted:
            f.write(f"{variant} | {variant.id}: {duration:.4f} seconds\n")
    """

    grf_nml.close()

    logger.info(
        f"[RENDER NML]"
        f"{command_line_args.grf_name} - complete "
        f"{utils.string_format_compile_time_deltas(start, time())}"
    )


if __name__ == "__main__":
    main()
