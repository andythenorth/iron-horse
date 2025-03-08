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
import global_constants
from polar_fox import git_info
from doc_helper import DocHelper

metadata = {}
metadata.update(global_constants.metadata)

# get args passed by makefile
command_line_args = utils.get_command_line_args()

docs_src = os.path.join(currentdir, "src", "docs_templates")

palette = utils.dos_palette_to_rgb()


def render_docs(
    doc_list,
    file_type,
    docs_output_path,
    iron_horse,
    consists,
    doc_helper,
    use_markdown=False,
    source_is_repo_root=False,
):
    roster = iron_horse.roster_manager.active_roster
    # expect Exception failures if there is no active roster, don't bother explicitly handling that case

    if source_is_repo_root:
        doc_path = os.path.join(currentdir)
    else:
        doc_path = docs_src
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(doc_path, format="text")

    for doc_name in doc_list:
        # .pt is the conventional extension for chameleon page templates
        template = docs_templates[doc_name + ".pt"]
        doc = template(
            roster=roster,
            consists=consists,
            iron_horse=iron_horse,
            global_constants=global_constants,
            command_line_args=command_line_args,
            git_info=git_info,
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
                consists=consists,
                global_constants=global_constants,
                command_line_args=command_line_args,
                git_info=git_info,
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
    docs_output_path, doc_helper, catalogues, template_name
):
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(docs_src, format="text")
    template = docs_templates[template_name + ".pt"]

    roster = iron_horse.roster_manager.active_roster
    for catalogue in catalogues:
        # model_type.assert_description_foamer_facts() CABBAGE
        doc_name = catalogue.id
        consists = roster.consists_by_catalogue[catalogue.id]['consists']

        doc = template(
            roster=roster,
            catalogue=catalogue,
            consists=consists,
            default_model_variant=catalogue.default_model_variant_from_roster,
            dedicated_trailer_catalogue_model_variant_mappings=catalogue.dedicated_trailer_catalogue_model_variant_mappings,
            iron_horse=iron_horse,
            global_constants=global_constants,
            command_line_args=command_line_args,
            git_info=git_info,
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


def render_docs_images(
    consist_catalogue_mapping, static_dir_dst, generated_graphics_path, doc_helper
):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs
    catalogue = consist_catalogue_mapping["catalogue"]

    vehicle_spritesheet = Image.open(
        os.path.join(generated_graphics_path, catalogue.id + ".png")
    )
    dos_palette = Image.open("palette_key.png").palette

    docs_image_variants = []

    for consist in consist_catalogue_mapping["consists"]:
        if consist.is_wagon_for_docs:
            # optimise output by only generating one livery image for wagons
            # we accidentally had 13k images in static dir at one point, many of them empty images for wagon variants
            # we *do* want docs images for all trailer model variants
            # CABBAGE cab consist stuff isn't working right yet - see Blaze is broken (should be more trailers)
            if (not consist.is_default_model_variant) and (consist.model_def.cab_id is None):
                continue

        intermediate_image = Image.new(
            "P",
            (doc_helper.docs_sprite_width(consist), doc_helper.docs_sprite_height),
            255,
        )
        intermediate_image.putpalette(dos_palette)

        if consist.model_def.docs_image_spriterow is not None:
            y_offset = 30 * consist.model_def.docs_image_spriterow
        # CABBAGE requires_custom_buy_menu_sprite could be folded into factory or catalogue entry
        elif consist.requires_custom_buy_menu_sprite:
            y_offset = 30 * consist.catalogue_entry.livery_def.relative_spriterow_num
        else:
            y_offset = (
                30
                * consist.catalogue_entry.livery_def.relative_spriterow_num
                * consist.gestalt_graphics.num_load_state_or_similar_spriterows
            )
        # relies on additional_liveries being in predictable row offsets (should be true as of July 2020)
        source_vehicle_image_tmp = vehicle_spritesheet.crop(
            box=(
                consist.buy_menu_x_loc,
                10 + y_offset,
                consist.buy_menu_x_loc + doc_helper.docs_sprite_width(consist),
                10 + y_offset + doc_helper.docs_sprite_height,
            )
        )
        crop_box_dest = (
            0,
            0,
            doc_helper.docs_sprite_width(consist),
            doc_helper.docs_sprite_height,
        )
        intermediate_image.paste(
            source_vehicle_image_tmp.crop(crop_box_dest), crop_box_dest
        )

        # add pantographs if needed
        if consist.pantograph_type is not None:
            # buy menu uses pans 'down', but in docs pans 'up' looks better, weird eh?
            pantographs_spritesheet = Image.open(
                os.path.join(
                    generated_graphics_path, catalogue.id + "_pantographs_up.png"
                )
            )
            pan_crop_width = consist.buy_menu_width
            # dual_headed is never anything but special casing to handle the OpenTTD magical behaviour eh? :)
            if consist.dual_headed:
                pan_crop_width = pan_crop_width * 2
            pantographs_image = pantographs_spritesheet.crop(
                box=(
                    consist.buy_menu_x_loc,
                    10,
                    consist.buy_menu_x_loc + pan_crop_width,
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

        for cc_remap_pair in consist.catalogue_entry.livery_def.docs_image_input_cc:
            # handle possible remap of CC1
            if consist.catalogue_entry.livery_def.remap_to_cc is not None:
                CC1_remap = consist.catalogue_entry.livery_def.remap_to_cc[
                    "company_colour1"
                ]
                CC2_remap = consist.catalogue_entry.livery_def.remap_to_cc[
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
                consist.id + "_" + remap_name + ".png",
            )
            dest_image.save(output_path, optimize=True, transparency=0)
            dest_image.close()


def export_roster_to_json(roster, output_dir="docs"):
    """
    Exports a roster to JSON for documentation and data interchange.

    Args:
        roster (Roster): The roster object containing engine and wagon consists.
        output_dir (str): Directory to save the JSON file.
    """
    data = {
        "name": roster.grf_name,
        "engines": [],
        "wagons": [],
    }

    # Extract engine properties
    for engine in roster.engine_consists:
        engine_data = {
            "id": getattr(engine, "id", "N/A"),
            "name": getattr(
                engine, "id", "Unnamed Engine"
            ),  # Using 'id' as a placeholder
            "power": getattr(engine, "power", 0),
            "max_speed": getattr(engine, "speed", 0),
        }
        data["engines"].append(engine_data)

    # Extract wagon properties
    for wagon in roster.wagon_consists:
        wagon_data = {
            "id": getattr(wagon, "id", "N/A"),
            "name": getattr(wagon, "id", "Unnamed Wagon"),
            "cargo_types": getattr(
                wagon, "cargo_types", []
            ),  # Empty list if not available
        }
        data["wagons"].append(wagon_data)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write to JSON file
    file_path = os.path.join(output_dir, f"{roster.grf_name}.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Roster exported to {file_path}")


def main():
    if command_line_args.suppress_docs:
        print("[SKIPPING DOCS] render_docs.py (suppress_docs makefile flag set)")
        return
    print("[RENDER DOCS]", " ".join(sys.argv))
    start = time()
    # don't init iron_horse on import of this module, do it explicitly inside main()
    iron_horse.main()

    roster = iron_horse.roster_manager.active_roster
    # can't pass roster in to DocHelper at init, multiprocessing fails as it can't pickle the roster object
    doc_helper = DocHelper(
        lang_strings=roster.get_lang_data("english", context="docs")["lang_strings"]
    )

    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
    num_pool_workers = command_line_args.num_pool_workers
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        print("Multiprocessing disabled: (PW=0)")
    else:
        use_multiprocessing = True
        # logger = multiprocessing.log_to_stderr()
        # logger.setLevel(25)
        # just print, no need for a coloured echo_message
        print("Multiprocessing enabled: (PW=" + str(num_pool_workers) + ")")

    # setting up a cache for compiled chameleon templates can significantly speed up template rendering
    chameleon_cache_path = os.path.join(
        currentdir, global_constants.chameleon_cache_dir
    )
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(chameleon_cache_path, exist_ok=True)
    os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

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

    # note we remove any consists that are clones, we don't need them in docs
    consists = [
        consist
        for consist in roster.consists_in_buy_menu_order
        if consist.is_clone == False
    ]
    # default sort for docs is by intro year
    consists = sorted(consists, key=lambda consist: consist.intro_year)
    dates = sorted([i.intro_year for i in consists])
    metadata["dates"] = (dates[0], dates[-1])

    # render standard docs from a list
    html_docs = [
        "code_reference",
        "get_started",
        "translations",
        "tech_tree_table_blue",
        "tech_tree_table_red",
        "tech_tree_table_blue_simplified",
        "tech_tree_table_red_simplified",
        "train_whack",
        "trains",
    ]
    txt_docs = ["readme"]
    license_docs = ["license"]
    markdown_docs = ["changelog"]

    render_docs_start = time()
    export_roster_to_json(roster)
    render_docs(
        html_docs, "html", html_docs_output_path, iron_horse, consists, doc_helper
    )
    render_docs(txt_docs, "txt", docs_output_path, iron_horse, consists, doc_helper)
    render_docs(
        license_docs,
        "txt",
        docs_output_path,
        iron_horse,
        consists,
        doc_helper,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(
        markdown_docs, "txt", docs_output_path, iron_horse, consists, doc_helper
    )
    render_docs(
        markdown_docs,
        "html",
        html_docs_output_path,
        iron_horse,
        consists,
        doc_helper,
        use_markdown=True,
    )
    print(
        "render_docs (base files)",
        utils.string_format_compile_time_deltas(render_docs_start, time()),
    )

    # render vehicle details
    # this is slow and _might_ go faster in an MP pool, but eh overhead...
    render_vehicle_details_start = time()
    render_docs_vehicle_details(
        html_docs_output_path,
        doc_helper,
        catalogues=roster.engine_catalogues,
        template_name="vehicle_details_engine",
    )
    print(
        "render_docs_vehicle_details",
        utils.string_format_compile_time_deltas(render_vehicle_details_start, time()),
    )

    # process images for use in docs
    # yes, I really did bother using a pool to save at best a couple of seconds, because FML :)
    generated_graphics_path = os.path.join(
        iron_horse.generated_files_path, "graphics", roster.grf_name
    )
    render_docs_images_start = time()

    if use_multiprocessing == False:
        for consist_catalogue_mapping in roster.consists_by_catalogue.values():
            render_docs_images(
                consist_catalogue_mapping,
                static_dir_dst,
                generated_graphics_path,
                doc_helper,
            )
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the catalogue?
        # probably potato / potato tbh
        pool = multiprocessing.Pool(processes=num_pool_workers)
        pool.starmap(
            render_docs_images,
            zip(
                roster.consists_by_catalogue.values(),
                repeat(static_dir_dst),
                repeat(generated_graphics_path),
                repeat(doc_helper),
            ),
        )
        pool.close()
        pool.join()
    print(
        "render_docs_images",
        utils.string_format_compile_time_deltas(render_docs_images_start, time()),
    )

    print(
        "[RENDER DOCS]",
        command_line_args.grf_name,
        "- complete",
        utils.string_format_compile_time_deltas(start, time()),
    )

    # CABBAGE MIGRATION REPORT
    cabbage_2_buyable_variants = {}
    for consist in consists:
        if len(consist.cabbage_buyable_variants) > 1:
            cabbage_2_buyable_variants[consist.id] = consist.cabbage_buyable_variants
    print(
        "Consists with > 1 buyable variants:",
        str(len(cabbage_2_buyable_variants.keys())),
    )
    """
    for consist in consists:
        if consist.gestalt_graphics.__class__.__name__ == "GestaltGraphicsVisibleCargo":
            if len(set(consist.units)) > 1:
                raise Exception(consist.id)
    """


if __name__ == "__main__":
    main()
