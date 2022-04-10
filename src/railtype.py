from railtypes import registered_railtypes


class Railtype(object):
    """
    Railtype - self explanatory?
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.disabled = False

    def register(self, disabled=False):
        registered_railtypes.append(self)
        self.disabled = disabled
