import copy
import importlib
import os
import pickle
import tomllib

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
        # engine_module_names only used once at __init__ time, it's a list of module names, not the actual consists
        self.engine_module_names = kwargs.get("engine_module_names")
        self.wagon_module_names_with_roster_ids = kwargs.get(
            "wagon_module_names_with_roster_ids"
        )
        self.engine_consists = []
        self.wagon_consists = []
        # create a structure to hold (buyable) variant groups
        # deliberately instantiated as none - cannot be populated as a structure until later, after all consists are inited
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
        self.freight_wagon_liveries = kwargs.get("freight_wagon_liveries", {})
        self.pax_mail_livery_groups = kwargs.get("pax_mail_livery_groups", {})
        self.wagon_recolour_colour_sets = []

    @property
    def engine_consists_excluding_clones(self):
        # we don't always want clones in the engine list (e.g. when generating tech tree in docs and similar cases)
        # this is a convenience wrapper to knock out any clones from engine list
        return [
            engine_consist
            for engine_consist in self.engine_consists
            if engine_consist.is_clone == False
        ]

    @property
    def wagon_consists_by_base_id(self):
        result = {}
        for wagon_consist in self.wagon_consists:
            result.setdefault(wagon_consist.model_type_id_root, [])
            result[wagon_consist.model_type_id_root].append(wagon_consist)
        return result

    @property
    def consists_in_buy_menu_order(self):
        result = []
        result.extend(self.engine_consists)
        for base_track_type_name in ["RAIL", "NG", "METRO"]:
            # CABBAGE refactor to model_type_id not base_id
            for base_id in self.wagon_consists_by_base_id.keys():
                wagon_consists = [
                    wagon_consist
                    for wagon_consist in self.wagon_consists_by_base_id[base_id]
                    if wagon_consist.base_track_type_name == base_track_type_name
                ]
                result.extend(
                    # note that we want the sort order to be U, A, B, C, D so special handling
                    # this *doesn*'t handle the case of changing _multiple_ times between U and A / B / C / D between generations
                    sorted(
                        wagon_consists,
                        key=lambda wagon_consist: {
                            "U": 1,
                            "A": 2,
                            "B": 3,
                            "C": 4,
                            "D": 5,
                        }[wagon_consist.subtype],
                    )
                )
        for consist in result:
            # if consist won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(consist)
            except:
                print("Pickling failed for consist:", consist.id)
                raise
        return result

    @property
    def consists_in_order_optimised_for_action_2_ids(self):
        # the base sort order for consists is for the buy menu, but this isn't effective for order in nml output
        # because randomised wagons need action 2 IDs spanning multiple other vehicles, and this can cause problems allocating enough action 2 IDs
        # therefore we re-order, to group (as far as we can) vehicles where IDs need to span
        # this isn't infallible, but reduces the extent to which the randomised wagons consume action 2 IDs
        consists = self.consists_in_buy_menu_order
        result = []
        randomised_wagons_by_track_gen_length_power = {}

        # Categorize consists by generation, length, track type, and speed
        for consist in consists:
            gen = consist.gen
            track_type = consist.base_track_type_name
            power = consist.power
            length = consist.length

            key = (track_type, gen, length, power)

            if key not in randomised_wagons_by_track_gen_length_power:
                randomised_wagons_by_track_gen_length_power[key] = {
                    "candidates": [],
                    "randomised": [],
                }

            if consist.is_randomised_wagon_type:
                randomised_wagons_by_track_gen_length_power[key]["randomised"].append(
                    consist
                )
            else:
                randomised_wagons_by_track_gen_length_power[key]["candidates"].append(
                    consist
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

    def get_wagon_randomisation_candidates(self, buyable_variant):
        randomisation_consist = buyable_variant.consist
        result = []
        for base_id, wagons in self.wagon_consists_by_base_id.items():
            for wagon_consist in wagons:
                if randomisation_consist.gen != wagon_consist.gen:
                    continue
                if (
                    randomisation_consist.base_track_type_name
                    != wagon_consist.base_track_type_name
                ):
                    continue
                if randomisation_consist.subtype != wagon_consist.subtype:
                    continue
                if (
                    randomisation_consist.model_type_id_root
                    == wagon_consist.model_type_id_root
                ):
                    continue
                if (
                    randomisation_consist.model_type_id_root
                    not in wagon_consist.randomised_candidate_groups
                ):
                    continue
                # if there are buyable variants that have random livery
                # then we want to only append those as it's more direct and leads to shorter candidate lists
                # otherwise append all the variants
                unit_variants = wagon_consist.units[0].unit_variants
                matched_results = []
                for unit_variant in unit_variants:
                    if (
                        unit_variant.buyable_variant.livery["colour_set"]
                        == buyable_variant.livery["colour_set"]
                    ):
                        matched_results.append(unit_variant)
                if len(matched_results) == 0:
                    for unit_variant in unit_variants:
                        if (
                            unit_variant.buyable_variant.livery["colour_set"]
                            in global_constants.wagon_livery_mixes[
                                buyable_variant.livery["colour_set"]
                            ]
                        ):
                            matched_results.append(unit_variant)
                result.extend(matched_results)
        if len(result) == 0:
            raise BaseException(
                randomisation_consist.id
                + " did not match any randomisation_candidates, possibly there are no matching wagons for base_id/length/gen"
            )
        if len(result) == 1:
            print(result)
            raise BaseException(
                randomisation_consist.id
                + " colour set "
                + buyable_variant.livery["colour_set"]
                + " has only one choice for randomisation_candidates, this is pointless nonsense, consider removing "
                + randomisation_consist.id
                + " or check that randomisation candidates provide this colour set"
            )
        if len(result) > 64:
            # we have a limited number of random bits, and we need to use them independently of company colour choices
            # so guard against consuming too many, 64 variants is 6 bits, and that's all we want to consume
            raise BaseException(
                randomisation_consist.id
                + " has more than 64 entries in randomised_candidate_groups, and will run out of random bits; reduce the number of candidates"
            )
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

    def get_liveries_by_name_cabbage_new(self, additional_livery_names):
        # CABBAGE - REFACTORING SHIM
        result = []
        try:
            result.extend(
                [
                    self.engine_and_pax_mail_car_liveries[additional_livery_name]
                    for additional_livery_name in additional_livery_names
                ]
            )
        except:
            # assume we've been passed a freight livery
            # CABBAGE - SHOULD ONLY BE ONE LIVERY NAME IN ACTUALITY
            for livery_name in additional_livery_names:
                result.append(global_constants.freight_wagon_liveries[livery_name])
        return result

    def get_liveries_by_name(self, additional_livery_names):
        # CABBAGE - LEGACY SUPPORT
        # for the general case, this is a convenience approach to insert a default_livery for ease of constructing template repeats
        # note that default_livery is not guaranteed to contain all the key/value pairs that additional_liveries has
        result = [self.default_livery]
        result.extend(
            [
                self.engine_and_pax_mail_car_liveries[additional_livery_name]
                for additional_livery_name in additional_livery_names
            ]
        )
        return result

    def get_pax_mail_liveries(self, default_livery_group_name, model_def):
        result = []
        # we can optionally specify liveries per consist via the model_def, otherwise use the default for this consist subclass
        if model_def.livery_group_name is not None:
            livery_group_name = model_def.livery_group_name
        else:
            livery_group_name = default_livery_group_name
        # will fail if the livery group is not defined in the roster
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
        # has to be explicitly called after all vehicles and vehicle units are registered to the roster

        # this structure is used to test for duplicate ids
        consist_ids = [consist.id for consist in self.consists_in_buy_menu_order]

        for consist in self.consists_in_buy_menu_order:
            if consist_ids.count(consist.id) > 1:
                raise BaseException(
                    "Error: vehicle id '"
                    + consist.id
                    + "' is defined more than once - to fix, search src for the duplicate"
                )
            if len(consist.units) == 0:
                raise BaseException("Error: " + consist.id + " has no units defined")
            elif len(consist.units) == 1:
                if consist.base_numeric_id <= global_constants.max_articulated_id:
                    # se
                    raise BaseException(
                        "Error: "
                        + consist.id
                        + " with base_numeric_id "
                        + str(consist.base_numeric_id)
                        + " needs a base_numeric_id larger than 16383 as the range below 16383 is reserved for articulated vehicles"
                    )
                    # utils.echo_message(consist.id + " with base_numeric_id " + str(consist.base_numeric_id) + " needs a base_numeric_id larger than 8200 as the range below 8200 is reserved for articulated vehicles")
                    # utils.echo_message(str(consist.base_numeric_id))
            elif len(consist.units) > 1:
                for numeric_id in consist.unique_numeric_ids:
                    if numeric_id > global_constants.max_articulated_id:
                        raise BaseException(
                            "Error: "
                            + consist.id
                            + " has a unit variant with numeric_id "
                            + str(numeric_id)
                            + " which is part of an articulated vehicle, and needs a numeric_id smaller than "
                            + str(global_constants.max_articulated_id)
                            + "\nUse a lower consist base_numeric_id\n"
                            + str(consist.units)
                        )
            for numeric_id in consist.unique_numeric_ids:
                if numeric_id in numeric_id_defender:
                    colliding_consist = numeric_id_defender[numeric_id]
                    # there is a specific case of reused vehicles that are allowed to overlap IDs (they will be grf-independent, and the compile doesn't actually care)
                    # if base_id matches both consists have been instantiated from the same source module...
                    if hasattr(consist, "model_type_id_root"):
                        if (
                            getattr(colliding_consist, "model_type_id_root", None)
                            == consist.model_type_id_root
                        ):
                            # it's fine if both consists are then in different rosters, as they will not conflict
                            if colliding_consist.roster.id != consist.roster.id:
                                continue
                    raise BaseException(
                        "Error: consist "
                        + consist.id
                        + " has a unit variant with a numeric_id that collides ("
                        + str(numeric_id)
                        + ") with a numeric_id of a unit variant in consist "
                        + colliding_consist.id
                        + "\n"
                        + str([unit.unit_variants for unit in consist.units])
                    )
                else:
                    numeric_id_defender[numeric_id] = consist
        # no return value needed

    def register_wagon_consist(self, wagon_consist):
        # eh this is a bit of a stub function, but we have to explicitly add the wagons when they're instantiated, and it seems cleaner to delegate it to the roster?
        self.wagon_consists.append(wagon_consist)

    def post_init_actions(self):
        # init of vehicle models has to happen after the roster is registered with RosterManager, otherwise they can't get the roster
        self.init_engine_modules()
        self.init_wagon_modules()
        self.init_wagon_recolour_colour_sets()

    def init_engine_modules(self):
        package_name = "vehicles." + self.id
        roster_id_providing_module = self.id
        # engines
        for engine_module_name in self.engine_module_names:
            engine_module_name = importlib.import_module(
                "." + engine_module_name, package_name
            )
            for model_def in engine_module_name.main():
                model_variant_factory = ModelVariantFactory(
                    model_def, self.id, roster_id_providing_module
                )
                if model_variant_factory.cabbage_new_livery_system:
                    for catalogue_index, _ in enumerate(
                        model_variant_factory.catalogue
                    ):
                        consist = model_variant_factory.produce(
                            catalogue_index=catalogue_index
                        )
                        self.engine_consists.append(consist)
                else:
                    consist = model_variant_factory.produce(catalogue_index="_cabbage")
                    self.engine_consists.append(consist)

    def init_wagon_modules(self):
        # wagons can be optionally reused from other rosters - there is no per-wagon selection, it's all-or-nothing for all the wagons in the module
        # this is not intended to be a common case, it's for things like torpedo cars where redrawing and redefining them for all rosters is pointless
        # this may cause compile failures when refactoring stuff due to cross-roster dependencies being broken, if so comment the calls out
        # validation
        for wagon_module_name_stem in self.wagon_module_names_with_roster_ids.keys():
            if wagon_module_name_stem not in global_constants.wagon_module_name_stems:
                utils.echo_message(
                    "Warning: ("
                    + self.id
                    + ") "
                    + wagon_module_name_stem
                    + " not found in global_constants.wagon_module_name_stems"
                )

        for wagon_module_name_stem in global_constants.wagon_module_name_stems:
            if "_randomised" in wagon_module_name_stem:
                # CABBAGE SKIP RANDOMISED WAGONS FOR NOW
                continue
            if wagon_module_name_stem in self.wagon_module_names_with_roster_ids.keys():
                roster_id_providing_module = self.wagon_module_names_with_roster_ids[
                    wagon_module_name_stem
                ]
                wagon_module_name = (
                    wagon_module_name_stem + "_" + roster_id_providing_module
                )
                package_name = "vehicles." + roster_id_providing_module
                try:
                    wagon_module = importlib.import_module(
                        "." + wagon_module_name, package_name
                    )
                    for model_def in wagon_module.main():
                        model_variant_factory = ModelVariantFactory(
                            model_def, self.id, roster_id_providing_module
                        )
                        if model_variant_factory.cabbage_new_livery_system:
                            if "Randomised" in model_def.class_name:
                                # CABBAGE SKIP RANDOMISED WAGONS FOR NOW
                                continue
                            # CABBAGE TRIM CATALOGUE TO FIRST ENTRY DUE TO ACTION 1 LIMIT TEMPORARILY BEING EXCEEDED BY OUTDATED TEMPLATING
                            for catalogue_index, _ in enumerate(
                                model_variant_factory.catalogue[0:1]
                            ):
                                consist = model_variant_factory.produce(
                                    catalogue_index=catalogue_index
                                )
                        else:
                            model_variant_factory.produce(catalogue_index="_cabbage")
                except ModuleNotFoundError:
                    raise ModuleNotFoundError(
                        wagon_module_name
                        + " in "
                        + package_name
                        + " as defined by "
                        + self.id
                        + ".wagon_module_names_with_roster_ids"
                    )
                except Exception:
                    raise

    def init_wagon_recolour_colour_sets(self):
        # wagon recolour liveries can be randomised across multiple colour sets
        # this is a run-time randomisation, relying on a procedure that takes parameters for the candidate livery numbers
        # however there are 10 parameters, and calls to the procedure are needed thousands of times per grf,
        # testing proved that generating thousands of procedure calls with 10 params directly in the nml was expensive in file size, both nml and grf
        # there are however a finite number of combinations that are actually needed (only 125 as of Sept 2024)
        # therefore we can provide a compile-time lookup table, and index into it using a procedure call with a single parameter
        # this does not have the same cost in nml or grf filesize
        seen_params = []
        for wagon_consist in self.wagon_consists:
            for unit in wagon_consist.unique_units:
                if getattr(wagon_consist, "use_colour_randomisation_strategies", False):
                    for unit_variant in unit.unit_variants:
                        seen_params.append(
                            unit_variant.get_wagon_recolour_strategy_params()
                        )
                        seen_params.append(
                            unit_variant.get_wagon_recolour_strategy_params(
                                context="purchase"
                            )
                        )

        self.wagon_recolour_colour_sets = list(set(seen_params))

    def add_buyable_variant_groups(self):
        # creating groups has to happen after *all* consists are inited

        # create the structure to hold the groups, this is set to None when the roster is inited, and should be None when this method is called
        if self.buyable_variant_groups is not None:
            raise BaseException(
                "add_buyable_variant_groups() called more than once for roster "
                + self.id
            )

        self.buyable_variant_groups = {}

        # for every buyable variant for every consist
        # - add a group if it doesn't already exist
        # - add the buyable variant as a member of the group
        for consist in self.consists_in_buy_menu_order:
            for buyable_variant in consist.buyable_variants:
                if (
                    not buyable_variant.buyable_variant_group_id
                    in self.buyable_variant_groups
                ):
                    self.buyable_variant_groups[
                        buyable_variant.buyable_variant_group_id
                    ] = BuyableVariantGroup(
                        id=buyable_variant.buyable_variant_group_id,
                    )
                self.buyable_variant_groups[
                    buyable_variant.buyable_variant_group_id
                ].add_buyable_variant(buyable_variant)
        # now deal with nested groups
        # we do this after creating all the groups, as some groups need to reference other groups
        for (
            buyable_variant_group_id,
            buyable_variant_group,
        ) in self.buyable_variant_groups.items():
            # we're only interested in nesting wagons as of May 2023
            parent_consist = buyable_variant_group.parent_consist
            if parent_consist.group_as_wagon:
                if parent_consist.use_named_buyable_variant_group is not None:
                    base_id_for_target_parent_consist = global_constants.buyable_variant_group_consist_base_ids_by_group_name[
                        parent_consist.use_named_buyable_variant_group
                    ]
                    candidate_parent_group = None
                    if (
                        base_id_for_target_parent_consist
                        not in self.wagon_consists_by_base_id
                    ):
                        error_message = (
                            base_id_for_target_parent_consist
                            + " not found in roster "
                            + self.id
                        )
                        error_message += (
                            "\n look in "
                            + self.id
                            + ".wagon_module_names_with_roster_ids as the module name may be incorrect there"
                        )
                        raise BaseException(error_message)
                    for consist in self.wagon_consists_by_base_id[
                        base_id_for_target_parent_consist
                    ]:
                        if (
                            consist.model_type_id_root
                            == base_id_for_target_parent_consist
                        ):
                            match_failed = False
                            if (
                                consist.base_track_type_name
                                != parent_consist.base_track_type_name
                            ):
                                match_failed = True
                            if consist.gen != parent_consist.gen:
                                match_failed = True
                            if consist.subtype != parent_consist.subtype:
                                match_failed = True
                            if not match_failed:
                                candidate_parent_group = consist.buyable_variants[
                                    0
                                ].buyable_variant_group
                                break
                else:
                    candidate_parent_group = parent_consist.buyable_variants[
                        0
                    ].buyable_variant_group

                # we can't assign parent group to current group, that would be silly / recursive
                if candidate_parent_group != buyable_variant_group:
                    buyable_variant_group.parent_group = candidate_parent_group

    def get_buyable_variants_in_buy_menu_order(self):
        # relies on the buyable variant group order already being sorted when it's constructed from consists_in_buy_menu_order
        # as a convenience, this flattens that order to a list that's easy to iterate over in template
        result = []
        for (
            buyable_variant_group_id,
            buyable_variant_group,
        ) in self.buyable_variant_groups.items():
            for buyable_variant in buyable_variant_group.buyable_variants:
                result.append(buyable_variant)
        return result

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

        for consist in self.consists_in_buy_menu_order:
            if (
                consist.name is not None
                and consist.model_variant_factory.cabbage_model_variant_is_default(
                    consist
                )
            ):
                lang_strings["STR_NAME_" + consist.id.upper()] = consist.name

        return {"global_pragma": global_pragma, "lang_strings": lang_strings}


class BuyableVariantGroup(object):
    """
    Simple class to hold groups of buyable variants.
    These provide the variant_group in nml.
    A group may comprise buyable variants for a single consist, or implement other rules.
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
        return self.buyable_variants[0].lead_unit_variant_matching_buyable_variant

    @property
    def parent_consist(self):
        # convenience function, note also parent_vehicle, which is often what we want
        return self.parent_vehicle.unit.consist
