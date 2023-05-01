import global_constants
import pickle
import utils


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
        # engines only used once at __init__ time, it's a list of modules, not the actual consists
        self.engines = kwargs.get("engines")
        self.engine_consists = []
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
        self.engine_liveries = kwargs.get("engine_liveries", [])
        self.wagon_liveries = kwargs.get("wagon_liveries", {})
        self.default_pax_liveries = kwargs.get("default_pax_liveries", [])
        self.suburban_pax_liveries = kwargs.get("suburban_pax_liveries", [])
        self.default_mail_liveries = kwargs.get("default_mail_liveries", [])
        self.electric_railcar_mail_liveries = kwargs.get(
            "electric_railcar_mail_liveries", []
        )
        self.diesel_railcar_mail_liveries = kwargs.get(
            "diesel_railcar_mail_liveries", []
        )
        self.default_metro_liveries = kwargs.get("default_metro_liveries", [])
        self.dvt_mail_liveries = kwargs.get("dvt_mail_liveries", [])

    @property
    def buy_menu_sort_order(self):
        result = []
        result.extend([consist.id for consist in self.engine_consists])
        for base_id in global_constants.buy_menu_sort_order_wagons:
            result.extend(
                sorted(
                    [wagon_consist.id for wagon_consist in self.wagon_consists[base_id]]
                )
            )
        return result

    @property
    def consists_in_buy_menu_order(self):
        result = []
        result.extend(self.engine_consists)
        for base_track_type_name in ["RAIL", "NG"]:
            for base_id in global_constants.buy_menu_sort_order_wagons:
                wagon_consists = [
                    wagon_consist
                    for wagon_consist in self.wagon_consists[base_id]
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
        # now guard against any consists missing from buy menu order or vice versa, as that wastes time asking 'wtf?' when they don't appear in game
        consist_id_defender = set([consist.id for consist in result])
        buy_menu_defender = set(self.buy_menu_sort_order)
        for id in buy_menu_defender.difference(consist_id_defender):
            utils.echo_message(
                "Warning: consist "
                + id
                + " in buy_menu_sort_order, but not found in registered_consists"
            )
        for id in consist_id_defender.difference(buy_menu_defender):
            utils.echo_message(
                "Warning: consist "
                + id
                + " in consists, but not in buy_menu_sort_order - won't show in game"
            )
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
                        super_group.extend(group)
                        seen = True
            if not seen:
                super_groups.append(group)
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
        print("CABBAGE 2000", randomisation_consist.id, "variant", buyable_variant.buyable_variant_num)
        print("target:", buyable_variant.livery["colour_set"])
        for base_id, wagons in self.wagon_consists.items():
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
                print("unit_variants", unit_variants)
                for unit_variant in unit_variants:
                    print("potential candidate:", unit_variant.id, "|", unit_variant.buyable_variant.livery["colour_set"])
                    if unit_variant.buyable_variant.livery["colour_set"] == buyable_variant.livery["colour_set"]:
                        matched_results.append(unit_variant)
                if len(matched_results) == 0:
                    for unit_variant in unit_variants:
                        if unit_variant.buyable_variant.livery["colour_set"] in global_constants.wagon_livery_mixes[buyable_variant.livery["colour_set"]]:
                            matched_results.append(unit_variant)
                result.extend(matched_results)
        print("RESULT:", result)
        if len(result) == 0:
            raise BaseException(
                randomisation_consist.id
                + " did not match any randomisation_candidates, possibly there are no matching wagons for base_id/length/gen"
            )
        if len(result) == 1:
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
                self.engine_liveries[additional_livery_name]
                for additional_livery_name in additional_livery_names
            ]
        )
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
                    raise BaseException(
                        "Error: "
                        + consist.id
                        + " with base_numeric_id "
                        + str(consist.base_numeric_id)
                        + " needs a base_numeric_id larger than 8200 as the range below 8200 is reserved for articulated vehicles"
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
                            + " (use a lower consist base_numeric_id)"
                        )
            for numeric_id in consist.unique_numeric_ids:
                if numeric_id in numeric_id_defender:
                    raise BaseException(
                        "Error: consist "
                        + consist.id
                        + " has a unit variant with numeric_id that collides ("
                        + str(numeric_id)
                        + ") with a numeric_id of a unit variant in another consist"
                    )
                else:
                    numeric_id_defender.append(numeric_id)
        # no return value needed

    def register_wagon_consist(self, wagon_consist):
        self.wagon_consists[wagon_consist.base_id].append(wagon_consist)
        wagon_consist.roster_id = self.id

    def post_init_actions(self):
        # init of consists has to happen after the roster is registered with RosterManager, otherwise vehicles can't get the roster
        for engine in self.engines:
            consist = engine.main(self.id)
            self.engine_consists.append(consist)
        self.wagon_consists = dict(
            [(base_id, []) for base_id in global_constants.buy_menu_sort_order_wagons]
        )

    def get_variant_group_id_from_named_group(self, group_name, consist):
        # composes a group id from a group name, and some properties from the consist
        return "{a}_{b}_gen_{c}{d}".format(
            a=group_name,
            b=consist.base_track_type_name.lower(),
            c=consist.gen,
            d=consist.subtype,
        )

    def add_buyable_variant_groups(self):
        # creating groups has to happen after *all* consists are inited

        # create the structure to hold the groups, this is set to None when the roster is inited, and should be None when this method is called
        if self.buyable_variant_groups is not None:
            raise BaseException(
                "add_buyable_variant_groups() called more than once for roster "
                + self.id
            )

        self.buyable_variant_groups = {}

        # for every consist
        # - add a group if it doesn't already exist
        # - add the consist as a member of the group
        for consist in self.consists_in_buy_menu_order:
            if not consist.buyable_variant_group_id in self.buyable_variant_groups:
                self.buyable_variant_groups[
                    consist.buyable_variant_group_id
                ] = BuyableVariantGroup(
                    id=consist.buyable_variant_group_id,
                    named_group=consist.use_named_buyable_variant_group,
                )
            self.buyable_variant_groups[consist.buyable_variant_group_id].add_consist(
                consist
            )


class BuyableVariantGroup(object):
    """
    Simple class to hold groups of buyable variants.
    These provide the variant_group in nml.
    A group may comprise the buyable variants for a single consist, or it may be composed of all the buyable variants from multiple consists.
    """

    def __init__(self, id, named_group):
        self.id = id
        self.named_group = named_group
        self.consists = []

    def add_consist(self, consist):
        self.consists.append(consist)

    @property
    def parent_consist(self):
        # first check if the consist has a named group, if it does then that will specify a consist base_id to match
        if self.named_group is not None:
            base_id = (
                global_constants.buyable_variant_group_consist_base_ids_by_group_name[
                    self.named_group
                ]
            )
            for consist in self.consists:
                if consist.base_id == base_id:
                    return consist
        # otherwise fall through to the first consist in the list
        # !! this may not give the intended result at all currently
        # !! - non-named groups, this might not be the parent vehicle at all
        # !! - named groups, we might want to control this by buy menu order (might already be so though)
        return self.consists[0]

    @property
    def total_number_of_buyable_consists(self):
        # the total number of buyable consists is the sum of buyable variants for all the consists in the group
        result = 0
        for consist in self.consists:
            for buyable_variant in consist.buyable_variants:
                result += 1
        return result

    @property
    def name(self):
        # assumes wagon groups as of April 2023, change if needed
        # !! might want to handle case of group_base_id = None?
        if self.named_group != None and self.total_number_of_buyable_consists > 1:
            try:
                return "string(STR_NAME_CONSIST_COMPOUND_TWO, string({a}), string({b}))".format(
                    a="STR_" + self.named_group.upper(),
                    b=self.parent_consist.wagon_title_subtype_str,
                )

            except:
                raise BaseException(self.parent_consist.id)
        else:
            return self.parent_consist.get_name()
