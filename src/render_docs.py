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
from collections import defaultdict

import iron_horse
import utils
import global_constants
from polar_fox import git_info

metadata = {}
metadata.update(global_constants.metadata)

# get args passed by makefile
command_line_args = utils.get_command_line_args()

docs_src = os.path.join(currentdir, "src", "docs_templates")

palette = utils.dos_palette_to_rgb()

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()


class DocHelper(object):
    # dirty class to help do some doc formatting

    # Some constants

    # these only used in docs as of April 2018
    buy_menu_sprite_max_width = 65  # up to 2 units eh
    buy_menu_sprite_height = 16

    def buy_menu_sprite_width(self, consist):
        if not consist.dual_headed:
            # +1 for the buffers etc
            return min((consist.buy_menu_width + 1), self.buy_menu_sprite_max_width)
        # openttd automatically handles dual head, but we need to calculate double width explicitly for docs
        if consist.dual_headed:
            return min((2 * 4 * consist.length) + 1, self.buy_menu_sprite_max_width)

    def get_vehicles_by_subclass(self, consists, filter_subclasses_by_name=None):
        # first find all the subclasses + their vehicles
        vehicles_by_subclass = {}
        for consist in consists:
            subclass = type(consist)
            if (
                filter_subclasses_by_name == None
                or subclass.__name__ in filter_subclasses_by_name
            ):
                if subclass in vehicles_by_subclass:
                    vehicles_by_subclass[subclass].append(consist)
                else:
                    vehicles_by_subclass[subclass] = [consist]
        # reformat to a list we can then sort so order is consistent
        result = [
            {
                "name": i.__name__,
                "doc": i.__doc__,
                "class_obj": subclass,
                "vehicles": vehicles_by_subclass[i],
            }
            for i in vehicles_by_subclass
        ]
        return sorted(result, key=lambda subclass: subclass["name"])

    def get_engines_by_roster_and_base_track_type(self, roster, base_track_type_name):
        result = []
        for consist in roster.engine_consists:
            if consist.base_track_type_name == base_track_type_name:
                result.append(consist)
        return result

    def get_wagons_by_roster_and_base_track_type(self, roster, base_track_type_name):
        result = []
        for wagon_class in global_constants.buy_menu_sort_order_wagons:
            for consist in roster.wagon_consists[wagon_class]:
                if consist.base_track_type_name == base_track_type_name:
                    result.append(consist)
        return result

    def engines_as_tech_tree(self, roster, consists, simplified_gameplay):
        # structure
        # |- base_track_type_name
        #    |- role_group
        #       |- role
        #          |- role child_branch
        #             |- generation
        #                |- engine consist
        # if there's no engine consist matching a combination of keys in the tree, there will be a None entry for that node in the tree, to ease walking the tree
        result = {}
        # much nested loops
        for base_track_type_and_label in self.base_track_type_names_and_labels:
            for role_group in global_constants.role_group_mapping:
                for role in global_constants.role_group_mapping[role_group]:
                    role_child_branches = {}
                    for role_child_branch in self.get_role_child_branches(
                        consists, base_track_type_and_label[0], role
                    ):
                        if not (simplified_gameplay and role_child_branch < 0):
                            role_child_branches[role_child_branch] = {}
                            # walk the generations, providing default None objects
                            for gen in range(
                                1,
                                len(roster.intro_years[base_track_type_and_label[0]])
                                + 1,
                            ):
                                role_child_branches[role_child_branch][gen] = None
                    # get the engines matching this role and track type, and place them into the child branches
                    for consist in consists:
                        if not (
                            simplified_gameplay and consist.role_child_branch_num < 0
                        ):
                            if (
                                consist.base_track_type_name == base_track_type_and_label[0]
                            ) and (consist.role == role):
                                role_child_branches[consist.role_child_branch_num][
                                    consist.gen
                                ] = consist
                    # only to role group to tree for this track type if there are actual vehicles in it
                    if len(role_child_branches) > 0:
                        result.setdefault(base_track_type_and_label, {})
                        result[base_track_type_and_label].setdefault(role_group, {})
                        result[base_track_type_and_label][role_group].setdefault(
                            role, {}
                        )
                        result[base_track_type_and_label][role_group][
                            role
                        ] = role_child_branches
        return result

    def get_role_child_branches_in_order(self, role_child_branches):
        # adjust the sort so that it's +ve, -ve for each value, e.g. [1, -1, 2, -2, 3, -3, 4, 5] etc
        # this gives the nicest order of related rows in tech tree, assuming that similar engines are in child_branch 1 and child_branch -1
        result = [i for i in role_child_branches]
        result.sort(key=lambda x: (abs(x), -x))
        return result

    def remap_company_colours(self, remap):
        result = {}
        input_colours = {"CC1": 198, "CC2": 80}
        for input_colour, output_colour in remap.items():
            for i in range(0, 8):
                result[
                    input_colours[input_colour] + i
                ] = self.get_palette_index_for_company_colour(output_colour, i)
        return result

    def get_palette_index_for_company_colour(self, company_colour, offset):
        return global_constants.company_colour_maps[company_colour][offset]

    def get_company_colour_as_rgb(self, company_colour, offset=0):
        return palette[
            self.get_palette_index_for_company_colour(company_colour, offset)
        ]

    @property
    def company_colour_names(self):
        return {
            "COLOUR_DARK_BLUE": "Dark Blue",
            "COLOUR_PALE_GREEN": "Pale Green",
            "COLOUR_PINK": "Pink",
            "COLOUR_YELLOW": "Yellow",
            "COLOUR_RED": "Red",
            "COLOUR_LIGHT_BLUE": "Light Blue",
            "COLOUR_GREEN": "Green",
            "COLOUR_DARK_GREEN": "Dark Green",
            "COLOUR_BLUE": "Blue",
            "COLOUR_CREAM": "Cream",
            "COLOUR_MAUVE": "Mauve",
            "COLOUR_PURPLE": "Purple",
            "COLOUR_ORANGE": "Orange",
            "COLOUR_BROWN": "Brown",
            "COLOUR_GREY": "Grey",
            "COLOUR_WHITE": "White",
        }

    def get_docs_livery_variants(self, consist):
        # dark blue / dark blue and red / white are defaults
        variants_config = []

        default_livery_examples = [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ]
        default_livery_examples.extend(
            getattr(consist.gestalt_graphics, "default_livery_extra_docs_examples", [])
        )

        additional_liveries = consist.gestalt_graphics.additional_liveries

        result = {}
        for cc_remap_pair in default_livery_examples:
            livery_name = self.get_livery_file_substr(cc_remap_pair)
            result[livery_name] = {}
            result[livery_name]["cc_remaps"] = {
                "CC1": cc_remap_pair[0],
                "CC2": cc_remap_pair[1],
            }
            result[livery_name]["docs_image_input_cc"] = cc_remap_pair
        variants_config.append(result)

        for additional_livery in additional_liveries:
            result = {}
            for cc_remap_pair in additional_livery["docs_image_input_cc"]:
                livery_name = self.get_livery_file_substr(cc_remap_pair)
                result[livery_name] = {}
                CC1_remap = (
                    additional_livery["remap_to_cc"]
                    if additional_livery["remap_to_cc"] is not None
                    else cc_remap_pair[0]
                )  # handle possible remap of CC1
                CC2_remap = cc_remap_pair[
                    1
                ]  # no forced remap to another cc for second colour, take it as is
                result[livery_name]["cc_remaps"] = {"CC1": CC1_remap, "CC2": CC2_remap}
                result[livery_name]["docs_image_input_cc"] = cc_remap_pair
            variants_config.append(result)
        return variants_config

    def get_livery_file_substr(self, cc_pair):
        result = []
        for colour_name in cc_pair:
            result.append(colour_name.split("COLOUR_")[1])
        return ("_").join(result).lower()

    def get_role_child_branches(self, consists, base_track_type_name, role):
        result = []
        for consist in consists:
            if consist.base_track_type_name == base_track_type_name:
                if consist.role is not None and consist.role == role:
                    result.append(consist.role_child_branch_num)
        return set(result)

    def filter_out_randomised_wagon_consists(self, wagon_consists):
        result = []
        for wagon_consist in wagon_consists:
            # extensible excludes as needed
            if wagon_consist.gestalt_graphics.__class__.__name__ not in [
                "GestaltGraphicsRandomisedWagon",
                "GestaltGraphicsCaboose"
            ]:
                result.append(wagon_consist)
        return result

    def get_vehicle_images_json(self, roster):
        # returns json formatted in various ways for randomising images according to various criteria
        # does not sort by roster as of July 2020
        result = {
            "sorted_by_vehicle_type": defaultdict(list),
            "sorted_by_base_track_type_and_vehicle_type": {},
        }

        for base_track_type_name, base_track_label in self.base_track_type_names_and_labels:
            result["sorted_by_base_track_type_and_vehicle_type"][
                base_track_type_name
            ] = defaultdict(list)

        # for vehicle_type, vehicle_consists in [engines, wagons]:
        # parse the engine and wagon consists into a consistent structure
        engines = ("engines", roster.engine_consists)
        wagon_consists = []
        for wagon_class in global_constants.buy_menu_sort_order_wagons:
            wagon_consists.extend(
                [consist for consist in roster.wagon_consists[wagon_class]]
            )
        wagon_consists = self.filter_out_randomised_wagon_consists(wagon_consists)
        wagons = ("wagons", wagon_consists)

        # this code repeats for both engines and wagons, but with different source lists
        for vehicle_type, vehicle_consists in [engines, wagons]:
            for consist in vehicle_consists:
                vehicle_data = [
                    consist.id,
                    str(self.buy_menu_sprite_width(consist)),
                    consist.base_numeric_id,
                ]
                result["sorted_by_vehicle_type"][vehicle_type].append(vehicle_data)
                result["sorted_by_base_track_type_and_vehicle_type"][
                    consist.base_track_type_name
                ][vehicle_type].append(vehicle_data)

        # guard against providing empty vehicle lists as they would require additional guards in js to prevent js failing
        for base_track_type_name, base_track_label in self.base_track_type_names_and_labels:
            vehicle_consists = result["sorted_by_base_track_type_and_vehicle_type"][
                base_track_type_name
            ]
            for vehicle_type in ["engines", "wagons"]:
                if len(vehicle_consists[vehicle_type]) == 0:
                    del vehicle_consists[vehicle_type]
            if len(vehicle_consists.keys()) == 0:
                del result["sorted_by_base_track_type_and_vehicle_type"][
                    base_track_type_name
                ]

        return json.dumps(result)

    def fetch_prop(self, result, prop_name, value):
        result["vehicle"][prop_name] = value
        result["subclass_props"].append(prop_name)
        return result

    def unpack_name_string(self, consist):
        substrings = consist.name.split("string(")
        # engines have an untranslated name defined via _name, wagons use a translated string
        if consist._name is not None:
            name = consist._name
        else:
            # strip out spaces and some nml boilerplate to get the string name in isolation
            name_substr = substrings[2].translate({ord(c): "" for c in "), "})
            name = base_lang_strings[name_substr]
        # !! this would be better generalised to 'consist.has_suffix', currently docs rendering is knowing too much about the internals of trains
        if (
            getattr(consist, "subtype", None) == "U"
            and getattr(consist, "str_name_suffix", None) != None
        ):
            suffix = base_lang_strings[substrings[3][0:-2]]
            return name + " (" + suffix + ")"
        else:
            return name

    def unpack_role_string_for_consist(self, consist):
        # strip off some nml boilerplate
        role_key = consist.buy_menu_role_string.replace("STR_ROLE, string(", "")
        role_key = role_key.replace(")", "")
        return base_lang_strings[role_key]

    def get_role_string_from_role(self, role):
        # mangle on some boilerplate to get the nml string
        for role_group, roles in global_constants.role_group_mapping.items():
            if role in roles:
                return base_lang_strings[
                    global_constants.role_string_mapping[role_group]
                ]

    def get_replaced_by_name(self, replacement_consist_id, consists):
        for consist in consists:
            if consist.id == replacement_consist_id:
                return self.unpack_name_string(consist)

    def power_formatted_for_docs(self, consist):
        if consist.wagons_add_power:
            return [str(consist.cab_power) + " hp"]
        elif consist.power_by_power_source is not None:
            # crude assumption we can just walk over the keys and they'll be in the correct order (oof!)
            # !! we actually need to control the order somewhere - see vehicle_power_source_tree??
            result = []
            for power_data in consist.vehicle_power_source_tree:
                power_source_name = base_lang_strings["STR_POWER_SOURCE_" + power_data[0]]
                power_value = str(consist.power_by_power_source[power_data[0]]) + " hp"
                result.append(power_source_name + " " + power_value)
            return result
        else:
            return [str(consist.power) + " hp"]

    def speed_formatted_for_docs(self, consist):
        result = [str(consist.speed) + " mph"]
        if consist.lgv_capable:
            result.append(str(consist.speed_on_lgv) + " mph (LGV)")
        return " / ".join(result)

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for vehicle in subclass["vehicles"]:
            result = {"vehicle": {}, "subclass_props": []}
            result = self.fetch_prop(
                result, "Vehicle Name", self.unpack_name_string(vehicle)
            )
            result = self.fetch_prop(result, "Gen", vehicle.gen)
            if vehicle.role is not None:
                result = self.fetch_prop(result, "Role", vehicle.role)
            result = self.fetch_prop(result, "Railtype", vehicle.track_type)
            result = self.fetch_prop(result, "HP", int(vehicle.power))
            result = self.fetch_prop(result, "Speed (mph)", vehicle.speed)
            result = self.fetch_prop(result, "Weight (t)", vehicle.weight)
            result = self.fetch_prop(
                result, "TE coefficient", vehicle.tractive_effort_coefficient
            )
            result = self.fetch_prop(result, "Intro Year", vehicle.intro_year)
            result = self.fetch_prop(result, "Vehicle Life", vehicle.vehicle_life)
            result = self.fetch_prop(result, "Buy Cost", vehicle.buy_cost)
            result = self.fetch_prop(result, "Running Cost", vehicle.running_cost)
            result = self.fetch_prop(
                result, "Loading Speed", [unit.loading_speed for unit in vehicle.units]
            )

            props_to_print[vehicle] = result["vehicle"]
            props_to_print[subclass["name"]] = result["subclass_props"]
        return props_to_print

    def get_base_numeric_id(self, consist):
        return consist.base_numeric_id

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]

    @property
    def base_track_type_names_and_labels(self):
        # list of pairs, need consistent order so can't use dict
        return [("RAIL", "Standard Gauge"), ("NG", "Narrow Gauge"), ("METRO", "Metro")]


def render_docs(
    doc_list,
    file_type,
    docs_output_path,
    iron_horse,
    consists,
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
            base_lang_strings=base_lang_strings,
            metadata=metadata,
            utils=utils,
            doc_helper=DocHelper(),
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
                doc_helper=DocHelper(),
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


def render_docs_vehicle_details(consist, docs_output_path, consists):
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(docs_src, format="text")
    template = docs_templates["vehicle_details.pt"]
    doc_name = consist.id

    roster = iron_horse.roster_manager.active_roster
    doc = template(
        roster=roster,
        consist=consist,
        consists=consists,
        global_constants=global_constants,
        command_line_args=command_line_args,
        git_info=git_info,
        base_lang_strings=base_lang_strings,
        metadata=metadata,
        utils=utils,
        doc_helper=DocHelper(),
        doc_name=doc_name,
    )
    doc_file = codecs.open(
        os.path.join(docs_output_path, doc_name + ".html"), "w", "utf8"
    )
    doc_file.write(doc)
    doc_file.close()


def render_docs_images(consist, static_dir_dst, generated_graphics_path):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs

    doc_helper = DocHelper()

    vehicle_spritesheet = Image.open(
        os.path.join(generated_graphics_path, consist.id + ".png")
    )
    # these 'source' var names for images are misleading
    source_vehicle_image = Image.new(
        "P",
        (doc_helper.buy_menu_sprite_width(consist), doc_helper.buy_menu_sprite_height),
        255,
    )
    source_vehicle_image.putpalette(Image.open("palette_key.png").palette)

    docs_image_variants = []

    for livery_counter, variant in enumerate(
        doc_helper.get_docs_livery_variants(consist)
    ):

        if not consist.dual_headed:
            # relies on additional_liveries being in predictable row offsets (should be true as of July 2020)
            y_offset = (consist.docs_image_spriterow + livery_counter) * 30
            source_vehicle_image_tmp = vehicle_spritesheet.crop(
                box=(
                    consist.buy_menu_x_loc,
                    10 + y_offset,
                    consist.buy_menu_x_loc + doc_helper.buy_menu_sprite_width(consist),
                    10 + y_offset + doc_helper.buy_menu_sprite_height,
                )
            )
        if consist.dual_headed:
            # oof, super special handling of dual-headed vehicles, OpenTTD handles this automatically in the buy menu, but docs have to handle explicitly
            # !! hard-coded values might fail in future, sort that out then if needed, they can be looked up in global constants
            # !! this also won't work with engine additional_liveries currently
            source_vehicle_image_1 = vehicle_spritesheet.copy().crop(
                box=(
                    224,
                    10,
                    224 + (4 * consist.length) + 1,
                    10 + doc_helper.buy_menu_sprite_height,
                )
            )
            source_vehicle_image_2 = vehicle_spritesheet.copy().crop(
                box=(
                    104,
                    10,
                    104 + (4 * consist.length) + 1,
                    10 + doc_helper.buy_menu_sprite_height,
                )
            )
            source_vehicle_image_tmp = source_vehicle_image.copy()
            source_vehicle_image_tmp.paste(
                source_vehicle_image_1,
                (
                    0,
                    0,
                    source_vehicle_image_1.size[0],
                    doc_helper.buy_menu_sprite_height,
                ),
            )
            source_vehicle_image_tmp.paste(
                source_vehicle_image_2,
                (
                    source_vehicle_image_1.size[0] - 1,
                    0,
                    source_vehicle_image_1.size[0] - 1 + source_vehicle_image_2.size[0],
                    doc_helper.buy_menu_sprite_height,
                ),
            )
        crop_box_dest = (
            0,
            0,
            doc_helper.buy_menu_sprite_width(consist),
            doc_helper.buy_menu_sprite_height,
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
                    10 + doc_helper.buy_menu_sprite_height,
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
                        10 + doc_helper.buy_menu_sprite_height,
                    )
                )
                crop_box_dest_pan_2 = (
                    int(doc_helper.buy_menu_sprite_width(consist) / 2),
                    0,
                    int(doc_helper.buy_menu_sprite_width(consist) / 2) + pan_crop_width,
                    doc_helper.buy_menu_sprite_height,
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
            {
                "source_vehicle_image": source_vehicle_image.copy(),
                "livery_metadata": variant,
            }
        )

    for variant in docs_image_variants:
        for colour_name, livery_metadata in variant["livery_metadata"].items():
            cc_remap_indexes = doc_helper.remap_company_colours(
                livery_metadata["cc_remaps"]
            )
            # probably fragile workaround to use the alternative livery spriterow
            # for the edge case that a docs default livery 2nd company colour matches the alternative livery triggers
            if "use_additional_livery_spriterow" in livery_metadata.keys():
                # this makes assumptions about there being a 2nd docs_image_variant with an appropriate spriterow
                processed_vehicle_image = docs_image_variants[1]["source_vehicle_image"]
            else:
                processed_vehicle_image = variant["source_vehicle_image"]
                cc_remap_indexes = doc_helper.remap_company_colours(
                    livery_metadata["cc_remaps"]
                )

            processed_vehicle_image = processed_vehicle_image.copy().point(
                lambda i: cc_remap_indexes[i] if i in cc_remap_indexes.keys() else i
            )

            # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
            processed_vehicle_image = processed_vehicle_image.resize(
                (
                    4 * processed_vehicle_image.size[0],
                    4 * doc_helper.buy_menu_sprite_height,
                ),
                resample=Image.Resampling.NEAREST,
            )
            output_path = os.path.join(
                static_dir_dst,
                "img",
                consist.id + "_" + colour_name + ".png",
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

    static_dir_src = os.path.join(docs_src, "html", "static")
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
    render_docs(html_docs, "html", html_docs_output_path, iron_horse, consists)
    render_docs(txt_docs, "txt", docs_output_path, iron_horse, consists)
    render_docs(
        license_docs,
        "txt",
        docs_output_path,
        iron_horse,
        consists,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, "txt", docs_output_path, iron_horse, consists)
    render_docs(
        markdown_docs,
        "html",
        html_docs_output_path,
        iron_horse,
        consists,
        use_markdown=True,
    )
    print("render_docs", time() - render_docs_start)

    # render vehicle details
    # this is slow and _might_ go faster in an MP pool, but eh overhead...
    render_vehicle_details_start = time()
    for consist in roster.engine_consists:
        consist.assert_description_foamer_facts()
        render_docs_vehicle_details(consist, html_docs_output_path, consists)
    print("render_docs_vehicle_details", time() - render_vehicle_details_start)

    # process images for use in docs
    # yes, I really did bother using a pool to save at best a couple of seconds, because FML :)
    generated_graphics_path = os.path.join(
        iron_horse.generated_files_path, "graphics", roster.grf_name
    )
    slow_start = time()
    if use_multiprocessing == False:
        for consist in consists:
            render_docs_images(consist, static_dir_dst, generated_graphics_path)
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the consist?
        # probably potato / potato tbh
        pool = multiprocessing.Pool(processes=num_pool_workers)
        pool.starmap(
            render_docs_images,
            zip(consists, repeat(static_dir_dst), repeat(generated_graphics_path)),
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
