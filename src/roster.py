from rosters import registered_rosters

class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.engine_consists = [engine.consist for engine in kwargs.get('engines')]
        self.wagon_consists = []

    @property
    def buy_menu_sort_order(self):
        return [consist.id for consist in self.engine_consists]

    def register(self):
        registered_rosters.append(self)
