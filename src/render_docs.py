import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
import multiprocessing
from itertools import repeat
from time import time
from PIL import Image
import markdown
import json

import iron_horse
import utils
from utils import timing
import global_constants
from doc_helper import DocHelper

metadata = {}
metadata.update(global_constants.metadata)

# get args passed by makefile
command_line_args = utils.get_command_line_args()

docs_src = os.path.join(currentdir, "src", "docs_templates")

palette = utils.dos_palette_to_rgb()


def render_docs(
    PageTemplateLoader,
    doc_list,
    file_type,
    docs_output_path,
    iron_horse,
    model_variants,
    doc_helper,
    use_markdown=False,
    source_is_repo_root=False,
):
    if source_is_repo_root:
        doc_path = os.path.join(currentdir)
    else:
        doc_path = docs_src

    docs_templates = PageTemplateLoader(doc_path, format="text")

    roster = iron_horse.roster_manager.active_roster
    # expect Exception failures if there is no active roster, don't bother explicitly handling that case

    for doc_name in doc_list:
        # .pt is the conventional extension for chameleon page templates
        template = docs_templates[doc_name + ".pt"]
        doc = template(
            roster=roster,
            catalogues=roster.catalogues,
            model_variants=model_variants,
            iron_horse=iron_horse,
            global_constants=global_constants,
            command_line_args=command_line_args,
            metadata=metadata,
            utils=utils,
            doc_helper=doc_helper,
            doc_name=doc_name,
        )
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = PageTemplateLoader(docs_src, format="text")[
                "markdown_wrapper.pt"
            ]
            doc = markdown_wrapper(
                content=markdown.markdown(doc),
                roster=roster,
                model_variants=model_variants,
                global_constants=global_constants,
                command_line_args=command_line_args,
                metadata=metadata,
                utils=utils,
                doc_helper=doc_helper,
                doc_name=doc_name,
            )
        # save the results of templating
        doc_file = codecs.open(
            os.path.join(docs_output_path, doc_name + "." + file_type),
            "w",
            "utf8",
        )
        doc_file.write(doc)
        doc_file.close()


def render_docs_vehicle_details(
    PageTemplateLoader, docs_output_path, doc_helper, catalogues, template_name
):

    docs_templates = PageTemplateLoader(docs_src, format="text")
    template = docs_templates[template_name + ".pt"]

    roster = iron_horse.roster_manager.active_roster
    for catalogue in catalogues:
        catalogue.assert_description_foamer_facts()
        doc_name = catalogue.model_id
        model_variants = roster.model_variants_by_catalogue[catalogue.model_id][
            "model_variants"
        ]

        doc = template(
            roster=roster,
            catalogue=catalogue,
            model_variants=model_variants,
            example_model_variant=catalogue.example_model_variant,
            iron_horse=iron_horse,
            global_constants=global_constants,
            command_line_args=command_line_args,
            metadata=metadata,
            utils=utils,
            doc_helper=doc_helper,
            doc_name=doc_name,
        )
        doc_file = codecs.open(
            os.path.join(docs_output_path, doc_name + ".html"), "w", "utf8"
        )
        doc_file.write(doc)
        doc_file.close()


def render_docs_badge_images(generated_graphics_path, static_dir_dst, doc_helper):
    badge_sprites_dir_src = os.path.join(generated_graphics_path, "badges")
    badge_sprites_dir_dst = os.path.join(static_dir_dst, "img", "badges")
    os.makedirs(badge_sprites_dir_dst)

    dos_palette = Image.open("palette_key.png").palette

    for livery_name, livery in iron_horse.livery_supplier.items():
        if livery.has_predrawn_badge_sprite:
            badge_spritesheet_filename = f"livery_{livery_name.lower()}.png"
            badge_spritesheet = Image.open(
                os.path.join(generated_graphics_path, "badges", badge_spritesheet_filename)
            )

            dest_image = Image.new(
                "P",
                (
                    14,
                    8,
                ),
                255,
            )

            badge_image_tmp = badge_spritesheet.crop(
                box=(
                    10,
                    10,
                    24,
                    18
                )
            )
            crop_box_dest = (
                0,
                0,
                14,
                8,
            )
            dest_image.paste(
                badge_image_tmp.crop(crop_box_dest), crop_box_dest
            )

            dest_image.putpalette(dos_palette)

            cc_remap_indexes = doc_helper.remap_company_colours(
                {"CC1": "COLOUR_RED", "CC2": "COLOUR_WHITE"}
            )
            dest_image = dest_image.copy().point(
                lambda i: cc_remap_indexes[i] if i in cc_remap_indexes.keys() else i
            )

            output_path = os.path.join(badge_sprites_dir_dst, badge_spritesheet_filename)
            dest_image.save(output_path, optimize=True, transparency=0)
            dest_image.close()


def render_docs_vehicle_images(
    model_variant_catalogue_mapping, static_dir_dst, generated_graphics_path, doc_helper
):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs
    catalogue = model_variant_catalogue_mapping["catalogue"]

    vehicle_spritesheet = Image.open(
        os.path.join(generated_graphics_path, catalogue.model_id + ".png")
    )
    dos_palette = Image.open("palette_key.png").palette

    docs_image_variants = []

    for model_variant in model_variant_catalogue_mapping["model_variants"]:
        if catalogue.wagon_quacker.quack:
            # optimise output by only generating one livery image for wagons
            # we accidentally had 13k images in static dir at one point, many of them empty images for wagon variants
            # we *do* want docs images for all trailer model variants
            if (
                (not model_variant.is_default_model_variant)
                and (catalogue.cab_engine_model is None)
                and (not model_variant.catalogue.wagon_quacker.is_pax_or_mail_car)
            ):
                continue

        intermediate_image = Image.new(
            "P",
            (
                doc_helper.docs_sprite_width(model_variant=model_variant),
                doc_helper.docs_sprite_height,
            ),
            255,
        )
        intermediate_image.putpalette(dos_palette)

        if model_variant.model_def.docs_image_spriterow is not None:
            y_offset = 30 * model_variant.model_def.docs_image_spriterow
        # !! requires_custom_buy_menu_sprite could be folded into producer or catalogue entry
        elif model_variant.requires_custom_buy_menu_sprite:
            # further possibly fragile special-casing
            if (getattr(model_variant, "livery_group_name", None) is not None) or (
                getattr(
                    model_variant.catalogue.cab_engine_model, "livery_group_name", None
                )
                is not None
            ):
                # if a livery group is used, the custom buy menu sprites will have been generated in livery order, with row offsets already applied as needed
                y_offset = 30 * model_variant.catalogue_entry.index
            else:
                # otherwise apply the row offset from the livery
                y_offset = (
                    30 * model_variant.catalogue_entry.livery_def.relative_spriterow_num
                )
        else:
            y_offset = (
                30
                * model_variant.catalogue_entry.livery_def.relative_spriterow_num
                * model_variant.gestalt_graphics.num_load_state_or_similar_spriterows
            )
        # relies on additional_liveries being in predictable row offsets (should be true as of July 2020)
        source_vehicle_image_tmp = vehicle_spritesheet.crop(
            box=(
                model_variant.buy_menu_x_loc,
                10 + y_offset,
                model_variant.buy_menu_x_loc
                + doc_helper.docs_sprite_width(model_variant=model_variant),
                10 + y_offset + doc_helper.docs_sprite_height,
            )
        )
        crop_box_dest = (
            0,
            0,
            doc_helper.docs_sprite_width(model_variant=model_variant),
            doc_helper.docs_sprite_height,
        )
        intermediate_image.paste(
            source_vehicle_image_tmp.crop(crop_box_dest), crop_box_dest
        )

        # add pantographs if needed
        if model_variant.pantograph_type is not None:
            # buy menu uses pans 'down', but in docs pans 'up' looks better, weird eh?
            pantographs_spritesheet = Image.open(
                os.path.join(
                    generated_graphics_path, catalogue.model_id + "_pantographs_up.png"
                )
            )
            pan_crop_width = model_variant.buy_menu_width
            # dual_headed is never anything but special casing to handle the OpenTTD magical behaviour eh? :)
            if model_variant.dual_headed:
                pan_crop_width = pan_crop_width * 2
            pantographs_image = pantographs_spritesheet.crop(
                box=(
                    model_variant.buy_menu_x_loc,
                    10,
                    model_variant.buy_menu_x_loc + pan_crop_width,
                    10 + doc_helper.docs_sprite_height,
                )
            )
            pantographs_mask = pantographs_image.copy()
            pantographs_mask = pantographs_mask.point(
                lambda i: 0 if i == 255 or i == 0 else 255
            ).convert(
                "1"
            )  # the inversion here of blue and white looks a bit odd, but potato / potato
            intermediate_image.paste(
                pantographs_image.crop(crop_box_dest),
                crop_box_dest,
                pantographs_mask.crop(crop_box_dest),
            )

        for (
            cc_remap_pair
        ) in model_variant.catalogue_entry.livery_def.docs_image_input_cc:
            # handle possible remap of CC1
            if model_variant.catalogue_entry.livery_def.remap_to_cc is not None:
                CC1_remap = model_variant.catalogue_entry.livery_def.remap_to_cc[
                    "company_colour1"
                ]
                CC2_remap = model_variant.catalogue_entry.livery_def.remap_to_cc[
                    "company_colour2"
                ]
                if CC1_remap == "company_colour1":
                    CC1_remap = cc_remap_pair[0]
                if CC1_remap == "company_colour2":
                    CC1_remap = cc_remap_pair[1]
                if CC2_remap == "company_colour1":
                    CC2_remap = cc_remap_pair[0]
                if CC2_remap == "company_colour2":
                    CC2_remap = cc_remap_pair[1]
            else:
                CC1_remap = cc_remap_pair[0]
                CC2_remap = cc_remap_pair[1]

            cc_remap_indexes = doc_helper.remap_company_colours(
                {"CC1": CC1_remap, "CC2": CC2_remap}
            )

            # CABBAGE - need to support non-CC defaults via purchase_swatch_colour_set_names
            # cabbage - this is only for 100% recolours of CC in game using recolour sprites, not for compile time recolours, which should already be baked in to the sprite
            # CABBAGE JFDI conditional insertions for non CC recolour, could clean up the entire flow
            custom_remap_indexes = None
            if (
                len(
                    model_variant.catalogue_entry.livery_def.purchase_swatch_colour_set_names
                )
                > 0
            ):
                colour_set_name = model_variant.catalogue_entry.livery_def.purchase_swatch_colour_set_names[
                    0
                ]
                if colour_set_name in global_constants.colour_sets:
                    colour_set = global_constants.colour_sets[colour_set_name]
                    custom_remap_indexes = {}
                    for i in range(8):
                        custom_remap_indexes[198 + i] = (
                            global_constants.custom_wagon_recolour_sprite_maps[
                                colour_set[0]
                            ][i]
                        )
            # CABBAGE JFDI conditional insertions for non CC recolour, could clean up the entire flow
            if custom_remap_indexes is not None:
                for k, v in custom_remap_indexes.items():
                    cc_remap_indexes[k] = v

            dest_image = intermediate_image.copy().point(
                lambda i: cc_remap_indexes[i] if i in cc_remap_indexes.keys() else i
            )

            # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
            dest_image = dest_image.resize(
                (
                    4 * intermediate_image.size[0],
                    4 * doc_helper.docs_sprite_height,
                ),
                resample=Image.Resampling.NEAREST,
            )

            remap_name = doc_helper.get_livery_file_substr(cc_remap_pair)
            output_path = os.path.join(
                static_dir_dst,
                "img",
                model_variant.id + "_" + remap_name + ".png",
            )
            dest_image.save(output_path, optimize=True, transparency=0)
            dest_image.close()


def export_roster_to_json(roster, output_dir="docs"):
    """
    Exports a roster to JSON for documentation and data interchange.

    Args:
        roster (Roster): The roster object containing engines and wagons.
        output_dir (str): Directory to save the JSON file.
    """
    json_start = time()

    data = {
        "name": roster.grf_name,
        "engines": [],
        "wagons": [],
    }

    # Extract engine properties
    for engine in roster.engine_model_variants:
        engine_data = {
            "model_id": getattr(engine, "model_id", "N/A"),
            "id": getattr(engine, "id", "N/A"),
            "name": getattr(
                engine, "name", "Unnamed Engine"
            ),  # Using 'id' as a placeholder
            "power": getattr(engine, "power", 0),
            "max_speed": getattr(engine, "speed", 0),
            "generation": getattr(engine, "gen"),
        }
        data["engines"].append(engine_data)

    # Extract wagon properties
    for wagon in roster.wagon_model_variants:
        wagon_data = {
            "id": getattr(wagon, "id", "N/A"),
            "name": getattr(wagon, "id", "Unnamed Wagon"),
            "cargo_types": getattr(
                wagon, "cargo_types", []
            ),  # Empty list if not available
            "generation": getattr(wagon, "gen"),
        }
        data["wagons"].append(wagon_data)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    """ # commented out as rarely used
    # Write to JSON file
    file_path = os.path.join(output_dir, f"{roster.grf_name}.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(
        f"Roster exported to {file_path} "
        f"{utils.string_format_compile_time_deltas(json_start, time())}"
    )
    """


def main():
    globals()["logger"] = utils.get_logger(__file__)
    if command_line_args.suppress_docs:
        logger.info("[SKIPPING DOCS] render_docs.py (suppress_docs makefile flag set)")
        return
    logger.info(f"[RENDER DOCS] {' '.join(sys.argv)}")
    start = time()
    # don't init iron_horse on import of this module, do it explicitly inside main()
    iron_horse.main()

    roster = iron_horse.roster_manager.active_roster

    # can't pass roster in to DocHelper at init, multiprocessing fails as it can't pickle the roster object
    doc_helper = DocHelper(
        lang_data=roster.get_lang_data("english", context="docs"),
    )

    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
    num_pool_workers = command_line_args.num_pool_workers
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        logger.info("Multiprocessing disabled: (PW=0)")
    else:
        use_multiprocessing = True
        # mp_logger = multiprocessing.log_to_stderr()
        # mp_logger.setLevel(25)
        # just print, no need for a coloured echo_message
        logger.info(f"Multiprocessing enabled: (PW={num_pool_workers})")

    # setting up a cache for compiled chameleon templates can significantly speed up template rendering
    chameleon_cache_path = os.path.join(
        currentdir, global_constants.chameleon_cache_dir
    )
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(chameleon_cache_path, exist_ok=True)
    os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_output_path = os.path.join(currentdir, "docs", command_line_args.grf_name)
    html_docs_output_path = os.path.join(docs_output_path, "html")
    if os.path.exists(docs_output_path):
        shutil.rmtree(docs_output_path)
    os.makedirs(docs_output_path)
    os.makedirs(html_docs_output_path)

    shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)
    # convenience for local development, this means docs/index.html can be opened from shell, and has list of links to tech tree, which is a common use case
    shutil.copyfile(
        os.path.join(docs_src, "local_docs_root.html"),
        os.path.join(currentdir, "docs", "index.html"),
    )

    static_dir_src = os.path.join(docs_src, "static")
    static_dir_dst = os.path.join(html_docs_output_path, "static")
    shutil.copytree(static_dir_src, static_dir_dst)

    # process images for use in docs
    generated_graphics_path = os.path.join(
        iron_horse.generated_files_path, "graphics", roster.grf_name
    )

    # we need to filesystem copy badge sprites
    # untimed - probably fine?
    render_docs_badge_images(generated_graphics_path, static_dir_dst, doc_helper)

    # process vehicle images for docs use
    # yes, I really did bother using a pool to save at best a couple of seconds, because FML :)
    render_docs_vehicle_images_start = time()
    if not use_multiprocessing:
        for (
            model_variant_catalogue_mapping
        ) in roster.model_variants_by_catalogue.values():
            render_docs_vehicle_images(
                model_variant_catalogue_mapping,
                static_dir_dst,
                generated_graphics_path,
                doc_helper,
            )
    else:
        pool = multiprocessing.Pool(processes=num_pool_workers)
        for (
            model_variant_catalogue_mapping
        ) in roster.model_variants_by_catalogue.values():
            pool.apply_async(
                render_docs_vehicle_images,
                args=(
                    model_variant_catalogue_mapping,
                    static_dir_dst,
                    generated_graphics_path,
                    doc_helper,
                ),
            )

        pool.close()
        # omit pool.join() if fire-and-forget is acceptable
        # pool.join()
    # note that we can't trivially get the time to actually render the docs images due to async
    logger.info(
        f"docs images *dispatched* via async: "
        f"{utils.string_format_compile_time_deltas(render_docs_vehicle_images_start, time())}"
    )

    # note we remove any model variants that are clones, we don't need them in docs
    model_variants = [
        model_variant
        for model_variant in roster.model_variants
        if model_variant.catalogue.clone_quacker.quack == False
    ]
    # default sort for docs is by intro year
    model_variants = sorted(
        model_variants, key=lambda model_variant: model_variant.catalogue.intro_year
    )
    dates = sorted([i.catalogue.intro_year for i in model_variants])
    metadata["dates"] = (dates[0], dates[-1])

    # render standard docs from a list
    html_docs = [
        "code_reference",  # 0.45 s?
        "get_started",  # 0.39 s?
        "liveries",
        "translations",  # 0.40 s?
        "tech_tree_table_blue",  # 0.82 s?
        "tech_tree_table_red",  # 0.84 s?
        "tech_tree_table_blue_simplified",  # 0.81 s?
        "tech_tree_table_red_simplified",  #  0.84 s?
        "train_whack",  # 0.35 s?
        "trains",  #  0.71 s?
    ]
    txt_docs = ["readme"]
    license_docs = ["license"]
    markdown_docs = ["changelog"]

    render_base_files_start = time()
    render_docs(
        PageTemplateLoader,
        html_docs,
        "html",
        html_docs_output_path,
        iron_horse,
        model_variants,
        doc_helper,
    )
    render_docs(
        PageTemplateLoader,
        txt_docs,
        "txt",
        docs_output_path,
        iron_horse,
        model_variants,
        doc_helper,
    )
    render_docs(
        PageTemplateLoader,
        license_docs,
        "txt",
        docs_output_path,
        iron_horse,
        model_variants,
        doc_helper,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(
        PageTemplateLoader,
        markdown_docs,
        "txt",
        docs_output_path,
        iron_horse,
        model_variants,
        doc_helper,
    )
    render_docs(
        PageTemplateLoader,
        markdown_docs,
        "html",
        html_docs_output_path,
        iron_horse,
        model_variants,
        doc_helper,
        use_markdown=True,
    )
    logger.info(
        f"render_docs (base files) "
        f"{utils.string_format_compile_time_deltas(render_base_files_start, time())}"
    )

    # render vehicle details
    # this is slow and _might_ go faster in an MP pool, but eh overhead...
    render_vehicle_details_start = time()
    render_docs_vehicle_details(
        PageTemplateLoader,
        html_docs_output_path,
        doc_helper,
        catalogues=roster.engine_catalogues,
        template_name="vehicle_details_engine",
    )
    logger.info(
        f"render_docs_vehicle_details "
        f"{utils.string_format_compile_time_deltas(render_vehicle_details_start, time())}"
    )

    export_roster_to_json(roster)

    logger.set_colour("cyan")
    logger.info(
        f"[RENDER DOCS] "
        f"{command_line_args.grf_name} - complete "
        f"{utils.string_format_compile_time_deltas(start, time())}"
    )
    logger.set_colour("reset")


if __name__ == "__main__":
    main()
