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
        self.wagon_modules_provided_by_other_rosters = kwargs.get(
            "wagon_modules_provided_by_other_rosters"
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

    @property
    def engine_consists_excluding_clones(self):
        # we don't always want clones in the engine list (e.g. when generating tech tree in docs and similar cases)
        # this is a convenience wrapper to knock out any clones from engine list
        return [
            engine_consist
            for engine_consist in self.engine_consists
            if engine_consist.cloned_from_consist is None
        ]

    @property
    def wagon_consists_by_base_id(self):
        result = {}
        for wagon_consist in self.wagon_consists:
            result.setdefault(wagon_consist.base_id, [])
            result[wagon_consist.base_id].append(wagon_consist)
        return result

    @property
    def consists_in_buy_menu_order(self):
        result = []
        result.extend(self.engine_consists)
        for base_track_type_name in ["RAIL", "NG", "METRO"]:
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
        all_randomised_candidate_groups = []
        randomised_wagons_by_track_type_name_and_gen = {}
        # we need to place wagons that are in randomisation groups together, then place the randomised wagon immediately after them
        # first find which wagons belong together, by consolidating their groups
        for consist in consists:
            if (
                len(consist.randomised_candidate_groups) > 0
                and consist.randomised_candidate_groups
                not in all_randomised_candidate_groups
            ):
                all_randomised_candidate_groups.append(
                    consist.randomised_candidate_groups
                )
            if consist.is_randomised_wagon_type:
                if (
                    consist.base_track_type_name
                    not in randomised_wagons_by_track_type_name_and_gen
                ):
                    randomised_wagons_by_track_type_name_and_gen[
                        consist.base_track_type_name
                    ] = {}
                if (
                    consist.gen
                    not in randomised_wagons_by_track_type_name_and_gen[
                        consist.base_track_type_name
                    ]
                ):
                    randomised_wagons_by_track_type_name_and_gen[
                        consist.base_track_type_name
                    ][consist.gen] = []
                randomised_wagons_by_track_type_name_and_gen[
                    consist.base_track_type_name
                ][consist.gen].append(consist)
        super_groups = []
        for group in all_randomised_candidate_groups:
            seen = False
            for group_id in sorted(group):
                for super_group in super_groups:
                    if group_id in super_group:
                        super_group.extend(copy.deepcopy(group))
                        seen = True
            if not seen:
                super_groups.append(copy.deepcopy(group))
        # super_groups will contain the same id multiple times, so consolidate to uniques
        super_groups = [list(set(super_group)) for super_group in super_groups]
        for super_group in super_groups:
            for (
                base_track_type_name,
                generations,
            ) in randomised_wagons_by_track_type_name_and_gen.items():
                for gen, randomised_wagons_consists in generations.items():
                    # first find all the randomisation candidate wagons to place together
                    # we need them by base track type and gen, then if they match this super_group
                    for consist in consists:
                        if (
                            consist.base_track_type_name == base_track_type_name
                            and consist.gen == gen
                        ):
                            for group_id in consist.randomised_candidate_groups:
                                if group_id in super_group:
                                    result.append(consist)
                                    break
                    # now find the actual randomised wagons that match this super group
                    # append those after their candidate wagons
                    for group_id in super_group:
                        for consist in randomised_wagons_consists:
                            if getattr(consist, "base_id", None) == group_id:
                                result.append(consist)
                                break
        # now append all the remaining consists that don't need special treatment
        for consist in consists:
            if consist not in result:
                result.append(consist)
        return result

    def get_wagon_randomisation_candidates(self, buyable_variant):
        randomisation_consist = buyable_variant.consist
        result = []
        for base_id, wagons in self.wagon_consists_by_base_id.items():
            for wagon_consist in wagons:
                if (
                    randomisation_consist.base_id
                    not in wagon_consist.randomised_candidate_groups
                ):
                    continue
                if (
                    randomisation_consist.base_track_type_name
                    != wagon_consist.base_track_type_name
                ):
                    continue
                if randomisation_consist.gen != wagon_consist.gen:
                    continue
                if randomisation_consist.subtype != wagon_consist.subtype:
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
                + " has only one choice for randomisation_candidates, this is pointless nonsense, consider removing "
                + randomisation_consist.id
            )
        if len(result) > 64:
            # we have a limited number of random bits, and we need to use them independently of company colour choices
            # so guard against consuming too many, 64 variants is 6 bits, and that's all we have spare
            raise BaseException(
                randomisation_consist.id
                + " has more than 64 entries in randomised_candidate_groups, and will run out of random bits; reduce the number of candidates"
            )
        # length of results needs to be power of 2 as random choice can only be picked from powers of 2s, so use utils.extend_list_to_power_of_2_length
        return utils.extend_list_to_power_of_2_length(result)

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

    def get_liveries_by_name(self, additional_livery_names):
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

    def get_pax_mail_liveries(self, default_livery_group_name, **kwargs):
        result = []
        # we can optionally specify liveries per consist by passing the liveries keyword when defining the vehicle, otherwise use the default for this consist subclass
        livery_group_name = kwargs.get("liveries", default_livery_group_name)
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
                            + " - use a lower consist base_numeric_id"
                        )
            for numeric_id in consist.unique_numeric_ids:
                if numeric_id in numeric_id_defender:
                    colliding_consist = numeric_id_defender[numeric_id]
                    # there is a specific case of reused vehicles that are allowed to overlap IDs (they will be grf-independent, and the compile doesn't actually care)
                    # if base_id matches both consists have been instantiated from the same source module...
                    if hasattr(consist, "base_id"):
                        if (
                            getattr(colliding_consist, "base_id", None)
                            == consist.base_id
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
                    )
                else:
                    numeric_id_defender[numeric_id] = consist
        # no return value needed

    def register_wagon_consist(self, wagon_consist):
        # eh this is a bit of a stub function, but we have to explicitly add the wagons when they're instantiated, and it seems cleaner to delegate it to the roster?
        self.wagon_consists.append(wagon_consist)

    def post_init_actions(self):
        # init of consists has to happen after the roster is registered with RosterManager, otherwise vehicles can't get the roster
        package_name = "vehicles." + self.id
        # engines
        for engine_module_name in self.engine_module_names:
            engine_module_name = importlib.import_module(
                "." + engine_module_name, package_name
            )
            consist = engine_module_name.main(self.id)
            self.engine_consists.append(consist)
            # clone consists are used to handle articulated engines of with length variants, e.g. diesels with variants of 1 or 2 units; more than one clone is supported
            for cloned_consist in consist.clones:
                self.engine_consists.append(cloned_consist)
        # wagons for this roster
        self.init_wagon_modules(self.id, global_constants.wagon_module_names)
        # wagons reused from other rosters - there is no per-wagon selection, it's all-or-nothing for all the wagons in the module
        # this is not intended to be a common case, it's for things like torpedo cars where redrawing and redefining them for all rosters is pointless
        # this may cause compile failures when refactoring stuff due to cross-roster dependencies being broken, if so comment the calls out
        for (
            roster_id_providing_modules,
            wagon_module_names,
        ) in self.wagon_modules_provided_by_other_rosters.items():
            # apply buy menu order to wagon_modules_provided_by_other_rosters (rather than having to manually keep the lists in sync)
            wagon_module_names_in_buy_menu_order = []
            for wagon_module_name in global_constants.wagon_module_names:
                if wagon_module_name in wagon_module_names:
                    wagon_module_names_in_buy_menu_order.append(wagon_module_name)
            self.init_wagon_modules(
                roster_id_providing_modules, wagon_module_names_in_buy_menu_order
            )

    def init_wagon_modules(self, roster_id_of_module, wagon_module_names):
        package_name = "vehicles." + roster_id_of_module
        for wagon_module_name_stem in wagon_module_names:
            wagon_module_name = wagon_module_name_stem + "_" + roster_id_of_module
            try:
                wagon_module = importlib.import_module(
                    "." + wagon_module_name, package_name
                )
                wagon_module.main(
                    self.id, roster_id_providing_module=roster_id_of_module
                )
            except ModuleNotFoundError:
                # the module might be provided from another roster, which is fine
                module_provided_by_another_roster = False
                for (
                    wagon_module_names_from_another_roster
                ) in self.wagon_modules_provided_by_other_rosters.values():
                    if wagon_module_name_stem in wagon_module_names_from_another_roster:
                        module_provided_by_another_roster = True
                        break
                if not module_provided_by_another_roster:
                    # we want to warn, not fail, if a module is missing
                    # to suppress this warning, add an empty module file with main() and pass
                    utils.echo_message(
                        "wagon_module "
                        + wagon_module_name
                        + " not found in roster "
                        + self.id
                    )
            except Exception:
                raise

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
                    for consist in self.wagon_consists_by_base_id[
                        base_id_for_target_parent_consist
                    ]:
                        if consist.base_id == base_id_for_target_parent_consist:
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

    def get_lang_data(self, lang):
        # strings optionally vary per roster, so we have a method to fetch all lang data via the roster
        global_pragma = {}
        lang_strings = {}
        with open(os.path.join(currentdir, "src", "lang", lang + ".toml"), "rb") as fp:
            lang_source = tomllib.load(fp)

        for node_name, node_value in lang_source.items():
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
            if consist._name is not None:
                lang_strings["STR_NAME_" + consist.id.upper()] = consist._name

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
