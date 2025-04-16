# JFDI module to help do some doc formatting

from collections import defaultdict
import json

import global_constants
import utils
from utils import timing


class DocHelper(object):
    # Some constants
    palette = utils.dos_palette_to_rgb()

    # these only used in docs as of April 2018
    docs_sprite_max_width = 65  # up to 2 units eh
    docs_sprite_height = 16

    def __init__(self, lang_strings):
        self.lang_strings = lang_strings

    def docs_sprite_width(self, catalogue=None, model_variant=None):
        # generally use catalogue for this
        # but fetching the example_model_variant from the roster fails in multiprocessing
        # therefore have the option to pass in a model_variant directly for that case
        if model_variant is None:
            model_variant = catalogue.example_model_variant
        if not model_variant.dual_headed:
            # +1 for the buffers etc
            return min((model_variant.buy_menu_width + 1), self.docs_sprite_max_width)
        # openttd automatically handles dual head, but we need to calculate double width explicitly for docs
        if model_variant.dual_headed:
            return min((2 * 4 * model_variant.length) + 1, self.docs_sprite_max_width)

    def get_catalogues_by_model_type_cls(self, catalogues):
        result = defaultdict(lambda: {"model_type_cls": None, "catalogues": []})

        for catalogue in catalogues:
            model_type_cls = catalogue.factory.model_type_cls
            key = model_type_cls.__name__
            if result[key]["model_type_cls"] is None:
                result[key]["model_type_cls"] = model_type_cls
            result[key]["catalogues"].append(catalogue)

        # Return a list of dicts sorted by the model type class name
        return sorted(result.values(), key=lambda x: x["model_type_cls"].__name__)

    def get_engine_catalogues_by_roster_and_base_track_type(
        self, roster, base_track_type
    ):
        result = []
        for catalogue in roster.engine_catalogues:
            if (
                not catalogue.base_track_type
                == base_track_type
            ):
                continue
            if catalogue.clone_quacker.quack:
                # exclude cloned models or things that act like clones
                continue
            result.append(catalogue)
        return result

    def get_wagon_catalogues_by_roster_and_base_track_type(
        self, roster, base_track_type
    ):
        result = []
        for catalogue in roster.wagon_catalogues:
            if (
                not catalogue.base_track_type
                == base_track_type
            ):
                continue
            if catalogue.clone_quacker.quack:
                # exclude cloned models or things that act like clones
                continue
            result.append(catalogue)
        return result

    def engines_as_tech_tree(self, roster, simplified_gameplay):
        if not simplified_gameplay:
            return roster.engine_model_tech_tree
        if simplified_gameplay:
            return roster.engine_model_tech_tree.simplified_tree

    def engine_model_counts(self, roster):
        # some engines aren't really engines
        # - snowploughs
        # - cab cars
        # - metro trains
        # - powered wagons for TGVs
        # - powered cabooses for propelling
        # - anything with a variant group parent is just a sub-variant of some sort
        really_engines = []
        not_really_engines = []
        for catalogue in roster.engine_catalogues:
            if catalogue.clone_quacker.quack:
                continue
            # this is JFDI reuse of existing attributes, if this gets flakey add a dedicated attribute for exclusion
            if (
                catalogue.example_model_variant.is_distributed_power_wagon
                or (
                    catalogue.example_model_variant.role
                    in ["driving_cab", "gronk", "lolz", "metro"]
                )
                or (catalogue.example_model_variant.subrole_child_branch_num > 999)
                or (catalogue.example_model_variant.subrole_child_branch_num < -999)
            ):
                not_really_engines.append(catalogue)
            else:
                really_engines.append(catalogue)
        # print("really_engines", [catalogue.model_id for catalogue in really_engines])
        # print("not_really_engines", [catalogue.model_id for catalogue in not_really_engines])
        really_engines_count = len(really_engines)
        not_really_engines_count = len(not_really_engines)
        total_count = really_engines_count + not_really_engines_count
        return {
            "total_count": total_count,
            "really_engines_count": really_engines_count,
            "not_really_engines_count": not_really_engines_count,
        }

    def wagon_model_counts(self, roster):
        # some wagons aren't really wagons
        # - randomised wagons, which just compose a set of choices from other wagons
        really_wagons = []
        not_really_wagons = []
        for catalogue in roster.wagon_catalogues:
            if catalogue.wagon_quacker.is_randomised_wagon_type:
                not_really_wagons.append(catalogue)
            else:
                really_wagons.append(catalogue)
        really_wagons_count = len(really_wagons)
        not_really_wagons_count = len(not_really_wagons)
        total_count = really_wagons_count + not_really_wagons_count
        return {
            "total_count": total_count,
            "really_wagons_count": really_wagons_count,
            "not_really_wagons_count": not_really_wagons_count,
        }

    def get_subrole_child_branches_in_order(self, subrole_child_branches):
        # adjust the sort so that it's +ve, -ve for each value, e.g. [1, -1, 2, -2, 3, -3, 4, 5] etc
        # this gives the nicest order of related rows in tech tree, assuming that similar engines are in child_branch 1 and child_branch -1
        result = [i for i in subrole_child_branches]
        result.sort(key=lambda x: (abs(x), -x))
        return result

    def remap_company_colours(self, remap):
        result = {}
        input_colours = {"CC1": 198, "CC2": 80}
        for input_colour, output_colour in remap.items():
            for i in range(0, 8):
                result[input_colours[input_colour] + i] = (
                    self.get_palette_index_for_company_colour(output_colour, i)
                )
        return result

    def get_palette_index_for_company_colour(self, company_colour, offset):
        return global_constants.company_colour_maps[company_colour][offset]

    def get_company_colour_as_rgb(self, company_colour, offset=0):
        return self.palette[
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

    def get_livery_file_substr(self, cc_pair):
        result = []
        for colour_name in cc_pair:
            result.append(colour_name.split("COLOUR_")[1])
        return ("_").join(result).lower()

    def get_subrole_child_branches(self, model_variants, base_track_type, role):
        result = []
        for model_variant in model_variants:
            if model_variant.base_track_type == base_track_type:
                if model_variant.subrole is not None and model_variant.subrole == role:
                    result.append(model_variant.subrole_child_branch_num)
        return set(result)

    def get_vehicle_images_json(self, roster):
        # does not sort by roster as of July 2020
        result = {
            "sorted_by_vehicle_type": defaultdict(list),
            "sorted_by_base_track_type_and_vehicle_type": {},
        }

        for base_track_type in self.base_track_types_with_display_names:
            result["sorted_by_base_track_type_and_vehicle_type"][
                base_track_type
            ] = defaultdict(list)

        # parse the engine and wagon model variants into a consistent structure
        engines = ("engines", roster.engine_catalogues)
        wagon_catalogues = []
        for catalogue in roster.wagon_catalogues:
            # extensible excludes as needed
            if catalogue.wagon_quacker.is_randomised_wagon_type:
                continue
            if catalogue.wagon_quacker.is_caboose:
                continue
            wagon_catalogues.append(catalogue)
        wagons = ("wagons", wagon_catalogues)

        # this code repeats for both engines and wagons, but with different source lists
        for vehicle_type, catalogues in [engines, wagons]:
            for catalogue in catalogues:
                vehicle_data = [
                    catalogue.model_id,
                    catalogue.default_entry.model_variant_id,
                    str(self.docs_sprite_width(catalogue)),
                    catalogue.model_def.base_numeric_id,
                ]
                result["sorted_by_vehicle_type"][vehicle_type].append(vehicle_data)
                result["sorted_by_base_track_type_and_vehicle_type"][
                    catalogue.base_track_type
                ][vehicle_type].append(vehicle_data)

        # guard against providing empty vehicle lists as they would require additional guards in js to prevent js failing
        for base_track_type in self.base_track_types_with_display_names:
            vehicles = result["sorted_by_base_track_type_and_vehicle_type"][
                base_track_type
            ]
            for vehicle_type in ["engines", "wagons"]:
                if len(vehicles[vehicle_type]) == 0:
                    del vehicles[vehicle_type]
            if len(vehicles.keys()) == 0:
                del result["sorted_by_base_track_type_and_vehicle_type"][
                    base_track_type
                ]

        return json.dumps(result)

    def unpack_name_string(self, catalogue):
        example_model_variant = catalogue.example_model_variant
        # engines have an untranslated name defined via name, wagons use a translated string
        if example_model_variant.name is not None:
            return example_model_variant.name
        else:
            name_parts = example_model_variant.get_name_parts(context="docs")
            result = []
            for name_part in name_parts:
                if name_part is not None:
                    # this will fail if name parts are found that don't correspond to string IDs (for example putting variables on the text stack)
                    result.append(self.lang_strings[name_part])

            if (
                catalogue.wagon_quacker.is_randomised_wagon_type
                or catalogue.wagon_quacker.is_caboose
            ):
                result.append("- Random")
            return " ".join(result)

    def clean_role_string(self, role_string):
        # remove any additional hint text (assumes a fixed format of 'role{BLACK} - optional hint text'
        return role_string.split("{BLACK}")[0]

    def get_role_string_from_catalogue(self, catalogue, badge_manager):
        role_string_name = badge_manager.get_badge_by_label(
            catalogue.example_model_variant.role_badge
        ).name
        return self.clean_role_string(self.lang_strings[role_string_name])

    def get_role_string_from_subrole(self, subrole, badge_manager):
        # used in docs for headers, no model variant available
        for role, subroles in global_constants.role_subrole_mapping.items():
            if subrole in subroles:
                role_string_name = badge_manager.get_badge_by_label("role/" + role).name
                return self.clean_role_string(self.lang_strings[role_string_name])

    def model_has_direct_replacement_in_tree(self, model_variant):
        replacement_model_variant = model_variant.catalogue.next_gen_catalogue.example_model_variant
        if replacement_model_variant.subrole != model_variant.subrole:
            return False
        elif (
            replacement_model_variant.subrole_child_branch_num
            != model_variant.subrole_child_branch_num
        ):
            return False
        elif replacement_model_variant.gen != model_variant.gen + 1:
            return False
        else:
            return True

    def power_formatted_for_docs(self, catalogue):
        example_model_variant = catalogue.example_model_variant
        if example_model_variant.is_distributed_power_wagon:
            return [str(catalogue.cab_engine_model.power) + " hp"]
        elif example_model_variant.power_by_power_source is not None:
            # crude assumption we can just walk over the keys and they'll be in the correct order (oof!)
            # !! we actually need to control the order somewhere - see vehicle_power_source_tree??
            # !! could be global_constants.power_source
            result = []
            for power_data in example_model_variant.vehicle_power_source_tree:
                power_source_name = self.lang_strings[
                    "STR_POWER_SOURCE_" + power_data[0]
                ]
                power_value = (
                    str(example_model_variant.power_by_power_source[power_data[0]])
                    + " hp"
                )
                result.append(power_source_name + " " + power_value)
            return result
        else:
            return [str(example_model_variant.power) + " hp"]

    def speed_formatted_for_docs(self, catalogue):
        example_model_variant = catalogue.example_model_variant
        if example_model_variant.speed == None:
            # unlimited speed
            return "No limit"
        result = [str(example_model_variant.speed) + " mph"]
        if example_model_variant.lgv_capable:
            result.append(str(example_model_variant.speed_on_lgv) + " mph (LGV)")
        return " / ".join(result)

    def capacity_formatted_for_docs(self, catalogue):
        capacity = sum(
            [
                unit.default_cargo_capacity
                for unit in catalogue.example_model_variant.units
            ]
        )
        # CABBAGE - we could attempt to find better units from the model type subclass?  At least for pax and mail?
        # default to t for tonnes, although this doesn't work for liquids, passengers etc
        return f"{capacity} t"

    def fetch_prop(self, result, prop_name, value):
        result[prop_name].append(value)

    def get_props_to_print_in_code_reference(self, catalogues):
        result = defaultdict(list)
        for catalogue in catalogues:
            # we print _mostly_ from example_model_variant here, not catalogue or model_def, to see what actually gets determined
            example_model_variant = catalogue.example_model_variant
            self.fetch_prop(result, "Vehicle Name", self.unpack_name_string(catalogue))
            self.fetch_prop(result, "Gen", example_model_variant.gen)
            self.fetch_prop(result, "Railtype", example_model_variant.track_type)
            self.fetch_prop(result, "HP", int(example_model_variant.power))
            self.fetch_prop(result, "Speed (mph)", example_model_variant.speed)
            self.fetch_prop(result, "Weight (t)", example_model_variant.weight)
            self.fetch_prop(
                result,
                "TE coefficient",
                example_model_variant.tractive_effort_coefficient,
            )
            self.fetch_prop(result, "Intro Year", catalogue.intro_year)
            self.fetch_prop(result, "Vehicle Life", example_model_variant.vehicle_life)
            self.fetch_prop(result, "Buy Cost", example_model_variant.buy_cost)
            self.fetch_prop(result, "Running Cost", example_model_variant.running_cost)
            self.fetch_prop(
                result,
                "Loading Speed",
                ", ".join(
                    [str(unit.loading_speed) for unit in example_model_variant.units]
                ),
            )
        return result

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]

    @property
    def base_track_types_with_display_names(self):
        # could fetch from lang strings, but eh, JFDI, it's docs
        return {"RAIL": "Standard Gauge", "NG": "Narrow Gauge", "METRO": "Metro"}

    def get_og_tags_content(self, doc_name, optional_model_variant):
        description = "CABBAGE"

        # base_url has to be predicted at compile time, assuming grf.farm or whatever is returned by utils.docs_base_url
        # as of July 2024, utils.docs_base_url relies on detecting git tags, read that to understand what it's doing
        base_url = utils.docs_base_url

        # generic or vehicle-specific image
        if optional_model_variant is not None:
            image_filename = optional_model_variant.id + "_red_white.png"
        else:
            image_filename = "og_tags_default.png"

        return {
            "description": description,
            "base_url": base_url,
            "image_filename": image_filename,
        }
