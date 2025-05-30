import importlib

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
        self.base_label_in_standardised_scheme = kwargs.get(
            "base_label_in_standardised_scheme"
        )
        self.non_standardised_rtt_fallback_labels = kwargs.get(
            "non_standardised_rtt_fallback_labels"
        )
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
        self.extends_RAIL = kwargs.get("extends_RAIL", False)
        self.extends_ELRL = kwargs.get("extends_ELRL", False)
        self.compatible_railtype_list = kwargs.get("compatible_railtype_list", [])
        self.powered_railtype_list = kwargs.get("powered_railtype_list", [])
        self.alternative_railtype_list = kwargs.get("alternative_railtype_list", [])
        self.use_custom_sprites = kwargs.get("use_custom_sprites", False)
        self.use_custom_signals = kwargs.get("use_custom_signals", False)
        self.suppress_for_nml = kwargs.get("suppress_for_nml", False)
        self.disabled = False

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

    @property
    def railtype_labels_by_vehicle_track_type_name_cabbage(self):
        result = {}
        for railtype in self:
            labels_list = []
            labels_list.append(railtype.label)
            labels_list.append(railtype.base_label_in_standardised_scheme)
            labels_list.extend(railtype.non_standardised_rtt_fallback_labels)
            result[railtype.vehicle_track_type_name] = labels_list

        return result

    @property
    def railtype_labels_for_railtypetable(self):
        # the railtypetable needs both lists of fallbacks by track_type_name, and all of the labels from each list so we can refer to them in e.g. tile checks
        # note that this is using the nml fallbacks for *vehicle* track_type NOT the compatible or powered powered properties for the railtypes
        # this is strictly not the scope of RailTypeManager, but it's a convenient place to add globally accessible railtype specific methods
        result = {}
        for labels in self.railtype_labels_by_vehicle_track_type_name_cabbage.values():
            result[labels[0]] = labels
        for labels in self.railtype_labels_by_vehicle_track_type_name_cabbage.values():
            for label in labels:
                if label not in result.keys():
                    result[label] = None
        return result

    def get_railtype_by_label(self, label):
        for railtype in self:
            if railtype.label == label:
                return railtype
        # no default return, error if not found
        raise ValueError(f"Not found: {label}")

    @property
    def lgv_railtype_labels(self):
        result = []
        for railtype in self:
            if railtype.is_lgv_railtype:
                # take the IH and standardised labels
                result.append(railtype.label)
                result.append(railtype.base_label_in_standardised_scheme)
        return result
