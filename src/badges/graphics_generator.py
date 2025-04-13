import os
from PIL import Image

import global_constants

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
