from rosters import registered_rosters

def register(roster):
    registered_rosters[roster.id] = roster


class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.buy_menu_sort_order = kwargs.get('buy_menu_sort_order')
        register(self)
