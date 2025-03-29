import copy
import importlib
import os
import pickle
import tomllib
from collections import defaultdict

currentdir = os.curdir

import global_constants
import utils

# get args passed by makefile
command_line_args = utils.get_command_line_args()

from train.factory import ModelVariantFactory


class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    In Iron Horse each roster is compiled to a standalone grf.
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.numeric_id = kwargs.get("numeric_id")
        self.grf_name = kwargs.get("grf_name")
        self.grfid = kwargs.get("grfid")
        self.str_grf_name = kwargs.get("str_grf_name")
        # engine_module_names only used once at __init__ time, it's a list of module names, not the actual model variants
        self.engine_module_names = kwargs.get("engine_module_names")
        self.wagon_module_names_with_roster_ids = kwargs.get(
            "wagon_module_names_with_roster_ids"
        )
        self.engine_model_variants_by_catalogue = defaultdict(list)
        self.wagon_model_variants_by_catalogue = defaultdict(list)
        # create a structure to hold (buyable) variant groups
        # deliberately instantiated as none - cannot be populated as a structure until later, after all model variants are inited
        self.buyable_variant_groups = None
        self.buyable_variant_group_base_ids = kwargs.get(
            "buyable_variant_group_base_ids", {}
        )
        self.intro_years = kwargs.get("intro_years")
        self.speeds = kwargs.get("speeds")
        self.freight_car_capacity_per_unit_length = kwargs.get(
            "freight_car_capacity_per_unit_length"
        )
        self.pax_car_capacity_per_unit_length = kwargs.get(
            "pax_car_capacity_per_unit_length"
        )
        self.pax_car_capacity_types = kwargs.get("pax_car_capacity_types")
        self.train_car_weight_factors = kwargs.get("train_car_weight_factors")
        self.engine_and_pax_mail_car_liveries = kwargs.get(
            "engine_and_pax_mail_car_liveries", []
        )
        self.pax_mail_livery_groups = kwargs.get("pax_mail_livery_groups", {})
        self.wagon_recolour_colour_sets = []

    @property
    def model_variants_by_catalogue(self):
        # With unique keys across engine and wagon dictionaries,
        # simply merge them using dictionary unpacking.
        return {
            **self.engine_model_variants_by_catalogue,
            **self.wagon_model_variants_by_catalogue,
        }

    @property
    def engine_catalogues(self):
        return [
            catalogue_entry["catalogue"]
            for catalogue_entry in self.engine_model_variants_by_catalogue.values()
        ]

    @property
    def wagon_catalogues(self):
        return [
            catalogue_entry["catalogue"]
            for catalogue_entry in self.wagon_model_variants_by_catalogue.values()
        ]

    @property
    def catalogues(self):
        # Gather catalogue instances from both engines and wagons
        return self.engine_catalogues + self.wagon_catalogues

    @property
    def engine_model_variants(self):
        # Flatten the list of engine model variants from the nested dict
        return [
            model_variant
            for catalogue_entry in self.engine_model_variants_by_catalogue.values()
            for model_variant in catalogue_entry["model_variants"]
        ]

    @property
    def wagon_model_variants(self):
        # Flatten the list of wagon model variants from the nested dict
        return [
            model_variant
            for catalogue_entry in self.wagon_model_variants_by_catalogue.values()
            for model_variant in catalogue_entry["model_variants"]
        ]

    @property
    def wagon_model_variants_by_base_id(self):
        result = {}
        for wagon_model_variant in self.wagon_model_variants:
            result.setdefault(wagon_model_variant.model_id_root, [])
            result[wagon_model_variant.model_id_root].append(wagon_model_variant)
        return result

    @property
    def model_variants_in_buy_menu_order(self):
        result = []
        result.extend(self.engine_model_variants)
        for base_track_type_name in ["RAIL", "NG", "METRO"]:
            # CABBAGE refactor to model_id not base_id
            for base_id in self.wagon_model_variants_by_base_id.keys():
                wagon_model_variants = [
                    wagon_model_variant
                    for wagon_model_variant in self.wagon_model_variants_by_base_id[
                        base_id
                    ]
                    if wagon_model_variant.base_track_type_name == base_track_type_name
                ]
                result.extend(
                    # note that we want the sort order to be U, A, B, C, D so special handling
                    # this *doesn*'t handle the case of changing _multiple_ times between U and A / B / C / D between generations
                    sorted(
                        wagon_model_variants,
                        key=lambda wagon_model_variant: {
                            "U": 1,
                            "A": 2,
                            "B": 3,
                            "C": 4,
                            "D": 5,
                        }[wagon_model_variant.subtype],
                    )
                )
        for model_variant in result:
            # if model_variant won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(model_variant)
            except:
                print("Pickling failed for model_variant:", model_variant.id)
                raise
        return result

    @property
    def model_variants_in_order_optimised_for_action_2_ids(self):
        # the base sort order for model variants is for the buy menu, but this isn't effective for order in nml output
        # because randomised wagons need action 2 IDs spanning multiple other vehicles, and this can cause problems allocating enough action 2 IDs
        # therefore we re-order, to group (as far as we can) vehicles where IDs need to span
        # this isn't infallible, but reduces the extent to which the randomised wagons consume action 2 IDs
        model_variants = self.model_variants_in_buy_menu_order
        result = []
        randomised_wagons_by_track_gen_length_power = {}

        # Categorize model variants by generation, length, track type, and power
        for model_variant in model_variants:
            gen = model_variant.gen
            track_type = model_variant.base_track_type_name
            power = model_variant.power
            length = model_variant.length

            key = (track_type, gen, length, power)

            if key not in randomised_wagons_by_track_gen_length_power:
                randomised_wagons_by_track_gen_length_power[key] = {
                    "candidates": [],
                    "randomised": [],
                }

            if model_variant.is_randomised_wagon_type:
                randomised_wagons_by_track_gen_length_power[key]["randomised"].append(
                    model_variant
                )
            else:
                randomised_wagons_by_track_gen_length_power[key]["candidates"].append(
                    model_variant
                )

        # Process each group based on the combined key
        for key in sorted(randomised_wagons_by_track_gen_length_power.keys()):
            candidates = randomised_wagons_by_track_gen_length_power[key]["candidates"]
            randomised_wagons = randomised_wagons_by_track_gen_length_power[key][
                "randomised"
            ]

            # Append candidates first
            result.extend(candidates)

            # Append randomised wagons after their candidates
            result.extend(randomised_wagons)

        return result

    @property
    def default_livery(self):
        # the default livery if no livery is explicitly specified by name
        return {
            "remap_to_cc": None,
            "docs_image_input_cc": [
                ("COLOUR_BLUE", "COLOUR_BLUE"),
                ("COLOUR_RED", "COLOUR_WHITE"),
            ],
        }

    def get_pax_mail_liveries(self, default_livery_group_name, model_def):
        result = []
        # we can optionally specify liveries per model_variant via the model_def, otherwise use the default for the model type subclass
        if model_def.livery_group_name is not None:
            livery_group_name = model_def.livery_group_name
        else:
            livery_group_name = default_livery_group_name
        # will fail if the livery group is not defined in the roster
        # CABBAGE SHIM
        for livery in self.pax_mail_livery_groups[livery_group_name]:
            livery_result = self.engine_and_pax_mail_car_liveries[livery[0]].copy()
            livery_result["relative_spriterow_num"] = livery[1]
            result.append(livery_result)
        return result

    def intro_year_ranges(self, base_track_type_name):
        # return a list of year pairs (first year, last year) for generations
        result = []
        end_date = global_constants.max_game_date
        for intro_year in reversed(self.intro_years[base_track_type_name]):
            result.append((intro_year, end_date))
            end_date = intro_year - 1
        result.reverse()
        return result

    def validate_vehicles(self, numeric_id_defender):
        # CABBAGE 7722 validate_vehicles is slow?  seems to add 1s or so and is called multiple times for different entry points
        # has to be explicitly called after all model variants and units are registered to the roster

        # this structure is used to test for duplicate ids
        model_variant_ids = [
            model_variant.id for model_variant in self.model_variants_in_buy_menu_order
        ]

        for model_variant in self.model_variants_in_buy_menu_order:
            if model_variant_ids.count(model_variant.id) > 1:
                raise BaseException(
                    f"Error: vehicle id '{model_variant.id}' is defined more than once - to fix, search src for the duplicate.\n"
                    f"The catalogue for one of them is:"
                    f"{model_variant.catalogue_entry.catalogue}"
                )
            if len(model_variant.units) == 0:
                raise BaseException(f"Error: {model_variant.id} has no units defined")
            elif len(model_variant.units) == 1:
                if model_variant.base_numeric_id <= global_constants.max_articulated_id:
                    raise BaseException(
                        f"Error: {model_variant.id} with base_numeric_id {model_variant.base_numeric_id} needs a base_numeric_id larger than 16383 "
                        f"as the range below 16383 is reserved for articulated vehicles.\n"
                        f"{model_variant.units}"
                    )
            elif len(model_variant.units) > 1:
                for numeric_id in model_variant.unique_numeric_ids:
                    if numeric_id > global_constants.max_articulated_id:
                        raise BaseException(
                            f"Error: {model_variant.id} has a unit variant with numeric_id {numeric_id} which is part of an articulated vehicle "
                            f"and needs a numeric_id smaller than {global_constants.max_articulated_id}.\n"
                            f"Use a lower base_numeric_id in the model_def.\n"
                            f"{model_variant.units}"
                        )
            for numeric_id in model_variant.unique_numeric_ids:
                if numeric_id in numeric_id_defender:
                    colliding_model_variant = numeric_id_defender[numeric_id]
                    # there is a specific case of reused vehicles that are allowed to overlap IDs (they will be grf-independent, and the compile doesn't actually care)
                    # if base_id matches both model variants have been instantiated from the same source module...
                    if hasattr(model_variant, "model_id_root"):
                        if (
                            getattr(colliding_model_variant, "model_id_root", None)
                            == model_variant.model_id_root
                        ):
                            # it's fine if both model variants are then in different rosters, as they will not conflict
                            if (
                                colliding_model_variant.roster.id
                                != model_variant.roster.id
                            ):
                                continue
                    raise ValueError(
                        f"Error: model variant {model_variant.id} has a unit variant with a numeric_id that collides "
                        f"({numeric_id}) with a numeric_id of a unit variant in model variant {colliding_model_variant.id}\n"
                        f"{[unit for unit in model_variant.units]}\n"
                        f"{model_variant.catalogue_entry.catalogue}\n"
                    )
                else:
                    numeric_id_defender[numeric_id] = model_variant
        # no return value needed

    def produce_engines(self):
        self.engine_model_variants_by_catalogue = {}
        package_name = "vehicles." + self.id
        roster_id_providing_module = self.id
        for engine_module_name in self.engine_module_names:
            engine_module = importlib.import_module(
                "." + engine_module_name, package_name
            )
            for model_def in engine_module.main():
                factory = ModelVariantFactory(
                    model_def, self.id, roster_id_providing_module
                )
                catalogue = factory.catalogue
                # Use the convenience property `id` on Catalogue
                catalogue_id = catalogue.id
                if catalogue_id not in self.engine_model_variants_by_catalogue:
                    self.engine_model_variants_by_catalogue[catalogue_id] = {
                        "catalogue": catalogue,
                        "model_variants": [],
                    }
                for catalogue_entry in catalogue:
                    model_variant = factory.produce(catalogue_entry=catalogue_entry)
                    self.engine_model_variants_by_catalogue[catalogue_id][
                        "model_variants"
                    ].append(model_variant)

    def produce_wagons(self):
        # Iterate over wagon module name stems and warn if not in global_constants
        for wagon_module_name_stem in self.wagon_module_names_with_roster_ids.keys():
            if wagon_module_name_stem not in global_constants.wagon_module_name_stems:
                utils.echo_message(
                    f"Warning: ({self.id}) {wagon_module_name_stem} not found in global_constants.wagon_module_name_stems"
                )

        self.wagon_model_variants_by_catalogue = (
            {}
        )  # Reset or initialize the grouping dict

        # temp book-keeping of randomised_wagons
        randomised_wagons_tmp = {}

        for wagon_module_name_stem in global_constants.wagon_module_name_stems:
            # CABBAGE NERFED OFF TO ENSURE IT COMPILES
            if '_randomised' in wagon_module_name_stem:
                continue
            if wagon_module_name_stem in self.wagon_module_names_with_roster_ids:
                roster_id_providing_module = self.wagon_module_names_with_roster_ids[
                    wagon_module_name_stem
                ]
                wagon_module_name = (
                    f"{wagon_module_name_stem}_{roster_id_providing_module}"
                )
                package_name = "vehicles." + roster_id_providing_module

                try:
                    wagon_module = importlib.import_module(
                        "." + wagon_module_name, package_name
                    )
                    for model_def in wagon_module.main():
                        factory = ModelVariantFactory(
                            model_def, self.id, roster_id_providing_module
                        )
                        catalogue = factory.catalogue
                        catalogue_id = (
                            catalogue.id
                        )  # Using the convenience property 'id'
                        if catalogue_id not in self.wagon_model_variants_by_catalogue:
                            self.wagon_model_variants_by_catalogue[catalogue_id] = {
                                "catalogue": catalogue,
                                "model_variants": [],
                            }
                        for catalogue_entry in catalogue:
                            model_variant = factory.produce(
                                catalogue_entry=catalogue_entry
                            )
                            self.wagon_model_variants_by_catalogue[catalogue_id][
                                "model_variants"
                            ].append(model_variant)
                            if model_variant.is_randomised_wagon_type:
                                randomised_wagons_tmp[
                                    self.get_tmp_unique_key_for_random_wagon_type_model_variant(
                                        model_variant.model_id_root, model_variant
                                    )
                                ] = model_variant
                except ModuleNotFoundError:
                    raise ModuleNotFoundError(
                        f"{wagon_module_name} in {package_name} as defined by {self.id}.wagon_module_names_with_roster_ids"
                    )
                except Exception:
                    raise

        # we have to provision wagon randomisation candidates after initialising all wagon model variants
        for model_variant in self.wagon_model_variants:
            for model_id_root in model_variant.randomised_candidate_groups:
                unique_key = (
                    self.get_tmp_unique_key_for_random_wagon_type_model_variant(
                        model_id_root, model_variant
                    )
                )
                # it's ok that there might be no randomised wagons for a specific generation, track type etc
                if unique_key in randomised_wagons_tmp:
                    dest_model_variant = randomised_wagons_tmp[unique_key]
                    dest_model_variant.wagon_randomisation_candidates.append(
                        model_variant
                    )
        for model_variant in randomised_wagons_tmp.values():
            print(model_variant.__class__.__name__, model_variant.wagon_randomisation_candidates)
            if len(model_variant.wagon_randomisation_candidates) == 0:
                raise BaseException(
                    f"{model_variant.id}"
                    f" did not match any randomisation_candidates, possibly there are no matching wagons for base_id/length/gen"
                )
            if len(model_variant.wagon_randomisation_candidates) == 1:
                print(model_variant.wagon_randomisation_candidates)
                raise BaseException(
                    f"{model_variant.id}"
                    f" colour set "
                    f"{model_variant.catalogue_entry.livery_def.colour_set}"
                    f" has only one choice for randomisation_candidates, this is pointless nonsense, consider removing "
                    f"{model_variant.id}"
                    f" or check that randomisation candidates provide this colour set"
                )
            if len(model_variant.wagon_randomisation_candidates) > 64:
                # CABBAGE TEMP
                model_variant.wagon_randomisation_candidates = model_variant.wagon_randomisation_candidates[0:8]
                continue
                # we have a limited number of random bits, and we need to use them independently of company colour choices
                # so guard against consuming too many, 64 variants is 6 bits, and that's all we want to consume
                raise BaseException(
                    f"{model_variant.id}"
                    f" has more than 64 entries in randomised_candidate_groups, and will run out of random bits; reduce the number of candidates\n"
                    f"{model_variant.wagon_randomisation_candidates}"
                )

    def get_tmp_unique_key_for_random_wagon_type_model_variant(
        self, model_id_root, model_variant
    ):
        # convenience method for a key, only used for accessing a temp structure
        return f"{model_id_root}_{model_variant.gen}_{model_variant.base_track_type_name}_{model_variant.subtype}_{model_variant.catalogue_entry.livery_def.livery_name}"

    def compute_wagon_recolour_sets(self):
        # wagon recolour liveries can be randomised across multiple colour sets
        # this is a run-time randomisation, relying on a procedure that takes parameters for the candidate livery numbers
        # however there are 10 parameters, and calls to the procedure are needed thousands of times per grf,
        # testing proved that generating thousands of procedure calls with 10 params directly in the nml was expensive in file size, both nml and grf
        # there are however a finite number of combinations that are actually needed (only 125 as of Sept 2024)
        # therefore we can provide a compile-time lookup table, and index into it using a procedure call with a single parameter
        # this does not have the same cost in nml or grf filesize
        # CABBAGE CAN THIS BE DERIVED FROM LIVERIES NOW?
        # WHAT ARE THE PARAMS?  - COLOURS, WEATHERING?
        seen_params = []
        for wagon_model_variant in self.wagon_model_variants:
            if getattr(
                wagon_model_variant, "use_colour_randomisation_strategies", False
            ):
                seen_params.append(
                    wagon_model_variant.get_wagon_recolour_strategy_params()
                )
                seen_params.append(
                    wagon_model_variant.get_wagon_recolour_strategy_params(
                        context="purchase"
                    )
                )

        self.wagon_recolour_colour_sets = list(set(seen_params))

    def add_buyable_variant_groups(self):
        # creating groups has to happen after *all* model variants are inited

        # create the structure to hold the groups, this is set to None when the roster is inited, and should be None when this method is called
        if self.buyable_variant_groups is not None:
            raise BaseException(
                "add_buyable_variant_groups() called more than once for roster "
                + self.id
            )

        self.buyable_variant_groups = {}

        # for every buyable variant for every model_variant
        # - add a group if it doesn't already exist
        # - add the buyable variant as a member of the group
        for model_variant in self.model_variants_in_buy_menu_order:
            for buyable_variant in model_variant.cabbage_buyable_variants:
                if (
                    not buyable_variant.model_variant.buyable_variant_group_id
                    in self.buyable_variant_groups
                ):
                    self.buyable_variant_groups[
                        buyable_variant.model_variant.buyable_variant_group_id
                    ] = PurchaseVariantGroup(
                        id=buyable_variant.model_variant.buyable_variant_group_id,
                    )
                self.buyable_variant_groups[
                    buyable_variant.model_variant.buyable_variant_group_id
                ].add_buyable_variant(buyable_variant)
        # now deal with nested groups
        # we do this after creating all the groups, as some groups need to reference other groups
        for (
            buyable_variant_group_id,
            buyable_variant_group,
        ) in self.buyable_variant_groups.items():
            # we're only interested in nesting wagons as of May 2023
            parent_model_variant = buyable_variant_group.parent_model_variant
            if parent_model_variant.group_as_wagon:
                if parent_model_variant.use_named_purchase_variant_group is not None:
                    base_id_for_target_parent_model_variant = global_constants.purchase_variant_group_base_model_ids_by_group_name[
                        parent_model_variant.use_named_purchase_variant_group
                    ]
                    candidate_parent_group = None
                    if (
                        base_id_for_target_parent_model_variant
                        not in self.wagon_model_variants_by_base_id
                    ):
                        error_message = (
                            base_id_for_target_parent_model_variant
                            + " not found in roster "
                            + self.id
                        )
                        error_message += (
                            "\n look in "
                            + self.id
                            + ".wagon_module_names_with_roster_ids as the module name may be incorrect there"
                        )
                        raise BaseException(error_message)
                    for model_variant in self.wagon_model_variants_by_base_id[
                        base_id_for_target_parent_model_variant
                    ]:
                        if (
                            model_variant.model_id_root
                            == base_id_for_target_parent_model_variant
                        ):
                            match_failed = False
                            if (
                                model_variant.base_track_type_name
                                != parent_model_variant.base_track_type_name
                            ):
                                match_failed = True
                            if model_variant.gen != parent_model_variant.gen:
                                match_failed = True
                            if model_variant.subtype != parent_model_variant.subtype:
                                match_failed = True
                            if not match_failed:
                                candidate_parent_group = (
                                    model_variant.buyable_variant_group
                                )
                                break
                else:
                    candidate_parent_group = parent_model_variant.buyable_variant_group

                # we can't assign parent group to current group, that would be silly / recursive
                if candidate_parent_group != buyable_variant_group:
                    buyable_variant_group.parent_group = candidate_parent_group

    def get_lang_data(self, lang, context):
        # strings optionally vary per roster, so we have a method to fetch all lang data via the roster
        global_pragma = {}
        lang_strings = {}
        # we have the option to suppress selected strings in specific contexts, using a dedicated suppression file
        suppressed_strings = tomllib.load(
            open(
                os.path.join(currentdir, "src", "lang", "suppressed_strings.toml"), "rb"
            )
        )

        with open(os.path.join(currentdir, "src", "lang", lang + ".toml"), "rb") as fp:
            lang_source = tomllib.load(fp)

        for node_name, node_value in lang_source.items():
            # first check if the string is suppressed in this roster, when building grf only (not docs)
            if context == "grf" and node_name in suppressed_strings:
                if self.id in suppressed_strings[node_name].get(
                    "suppressed_rosters", []
                ):
                    continue

            if node_name == "GLOBAL_PRAGMA":
                # explicit handling of global pragma items
                global_pragma["grflangid"] = node_value["grflangid"]
                global_pragma["plural"] = node_value["plural"]
                if node_value.get("gender", False):
                    global_pragma["gender"] = node_value["gender"]
                if node_value.get("case", False):
                    global_pragma["case"] = node_value["case"]
            else:
                # all lang strings should provide a default base value, which can optionally be over-ridden per roster
                if self.id in node_value.keys():
                    lang_strings[node_name] = node_value[self.id]
                else:
                    lang_strings[node_name] = node_value["base"]

        for model_variant in self.model_variants_in_buy_menu_order:
            if (
                model_variant.name is not None
                and model_variant.is_default_model_variant
            ):
                lang_strings["STR_NAME_" + model_variant.model_id.upper()] = (
                    model_variant.name
                )

        return {"global_pragma": global_pragma, "lang_strings": lang_strings}


class PurchaseVariantGroup(object):
    """
    Simple class to hold groups of buyable variants.
    These provide the variant_group in nml.
    A group may comprise buyable variants for a single model type, or implement other rules to group multiple model types.
    """

    def __init__(self, id):
        self.id = id
        self.buyable_variants = []
        self.parent_group = None

    def add_buyable_variant(self, buyable_variant):
        self.buyable_variants.append(buyable_variant)

    @property
    def parent_vehicle(self):
        # actually returns a unit_variant, but eh, equivalent to 'vehicle' in the nml templating
        return self.buyable_variants[0].model_variant.units[0]

    @property
    def parent_model_variant(self):
        # convenience function, note also parent_vehicle, which is often what we want
        return self.parent_vehicle.model_variant
