# JFDI module to help do some doc formatting

from collections import defaultdict
import json

import global_constants
import utils


class DocHelper(object):
    # Some constants
    palette = utils.dos_palette_to_rgb()

    # these only used in docs as of April 2018
    docs_sprite_max_width = 65  # up to 2 units eh
    docs_sprite_height = 16

    def __init__(self, lang_strings):
        self.lang_strings = lang_strings

    def docs_sprite_width(self, consist):
        if not consist.dual_headed:
            # +1 for the buffers etc
            return min((consist.buy_menu_width + 1), self.docs_sprite_max_width)
        # openttd automatically handles dual head, but we need to calculate double width explicitly for docs
        if consist.dual_headed:
            return min((2 * 4 * consist.length) + 1, self.docs_sprite_max_width)

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
        for consist in roster.engine_consists_excluding_clones:
            if consist.base_track_type_name == base_track_type_name:
                result.append(consist)
        return result

    def get_wagons_by_roster_and_base_track_type(self, roster, base_track_type_name):
        result = []
        for consist in roster.wagon_consists:
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
                        # special case to drop anything that shouldn't be in tech tree (e.g. TGV middle cars)
                        # this relies on forcing child branch IDs up into 1000+ values (which is probably fine?)
                        if (role_child_branch > 999) or (role_child_branch < -999):
                            continue
                        # allowed cases
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
                        if simplified_gameplay and consist.role_child_branch_num < 0:
                            continue
                        if (consist.role_child_branch_num > 999) or (
                            consist.role_child_branch_num < -999
                        ):
                            continue
                        if (
                            consist.base_track_type_name == base_track_type_and_label[0]
                        ) and (consist.role == role):
                            role_child_branches[consist.role_child_branch_num][
                                consist.gen
                            ] = consist
                    # only add role group to tree for this track type if there are actual vehicles in it
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

    def not_really_engine_consists(self, roster):
        # some engines aren't really engines
        # - snowploughs
        # - cab cars
        # - metro trains
        # - powered wagons for TGVs
        # - powered cabooses for propelling
        # - anything with a variant group parent is just a sub-variant of some sort
        result = []
        for consist in roster.engine_consists_excluding_clones:
            # this is JFDI reuse of existing attributes, if this gets flakey add a dedicated attribute for exclusion
            if (
                consist.buy_menu_additional_text_hint_driving_cab
                or consist.wagons_add_power
                or consist.role in ["pax_metro", "mail_metro", "metro", "gronk!"]
                or consist._buyable_variant_group_id is not None
            ):
                result.append(consist)
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

    def get_docs_livery_variants(self, consist):
        # dark blue / dark blue and red / white are defaults
        variants_config = []

        for buyable_variant in consist.buyable_variants:
            livery = consist.gestalt_graphics.all_liveries[
                buyable_variant.buyable_variant_num
            ]
            # docs_image_input_cc is mandatory for each livery, fail if it's not present
            if "docs_image_input_cc" not in livery.keys():
                raise BaseException(consist + livery)
            docs_image_input_cc = livery["docs_image_input_cc"].copy()
            # as of Dec 2022 only the default livery has per-vehicle extendable colour combos
            # all other liveries have the examples baked into the livery
            if buyable_variant.buyable_variant_num == 0:
                docs_image_input_cc.extend(
                    getattr(
                        consist.gestalt_graphics,
                        "default_livery_extra_docs_examples",
                        [],
                    )
                )
            for cc_remap_pair in docs_image_input_cc:
                result = {}
                livery_name = (
                    "variant_"
                    + str(buyable_variant.buyable_variant_num)
                    + "_"
                    + self.get_livery_file_substr(cc_remap_pair)
                )
                result["livery_name"] = livery_name
                # handle possible remap of CC1
                if livery.get("remap_to_cc", None) is not None:
                    CC1_remap = livery["remap_to_cc"]["company_colour1"]
                    CC2_remap = livery["remap_to_cc"]["company_colour2"]
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
                result["cc_remaps"] = {"CC1": CC1_remap, "CC2": CC2_remap}
                result["docs_image_input_cc"] = cc_remap_pair
                result["buyable_variant"] = buyable_variant
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
                "GestaltGraphicsCaboose",
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

        for (
            base_track_type_name,
            base_track_label,
        ) in self.base_track_type_names_and_labels:
            result["sorted_by_base_track_type_and_vehicle_type"][
                base_track_type_name
            ] = defaultdict(list)

        # for vehicle_type, vehicle_consists in [engines, wagons]:
        # parse the engine and wagon consists into a consistent structure
        engines = ("engines", roster.engine_consists_excluding_clones)
        wagon_consists = self.filter_out_randomised_wagon_consists(
            roster.wagon_consists
        )
        wagons = ("wagons", wagon_consists)

        # this code repeats for both engines and wagons, but with different source lists
        for vehicle_type, vehicle_consists in [engines, wagons]:
            for consist in vehicle_consists:
                vehicle_data = [
                    consist.id,
                    str(self.docs_sprite_width(consist)),
                    consist.base_numeric_id,
                ]
                result["sorted_by_vehicle_type"][vehicle_type].append(vehicle_data)
                result["sorted_by_base_track_type_and_vehicle_type"][
                    consist.base_track_type_name
                ][vehicle_type].append(vehicle_data)

        # guard against providing empty vehicle lists as they would require additional guards in js to prevent js failing
        for (
            base_track_type_name,
            base_track_label,
        ) in self.base_track_type_names_and_labels:
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
        # engines have an untranslated name defined via _name, wagons use a translated string
        if consist._name is not None:
            return consist._name
        else:
            name_parts = consist.get_name_parts(context="docs", unit_variant=None)
            result = []
            for name_part in name_parts:
                if name_part is not None:
                    # this will fail if name parts are found that don't correspond to string IDs (for example putting variables on the text stack)
                    result.append(self.lang_strings[name_part])
            return " ".join(result)

    def unpack_role_string_for_consist(self, consist):
        # strip off some nml boilerplate
        role_key = consist.buy_menu_additional_text_role_string.replace(
            "STR_ROLE, string(", ""
        )
        role_key = role_key.replace(")", "")
        return self.lang_strings[role_key]

    def get_role_string_from_role(self, role):
        # mangle on some boilerplate to get the nml string
        for role_group, roles in global_constants.role_group_mapping.items():
            if role in roles:
                return self.lang_strings[
                    global_constants.role_string_mapping[role_group]
                ]

    def get_replaced_by_name(self, replacement_consist_id, consists):
        for consist in consists:
            if consist.id == replacement_consist_id:
                return self.unpack_name_string(consist)

    def consist_has_direct_replacment(self, consist):
        if consist.replacement_consist.role != consist.role:
            return False
        elif (
            consist.replacement_consist.role_child_branch_num
            != consist.role_child_branch_num
        ):
            return False
        elif consist.replacement_consist.gen != consist.gen + 1:
            return False
        else:
            return True

    def power_formatted_for_docs(self, consist):
        if consist.wagons_add_power:
            return [str(consist.cab_power) + " hp"]
        elif consist.power_by_power_source is not None:
            # crude assumption we can just walk over the keys and they'll be in the correct order (oof!)
            # !! we actually need to control the order somewhere - see vehicle_power_source_tree??
            result = []
            for power_data in consist.vehicle_power_source_tree:
                power_source_name = self.lang_strings[
                    "STR_POWER_SOURCE_" + power_data[0]
                ]
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
