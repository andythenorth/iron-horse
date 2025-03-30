# CABBAGE - convert to @dataclass?
# ALSO - move to train/badge.py? - ¿ might not just be trains ?


class Badge(object):
    """Simple generic class for badges"""

    def __init__(self, label, **kwargs):
        self.label = label
        self.name = kwargs.get("name", None)


class BadgeManager(list):
    """
    It's convenient to have a structure for working with badges.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_badge(self, label, **kwargs):
        # if not a duplicate, add the badge
        if self.get_badge_by_label(label) is None:
            self.append(Badge(label, **kwargs))
        # no return as of now, not needed

    def get_badge_by_label(self, label):
        for badge in self:
            if badge.label == label:
                return badge
        return None
