class Railtype(object):
    """
    Railtype - self explanatory?
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.label = kwargs.get("label")
        self.introduction_date = kwargs.get("introduction_date", None)  # "yyyy,mm,dd"
        self.rosters = kwargs.get("rosters", None)
        # 0 is no limit
        self.speed_limit = kwargs.get("speed_limit", 0)
        self.curve_speed_multiplier = kwargs.get("curve_speed_multiplier", 0)
        self.railtype_flags = kwargs.get("railtype_flags", None)
        self.construction_cost = kwargs.get("construction_cost", None)
        self.maintenance_cost = kwargs.get("construction_cost", None)
        self.sort_order = kwargs.get("sort_order", None)
        self.extends_RAIL = kwargs.get("extends_RAIL", False)
        self.extends_ELRL = kwargs.get("extends_ELRL", False)
        self.compatible_railtype_list = kwargs.get("compatible_railtype_list", [])
        self.powered_railtype_list = kwargs.get("powered_railtype_list", [])
        self.alternative_railtype_list = kwargs.get("alternative_railtype_list", [])
        self.use_custom_sprites = kwargs.get("use_custom_sprites", False)
        self.use_custom_signals = kwargs.get("use_custom_signals", False)
        self.disabled = False

    def make_nml_railtype_list(self, railtype_list):
        result = ",".join(['"' + railtype + '"' for railtype in railtype_list])
        return "[" + result + "]"
