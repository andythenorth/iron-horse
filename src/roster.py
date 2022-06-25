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
        self.intro_dates = kwargs.get("intro_dates")
        self.speeds = kwargs.get("speeds")
        self.freight_car_capacity_per_unit_length = kwargs.get(
            "freight_car_capacity_per_unit_length"
        )
        self.pax_car_capacity_per_unit_length = kwargs.get(
            "pax_car_capacity_per_unit_length"
        )
        self.pax_car_capacity_types = kwargs.get("pax_car_capacity_types")
        self.train_car_weight_factors = kwargs.get("train_car_weight_factors")
        self.caboose_families = kwargs.get("caboose_families")
        self.caboose_default_family_by_generation = kwargs.get(
            "caboose_default_family_by_generation"
        )
        self.livery_presets = kwargs.get("livery_presets", [])

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
        for base_track_type in ["RAIL", "NG"]:
            for base_id in global_constants.buy_menu_sort_order_wagons:
                wagon_consists = [
                    wagon_consist
                    for wagon_consist in self.wagon_consists[base_id]
                    if wagon_consist.base_track_type == base_track_type
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

    def get_wagon_randomisation_candidates(self, randomisation_consist):
        result = []
        for base_id, wagons in self.wagon_consists.items():
            for wagon_consist in wagons:
                if (
                    randomisation_consist.base_id
                    not in wagon_consist.randomised_candidate_groups
                ):
                    continue
                if (
                    randomisation_consist.base_track_type
                    != wagon_consist.base_track_type
                ):
                    continue
                if randomisation_consist.gen != wagon_consist.gen:
                    continue
                if randomisation_consist.subtype != wagon_consist.subtype:
                    continue
                result.append(wagon_consist)
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
        if len(result) > 16:
            # we have a limited number of random bits, and we need to use them independently of company colour choices
            # so guard against consuming too many, 16 variants is 4 bits, and that's quite enough
            print(result)
            raise BaseException(
                randomisation_consist.id
                + " has more than 16 entries in randomised_candidate_groups, and will run out of random bits; reduce the number of candidates"
            )
        # length of results needs to be power of 2 as random choice can only be picked from powers of 2s (1 bit = 2 options, 2 bits = 4 options, 3 bits = 8 options, 4 bits = 16 options)
        # so just do a clunky manual append here, JFDI, not figuring out a power of 2 detector at this time of night :P
        # this will cause uneven probabilities, but eh, life is not perfect
        if len(result) == 3:
            result.append(result[0])
        # this relies on recursing a bit to get to 8 as needed
        if len(result) >= 5 and len(result) < 9:
            result.extend(result[: 8 - len(result)])
        if len(result) >= 9:
            result.extend(result[: 16 - len(result)])
        return result

    def intro_date_ranges(self, base_track_type):
        # return a list of date pairs (first year, last year) for generations
        result = []
        end_date = global_constants.max_game_date
        for intro_date in reversed(self.intro_dates[base_track_type]):
            result.append((intro_date, end_date))
            end_date = intro_date - 1
        result.reverse()
        return result

    def validate_vehicles(self, numeric_id_defender):
        # has to be explicitly called after all vehicles and vehicle units are registered to the roster
        for consist in self.consists_in_buy_menu_order:
            if len(consist.units) == 0:
                raise BaseException("Error: " + consist.id + " has no units defined")
            elif len(consist.units) == 1:
                if consist.base_numeric_id <= global_constants.max_articulated_id:
                    #raise BaseException("Error: " + consist.id + " with base_numeric_id " + str(consist.base_numeric_id) + " needs a base_numeric_id larger than 8200 as the range below 8200 is reserved for articulated vehicles")
                    utils.echo_message(consist.id + " with base_numeric_id " + str(consist.base_numeric_id) + " needs a base_numeric_id larger than 8200 as the range below 8200 is reserved for articulated vehicles")
            elif len(consist.units) > 1:
                if consist.base_numeric_id > global_constants.max_articulated_id:
                    raise BaseException("Error: " + consist.id + " with base_numeric_id " + str(consist.base_numeric_id) + " is an articulated vehicle, and needs a base_numeric_id smaller than 8190")
            for unit in set(consist.units):
                if unit.numeric_id in numeric_id_defender:
                    raise BaseException("Error: unit "
                            + unit.id
                            + " has a numeric_id that collides ("
                            + str(unit.numeric_id)
                            + ") with a numeric_id of unit in another consist"
                    )
                else:
                    numeric_id_defender.append(unit.numeric_id)
        # no return value needed

    def register_wagon_consist(self, wagon_consist):
        self.wagon_consists[wagon_consist.base_id].append(wagon_consist)
        wagon_consist.roster_id = self.id

    def post_init_actions(self):
        # init has to happen after the roster is registered with RosterManager, otherwise vehicles can't get the roster
        for engine in self.engines:
            consist = engine.main(self.id)
            self.engine_consists.append(consist)
        self.wagon_consists = dict(
            [(base_id, []) for base_id in global_constants.buy_menu_sort_order_wagons]
        )
