class Badge(object):
    """Simple generic class for badges"""

    def __init__(self, label, **kwargs):
        self.label = label
        self.name = kwargs.get("name", None)
