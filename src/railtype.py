import importlib
import string

import global_constants


# !! could be @dataclass, but little benefit to changing currently
class Railtype(object):
    """
    Railtype - self explanatory?
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.vehicle_track_type_name = kwargs.get("vehicle_track_type_name")
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
        self.is_lgv_railtype = kwargs.get("is_lgv_railtype", False)
        self.alternative_railtype_list = kwargs.get("alternative_railtype_list", [])
        self.use_custom_sprites = kwargs.get("use_custom_sprites", False)
        self.use_custom_signals = kwargs.get("use_custom_signals", False)
        self.suppress_for_nml = kwargs.get("suppress_for_nml", False)
        self.disabled = False
        self.compatible_railtype_list = kwargs.get("compatible_railtype_list", [])
        self.powered_railtype_list = kwargs.get("powered_railtype_list", [])

    def make_nml_railtype_list(self, railtype_list):
        result = ",".join(['"' + railtype + '"' for railtype in railtype_list])
        return "[" + result + "]"


class RailTypeManager(list):
    """
    It's convenient to have a structure for working with railtypes.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_railtypes(self, railtype_module_names):
        for railtype_module_name in railtype_module_names:
            railtype_module = importlib.import_module(
                "." + railtype_module_name, package="railtypes"
            )
            railtype = railtype_module.main(disabled=False)
            self.append(railtype)

    def get_railtype_by_vehicle_track_type_name(self, vehicle_track_type_name):
        for railtype in self:
            if railtype.vehicle_track_type_name == vehicle_track_type_name:
                return railtype
        raise ValueError(f"No railtype found with vehicle_track_type_name={vehicle_track_type_name}")

    @property
    def railtype_labels_by_vehicle_track_type_name_cabbage(self):
        result = {}
        for railtype in self:
            labels_list = []
            labels_list.append(railtype.label)
            result[railtype.vehicle_track_type_name] = labels_list

        return result

    @property
    def lgv_railtype_labels(self):
        result = []
        for railtype in self:
            if railtype.is_lgv_railtype:
                result.append(railtype.label)
        return result
