import global_constants
import utils
from utils import timing
from badges import _static_badges
from badges.graphics_generator import BadgeGraphicsGenerator

# CABBAGE - convert to @dataclass?
# ALSO - move to train/badge.py? - ¿ might not just be trains ?


class Badge(object):
    """Simple generic class for badges"""

    def __init__(self, label, **kwargs):
        self.label = label
        self.name = kwargs.get("name", None)
        self._flags = kwargs.get("flags", [])
        self.sprite = kwargs.get("sprite", None)

    @property
    def flags(self):
        result = self._flags
        if self.sprite is not None:
            result.append("BADGE_FLAG_NAME_USE_COMPANY_COLOUR")
        return ",".join(set(result))


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
        # purely static badges
        # CABBAGE SPLIT UP _static_badges to badges by domain / concern?  MAYBE NOT NEEDED
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

    @timing
    def cabbage_init_badges_2(self, **kwargs):
        # CABBAGE SHIM TO ADD DEFAULT BADGES UNTIL A BETTER PATTERN IS ESTABLISHED
        # THIS IS FOR BADGES THAT NEED SOMETHING PASSED

        roster_manager = kwargs["roster_manager"]

        if roster_manager.active_roster is not None:
            self.add_badge(
                f"newgrf/{utils.grfid_to_dword(roster_manager.active_roster.grfid)}"
            )

        for roster in roster_manager:
            for catalogue in roster.catalogues:
                # vehicle_family_badge should always be found, error if not
                self.add_badge(
                    label=catalogue.default_model_variant_from_roster.vehicle_family_badge,
                )
                if catalogue.default_model_variant_from_roster.catalogue_entry.model_is_randomised_wagon_type:
                    # this is inherently inefficient as it walks ALL the candidates, but actually only needs one vehicle name for each vehicle_family_id
                    # but...probably fine as of April 2025 - the whole method timed at < 0.1s
                    for label, name in catalogue.default_model_variant_from_roster.cabbage_wagon_randomisation_candidate_assortment_unique_names.items():
                        self.add_badge(
                            label=f"ih_randomised_wagon/candidates/{label}",
                            #name=f"{name}",
                        )

        # power source badges
        for power_source in global_constants.power_sources.keys():
            self.add_badge(
                label=f"power_source/{power_source.lower()}",
                name=f"STR_BADGE_POWER_SOURCE_{power_source}",
            )

        # livery badges
        livery_supplier = kwargs["livery_supplier"]

        self.add_badge(
            label=f"livery",
            name="STR_BADGE_LIVERY",
        )
        for livery in livery_supplier.values():
            name=f"STR_BADGE_LIVERY_{livery.livery_name}"
            sprite = None
            if livery.is_freight_wagon_livery:
                sprite = f"{livery.livery_name.lower()}"
            self.add_badge(
                label=livery.badge_label,
                sprite=sprite,
                name=name,
            )

        # copy elements of the livery_def into badges, for both behaviour and debugging
        self.add_badge(
            label=f"ih_livery_def/use_weathering/false",
        )
        self.add_badge(
            label=f"ih_livery_def/use_weathering/true",
        )
        for (
            colour_set_name
        ) in livery_supplier.cabbage_valid_freight_livery_colour_set_names_and_nums:
            self.add_badge(
                label=f"ih_livery_def/colour_set_names/{colour_set_name}",
                #name=f"STR_BADGE_COLOUR_SET_NAME_{colour_set_name.upper()}",
            )

    def render_graphics(self, iron_horse, graphics_input_path, graphics_output_path):
        badge_graphics_generator = BadgeGraphicsGenerator(
            self, iron_horse, graphics_input_path, graphics_output_path
        )
        badge_graphics_generator.render_livery_badges()


