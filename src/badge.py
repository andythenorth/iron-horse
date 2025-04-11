import os
from PIL import Image

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
        self.sprite = kwargs.get("sprite", None)


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
            label=f"ih_livery",
        )
        for livery in livery_supplier.values():
            sprite = None
            if livery.is_freight_wagon_livery:
                sprite = f"{livery.livery_name.lower()}"
            self.add_badge(
                label=f"ih_livery/{livery.livery_name.lower()}",
                sprite=sprite,
            )

        self.add_badge(
            label=f"freight_livery_colour_set_name",
            name=f"STR_BADGE_COLOUR_SET_NAME",
        )
        for (
            colour_set_name
        ) in livery_supplier.cabbage_valid_freight_livery_colour_set_names_and_nums:
            self.add_badge(
                label=f"freight_livery_colour_set_name/{colour_set_name}",
                name=f"STR_BADGE_COLOUR_SET_NAME_{colour_set_name.upper()}",
            )

    def render_graphics(self, iron_horse, graphics_input_path, graphics_output_path):
        badge_graphics_generator = BadgeGraphicsGenerator(
            self, iron_horse, graphics_input_path, graphics_output_path
        )
        badge_graphics_generator.render_livery_badges()


class BadgeGraphicsGenerator:
    """
    intended as a singleton
    didn't name it "Pipelines" because as of April 2025 it's just a set of self-contained methods, it doesn't have a full pipeline approach
    """

    def __init__(
        self, badge_manager, iron_horse, graphics_input_path, graphics_output_path
    ):
        self.badge_manager = badge_manager
        self.iron_horse = iron_horse
        self.graphics_input_path = graphics_input_path
        self.graphics_output_path = graphics_output_path
        self.badge_sprites_output_path = os.path.join(
            self.graphics_output_path, "badges"
        )
        # this should maybe be wrapped in an isolation method but eh, do it on init for now
        os.makedirs(self.badge_sprites_output_path, exist_ok=True)

    def render_livery_badges(self):

        # CABBAGE for now only livery badges
        livery_badge_spritesheet = Image.open(
            os.path.join(self.graphics_input_path, "badges", "cabbage_badge.png")
        )
        DOS_PALETTE = Image.open("palette_key.png").palette
        if "icc_profile" in livery_badge_spritesheet.info:
            livery_badge_spritesheet.info.pop("icc_profile")

        for (
            livery_name,
            livery,
        ) in self.iron_horse.livery_supplier.freight_wagon_liveries.items():
            output_path = os.path.join(
                self.badge_sprites_output_path,
                f"{livery.livery_name.lower()}.png",
            )
            # the dimensions of the spritesheet, with 10px padding around the actual sprite
            badge_spritesheet_dimensions = {"x": 34, "y": 32}

            x_offset = 30 * (len(livery.purchase_swatch) - 1)
            dest_image = livery_badge_spritesheet.copy().crop(
                box=(
                    x_offset,
                    0,
                    x_offset + badge_spritesheet_dimensions["x"],
                    badge_spritesheet_dimensions["y"],
                )
            )
            # possibly overkill, the input image should already be DOS palette, but eh, JFDI
            dest_image.putpalette(DOS_PALETTE)

            target_recolour_range_starting_indexes = [202, 84, 244, 215]

            target_recolour_map = {}

            for counter, colour_set_name in enumerate(livery.purchase_swatch):
                if colour_set_name == "company_colour":
                    continue

                if colour_set_name in ["complement_company_colour"]:
                    # just force to a brighter version of company colour 1
                    # this isn't strictly accurate, but visually gets the idea across ok
                    remap = 205
                else:
                    # take the first map name from the colour_set pair
                    colour_name = global_constants.colour_sets[colour_set_name][0]

                    if "COLOUR_" in colour_name:
                        # assume it's a default CC name constant
                        remap = global_constants.company_colour_maps[colour_name][4]
                    else:
                        remap = global_constants.custom_wagon_recolour_sprite_maps[
                            colour_name
                        ][4]

                target_recolour_map.update(
                    {target_recolour_range_starting_indexes[counter]: remap}
                )

            # *dont* do the point inside the loop, it leads to remapping of already-remapped colours
            dest_image = dest_image.point(
                lambda i: (
                    target_recolour_map[i] if i in target_recolour_map.keys() else i
                )
            )

            dest_image.save(output_path)
            dest_image.close()

        livery_badge_spritesheet.close()
