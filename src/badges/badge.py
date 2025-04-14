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

    def render_graphics(self, iron_horse, graphics_input_path, graphics_output_path):
        badge_graphics_generator = BadgeGraphicsGenerator(
            self, iron_horse, graphics_input_path, graphics_output_path
        )
        badge_graphics_generator.render_livery_badges()

    def produce_badges(self, **kwargs):
        # explicit, not on __init__, more controllable
        self.produce_badges_from_static_config(**kwargs)
        self.produce_grf_metadata_badges(**kwargs)
        self.produce_railtype_badges(**kwargs)
        self.produce_power_source_badges(**kwargs)
        self.produce_livery_badges(**kwargs)
        self.produce_vehicle_family_badges(**kwargs)
        self.produce_formation_ruleset_badges(**kwargs)
        self.produce_randomised_wagon_candidate_badges(**kwargs)
        self.produce_tech_tree_badges(**kwargs)

    def produce_badges_from_static_config(self, **kwargs):
        # purely static badges
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

    def produce_grf_metadata_badges(self, **kwargs):
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            self.add_badge(
                f"newgrf/{utils.grfid_to_dword(roster_manager.active_roster.grfid)}"
            )

    def produce_railtype_badges(self, **kwargs):
        railtype_manager = kwargs["railtype_manager"]
        for railtype in railtype_manager:
            self.add_badge(
                label=f"ih_railtype/{railtype.label}",
                flags=["BADGE_FLAG_COPY_TO_RELATED_ENTITY"],
            )

    def produce_vehicle_family_badges(self, **kwargs):
        roster_manager = kwargs["roster_manager"]
        for roster in roster_manager:
            for catalogue in roster.catalogues:
                # vehicle_family_badge should always be found, just allow unhandled error if not
                self.add_badge(
                    label=catalogue.default_model_variant_from_roster.vehicle_family_badge,
                )

    def produce_randomised_wagon_candidate_badges(self, **kwargs):
        # this is for debug use
        roster_manager = kwargs["roster_manager"]
        for roster in roster_manager:
            for catalogue in roster.catalogues:
                if (
                    catalogue.default_model_variant_from_roster.catalogue_entry.model_is_randomised_wagon_type
                ):
                    # this is inherently inefficient as it walks ALL the candidates, but actually only needs one vehicle name for each vehicle_family_id
                    # but...probably fine as of April 2025 - the whole method timed at < 0.05s
                    for (
                        label,
                        name,
                    ) in (
                        catalogue.default_model_variant_from_roster.cabbage_wagon_randomisation_candidate_assortment_unique_names.items()
                    ):
                        self.add_badge(
                            label=f"ih_randomised_wagon/candidates/{label}",
                        )

    def produce_power_source_badges(self, **kwargs):
        for power_source in global_constants.power_sources.keys():
            self.add_badge(
                label=f"power_source/{power_source.lower()}",
                name=f"STR_BADGE_POWER_SOURCE_{power_source}",
            )

    def produce_livery_badges(self, **kwargs):
        # this includes some badges which could strictly be static, but we group all livery concerns together in this method
        livery_supplier = kwargs["livery_supplier"]

        self.add_badge(
            label=f"livery",
            name="STR_BADGE_LIVERY",
        )
        for livery in livery_supplier.values():
            name = f"STR_BADGE_LIVERY_{livery.livery_name}"
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
            )

    def produce_formation_ruleset_badges(self, **kwargs):
        self.add_badge(
            label=f"ih_formation_ruleset",
        )
        self.add_badge(
            label=f"ih_formation_ruleset/flags/report_as_pax_car",
        )
        self.add_badge(
            label=f"ih_formation_ruleset/flags/report_as_mail_car",
        )
        # these are for debug use
        roster_manager = kwargs["roster_manager"]
        for roster in roster_manager:
            for catalogue in roster.catalogues:
                if (
                    catalogue.default_model_variant_from_roster.gestalt_graphics.formation_ruleset is not None
                    ):
                    self.add_badge(f"ih_formation_ruleset/{catalogue.default_model_variant_from_roster.gestalt_graphics.formation_ruleset}")


    def produce_tech_tree_badges(self, **kwargs):
        # this is for debug use
        # gen is NOT part of the tech tree as of April 2025, decided it's a standalone item
        roster_manager = kwargs["roster_manager"]

        self.add_badge(label="ih_tech_tree")

        for roster in roster_manager:
            for catalogue in roster.catalogues:
                self.add_badge(
                    label=f"ih_tech_tree/subrole/{catalogue.default_model_variant_from_roster.subrole}"
                )
                self.add_badge(
                    label=f"ih_tech_tree/subrole_child_branch_num/{catalogue.default_model_variant_from_roster.subrole_child_branch_num}"
                )
                self.add_badge(
                    label=f"ih_tech_tree/joker/{catalogue.default_model_variant_from_roster.joker}"
                )
                self.add_badge(
                    label=f"ih_tech_tree/intro_year/{catalogue.default_model_variant_from_roster.intro_year}"
                )
                self.add_badge(
                    label=f"ih_tech_tree/intro_date_months_offset/{catalogue.default_model_variant_from_roster.intro_date_months_offset}"
                )

                if (
                    catalogue.default_model_variant_from_roster.replacement_model_variant
                    is not None
                ):
                    self.add_badge(
                        label=f"ih_tech_tree/replacement/{catalogue.default_model_variant_from_roster.replacement_model_variant.vehicle_family_badge}"
                    )
