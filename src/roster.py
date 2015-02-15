from rosters import registered_rosters

class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.engines = kwargs.get('engines')

    @property
    def buy_menu_sort_order(self):
        return [engine.consist.id for engine in self.engines]

    def register(self):
        registered_rosters.append(self)
