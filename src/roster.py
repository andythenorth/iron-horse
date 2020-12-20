from rosters import registered_rosters
import global_constants
import pickle


class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.numeric_id = kwargs.get("numeric_id")
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
        self.train_car_weight_factors = kwargs.get("train_car_weight_factors")
        self.livery_presets = kwargs.get("livery_presets", [])
        self.disabled = False

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

    def register_wagon_consist(self, wagon_consist):
        self.wagon_consists[wagon_consist.base_id].append(wagon_consist)
        wagon_consist.roster_id = self.id

    def register(self, disabled=False):
        registered_rosters.append(self)
        self.disabled = disabled
        for engine in self.engines:
            consist = engine.main(self.id)
            self.engine_consists.append(consist)
        self.wagon_consists = dict(
            [(base_id, []) for base_id in global_constants.buy_menu_sort_order_wagons]
        )
