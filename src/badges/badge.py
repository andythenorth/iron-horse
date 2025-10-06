import global_constants
import utils
from utils import timing
from badges import _static_badges
from badges.graphics_generator import BadgeGraphicsGenerator


# could be @dataclass but eh
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

    @property
    def badges_in_table_order(self):
        # 1. badge display order in OpenTTD is *not* guaranteed (as of April 2025)....so just do a basic alpha sort for now
        # 2. alpha sort is better than default append order
        # 3. alpha also makes badge order in the generated nml easier to read for debugging
        return sorted(self, key=lambda badge: badge.label)

    def render_graphics(self, iron_horse, graphics_input_path, graphics_output_path):
        badge_graphics_generator = BadgeGraphicsGenerator(
            self, iron_horse, graphics_input_path, graphics_output_path
        )
        # badge sprites may also be available from OpenTTD for some common cases
        badge_graphics_generator.render_predrawn_livery_badges()
        badge_graphics_generator.render_generated_livery_badges()

    def produce_badges(self, **kwargs):
        # explicit, not on __init__, more controllable
        self.produce_badges_from_static_config(**kwargs)
        self.produce_grf_metadata_badges(**kwargs)
        self.produce_railtype_badges(**kwargs)
        self.produce_power_source_badges(**kwargs)
        self.produce_distributed_power_badges(**kwargs)
        self.produce_livery_badges(**kwargs)
        self.produce_vehicle_family_badges(**kwargs)
        self.produce_formation_ruleset_badges(**kwargs)
        self.produce_general_metadata_badges(**kwargs)
        self.produce_randomised_wagon_candidate_badges(**kwargs)
        self.produce_tech_tree_badges(**kwargs)
        self.produce_pantograph_display_badges(**kwargs)

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
        # these are really just an experiment to see if they aid debug, they don't do anything else as of April 2025, and `dumpinfo railtypes` gets the same result
        railtype_manager = kwargs["railtype_manager"]
        self.add_badge(
            label=f"ih_railtype",
        )
        for railtype in railtype_manager:
            self.add_badge(
                label=f"ih_railtype/{railtype.label}",
                flags=[
                    "BADGE_FLAG_COPY_TO_RELATED_ENTITY"
                ],  # !! doesn't appear to be copying to vehicle as of April 2025
            )

    def produce_vehicle_family_badges(self, **kwargs):
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            for catalogue in roster_manager.active_roster.catalogues:
                # vehicle_family_badge should always be found, just allow unhandled error if not
                self.add_badge(
                    label=catalogue.vehicle_family_badge,
                )

    def produce_randomised_wagon_candidate_badges(self, **kwargs):
        # this is for debug use
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            for catalogue in roster_manager.active_roster.catalogues:
                if catalogue.wagon_quacker.is_randomised_wagon_type:
                    for (
                        badge
                    ) in catalogue.example_model_variant.randomised_wagon_badges:
                        self.add_badge(
                            label=f"{badge}",
                        )

    def produce_power_source_badges(self, **kwargs):
        for power_source in global_constants.power_sources.keys():
            self.add_badge(
                label=f"power_source/{power_source.lower()}",
                name=f"STR_BADGE_POWER_SOURCE_{power_source}",
            )

    def produce_pantograph_display_badges(self, **kwargs):
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            for catalogue in roster_manager.active_roster.catalogues:
                for badge in catalogue.vehicle_family_pantograph_display_badges:
                    self.add_badge(
                        label=f"{badge}",
                    )

    def produce_distributed_power_badges(self, **kwargs):
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            for catalogue in roster_manager.active_roster.catalogues:
                for badge in catalogue.example_model_variant.distributed_power_badges:
                    self.add_badge(
                        label=f"{badge}",
                    )

    def produce_livery_badges(self, **kwargs):
        # this includes some badges which could strictly be static, but we group all livery concerns together in this method
        livery_supplier = kwargs["livery_supplier"]

        # we split the display/filter badge from the behaviour badges
        # as we want to consolidate some badges for display, but leave them split for behaviour (for example, random vs. non-random freight wagons of same hue)
        self.add_badge(
            label=f"livery",
            name="STR_BADGE_LIVERY",
        )
        for livery in livery_supplier.consolidated_liveries_for_badge_display:
            name = f"STR_BADGE_LIVERY_{livery.livery_name}"
            sprite = None
            if livery.is_freight_wagon_livery or livery.has_predrawn_badge_sprite:
                sprite = f"livery_{livery.livery_name.lower()}"
            self.add_badge(
                label=livery.display_and_filter_name_badge_label,
                sprite=sprite,
                name=name,
            )

        # copy elements of the livery_def into badges, for both behaviour and debugging
        self.add_badge(
            label=f"ih_livery_def/use_weathering/False",
        )
        self.add_badge(
            label=f"ih_livery_def/use_weathering/True",
        )

        # internal names, no consolidation across liveries
        for livery in livery_supplier.values():
            self.add_badge(livery.internal_name_badge_label)
        # colour sets
        for (
            colour_set_name
        ) in livery_supplier.freight_livery_colour_set_indexes_and_names:
            self.add_badge(
                label=f"ih_livery_def/colour_set_names/{colour_set_name}",
            )

    def produce_formation_ruleset_badges(self, **kwargs):
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            for catalogue in roster_manager.active_roster.catalogues:
                for badge in catalogue.example_model_variant.formation_ruleset_badges:
                    self.add_badge(f"{badge}")

    def produce_general_metadata_badges(self, **kwargs):
        # model variants not catalogues here, metadata can vary per model variant
        roster_manager = kwargs["roster_manager"]
        if roster_manager.active_roster is not None:
            for model_variant in roster_manager.active_roster.model_variants:
                for badge in model_variant.general_metadata_badges:
                    self.add_badge(f"{badge}")

    def produce_tech_tree_badges(self, **kwargs):
        # this is for debug use
        # gen is NOT part of the tech tree as of April 2025, decided it's a standalone item
        roster_manager = kwargs["roster_manager"]

        self.add_badge(label="ih_tech_tree")

        if roster_manager.active_roster is not None:
            for catalogue in roster_manager.active_roster.catalogues:
                for badge in catalogue.example_model_variant.tech_tree_badges:
                    self.add_badge(f"{badge}")
