import global_constants
import utils
from badges import _static_badges

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

    def cabbage_init_badges_1(self):
        # CABBAGE SHIM TO ADD DEFAULT BADGES UNTIL A BETTER PATTERN IS ESTABLISHED
        # CABBAGE SPLIT UP _static_badges to badges by domain / concern
        for (
            badge_class_label,
            badge_class_properties,
        ) in _static_badges.static_badges.items():
            # first create a badge for the class
            self.add_badge(
                label=badge_class_label,
                name=badge_class_properties.get("name", None),
            )
            # then create the badges for the class
            for sublabel, sublabel_properties in badge_class_properties.get(
                "sublabels", {}
            ).items():
                self.add_badge(
                    label=badge_class_label + "/" + sublabel,
                    name=sublabel_properties.get("name", None),
                )

        for power_source in global_constants.power_sources.keys():
            self.add_badge(
                label=f"power_source/{power_source.lower()}",
                name=f"STR_BADGE_POWER_SOURCE_{power_source}",
            )

    def cabbage_init_badges_2(self, **kwargs):
        # CABBAGE SHIM TO ADD DEFAULT BADGES UNTIL A BETTER PATTERN IS ESTABLISHED
        # THIS IS FOR BADGES THAT NEED SOMETHING PASSED

        roster_manager = kwargs["roster_manager"]

        if roster_manager.active_roster is not None:
            self.add_badge(
                f"newgrf/{utils.grfid_to_dword(roster_manager.active_roster.grfid)}"
            )

        # CABBAGE - CATALOGUES THOUGH?
        # !! this was provably slow as of March 2025, due to walking all variants, but that might be solved now?
        for roster in roster_manager:
            for model_variant in roster.model_variants:
                if model_variant.vehicle_family_badge is not None:
                    self.add_badge(
                        label=model_variant.vehicle_family_badge,
                    )

        livery_supplier = kwargs["livery_supplier"]

        self.add_badge(
            label=f"freight_livery_colour_set_name",
            name=f"STR_BADGE_COLOUR_SET_NAME",
        )
        for colour_set_name in livery_supplier.cabbage_valid_freight_livery_colour_set_names_and_nums:
            self.add_badge(
                label=f"freight_livery_colour_set_name/{colour_set_name}",
                name=f"STR_BADGE_COLOUR_SET_NAME_{colour_set_name.upper()}",
            )
