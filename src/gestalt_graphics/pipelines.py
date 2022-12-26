import os.path

currentdir = os.curdir

import filecmp
from PIL import Image, ImageOps

import polar_fox
from polar_fox.graphics_units import (
    SimpleRecolour,
    AppendToSpritesheet,
    AddCargoLabel,
    AddBuyMenuSprite,
    TransposeAsymmetricSprites,
)
import polar_fox.pixa as pixa
from polar_fox.pixa import Spritesheet, PieceCargoSprites
from gestalt_graphics import graphics_constants

DOS_PALETTE = Image.open("palette_key.png").palette

"""
Pipelines can be dedicated to a single task such as SimpleRecolourPipeline
Or they can compose units for more complicated tasks, such as colouring and loading a specific vehicle type
"""


class Pipeline(object):
    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        # actually, there's nothing to do eh :P
        pass

    @property
    def vehicle_source_input_path(self):
        # convenience method to get the vehicle template image
        # I considered having this return the Image, not just the path, but it's not saving much, and is less obvious what it does when used
        return os.path.join(
            currentdir,
            "src",
            "graphics",
            self.consist.roster_id,
            self.consist.id + ".png",
        )

    @property
    def chassis_input_path(self):
        # convenience method to get the path for the chassis image
        return os.path.join(
            currentdir, "src", "graphics", "chassis", self.vehicle_unit.chassis + ".png"
        )

    @property
    def roof_input_path(self):
        # convenience method to get the path for the roof image
        return os.path.join(
            currentdir, "src", "graphics", "roofs", self.vehicle_unit.roof + ".png"
        )

    def process_buy_menu_sprite(self, spritesheet):
        # this function is passed (uncalled) into the pipeline, and then called at render time
        # this is so that it has the processed spritesheet available, which is essential for creating buy menu sprites
        # n.b if buy menu sprite processing has conditions by vehicle type, could pass a dedicated function for each type of processing

        # hard-coded positions for buy menu sprite (if used - it's optional)
        x_offset = 0
        # !! this appears to work, but the implementation is stupidly broken
        # it has legacy handling relating to company colour based liveries
        # it has handling for buyable variants
        # it has handling for repeating units
        # it has handling for non-reperating units
        # it has handling for special cases by gestalt
        # !! it appears to sometimes generate twice the amount of buy menu sprite as required (see Peasweep) - this relates to repeating over the units and unit_variants
        for unit_counter, unit in enumerate(self.consist.units):
            for unit_variant_counter, unit_variant in enumerate(unit.unit_variants):
                # !! currently no cap on purchase menu sprite width
                # !! consist has a buy_menu_width prop which caps to 64 which could be used (+1px overlap)
                unit_length_in_pixels = 4 * unit.vehicle_length
                # this is jank because some articulated consists with fancy rulesets need to flip some vehicles
                # this is probably pretty fragile, but eh, JFDI
                ruleset_offset_num_rows_jank = 0
                if getattr(self.consist.gestalt_graphics, "consist_ruleset", None) in [
                    "metro"
                ]:
                    if unit_counter % 2 != 0:
                        ruleset_offset_num_rows_jank = 2  # hard-coded to metro currently
                if getattr(self.consist.gestalt_graphics, "consist_ruleset", None) in [
                    "articulated_permanent_twin_sets"
                ]:
                    # hard-coded to twin articulated automobile carriers currently
                    # offset for 2nd unit to skip mask
                    if unit_counter == 1:
                        ruleset_offset_num_rows_jank = 1
                # additional_liveries jank for engines eh
                spriterows_per_livery = 0 # this is so broken, and is needed to make certain consists work
                if len(self.consist.gestalt_graphics.all_liveries) > 1:
                    # !! massive JFDI hax to make this work - really the gestalt should know how many rows are consumed per livery
                    if (
                        self.consist.gestalt_graphics.__class__.__name__
                        == "GestaltGraphicsConsistPositionDependent"
                    ):
                        spriterows_per_livery = 2
                    else:
                        spriterows_per_livery = 1
                ruleset_offset_num_rows_jank = unit_counter * spriterows_per_livery
                unit_spriterow_offset = (
                    unit.spriterow_num + ruleset_offset_num_rows_jank
                ) * graphics_constants.spriterow_height
                for cc_livery_counter, cc_livery in enumerate(
                    getattr(self.consist.gestalt_graphics, "all_liveries", ["default"])
                ):
                    crop_box_src = (
                        224,
                        10 + unit_spriterow_offset + (cc_livery_counter * 30 * spriterows_per_livery),
                        224
                        + unit_length_in_pixels
                        + 1,  # allow for 1px coupler / corrider overhang
                        26 + unit_spriterow_offset + (cc_livery_counter * 30 * spriterows_per_livery),
                    )
                    crop_box_dest = (
                        360 + x_offset,
                        10 + (cc_livery_counter * 30 * spriterows_per_livery),
                        360
                        + x_offset
                        + unit_length_in_pixels
                        + 1,  # allow for 1px coupler / corrider overhang
                        26 + (cc_livery_counter * 30 * spriterows_per_livery),
                    )
                    custom_buy_menu_sprite = spritesheet.sprites.copy().crop(crop_box_src)
                    spritesheet.sprites.paste(custom_buy_menu_sprite, crop_box_dest)
                    # increment x offset for pasting in next vehicle
                x_offset += unit_length_in_pixels
        return spritesheet

    def render_common(
        self,
        input_image,
        units,
        output_base_name=None,
        output_suffix="",
    ):
        # expects to be passed a PIL Image object
        # units is a list of objects, with their config data already baked in (don't have to pass anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        if output_base_name is None:
            # default to consist name for file name, but can over-ride for e.g. containers by passing something in
            output_base_name = self.consist.id
        output_path = os.path.join(
            self.graphics_output_path,
            output_base_name + output_suffix + ".png",
        )
        # we put the class name into the tmp output to
        # (1) avoid clashes where file already exists with > 1 pipelines
        # (2) aids debugging - can see explicit output from each pipeline
        output_path_tmp = os.path.join(
            self.graphics_output_path,
            "tmp",
            output_base_name + output_suffix + "." + self.__class__.__name__ + ".png",
        )
        spritesheet = pixa.make_spritesheet_from_image(input_image, DOS_PALETTE)

        for unit in units:
            spritesheet = unit.render(spritesheet)
        # I don't normally leave commented-out code behind, but I'm bored of looking in the PIL docs for how to show the image during compile
        # if self.consist.id == 'velaro_thing':
        # spritesheet.sprites.show()

        # save a tmp file first and compare to existing file (if any)
        # this prevents destroying the nmlc sprite cache with every graphics run by needlessly replacing the files
        if os.path.exists(output_path_tmp):
            # tmp path should not exist, if it does we either have
            # - the same filename being written more than once, in multiprocessing pool, which suggests duplicates in some list of items to be rendered
            # - artefacts from a previous failed compile
            # either way, raise, because this was a previous source of intermittent compile failures
            # - problem in 2021 was tmp file being deleted by one pool worker whilst another pool worker was still trying to work with it
            # - that is solved structurally since Jun 2022 by writing to a tmp dir managed by render_graphics, and not deleting the file directly after the comparison
            raise (BaseException("Exists:", output_path_tmp))
        if os.path.exists(output_path):
            # save tmp file
            spritesheet.save(output_path_tmp)
            if not filecmp.cmp(output_path, output_path_tmp):
                # print("replacing", output_path) # comment this in / out as needed, generally it's a bit noisy to leave in
                spritesheet.save(output_path)
            # we don't remove the tmp output files here, they don't do any harm, and the entire dir is removed by render_graphics when appropriate
        else:
            spritesheet.save(output_path)

    def render(self, consist, graphics_output_path):
        raise NotImplementedError("Implement me in %s" % repr(self))


class PassThroughPipeline(Pipeline):
    """
    Solely opens the input image and saves it, when there's no processing, but we need to copy the spritesheet file to generated graphics dir.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def render(self, consist, global_constants, graphics_output_path):
        self.units = []
        self.consist = consist
        self.graphics_output_path = graphics_output_path

        input_image = Image.open(self.vehicle_source_input_path)
        self.render_common(input_image, self.units)
        input_image.close()


class GenerateSpritelayerCargoSets(Pipeline):
    """
    Creates a spritesheet with a set of composited cargos for use on a dedicated spritelayer.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def resolve_template_name(self, variant):
        # figure out which template png to use based on gestalt length + cargo pattern
        # - e.g. 32px_40_20, 32px_20_20_20 etc?
        result = [str(self.spritelayer_cargo.length) + "px"]
        # cargo items measured in 'feet', due to their origin with intermodal containers
        # 'feet' does not have to be realistic, but an 8/8 wagon fits 60 foot-length of cargo sprites
        # the value is picked out from the cargo sprite filenames, which must conform to the correct pattern
        for container in variant:
            result.append(container.split("_foot")[0][-2:])
        return (
            self.spritelayer_cargo.base_id
            + "_template_"
            + self.spritelayer_cargo_set.graphics_template_subtype_name
            + "_"
            + "_".join(result)
        )

    def add_cargo_spriterows(self):
        for variant in self.spritelayer_cargo_set.variants:
            template_path = os.path.join(
                currentdir,
                "src",
                "graphics",
                "cargo_templates",
                self.resolve_template_name(variant) + ".png",
            )
            template_image = Image.open(template_path)

            # get the loc points and sort them for display
            # !! loc points might need extended to support double stack ??
            loc_points = [
                (pixel[0], pixel[1] - 10, pixel[2])
                for pixel in pixa.pixascan(template_image)
                if pixel[2] in [226, 240, 244]
            ]
            loc_points_grouped_and_sorted_for_display = {}
            for angle_index, bbox in enumerate(
                self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed
            ):
                pixels = []
                for pixel in loc_points:
                    if pixel[0] >= bbox[0] and pixel[0] <= (bbox[0] + bbox[1]):
                        pixels.append(pixel)
                        # catch invalid pixels
                        if (1 + [226, 240, 244].index(pixel[2])) > len(variant):
                            message = template_path
                            message += (
                                " contains pixel colour "
                                + str(pixel[2])
                                + " which implies "
                                + str(1 + [226, 240, 244].index(pixel[2]))
                                + " cargo sprites"
                            )
                            message += (
                                " but the variant only defines "
                                + str(len(variant))
                                + " cargo sprite(s)"
                            )
                            raise ValueError(message)
                # fake sprite sorter - cargo sprites nearer front need to overlap cargo sprites behind
                # position pixel colour indexes (in the palette) must be in ascending order for left->right positions in <- view
                # required index colours are 226, 240, 244
                # the fake sprite sorter then just sorts ascending or descending as required for each angle
                # !! double stack might be possible to handle just using this rudimentary sprite sorting ?? (or extending it??)
                pixels = sorted(pixels, key=lambda pixel: pixel[2])
                if angle_index in [3, 4, 5]:
                    pixels.reverse()
                loc_points_grouped_and_sorted_for_display[angle_index] = pixels

            # get all cargo sprites for this variant, and put them in a single structure
            # n.b the implementation of this is likely inefficient as it will repetively open the same cargo sprites from the filesystem,
            # but so far that seems to have negligible performance cost, and caching all cargo sprites earlier in the loop would add unwanted complexity
            cargos_for_this_variant = []
            for cargo_item in variant:
                cargo_item_path = os.path.join(
                    currentdir,
                    "src",
                    "polar_fox",
                    "graphics",
                    self.spritelayer_cargo.base_id,
                    cargo_item + ".png",
                )
                cargo_item_image = Image.open(cargo_item_path)

                # if self.spritelayer_cargo.id == 'intermodal_box_32px':
                # cargo_item_image.show()
                bboxes = []
                # only a 3 tuple in global constants bounding box definitions (no y position), we need a 4 tuple inc. y position
                # also the format of bounding boxes needs converted to PIL crop box format
                for (
                    bbox
                ) in (
                    self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed
                ):
                    bboxes.append([bbox[0], 10, bbox[0] + bbox[1], 10 + bbox[2]])

                cargo_sprites = pixa.get_arbitrary_angles(cargo_item_image, bboxes)
                if (
                    self.spritelayer_cargo.gestalt_graphics.cargo_sprites_are_asymmetric
                    == False
                ):
                    # if cargo item sprites are symmetric (e.g. containers), angles 0-3 need to be copied from angles 4-7
                    for i in range(4):
                        cargo_sprites[i] = cargo_sprites[i + 4]

                # if self.spritelayer_cargo.id == 'intermodal_box_32px':
                # cargo_sprites[0][0].show()

                cargos_for_this_variant.append((cargo_item, cargo_sprites))

            variant_output_image = Image.open(
                os.path.join(currentdir, "src", "graphics", "spriterow_template.png")
            )
            variant_output_image = variant_output_image.copy().crop(
                (
                    0,
                    10,
                    graphics_constants.spritesheet_width,
                    10 + graphics_constants.spriterow_height,
                )
            )
            floor_height_yoffset = self.spritelayer_cargo.floor_height_for_platform_type

            for (
                angle_index,
                pixels,
            ) in loc_points_grouped_and_sorted_for_display.items():
                for pixel in pixels:
                    # use the pixel colour to look up which cargo_item sprites to use, relies on hard-coded pixel colours
                    # print(self.spritelayer_cargo.id, variant, angle_index, pixels, cargos_for_this_variant)
                    cargo_item_for_this_loc_point = cargos_for_this_variant[
                        [226, 240, 244].index(pixel[2])
                    ]  # one line python stupidity
                    cargo_sprites = cargo_item_for_this_loc_point[1]
                    cargo_sprite_width = cargo_sprites[angle_index][0].size[0]
                    cargo_sprite_height = cargo_sprites[angle_index][0].size[1]
                    # loc_point_y_transform then moves the loc point to the left-most corner of the cargo sprite
                    # this makes it easier to place the loc point pixels in the templates
                    # !! these might need splitting up by spritelayer_cargo for different types of sprites, depending on their shape
                    # !! if self.spritelayer_cargo.base_id == "intermodal_containers":
                    loc_point_y_transforms = {
                        "15": [1, 3, 1, 2, 1, 3, 1, 2],  # !! untested, may be incorrect
                        "20": [1, 3, 1, 2, 1, 3, 1, 2],
                        "30": [1, 3, 1, 3, 1, 3, 1, 3],
                        "40": [1, 3, 1, 4, 1, 3, 1, 4],
                    }
                    container_foot_length = cargo_item_for_this_loc_point[0].split(
                        "_foot"
                    )[0][
                        -2:
                    ]  # extra special way to slice the length out of the name :P
                    loc_point_y_transform = loc_point_y_transforms[
                        container_foot_length
                    ][angle_index]
                    # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
                    cargo_sprite_bounding_box = (
                        pixel[0],
                        pixel[1]
                        - cargo_sprite_height
                        + loc_point_y_transform
                        + floor_height_yoffset,
                        pixel[0] + cargo_sprite_width,
                        pixel[1] + loc_point_y_transform + floor_height_yoffset,
                    )

                    variant_output_image.paste(
                        cargo_sprites[angle_index][0],
                        cargo_sprite_bounding_box,
                        cargo_sprites[angle_index][1],
                    )

            if self.spritelayer_cargo.provide_container_shadows:
                # create a mask to place black shadows between adjacent containers
                combo_check = ["empty" if "empty" in i else "occupied" for i in variant]
                # *vehicles with 3 containers only (32px)*
                # don't allow combinations of only two adjacent 20 foot containers as it's TMWFTLB to provide the shadow for them
                # two 20 foot with a gap between are supported
                # solitary 20 foot containers of any length in any position are not prevented, but look bad (looks like loading didn't finish)
                if len(combo_check) == 3:
                    if combo_check in [
                        ["occupied", "occupied", "empty"],
                        ["empty", "occupied", "occupied"],
                    ]:
                        raise ValueError(
                            self.spritelayer_cargo_set.id
                            + " - this pattern of (20 foot) containers isn't supported (can't composite shadows for it): "
                            + str(combo_check)
                        )

                # don't draw shadows if there are empty slots
                if combo_check.count("empty") == 0:
                    shadow_image = template_image.copy().crop(
                        (
                            0,
                            10 - floor_height_yoffset,
                            self.global_constants.sprites_max_x_extent,
                            10
                            + graphics_constants.spriterow_height
                            - floor_height_yoffset,
                        )
                    )
                    shadow_mask = shadow_image.copy()
                    shadow_mask = shadow_mask.point(
                        lambda i: 255 if i == 1 else 0
                    ).convert(
                        "1"
                    )  # assume shadow is always colour index 1 in the palette
                    variant_output_image.paste(shadow_image, mask=shadow_mask)

            # if self.spritelayer_cargo.id == 'intermodal_box_32px':
            # variant_output_image.show()
            variant_spritesheet = pixa.make_spritesheet_from_image(
                variant_output_image, DOS_PALETTE
            )
            crop_box_dest = (
                0,
                0,
                self.global_constants.sprites_max_x_extent,
                graphics_constants.spriterow_height,
            )
            self.units.append(AppendToSpritesheet(variant_spritesheet, crop_box_dest))
            variant_output_image.close()
            template_image.close()

    def render(
        self, spritelayer_cargo_set_pair, global_constants, graphics_output_path
    ):
        self.units = []
        self.spritelayer_cargo = spritelayer_cargo_set_pair[0]
        self.spritelayer_cargo_set = spritelayer_cargo_set_pair[1]
        self.global_constants = global_constants
        self.graphics_output_path = graphics_output_path

        self.add_cargo_spriterows()

        # for this pipeline, input_image is just blank white 10px high image, to which the vehicle sprites are then appended
        input_image = Image.new("P", (graphics_constants.spritesheet_width, 10), 255)
        input_image.putpalette(DOS_PALETTE)
        self.render_common(
            input_image,
            self.units,
            output_base_name=self.spritelayer_cargo_set.id(self.spritelayer_cargo),
        )


class CheckBuyMenuOnlyPipeline(Pipeline):
    """
    Opens the input image, inserts a custom buy menu if required, then saves with no other changes.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def render(self, consist, global_constants, graphics_output_path):
        self.units = []
        self.consist = consist
        self.graphics_output_path = graphics_output_path

        if self.consist.buy_menu_x_loc == 360:
            # !! this currently will cause the vehicle spritesheet buy menu sprites to be copied to the pans spritesheet,
            # !! it needs pixels from the pans spritesheet, but automated buy menu sprites need providing first
            self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        input_image = Image.open(self.vehicle_source_input_path)
        self.render_common(input_image, self.units)
        input_image.close()


class GenerateEmptySpritesheet(Pipeline):
    """
    Trivial generation of an empty spritesheet (with bounding boxes), which will then be used in following pipelines.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def render(self, consist, global_constants, graphics_output_path):
        self.units = []
        self.consist = consist
        self.graphics_output_path = graphics_output_path

        empty_spriterow_image = Image.open(
            os.path.join(currentdir, "src", "graphics", "spriterow_template.png")
        )

        self.render_common(empty_spriterow_image, self.units)
        empty_spriterow_image.close()


class GenerateBuyMenuSpriteFromRandomisationCandidatesPipeline(Pipeline):
    """
    Creates a custom buy menu composed from the randomisation candidates for this wagon, then saves with no other changes.
    Possibly this could have been a unit not a pipeline, but eh.
    This way was marginally easier to integrate.
    Also keeps a clean separation between the generation of the vehicle sprites and the fancy buy menu sprite.
    Potato / potato.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def process_buy_menu_sprite_from_randomisation_candidates(self, spritesheet):
        # this function is passed (uncalled) into the pipeline, and then called at render time

        # take the first and last candidates;
        # note that we have to call set here, due to the way random candidates are padded out to make power of 2 list lengths for random bits
        # we have to use frozen_roster_items as the roster object won't pickle for multiprocessing use (never figured out why)
        if len(self.consist.units) > 1:
            raise BaseException(
                "GenerateBuyMenuSpriteFromRandomisationCandidatesPipeline won't work with articulated consists - called by "
                + self.consist.id
            )
        unit_length_in_pixels = 4 * self.consist.units[0].vehicle_length
        unit_slice_length_in_pixels = (
            int(unit_length_in_pixels / 2)
            + graphics_constants.randomised_wagon_extra_unit_width
        )
        dice_image_width = graphics_constants.dice_image_width
        dice_image_height = 16
        fade_image_width = 2
        fade_image_height = 16

        # I tried doing fancy generic counter maths for offsets etc, but it got stupid, just hard-code everything, there are only 2 wagon parts to draw
        slice_configuration = [
            dict(
                x_offset_src=0,
                x_offset_dest=unit_slice_length_in_pixels + dice_image_width + 1,
            ),
            dict(
                x_offset_src=int(unit_length_in_pixels - unit_slice_length_in_pixels),
                x_offset_dest=0,
            ),
        ]
        for (
            spriterow_num_dest,
            source_data,
        ) in self.consist.gestalt_graphics.buy_menu_sprite_variants(
            self.consist
        ).items():
            for counter, (source_vehicle, spriterow_num_src) in enumerate(source_data):
                # note that we want the *generated* source wagon spritesheet
                source_vehicle_input_path = os.path.join(
                    self.graphics_output_path,
                    source_vehicle.id + ".png",
                )
                source_vehicle_image = Image.open(source_vehicle_input_path)
                if self.consist.id == "randomised_box_car_pony_gen_1A":
                    # source_vehicle_image.show()
                    pass
                y_offset_src = spriterow_num_src * graphics_constants.spriterow_height
                y_offset_dest = spriterow_num_dest * graphics_constants.spriterow_height
                crop_box_src = (
                    224 + slice_configuration[counter]["x_offset_src"],
                    10 + y_offset_src,
                    224
                    + slice_configuration[counter]["x_offset_src"]
                    + unit_slice_length_in_pixels
                    + 1,  # allow for 1px coupler / corrider overhang
                    26 + y_offset_src,
                )
                crop_box_dest = (
                    360 + slice_configuration[counter]["x_offset_dest"],
                    10 + y_offset_dest,
                    360
                    + slice_configuration[counter]["x_offset_dest"]
                    + unit_slice_length_in_pixels
                    + 1,  # allow for 1px coupler / corrider overhang
                    26 + y_offset_dest,
                )
                custom_buy_menu_sprite = source_vehicle_image.crop(crop_box_src)
                spritesheet.sprites.paste(custom_buy_menu_sprite, crop_box_dest)

            dice_image = Image.open(
                os.path.join(
                    currentdir, "src", "graphics", "randomised_wagon_overlay.png"
                )
            ).crop((10, 10, 10 + dice_image_width, 10 + dice_image_height))
            dice_recolour_maps = {
                1: [
                    {170: 1, 171: 2, 188: 9, 51: 12, 69: 15, 226: 9},
                    {170: 181, 171: 182, 188: 9, 51: 12, 69: 15, 226: 9},
                ],
                2: [
                    {170: 1, 171: 2, 188: 188, 51: 51, 69: 69, 226: 188},
                    {170: 14, 171: 15, 188: 64, 51: 65, 69: 189, 226: 188},
                ],
                3: [
                    {170: 1, 171: 2, 188: 45, 51: 47, 69: 49, 226: 45},
                    {170: 14, 171: 15, 188: 182, 51: 164, 69: 165, 226: 45},
                ],
            }
            # the consist gen % 2 is to alternate the overlay colour between generations, to aid distinguising them when replacing vehicles
            dice_recolour_map = dice_recolour_maps[
                self.consist.gestalt_graphics.dice_colour
            ][self.consist.gen % 2]
            dice_image = dice_image.point(
                lambda i: dice_recolour_map[i] if i in dice_recolour_map.keys() else i
            )
            x_offset_dest = unit_slice_length_in_pixels + 1
            crop_box_dest = (
                360 + x_offset_dest,
                10 + y_offset_dest,
                360 + x_offset_dest + dice_image_width,
                10 + y_offset_dest + dice_image_height,
            )
            spritesheet.sprites.paste(dice_image, crop_box_dest)

            fade_image = Image.open(
                os.path.join(
                    currentdir, "src", "graphics", "randomised_wagon_overlay.png"
                )
            ).crop((10, 30, 10 + fade_image_width, 30 + fade_image_height))
            # create a mask so that we paste only the overlay pixels (no blue pixels)
            fade_image_mask = fade_image.copy()
            fade_image_mask = fade_image_mask.point(
                lambda i: 0 if i == 226 else 255
            ).convert("1")
            for counter in range(2):
                x_offset_dest = counter * (
                    (2 * unit_slice_length_in_pixels) + dice_image_width
                )
                crop_box_dest = (
                    360 + x_offset_dest,
                    10 + y_offset_dest,
                    360 + x_offset_dest + fade_image_width,
                    10 + y_offset_dest + dice_image_height,
                )
                spritesheet.sprites.paste(fade_image, crop_box_dest, fade_image_mask)
                # flip the image for the next time we paste it (this creates a better symmetry at each side of the image)
                fade_image = ImageOps.mirror(fade_image)
                fade_image_mask = ImageOps.mirror(fade_image_mask)

        if self.consist.id == "randomised_box_car_pony_gen_5B":
            # spritesheet.sprites.show()
            pass

        return spritesheet

    def render(self, consist, global_constants, graphics_output_path):
        self.units = []
        self.consist = consist
        self.graphics_output_path = graphics_output_path

        self.units.append(
            AddBuyMenuSprite(self.process_buy_menu_sprite_from_randomisation_candidates)
        )

        # note that this comes from generated/graphics/[grf-name]/, and expects to find an appropriate generated spritesheet in that location
        spritesheet_image = Image.open(
            os.path.join(self.graphics_output_path, self.consist.id + ".png")
        )

        self.render_common(spritesheet_image, self.units)
        spritesheet_image.close()


class GeneratePantographsSpritesheetPipeline(Pipeline):
    """
    Adds additional spritesheets for pantographs (up and down), which are provided in the grf as sprite layers.
    Whilst this is not a common use case, when it's needed, it's needed.
    Similar approach can be used for anything else provided in sprite layers.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def add_pantograph_spriterows(self):
        # !! this will eventually need extending for articulated vehicles
        # !! that can be done by weaving in a repeat over units, to draw multiple pantograph blocks, using the same pattern as the vehicle Spritesheet
        # !! the spriteset templates should then match the main vehicle, just changing path

        pantograph_input_images = {
            "diamond-single": "diamond.png",
            "diamond-double": "diamond.png",
            "diamond-single-with-base": "diamond-with-base.png",
            "z-shaped-single": "z-shaped.png",
            "z-shaped-double": "z-shaped.png",
            "z-shaped-single-reversed": "z-shaped-reversed.png",
            "z-shaped-single-with-base": "z-shaped-with-base.png",
        }
        pantograph_input_path = os.path.join(
            currentdir,
            "src",
            "graphics",
            "pantographs",
            pantograph_input_images[self.consist.pantograph_type],
        )
        pantograph_input_image = Image.open(pantograph_input_path)

        bboxes = []
        # only a 3 tuple in global constants bounding box definitions (no y position), we need a 4 tuple inc. y position
        # also the format of bounding boxes needs converted to PIL crop box format
        for yoffset in (10, 40):
            for (
                bbox
            ) in self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed:
                bboxes.append([bbox[0], yoffset, bbox[0] + bbox[1], yoffset + bbox[2]])

        pantograph_sprites = pixa.get_arbitrary_angles(pantograph_input_image, bboxes)
        # needs to slice out A down, A up, B down, B up, depending on type
        # but B is probably just A reversed
        # so two spriterows is enough: down, up
        # two colours of loc pixel, for A and B positions
        spriterow_pantograph_state_maps = {
            "diamond-single": {"down": ["a"], "up": ["A"]},
            "diamond-double": {
                "down": ["a", "a"],
                "up": ["A", "A"],
            },  # A and B functionally identical here, so just use A
            "diamond-single-with-base": {"down": ["a"], "up": ["A"]},
            "z-shaped-single": {"down": ["a"], "up": ["A"]},
            "z-shaped-single-reversed": {"down": ["a"], "up": ["A"]},
            "z-shaped-double": {
                "down": ["a", "b"],
                "up": ["A", "b"],
            },  # aB was tried and removed, TMWFTLB, instead just use Ab and respect depot flip
            "z-shaped-single-with-base": {"down": ["a"], "up": ["A"]},
        }
        pantograph_state_sprite_map = {
            "a": [
                pantograph_sprites[0],
                pantograph_sprites[1],
                pantograph_sprites[2],
                pantograph_sprites[3],
                pantograph_sprites[4],
                pantograph_sprites[5],
                pantograph_sprites[6],
                pantograph_sprites[7],
            ],
            "A": [
                pantograph_sprites[8],
                pantograph_sprites[9],
                pantograph_sprites[10],
                pantograph_sprites[11],
                pantograph_sprites[12],
                pantograph_sprites[13],
                pantograph_sprites[14],
                pantograph_sprites[15],
            ],
            "b": [
                pantograph_sprites[4],
                pantograph_sprites[5],
                pantograph_sprites[6],
                pantograph_sprites[7],
                pantograph_sprites[0],
                pantograph_sprites[1],
                pantograph_sprites[2],
                pantograph_sprites[3],
            ],
            "B": [
                pantograph_sprites[12],
                pantograph_sprites[13],
                pantograph_sprites[14],
                pantograph_sprites[15],
                pantograph_sprites[8],
                pantograph_sprites[9],
                pantograph_sprites[10],
                pantograph_sprites[11],
            ],
        }

        vehicle_input_image = Image.open(self.vehicle_source_input_path)
        # get the loc points
        loc_points = [
            (pixel[0], pixel[1], pixel[2])
            for pixel in pixa.pixascan(vehicle_input_image)
            if pixel[2] == 226 or pixel[2] == 164
        ]
        # loc points are in arbitrary row in source spritesheet but need to be moved up in output, so shift the y offset by the required amount
        loc_points = [
            (
                pixel[0],
                pixel[1] - (self.consist.gestalt_graphics.num_pantograph_rows * graphics_constants.spriterow_height),
                pixel[2],
            )
            for pixel in loc_points
        ]
        # sort them in y order, this causes sprites to overlap correctly when there are multiple loc points for an angle
        loc_points = sorted(loc_points, key=lambda x: x[1])

        empty_spriterow_image = Image.open(
            os.path.join(currentdir, "src", "graphics", "spriterow_template.png")
        )
        empty_spriterow_image = empty_spriterow_image.crop(
            (
                0,
                10,
                graphics_constants.spritesheet_width,
                10 + graphics_constants.spriterow_height,
            )
        )
        # empty_spriterow_image.show()

        # create the empty spritesheet to paste into; in some cases this creates redundant spriterows, but it's fine
        pantograph_output_image = Image.new(
            "P",
            (
                graphics_constants.spritesheet_width,
                (2 * self.consist.gestalt_graphics.num_pantograph_rows * graphics_constants.spriterow_height) + 10,
            ),
            255,
        )
        pantograph_output_image.putpalette(DOS_PALETTE)
        for i in range(self.consist.gestalt_graphics.num_pantograph_rows + 1):
            pantograph_output_image.paste(
                empty_spriterow_image,
                (0, 10 + (i * graphics_constants.spriterow_height)),
            )

        state_map = spriterow_pantograph_state_maps[self.consist.pantograph_type][
            self.pantograph_state
        ]
        for pixel in loc_points:
            angle_num = 0
            for counter, bbox in enumerate(
                self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed
            ):
                if pixel[0] >= bbox[0]:
                    angle_num = counter
            pantograph_sprite_num = angle_num

            pantograph_width = pantograph_sprites[pantograph_sprite_num][0].size[0]
            pantograph_height = pantograph_sprites[pantograph_sprite_num][0].size[1]
            # the +1s for height adjust the crop box to include the loc point
            # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
            pantograph_bounding_box = (
                pixel[0],
                pixel[1] - pantograph_height + 1,
                pixel[0] + pantograph_width,
                pixel[1] + 1,
            )
            if pixel[2] == 164:
                # it's b or B
                state_sprites = pantograph_state_sprite_map[state_map[1]]
            else:
                # it's a or A
                state_sprites = pantograph_state_sprite_map[state_map[0]]
            pantograph_output_image.paste(
                state_sprites[pantograph_sprite_num][0],
                pantograph_bounding_box,
                state_sprites[pantograph_sprite_num][1],
            )

        # add debug sprites with vehicle-pantograph comp for ease of checking
        # this very much assumes that the vehicle image has been generated, which holds currently due to the order pipelines are run in (and are in series)
        vehicle_debug_image = Image.open(
            os.path.join(self.graphics_output_path, self.consist.id + ".png")
        )
        vehicle_debug_image = vehicle_debug_image.copy().crop(
            (
                0,
                10,
                graphics_constants.spritesheet_width,
                10 + graphics_constants.spriterow_height,
            )
        )
        pantograph_output_image.paste(
            vehicle_debug_image,
            (0, 10 + (self.consist.gestalt_graphics.num_pantograph_rows * graphics_constants.spriterow_height)),
        )
        pantograph_debug_image = pantograph_output_image.copy().crop(
            (
                0,
                10,
                graphics_constants.spritesheet_width,
                10 + graphics_constants.spriterow_height,
            )
        )
        pantograph_debug_mask = pantograph_debug_image.copy()
        pantograph_debug_mask = pantograph_debug_mask.point(
            lambda i: 0 if i == 255 or i == 0 else 255
        ).convert(
            "1"
        )  # the inversion here of blue and white looks a bit odd, but potato / potato
        pantograph_output_image.paste(
            pantograph_debug_image,
            (0, 10 + (self.consist.gestalt_graphics.num_pantograph_rows * graphics_constants.spriterow_height)),
            pantograph_debug_mask,
        )

        # make spritesheet
        pantograph_spritesheet = pixa.make_spritesheet_from_image(
            pantograph_output_image, DOS_PALETTE
        )
        crop_box_dest = (
            0,
            10,
            self.global_constants.sprites_max_x_extent,
            10 + (2 * self.consist.gestalt_graphics.num_pantograph_rows * graphics_constants.spriterow_height),
        )
        self.units.append(AppendToSpritesheet(pantograph_spritesheet, crop_box_dest))
        pantograph_input_image.close()
        vehicle_input_image.close()
        empty_spriterow_image.close()

    def render(self, consist, global_constants, graphics_output_path):
        self.units = []
        self.consist = consist
        self.global_constants = global_constants
        self.graphics_output_path = graphics_output_path

        self.add_pantograph_spriterows()

        if self.consist.buy_menu_x_loc == 360:
            self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        # this will render a spritesheet with an additional suffix, separate from the vehicle spritesheet
        input_image = Image.open(self.vehicle_source_input_path).crop(
            (0, 0, graphics_constants.spritesheet_width, 10)
        )
        output_suffix = "_pantographs_" + self.pantograph_state
        self.render_common(input_image, self.units, output_suffix=output_suffix)
        input_image.close()


class GeneratePantographsUpSpritesheetPipeline(GeneratePantographsSpritesheetPipeline):
    """Sparse subclass, solely to set pan 'up' state (simplest way to implement this)."""

    pantograph_state = "up"  # lol, actually valid class vars

    def __init__(self):
        super().__init__()


class GeneratePantographsDownSpritesheetPipeline(
    GeneratePantographsSpritesheetPipeline
):
    """Sparse subclass, solely to set pan 'down' state (simplest way to implement this)."""

    pantograph_state = "down"  # lol, actually valid class vars

    def __init__(self):
        super().__init__()


class ExtendSpriterowsForCompositedSpritesPipeline(Pipeline):
    """ "
    Extends a spritesheet with variations on vehicle graphics, liveries, cargos etc.
    Copied from Road Hog where it became convoluted to handle many cases.
    Not easy to simplify, generating graphics has many facets.
    Individual methods handle specific compositing tasks.
    == Commentary ==
    Arguably there is some structural entity missing, between pipeline and unit.
    The methods maybe do too much without being encapsulated.
    Maybe a UnitConfig or something.
    But it seems to work ok.
    And I can read it.
    Which matters.
    So eh.
    """

    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        # initing things here is proven to have unexpected results, as the processor will be shared across multiple vehicles
        super().__init__()

    def get_spriterow_types_for_consist(self):
        # builds a map of spriterows for the entire consist by walking gestalt graphics for each unique unit
        # might be that this should be handled via the gestalt graphics class, but potato / potato here I think
        result = []
        for unit in self.consist.unique_units:
            unit_rows = []
            # assumes gestalt_graphics is used to handle all row types, no other cases at time of writing, could be changed eh?
            unit_rows.extend(self.consist.gestalt_graphics.get_output_row_types())
            result.append(unit_rows)
        return result

    def comp_chassis_and_body(self, body_image):
        crop_box_input_1 = (
            0,
            10,
            self.sprites_max_x_extent,
            10 + graphics_constants.spriterow_height,
        )
        chassis_image = Image.open(self.chassis_input_path).crop(crop_box_input_1)

        # roof is composited (N.B. gangways are not, just draw them in vehicle sprite, handling asymmetric railcar cases would be one step too far on automation)
        if (
            self.vehicle_unit.roof is not None
            and not self.vehicle_unit.suppress_roof_sprite
        ):
            crop_box_roof_dest = (
                0,
                0,
                self.sprites_max_x_extent,
                graphics_constants.spriterow_height,
            )
            roof_image = Image.open(self.roof_input_path).crop(crop_box_input_1)

            # the roof image has false colour pixels to aid drawing; remove these by converting to white, also convert any blue to white
            roof_image = roof_image.point(lambda i: 255 if i == 226 else i)

            # create a mask so that we paste only the roof pixels over the chassis (no blue pixels)
            roof_mask = roof_image.copy()
            roof_mask = roof_mask.point(lambda i: 0 if i == 255 else 255).convert(
                "1"
            )  # the inversion here of blue and white looks a bit odd, but potato / potato
            chassis_image.paste(roof_image, crop_box_roof_dest, roof_mask)
        # if self.consist.id == 'box_car_pony_gen_1A':
        # chassis_image.show()

        # chassis and roofs are *always* symmetrical, with 4 angles drawn; for vehicles with asymmetric bodies, copy and paste to provide all 8 angles
        if self.vehicle_unit.symmetry_type == "asymmetric":
            crop_box_input_2 = (
                self.global_constants.spritesheet_bounding_boxes_symmetric_unreversed[
                    4
                ][0],
                0,
                self.sprites_max_x_extent,
                0 + graphics_constants.spriterow_height,
            )
            chassis_image_2 = chassis_image.copy().crop(crop_box_input_2)

            crop_box_input_2_dest = (
                self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[
                    0
                ][0],
                0,
                self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[
                    0
                ][0]
                + chassis_image_2.size[0],
                0 + graphics_constants.spriterow_height,
            )
            chassis_image.paste(chassis_image_2, crop_box_input_2_dest)

        # the body image has false colour pixels for the chassis, to aid drawing; remove these by converting to white, also convert any blue to white
        body_image = body_image.point(
            lambda i: 255 if (i in range(178, 192) or i == 0) else i
        )
        # body_image.show()

        # create a mask so that we paste only the vehicle pixels over the chassis (no blue pixels)
        body_mask = body_image.copy()
        body_mask = body_mask.point(lambda i: 0 if i == 255 else 255).convert(
            "1"
        )  # the inversion here of blue and white looks a bit odd, but potato / potato

        # body_mask.show()
        crop_box_chassis_body_comp = (
            0,
            0,
            self.sprites_max_x_extent,
            0 + graphics_constants.spriterow_height,
        )
        chassis_image.paste(body_image, crop_box_chassis_body_comp, body_mask)

        # chassis_image.show()
        return chassis_image

    def add_generic_spriterows(self, spriterow_type):

        crop_box_source = (
            0,
            self.base_yoffs,
            self.sprites_max_x_extent,
            self.base_yoffs + graphics_constants.spriterow_height,
        )
        vehicle_generic_spriterow_input_image = self.comp_chassis_and_body(
            self.vehicle_source_image.copy().crop(crop_box_source)
        )
        # vehicle_generic_spriterow_input_image.show() # comment in to see the image when debugging
        empty_spriterow_image = Image.open(
            os.path.join(currentdir, "src", "graphics", "spriterow_template.png")
        )
        empty_spriterow_image = empty_spriterow_image.crop(
            (
                0,
                10,
                graphics_constants.spritesheet_width,
                10 + graphics_constants.spriterow_height,
            )
        )

        variants = self.consist.gestalt_graphics.get_generic_spriterow_output_variants(
            spriterow_type
        )
        for variant in variants:
            if variant["mask_row_offset_count"] == None:
                mask = None
            else:
                mask_rows_offset = self.base_yoffs + (
                    variant["mask_row_offset_count"]
                    * graphics_constants.spriterow_height
                )
                crop_box_mask_source = (
                    0,
                    mask_rows_offset,
                    self.sprites_max_x_extent,
                    mask_rows_offset + graphics_constants.spriterow_height,
                )
                crop_box_mask_dest = (
                    0,
                    0,
                    self.sprites_max_x_extent,
                    graphics_constants.spriterow_height,
                )
                mask_source = (
                    self.vehicle_source_image.copy()
                    .crop(crop_box_mask_source)
                    .point(lambda i: 255 if i == 226 else 0)
                    .convert("1")
                )
                mask = Image.new(
                    "1",
                    (
                        self.sprites_max_x_extent,
                        graphics_constants.spriterow_height,
                    ),
                    0,
                )
                mask.paste(mask_source, crop_box_mask_dest)
                # if self.consist.id == "hood_open_car_pony_gen_1A":
                # mask_source.show()

            generic_spriterow_variant_image = empty_spriterow_image.copy()
            generic_spriterow_variant_image.paste(
                vehicle_generic_spriterow_input_image, box=None, mask=mask
            )

            generic_spriterow_variant_image_as_spritesheet = (
                pixa.make_spritesheet_from_image(
                    generic_spriterow_variant_image, DOS_PALETTE
                )
            )
            crop_box_dest = (
                0,
                0,
                self.sprites_max_x_extent,
                graphics_constants.spriterow_height,
            )
            self.units.append(
                AppendToSpritesheet(
                    generic_spriterow_variant_image_as_spritesheet, crop_box_dest
                )
            )
            if variant["body_recolour_map"] is not None:
                self.units.append(SimpleRecolour(variant["body_recolour_map"]))
            self.units.append(
                AddCargoLabel(
                    label=variant["label"],
                    x_offset=self.sprites_max_x_extent + 5,
                    y_offset=-1 * graphics_constants.spriterow_height,
                )
            )

    def add_livery_spriterows(self):
        # no loading / loaded states, intended for tankers etc
        # provides cargo-specific recolourings, a default recolouring, and template alternates 1CC or 2CC livery on user flip

        # first add the CC alternative livery, as it's easier to add first than handle adding it after arbitrary cargo livery rows
        crop_box_source = (
            0,
            self.base_yoffs,
            self.sprites_max_x_extent,
            self.base_yoffs + graphics_constants.spriterow_height,
        )

        vehicle_livery_spriterow_input_image = self.comp_chassis_and_body(
            self.vehicle_source_image.copy().crop(crop_box_source)
        )
        vehicle_livery_spriterow_input_as_spritesheet = (
            pixa.make_spritesheet_from_image(
                vehicle_livery_spriterow_input_image, DOS_PALETTE
            )
        )

        for (
            weathered_variant,
            recolour_maps,
        ) in self.consist.gestalt_graphics.weathered_variants.items():
            for label, recolour_map in recolour_maps:
                crop_box_dest = (
                    0,
                    0,
                    self.sprites_max_x_extent,
                    graphics_constants.spriterow_height,
                )

                self.units.append(
                    AppendToSpritesheet(
                        vehicle_livery_spriterow_input_as_spritesheet, crop_box_dest
                    )
                )
                self.units.append(SimpleRecolour(recolour_map))
                self.units.append(
                    AddCargoLabel(
                        label=label,
                        x_offset=self.sprites_max_x_extent + 5,
                        y_offset=-1 * graphics_constants.spriterow_height,
                    )
                )

    def add_pax_mail_car_with_opening_doors_spriterows(self, row_count):
        # this loop builds the spriterow and comps doors etc
        for row_num in range(int(row_count / 2)):

            # get doors
            doors_bboxes = (
                self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed
            )
            crop_box_doors_source = (
                doors_bboxes[1][0],
                self.base_yoffs + (row_num * graphics_constants.spriterow_height),
                doors_bboxes[3][0] + doors_bboxes[3][1],
                self.base_yoffs
                + (row_num * graphics_constants.spriterow_height)
                + graphics_constants.spriterow_height,
            )
            doors_image = self.vehicle_source_image.copy().crop(crop_box_doors_source)

            # the doors image has false colour pixels for the body, to aid drawing; remove these by converting to white, also convert any blue to white
            doors_image = doors_image.point(
                lambda i: 255 if (i in range(178, 192) or i == 0) else i
            )
            # if self.consist.id == 'mail_car_pony_gen_4C':
            # doors_image.show()

            # create a mask so that we paste only the door pixels over the body (no blue pixels)
            doors_mask = doors_image.copy()
            doors_mask = doors_mask.point(lambda i: 0 if i == 255 else 255).convert(
                "1"
            )  # the inversion here of blue and white looks a bit odd, but potato / potato
            # doors_mask.show()

            crop_box_source = (
                0,
                self.base_yoffs + (row_num * graphics_constants.spriterow_height),
                self.sprites_max_x_extent,
                self.base_yoffs
                + (row_num * graphics_constants.spriterow_height)
                + graphics_constants.spriterow_height,
            )
            pax_mail_car_spriterow_input_image = self.comp_chassis_and_body(
                self.vehicle_source_image.copy().crop(crop_box_source)
            )

            crop_box_comped_body_and_chassis = (
                self.second_col_start_x,
                0,
                self.second_col_start_x + self.col_image_width,
                graphics_constants.spriterow_height,
            )

            pax_mail_car_spriterow_input_image = (
                pax_mail_car_spriterow_input_image.crop(
                    crop_box_comped_body_and_chassis
                )
            )

            # empty/loaded state and loading state will need pasting once each, so two crop boxes needed
            crop_box_comp_dest_1 = (
                self.second_col_start_x,
                0,
                self.second_col_start_x + self.col_image_width,
                graphics_constants.spriterow_height,
            )
            crop_box_comp_dest_2 = (
                self.second_col_start_x,
                graphics_constants.spriterow_height,
                self.second_col_start_x + self.col_image_width,
                2 * graphics_constants.spriterow_height,
            )
            crop_box_comp_dest_doors = (
                self.second_col_start_x + doors_bboxes[1][0] - doors_bboxes[0][0],
                graphics_constants.spriterow_height,
                self.second_col_start_x
                + doors_bboxes[1][0]
                - doors_bboxes[0][0]
                + doors_image.size[0],
                2 * graphics_constants.spriterow_height,
            )

            pax_mail_car_image = Image.new(
                "P",
                (
                    graphics_constants.spritesheet_width,
                    2 * graphics_constants.spriterow_height,
                ),
                255,
            )
            pax_mail_car_image.putpalette(DOS_PALETTE)
            pax_mail_car_image.paste(
                pax_mail_car_spriterow_input_image, crop_box_comp_dest_1
            )
            pax_mail_car_image.paste(
                pax_mail_car_spriterow_input_image, crop_box_comp_dest_2
            )
            # add doors
            pax_mail_car_image.paste(doors_image, crop_box_comp_dest_doors, doors_mask)
            # if self.consist.id == 'luxury_passenger_car_pony_gen_6U':
            # pax_mail_car_col_image.show()

            crop_box_dest = (
                0,
                0,
                self.sprites_max_x_extent,
                2 * graphics_constants.spriterow_height,
            )
            pax_mail_car_image_as_spritesheet = pixa.make_spritesheet_from_image(
                pax_mail_car_image, DOS_PALETTE
            )
            # if self.consist.id == 'luxury_passenger_car_pony_gen_6U':
            # pax_mail_car_image_as_spritesheet.sprites.show()
            self.units.append(
                AppendToSpritesheet(pax_mail_car_image_as_spritesheet, crop_box_dest)
            )

    def add_box_car_with_opening_doors_spriterows(self):
        # all wagons using this gestalt repaint the relevant base sprite for the wagon's generation and subtype
        id_base = self.consist.gestalt_graphics.id_base
        if self.consist.base_track_type_name == "NG":
            id_base = id_base + "_ng"
        box_car_id = self.consist.get_wagon_id(
            id_base=id_base,
            roster_id=self.consist.roster_id,
            gen=self.consist.gen,
            subtype=self.consist.subtype + ".png",
        )
        box_car_input_path = os.path.join(
            currentdir, "src", "graphics", self.consist.roster_id, box_car_id
        )

        # two spriterows, closed doors and open doors
        crop_box_source_1 = (
            0,
            self.base_yoffs,
            self.sprites_max_x_extent,
            self.base_yoffs + graphics_constants.spriterow_height,
        )
        crop_box_source_2 = (
            0,
            self.base_yoffs + graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            self.base_yoffs + 2 * graphics_constants.spriterow_height,
        )
        box_car_input_image_1 = self.comp_chassis_and_body(
            Image.open(box_car_input_path).crop(crop_box_source_1)
        )
        box_car_input_image_2 = self.comp_chassis_and_body(
            Image.open(box_car_input_path).crop(crop_box_source_2)
        )
        # if self.consist.id == 'box_car_pony_gen_1A':
        # box_car_input_image_1.show() # comment in to see the image when debugging

        # empty/loaded state and loading state will need pasting once each, so two crop boxes needed
        # open doors are shown, but no cargo, TMWFTLB, see notes in GestaltGraphicsBoxCarOpeningDoors
        crop_box_comp_dest_1 = (
            0,
            0,
            self.sprites_max_x_extent,
            graphics_constants.spriterow_height,
        )
        crop_box_comp_dest_2 = (
            0,
            graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )
        box_car_rows_image = Image.new(
            "P",
            (
                graphics_constants.spritesheet_width,
                2 * graphics_constants.spriterow_height,
            ),
        )
        box_car_rows_image.putpalette(DOS_PALETTE)

        box_car_rows_image.paste(box_car_input_image_1, crop_box_comp_dest_1)
        box_car_rows_image.paste(box_car_input_image_2, crop_box_comp_dest_2)

        crop_box_dest = (
            0,
            0,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )

        box_car_rows_image_as_spritesheet = pixa.make_spritesheet_from_image(
            box_car_rows_image, DOS_PALETTE
        )

        for (
            weathered_variant,
            recolour_maps,
        ) in self.consist.gestalt_graphics.weathered_variants.items():
            self.units.append(
                AppendToSpritesheet(box_car_rows_image_as_spritesheet, crop_box_dest)
            )
            self.units.append(SimpleRecolour(recolour_maps[0][1]))
            box_car_input_image_1.close()

    def add_caboose_spriterows(self, row_count):
        for row_num in range(row_count):
            row_offset = row_num * graphics_constants.spriterow_height

            crop_box_source = (
                0,
                self.base_yoffs + row_offset,
                self.sprites_max_x_extent,
                self.base_yoffs + row_offset + graphics_constants.spriterow_height,
            )
            caboose_car_spriterow_input_image = self.comp_chassis_and_body(
                self.vehicle_source_image.copy().crop(crop_box_source)
            )

            crop_box_comp_dest = (
                0,
                0,
                self.sprites_max_x_extent,
                graphics_constants.spriterow_height,
            )
            caboose_car_rows_image = Image.new(
                "P",
                (
                    graphics_constants.spritesheet_width,
                    graphics_constants.spriterow_height,
                ),
            )
            caboose_car_rows_image.putpalette(DOS_PALETTE)

            caboose_car_rows_image.paste(
                caboose_car_spriterow_input_image, crop_box_comp_dest
            )
            # caboose_car_rows_image.show()

            crop_box_dest = (
                0,
                0,
                self.sprites_max_x_extent,
                graphics_constants.spriterow_height,
            )

            caboose_car_rows_image_as_spritesheet = pixa.make_spritesheet_from_image(
                caboose_car_rows_image, DOS_PALETTE
            )

            self.units.append(
                AppendToSpritesheet(
                    caboose_car_rows_image_as_spritesheet, crop_box_dest
                )
            )
            self.units.append(
                SimpleRecolour(self.consist.gestalt_graphics.recolour_map)
            )

    def add_bulk_cargo_spriterows(self):
        cargo_group_row_height = 2 * graphics_constants.spriterow_height

        # note that bulk cargo *can* support asymmetric spritesheets (piece cannot) - see ore dump cars for example
        crop_box_cargo = (
            0,
            self.base_yoffs,
            self.sprites_max_x_extent,
            self.base_yoffs + (2 * graphics_constants.spriterow_height),
        )
        cargo_base_image = self.vehicle_source_image.copy().crop(crop_box_cargo)
        # the loading/loaded image has false colour pixels for the cargo; keep only these, removing everything else
        cargo_base_image = cargo_base_image.point(
            lambda i: 255 if (i not in range(170, 177)) else i
        )
        # if self.consist.id == "dump_car_pony_gen_3A":
        # cargo_base_image.show()

        # create a mask so that we paste only the cargo pixels over the body (no blue pixels)
        cargo_base_mask = cargo_base_image.copy()
        cargo_base_mask = cargo_base_mask.point(
            lambda i: 0 if i == 255 else 255
        ).convert(
            "1"
        )  # the inversion here of blue and white looks a bit odd, but potato / potato
        # if self.consist.id == "dump_car_pony_gen_3A":
        # cargo_base_mask.show()

        # loading and loaded state will need pasting once each, so two crop boxes needed
        crop_box_comp_dest_1 = (
            0,
            0,
            self.sprites_max_x_extent,
            graphics_constants.spriterow_height,
        )
        crop_box_comp_dest_2 = (
            0,
            graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )
        crop_box_comp_dest_3 = (
            0,
            0,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )

        # this is dirty shorthand and relies on has_cover yielding 0 or 1 for an additional offset (empty row is second row if has_cover is True)
        empty_row_yoffs = self.cur_vehicle_empty_row_yoffs + (
            graphics_constants.spriterow_height
            * self.consist.gestalt_graphics.has_cover
        )

        crop_box_vehicle_body = (
            0,
            empty_row_yoffs,
            self.sprites_max_x_extent,
            empty_row_yoffs + graphics_constants.spriterow_height,
        )

        vehicle_base_image = self.comp_chassis_and_body(
            self.vehicle_source_image.copy().crop(crop_box_vehicle_body)
        )
        # vehicle_base_image.show()

        bulk_cargo_rows_image = Image.new(
            "P", (graphics_constants.spritesheet_width, cargo_group_row_height), 255
        )
        bulk_cargo_rows_image.putpalette(DOS_PALETTE)

        # paste the empty state into two rows, then paste the cargo over those rows
        bulk_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_1)
        bulk_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_2)
        bulk_cargo_rows_image.paste(
            cargo_base_image, crop_box_comp_dest_3, cargo_base_mask
        )
        # if self.consist.id == "dump_car_pony_gen_3A":
        # bulk_cargo_rows_image.show()

        crop_box_dest = (0, 0, self.sprites_max_x_extent, cargo_group_row_height)
        bulk_cargo_rows_image_as_spritesheet = pixa.make_spritesheet_from_image(
            bulk_cargo_rows_image, DOS_PALETTE
        )

        # !! note that body_recolour_map is unused and unsupported as of March 2022
        # at March 2022 all wagons with bulk cargo are drawn using actual colours
        # the purple range used for cargo recolouring would clash with the typical body recolouring (and the default body recolour map on this gestalt)
        # this could be worked around by using the dark red option, but work would be needed to eliminate the clash
        # !! we still have to duplicate the entire set of bulk spriterows per weathered variant, as the nml templating expects this (would be unwise to snowflake it)
        for (
            label,
            cargo_recolour_map,
        ) in polar_fox.constants.bulk_cargo_recolour_maps:
            body_recolour_map = self.consist.gestalt_graphics.weathered_variants[
                "unweathered"
            ]
            self.units.append(
                AppendToSpritesheet(bulk_cargo_rows_image_as_spritesheet, crop_box_dest)
            )
            self.units.append(SimpleRecolour(body_recolour_map))
            self.units.append(SimpleRecolour(cargo_recolour_map))
            self.units.append(
                AddCargoLabel(
                    label=label,
                    x_offset=self.sprites_max_x_extent + 5,
                    y_offset=-1 * cargo_group_row_height,
                )
            )

    def add_piece_cargo_spriterows(self):
        cargo_group_output_row_height = 2 * graphics_constants.spriterow_height

        # Overview
        # 2 spriterows for the vehicle loading / loaded states, with pink loc points for cargo
        # a mask row for the vehicle, with pink mask area, which is converted to black and white mask image
        # an overlay for the vehicle, created from the vehicle empty state spriterow, and comped with the mask after each cargo has been placed
        # - there is a case not handled, where long cargo sprites will overlap cabbed vehicles in / direction with cab at N end, hard to solve
        # - this has no awareness of vehicle symmetry_type property, so will needlessly scan too many pixels for symmetric vehicles
        #   that's TMWFTLB to fix right now, as it will require relative offsets of all the loc points for probably very little performance gain
        # note that piece *cannot* support asymmetric spritesheets (bulk can), TMWFTLB to support currently
        # - asymmetric vehicle support might be possible if really needed, but cargo sprites will be symmetric
        # - for asymmetric cargo sprites, use spritelayer cargos instead (see automobile or intermodal cargos)
        crop_box_vehicle_cargo_loc_row = (
            self.second_col_start_x,
            self.base_yoffs,
            self.second_col_start_x + self.col_image_width,
            self.base_yoffs + graphics_constants.spriterow_height,
        )
        vehicle_cargo_loc_image = self.vehicle_source_image.copy().crop(
            crop_box_vehicle_cargo_loc_row
        )
        # get the loc points
        loc_points = [
            (pixel[0] + self.second_col_start_x, pixel[1], pixel[2])
            for pixel in pixa.pixascan(vehicle_cargo_loc_image)
            if pixel[2] == 226
        ]
        # two cargo rows needed, so extend the loc points list
        loc_points.extend([(pixel[0], pixel[1] + 30, pixel[2]) for pixel in loc_points])
        # sort them in y order, this causes sprites to overlap correctly when there are multiple loc points for an angle
        loc_points = sorted(loc_points, key=lambda x: x[1])

        # this is dirty shorthand and relies on has_cover yielding 0 or 1 for an additional offset (empty row is second row if has_cover is True)
        empty_row_yoffs = self.cur_vehicle_empty_row_yoffs + (
            graphics_constants.spriterow_height
            * self.consist.gestalt_graphics.has_cover
        )

        crop_box_vehicle_body = (
            0,
            empty_row_yoffs,
            self.sprites_max_x_extent,
            empty_row_yoffs + graphics_constants.spriterow_height,
        )
        vehicle_base_image = self.comp_chassis_and_body(
            self.vehicle_source_image.copy().crop(crop_box_vehicle_body)
        )

        crop_box_mask_source = (
            self.second_col_start_x,
            self.base_yoffs + graphics_constants.spriterow_height,
            self.second_col_start_x + self.col_image_width,
            self.base_yoffs + (2 * graphics_constants.spriterow_height),
        )
        crop_box_mask_dest = (
            self.second_col_start_x,
            0,
            self.second_col_start_x + self.col_image_width,
            graphics_constants.spriterow_height,
        )
        vehicle_mask_source = (
            self.vehicle_source_image.copy()
            .crop(crop_box_mask_source)
            .point(lambda i: 255 if i == 226 else 0)
            .convert("1")
        )
        vehicle_mask = Image.new(
            "1", (self.sprites_max_x_extent, graphics_constants.spriterow_height), 0
        )
        vehicle_mask.paste(vehicle_mask_source, crop_box_mask_dest)
        # if self.consist.id == "open_car_pony_gen_1A":
        # vehicle_mask.show()

        # mask and empty state will need pasting once for each of two cargo rows, so two crop boxes needed
        crop_box_comp_dest_1 = (
            0,
            0,
            self.sprites_max_x_extent,
            graphics_constants.spriterow_height,
        )
        crop_box_comp_dest_2 = (
            0,
            graphics_constants.spriterow_height,
            self.sprites_max_x_extent,
            2 * graphics_constants.spriterow_height,
        )

        piece_cargo_rows_image = Image.new(
            "P", (graphics_constants.spritesheet_width, cargo_group_output_row_height)
        )
        piece_cargo_rows_image.putpalette(DOS_PALETTE)
        # paste empty states in for the cargo rows (base image = empty state)
        piece_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_1)
        piece_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_2)
        # if self.consist.id == "open_car_pony_gen_1A":
        # piece_cargo_rows_image.show()
        crop_box_dest = (0, 0, self.sprites_max_x_extent, cargo_group_output_row_height)

        piece_cargo_sprites = PieceCargoSprites(
            polar_fox_constants=polar_fox.constants,
            polar_fox_graphics_path=os.path.join("src", "polar_fox", "graphics"),
        )
        for cargo_filename in polar_fox.constants.piece_vehicle_type_to_sprites_maps[
            self.consist.gestalt_graphics.piece_type
        ]:
            # n.b. Iron Horse assumes cargo length is always equivalent from vehicle length (probably fine)
            cargo_sprites = piece_cargo_sprites.get_cargo_sprites_all_angles_for_length(
                cargo_filename, self.vehicle_unit.vehicle_length
            )

            vehicle_comped_image = piece_cargo_rows_image.copy()

            for pixel in loc_points:
                angle_num = 0
                for counter, bbox in enumerate(
                    self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed
                ):
                    if pixel[0] >= bbox[0]:
                        angle_num = counter
                # clamp angle_num to 4, cargo sprites are symmetrical, only 4 angles provided
                if angle_num > 3:
                    angle_num = angle_num % 4
                cargo_sprite_num = angle_num

                # loaded sprites are the second block of 4 in the cargo sprites list
                if pixel[1] >= graphics_constants.spriterow_height:
                    cargo_sprite_num = cargo_sprite_num + 4

                cargo_width = cargo_sprites[cargo_sprite_num][0].size[0]
                cargo_height = cargo_sprites[cargo_sprite_num][0].size[1]
                # the +1s for height adjust the crop box to include the loc point
                # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
                cargo_bounding_box = (
                    pixel[0],
                    pixel[1] - cargo_height + 1,
                    pixel[0] + cargo_width,
                    pixel[1] + 1,
                )
                vehicle_comped_image.paste(
                    cargo_sprites[cargo_sprite_num][0],
                    cargo_bounding_box,
                    cargo_sprites[cargo_sprite_num][1],
                )

            # vehicle overlay with mask - overlays any areas where cargo shouldn't show
            vehicle_comped_image.paste(
                vehicle_base_image, crop_box_comp_dest_1, vehicle_mask
            )
            vehicle_comped_image.paste(
                vehicle_base_image, crop_box_comp_dest_2, vehicle_mask
            )
            # if self.consist.id == "open_car_pony_gen_1A":
            # vehicle_comped_image.show()

            vehicle_comped_image_as_spritesheet = pixa.make_spritesheet_from_image(
                vehicle_comped_image, DOS_PALETTE
            )

            body_recolour_map = self.consist.gestalt_graphics.weathered_variants[
                "unweathered"
            ]
            self.units.append(
                AppendToSpritesheet(vehicle_comped_image_as_spritesheet, crop_box_dest)
            )
            self.units.append(SimpleRecolour(body_recolour_map))
            self.units.append(
                AddCargoLabel(
                    label=cargo_filename,
                    x_offset=self.sprites_max_x_extent + 5,
                    y_offset=-1 * cargo_group_output_row_height,
                )
            )

    def render(self, consist, global_constants, graphics_output_path):
        self.units = (
            []
        )  # graphics units not same as consist units ! confusing overlap of terminology :(
        self.consist = consist
        self.global_constants = global_constants
        self.graphics_output_path = graphics_output_path
        self.sprites_max_x_extent = self.global_constants.sprites_max_x_extent
        self.first_col_start_x = (
            self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[0][0]
        )
        self.second_col_start_x = (
            self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[4][0]
        )
        self.col_image_width = self.sprites_max_x_extent - self.second_col_start_x

        self.vehicle_source_image = Image.open(self.vehicle_source_input_path)

        # the cumulative_input_spriterow_count updates per processed group of spriterows, and is key to making this work
        # !! input_spriterow_count looks a bit weird though; I tried moving it to gestalts, but didn't really work
        cumulative_input_spriterow_count = 0
        for vehicle_counter, vehicle_rows in enumerate(
            self.get_spriterow_types_for_consist()
        ):
            # 'vehicle_unit' not 'unit' to avoid conflating with graphics processor 'unit'
            self.vehicle_unit = self.consist.unique_units[
                vehicle_counter
            ]  # !!  this is ugly hax, I didn't want to refactor the iterator above to contain the vehicle
            self.cur_vehicle_empty_row_yoffs = (
                10
                + cumulative_input_spriterow_count * graphics_constants.spriterow_height
            )
            for spriterow_type in vehicle_rows:
                self.base_yoffs = 10 + (
                    graphics_constants.spriterow_height
                    * cumulative_input_spriterow_count
                )
                if spriterow_type == "empty":
                    input_spriterow_count = 1
                    self.add_generic_spriterows(spriterow_type)
                if spriterow_type == "has_cover":
                    input_spriterow_count = 1
                    self.add_generic_spriterows(spriterow_type)
                elif spriterow_type == "livery_spriterows":
                    input_spriterow_count = 1
                    self.add_livery_spriterows()
                elif spriterow_type == "box_car_with_opening_doors_spriterows":
                    input_spriterow_count = 2
                    self.add_box_car_with_opening_doors_spriterows()
                elif spriterow_type == "caboose_spriterows":
                    input_spriterow_count = self.consist.gestalt_graphics.num_variations
                    self.add_caboose_spriterows(input_spriterow_count)
                elif spriterow_type == "pax_mail_cars_with_doors":
                    input_spriterow_count = (
                        self.consist.gestalt_graphics.total_spriterow_count
                    )
                    self.add_pax_mail_car_with_opening_doors_spriterows(
                        input_spriterow_count
                    )
                elif spriterow_type == "bulk_cargo":
                    input_spriterow_count = 2
                    self.add_bulk_cargo_spriterows()
                elif spriterow_type == "piece_cargo":
                    input_spriterow_count = 2
                    self.add_piece_cargo_spriterows()
                cumulative_input_spriterow_count += input_spriterow_count
            # self.vehicle_unit is hax, and is only valid inside this loop, so clear it to prevent incorrectly relying on it outside the loop in future :P
            self.vehicle_unit = None

        if hasattr(self.consist.gestalt_graphics, "asymmetric_row_map"):
            self.units.append(
                TransposeAsymmetricSprites(
                    graphics_constants.spriterow_height,
                    global_constants.spritesheet_bounding_boxes_asymmetric_unreversed,
                    self.consist.gestalt_graphics.asymmetric_row_map,
                )
            )

        if self.consist.buy_menu_x_loc == 360:
            self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        # for this pipeline, input_image is just blank white 10px high image, to which the vehicle sprites are then appended
        input_image = Image.new("P", (graphics_constants.spritesheet_width, 10), 255)
        input_image.putpalette(DOS_PALETTE)
        self.render_common(input_image, self.units)
        self.vehicle_source_image.close()


def get_pipelines(pipeline_names):
    # return a pipeline by name;
    # add pipelines here when creating new ones
    # this is a bit hokey, there's probably a simpler way to do this but eh
    # looks like it could be replaced by a simple dict lookup directly from gestalt_graphics, but eh, I tried, it's faff
    pipelines = {
        "pass_through_pipeline": PassThroughPipeline,
        "check_buy_menu_only": CheckBuyMenuOnlyPipeline,
        "generate_buy_menu_sprite_from_randomisation_candidates": GenerateBuyMenuSpriteFromRandomisationCandidatesPipeline,
        "generate_empty_spritesheet": GenerateEmptySpritesheet,
        "extend_spriterows_for_composited_sprites_pipeline": ExtendSpriterowsForCompositedSpritesPipeline,
        "generate_pantographs_up_spritesheet": GeneratePantographsUpSpritesheetPipeline,
        "generate_pantographs_down_spritesheet": GeneratePantographsDownSpritesheetPipeline,
        "generate_spritelayer_cargo_sets": GenerateSpritelayerCargoSets,
    }
    return [pipelines[pipeline_name]() for pipeline_name in pipeline_names]


def main():
    print("yeah, pipelines.main() does nothing")


if __name__ == "__main__":
    main()
