from rosters import registered_rosters
import global_constants
import pickle

class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.engine_consists = []
        for engine in kwargs.get('engines'):
            self.engine_consists.append(engine.consist)
            engine.consist.roster = self.id
        self.wagon_consists = dict([(base_id, []) for base_id in global_constants.buy_menu_sort_order_wagons])
        self.speeds = kwargs.get('speeds')

    @property
    def buy_menu_sort_order(self):
        result = []
        result.extend([consist.id for consist in self.engine_consists])
        for base_id in global_constants.buy_menu_sort_order_wagons:
            result.extend(sorted([wagon_consist.id for wagon_consist in self.wagon_consists[base_id]]))
        return result

    @property
    def consists_in_buy_menu_order(self):
        result = []
        result.extend(self.engine_consists)
        for base_id in global_constants.buy_menu_sort_order_wagons:
            result.extend(sorted(self.wagon_consists[base_id], key=lambda wagon_consist: wagon_consist.wagon_generation))
        for consist in result:
            # if consist won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(consist)
            except:
                print("Pickling failed for consist:", consist.id)
                raise
        return result

    def register_wagon_consist(self, wagon_consist):
        self.wagon_consists[wagon_consist.type_config.base_id].append(wagon_consist)
        wagon_consist.roster = self.id

    def register(self):
        registered_rosters.append(self)
