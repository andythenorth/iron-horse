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
    consist, template_name, docs_output_path, consists, doc_helper
):
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(docs_src, format="text")
    template = docs_templates[template_name + ".pt"]
    doc_name = consist.id

    roster = iron_horse.roster_manager.active_roster
    doc = template(
        roster=roster,
        consist=consist,
        consists=consists,
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


def render_docs_images(consist, static_dir_dst, generated_graphics_path, doc_helper):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs

    vehicle_spritesheet = Image.open(
        os.path.join(generated_graphics_path, consist.id + ".png")
    )
    # these 'source' var names for images are misleading
    source_vehicle_image = Image.new(
        "P",
        (doc_helper.docs_sprite_width(consist), doc_helper.docs_sprite_height),
        255,
    )
    source_vehicle_image.putpalette(Image.open("palette_key.png").palette)

    docs_image_variants = []

    for variant in doc_helper.get_docs_livery_variants(consist):
        # !! massive JFDI hax to make this work - really the gestalt should know how many rows are consumed per livery
        if (
            consist.gestalt_graphics.__class__.__name__
            == "GestaltGraphicsConsistPositionDependent"
        ):
            y_offset = 60 * variant["buyable_variant"].relative_spriterow_num
        else:
            if consist.docs_image_spriterow is not None:
                y_offset = 30 * consist.docs_image_spriterow
            else:
                y_offset = 30 * variant["buyable_variant"].relative_spriterow_num
        if not consist.dual_headed:
            # relies on additional_liveries being in predictable row offsets (should be true as of July 2020)
            source_vehicle_image_tmp = vehicle_spritesheet.crop(
                box=(
                    consist.buy_menu_x_loc,
                    10 + y_offset,
                    consist.buy_menu_x_loc + doc_helper.docs_sprite_width(consist),
                    10 + y_offset + doc_helper.docs_sprite_height,
                )
            )
        if consist.dual_headed:
            # oof, super special handling of dual-headed vehicles, OpenTTD handles this automatically in the buy menu, but docs have to handle explicitly
            # !! hard-coded values might fail in future, sort that out then if needed, they can be looked up in global constants
            # !! this also won't work with engine additional_liveries currently
            source_vehicle_image_1 = vehicle_spritesheet.copy().crop(
                box=(
                    224,
                    10 + y_offset,
                    224 + (4 * consist.length) + 1,
                    10 + y_offset + doc_helper.docs_sprite_height,
                )
            )
            source_vehicle_image_2 = vehicle_spritesheet.copy().crop(
                box=(
                    104,
                    10 + y_offset,
                    104 + (4 * consist.length) + 1,
                    10 + y_offset + doc_helper.docs_sprite_height,
                )
            )
            source_vehicle_image_tmp = source_vehicle_image.copy()
            source_vehicle_image_tmp.paste(
                source_vehicle_image_1,
                (
                    0,
                    0,
                    source_vehicle_image_1.size[0],
                    doc_helper.docs_sprite_height,
                ),
            )
            source_vehicle_image_tmp.paste(
                source_vehicle_image_2,
                (
                    source_vehicle_image_1.size[0] - 1,
                    0,
                    source_vehicle_image_1.size[0] - 1 + source_vehicle_image_2.size[0],
                    doc_helper.docs_sprite_height,
                ),
            )
        crop_box_dest = (
            0,
            0,
            doc_helper.docs_sprite_width(consist),
            doc_helper.docs_sprite_height,
        )
        source_vehicle_image.paste(
            source_vehicle_image_tmp.crop(crop_box_dest), crop_box_dest
        )

        # add pantographs if needed
        if consist.pantograph_type is not None:
            # buy menu uses pans 'down', but in docs pans 'up' looks better, weird eh?
            pantographs_spritesheet = Image.open(
                os.path.join(
                    generated_graphics_path, consist.id + "_pantographs_up.png"
                )
            )
            pan_crop_width = consist.buy_menu_width
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
            source_vehicle_image.paste(
                pantographs_image.crop(crop_box_dest),
                crop_box_dest,
                pantographs_mask.crop(crop_box_dest),
            )

            if consist.dual_headed:
                # oof, super special handling of pans for dual-headed vehicles
                pan_start_x_loc = (
                    global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[
                        2
                    ][0]
                )
                pantographs_image = pantographs_spritesheet.crop(
                    box=(
                        pan_start_x_loc,
                        10,
                        pan_start_x_loc + pan_crop_width,
                        10 + doc_helper.docs_sprite_height,
                    )
                )
                crop_box_dest_pan_2 = (
                    int(doc_helper.docs_sprite_width(consist) / 2),
                    0,
                    int(doc_helper.docs_sprite_width(consist) / 2) + pan_crop_width,
                    doc_helper.docs_sprite_height,
                )
                pantographs_mask = pantographs_image.copy()
                pantographs_mask = pantographs_mask.point(
                    lambda i: 0 if i == 255 or i == 0 else 255
                ).convert(
                    "1"
                )  # the inversion here of blue and white looks a bit odd, but potato / potato
                source_vehicle_image.paste(
                    pantographs_image, crop_box_dest_pan_2, pantographs_mask
                )
                pantographs_spritesheet.close()
        docs_image_variants.append(
            [
                source_vehicle_image.copy(),
                variant,
            ]
        )

    for processed_vehicle_image, variant in docs_image_variants:
        cc_remap_indexes = doc_helper.remap_company_colours(variant["cc_remaps"])
        # probably fragile workaround to use the alternative livery spriterow
        # for the edge case that a docs default livery 2nd company colour matches the alternative livery triggers
        # !! but this is the same line as above?? what's it supposed to be doing?
        cc_remap_indexes = doc_helper.remap_company_colours(variant["cc_remaps"])

        processed_vehicle_image = processed_vehicle_image.copy().point(
            lambda i: cc_remap_indexes[i] if i in cc_remap_indexes.keys() else i
        )

        # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
        processed_vehicle_image = processed_vehicle_image.resize(
            (
                4 * processed_vehicle_image.size[0],
                4 * doc_helper.docs_sprite_height,
            ),
            resample=Image.Resampling.NEAREST,
        )
        output_path = os.path.join(
            static_dir_dst,
            "img",
            consist.id + "_" + variant["livery_name"] + ".png",
        )
        processed_vehicle_image.save(output_path, optimize=True, transparency=0)
    source_vehicle_image.close()


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
    doc_helper = DocHelper(lang_strings=roster.get_lang_data("english")["lang_strings"])

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
    shutil.copyfile(os.path.join(docs_src, "local_docs_root.html"), os.path.join(currentdir, "docs", "index.html"))

    static_dir_src = os.path.join(docs_src, "static")
    static_dir_dst = os.path.join(html_docs_output_path, "static")
    shutil.copytree(static_dir_src, static_dir_dst)

    consists = roster.consists_in_buy_menu_order
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
    print("render_docs", time() - render_docs_start)

    # render vehicle details
    # this is slow and _might_ go faster in an MP pool, but eh overhead...
    render_vehicle_details_start = time()
    for consist in roster.engine_consists:
        consist.assert_description_foamer_facts()
        render_docs_vehicle_details(
            consist,
            "vehicle_details_engine",
            html_docs_output_path,
            consists,
            doc_helper,
        )
    """
    for wagon_class in global_constants.buy_menu_sort_order_wagons:
        for consist in roster.wagon_consists[wagon_class]:
            render_docs_vehicle_details(consist, "vehicle_details_wagon", html_docs_output_path, consists)
    """
    print("render_docs_vehicle_details", time() - render_vehicle_details_start)

    # process images for use in docs
    # yes, I really did bother using a pool to save at best a couple of seconds, because FML :)
    generated_graphics_path = os.path.join(
        iron_horse.generated_files_path, "graphics", roster.grf_name
    )
    slow_start = time()
    if use_multiprocessing == False:
        for consist in consists:
            render_docs_images(
                consist, static_dir_dst, generated_graphics_path, doc_helper
            )
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the consist?
        # probably potato / potato tbh
        pool = multiprocessing.Pool(processes=num_pool_workers)
        pool.starmap(
            render_docs_images,
            zip(
                consists,
                repeat(static_dir_dst),
                repeat(generated_graphics_path),
                repeat(doc_helper),
            ),
        )
        pool.close()
        pool.join()
    print("render_docs_images", time() - slow_start)

    print(
        "[RENDER DOCS]",
        command_line_args.grf_name,
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
