import os.path
currentdir = os.curdir

import filecmp
from PIL import Image

import polar_fox
from polar_fox.graphics_units import SimpleRecolour, AppendToSpritesheet, AddCargoLabel, AddBuyMenuSprite
from polar_fox.pixa import Spritesheet, pixascan
from gestalt_graphics import graphics_constants

DOS_PALETTE = Image.open('palette_key.png').palette

"""
Pipelines can be dedicated to a single task such as SimpleRecolourPipeline
Or they can compose units for more complicated tasks, such as colouring and loading a specific vehicle type
"""

class Pipeline(object):
    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        # actually, there's nothing to do eh :P
        pass

    def make_spritesheet_from_image(self, input_image):
        spritesheet = Spritesheet(width=input_image.size[0], height=input_image.size[1] , palette=DOS_PALETTE)
        spritesheet.sprites.paste(input_image)
        return spritesheet

    @property
    def vehicle_source_input_path(self):
        # convenience method to get the vehicle template image
        # I considered having this return the Image, not just the path, but it's not saving much, and is less obvious what it does when used
        return os.path.join(currentdir, 'src', 'graphics', self.consist.roster_id, self.consist.id + '.png')

    @property
    def chassis_input_path(self):
        # convenience method to get the path for the chassis image
        return os.path.join(currentdir, 'src', 'graphics', 'chassis', self.vehicle_unit.chassis + '.png')

    @property
    def roof_input_path(self):
        # convenience method to get the path for the roof image
        return os.path.join(currentdir, 'src', 'graphics', 'roofs', self.vehicle_unit.roof + '.png')

    def get_arbitrary_angles(self, input_image, bounding_boxes):
        # given an image and a list of arbitrary bounding boxes...
        # ...return a list of two tuples with sprite and mask
        # this can then be used for compositing
        # note the arbitrary order of sprites which makes this very flexible
        result = []
        for bounding_box in bounding_boxes:
            sprite = input_image.copy()
            sprite = sprite.crop(bounding_box)
            mask = sprite.copy()
            # !! .point is noticeably slow although not signifcantly so with only 3 cargo types
            # !! check this again if optimisation is a concern - can cargos be processed once and passed to the pipeline?
            # !! as of Oct 2018, I tested commenting out *all* piece cargo processing, including calls to this method
            # !! that cut only 1s from an 11s graphics processing run on single CPU
            # !! so optimising this is TMWFTLB currently; instead simply using multiprocessing cuts graphics run to 2s
            mask = mask.point(lambda i: 0 if i == 0 else 255).convert("1")
            result.append((sprite, mask))
        return result

    def process_buy_menu_sprite(self, spritesheet):
        # this function is passed (uncalled) into the pipeline, and then called at render time
        # this is so that it has the processed spritesheet available, which is essential for creating buy menu sprites
        # n.b if buy menu sprite processing has conditions by vehicle type, could pass a dedicated function for each type of processing

        # hard-coded positions for buy menu sprite (if used - it's optional)
        x_offset = 0
        for counter, unit in enumerate(self.consist.units):
            # !! currently no cap on purchase menu sprite width
            # !! consist has a buy_menu_width prop which caps to 64 which could be used (+1px overlap)
            unit_length_in_pixels = 4 * unit.vehicle_length
            # this is jank because some articulated consists with fancy rulesets need to flip some vehicles
            # this is probably pretty fragile, but eh, JFDI
            ruleset_offset_num_rows_jank = 0
            if getattr(self.consist.gestalt_graphics, 'consist_ruleset', None) in ['metro']:
                if counter % 2 != 0:
                    ruleset_offset_num_rows_jank = 4 # hard-coded to metro currently
            unit_spriterow_offset = (unit.spriterow_num + ruleset_offset_num_rows_jank) * graphics_constants.spriterow_height
            crop_box_src = (224,
                            10 + unit_spriterow_offset,
                            224 + unit_length_in_pixels + 1, # allow for 1px coupler / corrider overhang
                            26 + unit_spriterow_offset)
            crop_box_dest = (360 + x_offset,
                             10,
                             360 + x_offset + unit_length_in_pixels + 1, # allow for 1px coupler / corrider overhang
                             26)
            custom_buy_menu_sprite = spritesheet.sprites.copy().crop(crop_box_src)
            spritesheet.sprites.paste(custom_buy_menu_sprite, crop_box_dest)
            # increment x offset for pasting in next vehicle
            x_offset += unit_length_in_pixels
        return spritesheet

    def render_common(self, input_image, units, output_base_name=None, output_suffix=''):
        # expects to be passed a PIL Image object
        # units is a list of objects, with their config data already baked in (don't have to pass anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        if output_base_name is None:
            # default to consist name for file name, but can over-ride for e.g. containers by passing something in
            output_base_name = self.consist.id
        output_path = os.path.join(currentdir, 'generated', 'graphics', output_base_name + output_suffix + '.png')
        output_path_tmp = os.path.join(currentdir, 'generated', 'graphics', output_base_name + output_suffix + '.new.png')
        spritesheet = self.make_spritesheet_from_image(input_image)

        for unit in units:
            spritesheet = unit.render(spritesheet)
        # I don't normally leave commented-out code behind, but I'm bored of looking in the PIL docs for how to show the image during compile
        #if self.consist.id == 'velaro_thing':
            #spritesheet.sprites.show()

        # save a tmp file first and compare to existing file (if any)
        # this prevents destroying the nmlc sprite cache with every graphics run by needlessly replacing the files
        # !! this should arguably be moved into pixa
        if os.path.exists(output_path):
            # save tmp file
            spritesheet.save(output_path_tmp)
            # only save final output file if an existing file doesn't match tmp
            if not filecmp.cmp(output_path, output_path_tmp):
                print("replacing", output_path)
                spritesheet.save(output_path)
            os.remove(output_path_tmp)
        else:
            spritesheet.save(output_path)

    def render(self, consist):
        raise NotImplementedError("Implement me in %s" % repr(self))


class PassThroughPipeline(Pipeline):
    """
    Solely opens the input image and saves it, this more of a theoretical case, there's no actual reason to use this.
    """
    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def render(self, consist, global_constants):
        self.units = []
        self.consist = consist

        input_image = Image.open(self.vehicle_source_input_path)
        self.render_common(input_image, self.units)


class GenerateCompositedIntermodalContainers(Pipeline):
    """
    Creates a spritesheet with a set of composited intermodal containers,
    This works a little differently to vehicle pipelines, but close enough that it's worth using pipelines to share spritesheet save code etc.
    """
    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def resolve_template_name(self, variant):
        # figure out which template png to use based on gestalt length + container pattern
        # - e.g. 32px_40_20, 32px_20_20_20 etc?
        result = [str(self.intermodal_container_gestalt.length) + 'px']
        for container in variant:
            result.append(container.split('_foot')[0][-2:])
        return 'intermodal_template_' + '_'.join(result)

    def add_container_spriterows(self):
        for variant in self.intermodal_container_gestalt.variants:
            template_path = os.path.join(currentdir, 'src', 'graphics', 'intermodal_containers', self.resolve_template_name(variant) + '.png')
            template_image = Image.open(template_path)

            # get the loc points and sort them for display
            # !! loc points might need extended to support double stack ??
            loc_points = [(pixel[0], pixel[1] - 10, pixel[2]) for pixel in pixascan(template_image) if pixel[2] in [226, 240, 244]]
            loc_points_grouped_and_sorted_for_display = {}
            for angle_index, bbox in enumerate(self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed):
                pixels=[]
                for pixel in loc_points:
                    if pixel[0] >= bbox[0] and pixel[0] <= (bbox[0] + bbox[1]):
                        pixels.append(pixel)
                        # catch invalid pixels
                        if (1 + [226, 240, 244].index(pixel[2])) > len(variant):
                            message = template_path
                            message += " contains pixel colour " + str(pixel[2]) + " which implies " + str(1 + [226, 240, 244].index(pixel[2])) + " containers"
                            message += " but the variant only defines " + str(len(variant)) + " container sprite(s)"
                            raise ValueError(message)
                # fake sprite sorter - containers nearer front need to overlap containers behind
                # position pixel colour indexes (in the palette) must be in ascending order for left->right positions in <- view
                # required index colours are 226, 240, 244
                # the fake sprite sorter then just sorts ascending or descending as required for each angle
                # !! double stack might be possible to handle just using this rudimentary sprite sorting ?? (or extending it??)
                pixels = sorted(pixels, key=lambda pixel: pixel[2])
                if angle_index in [3, 4, 5]:
                    pixels.reverse()
                loc_points_grouped_and_sorted_for_display[angle_index] = pixels

            # get the sprites for all containers for this variant, and put them in a single structure
            # n.b the implementation of this is likely inefficient as it will repetively open the same containers from the filesystem,
            # but so far that seems to have negligible performance cost, and caching all containers earlier in the loop would add unwanted complexity
            container_sprites_for_this_variant = []
            for container in variant:
                container_path = os.path.join(currentdir, 'src', 'graphics', 'intermodal_containers', container + '.png')
                container_image = Image.open(container_path)
                #if self.intermodal_container_gestalt.id == 'intermodal_box_32px':
                    #container_image.show()
                bboxes = []
                # only a 3 tuple in global constants bounding box definitions (no y position), we need a 4 tuple inc. y position
                # also the format of bounding boxes needs converted to PIL crop box format
                for bbox in self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed:
                    bboxes.append([bbox[0], 10, bbox[0] + bbox[1], 10 + bbox[2]])

                # !! containers are symmetric?
                # !! angles 0-3 need to be copied from angles 4-7
                container_sprites = self.get_arbitrary_angles(container_image, bboxes)
                #if self.intermodal_container_gestalt.id == 'intermodal_box_32px':
                    #container_sprites[6][0].show()
                container_sprites_for_this_variant.append(container_sprites)

            variant_output_image = Image.open(os.path.join(currentdir, 'src', 'graphics', 'spriterow_template.png'))
            variant_output_image = variant_output_image.crop((0, 10, graphics_constants.spritesheet_width, 10 + graphics_constants.spriterow_height))

            for angle_index, pixels in loc_points_grouped_and_sorted_for_display.items():
                for pixel in pixels:
                    # use the pixel colour to look up which container sprites to use, relies on hard-coded pixel colours
                    # print(self.intermodal_container_gestalt.id, variant, angle_index, pixels, container_sprites_for_this_variant)
                    container_sprites = container_sprites_for_this_variant[[226, 240, 244].index(pixel[2])] # one line python stupidity
                    container_width = container_sprites[angle_index][0].size[0]
                    container_height = container_sprites[angle_index][0].size[1]
                    # the +1s for height adjust the crop box to include the loc point
                    # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
                    container_bounding_box = (pixel[0],
                                              pixel[1] - container_height + 1,
                                              pixel[0] + container_width,
                                              pixel[1] + 1)

                    variant_output_image.paste(container_sprites[angle_index][0], container_bounding_box, container_sprites[angle_index][1])

            # create a mask to place black shadows between adjacent containers
            combo_check = ['empty' if 'empty' in i else 'occupied' for i in variant]
            # *vehicles with 3 containers only (32px)*
            # don't allow combinations of only two adjacent 20 foot containers as it's TMWFTLB to provide the shadow for them
            # two 20 foot with a gap between are supported
            # solitary 20 foot containers of any length in any position are not prevented, but look bad (looks like loading didn't finish)
            if len(combo_check) == 3:
                if combo_check in [['occupied', 'occupied', 'empty'], ['empty', 'occupied', 'occupied']]:
                    raise ValueError(self.intermodal_container_gestalt.id +" - this pattern of (20 foot) containers isn't supported (can't composite shadows for it): " + str(combo_check))

            # don't draw shadows if there are empty slots
            if combo_check.count('empty') == 0:
                shadow_image = template_image.copy().crop((0, 10, self.global_constants.sprites_max_x_extent, 10 + graphics_constants.spriterow_height))
                shadow_mask = shadow_image.copy()
                shadow_mask = shadow_mask.point(lambda i: 255 if i == 1 else 0).convert("1") # assume shadow is always colour index 1 in the palette
                variant_output_image.paste(shadow_image, mask=shadow_mask)

            #if self.intermodal_container_gestalt.id == 'intermodal_box_32px':
                #variant_output_image.show()
            variant_spritesheet = self.make_spritesheet_from_image(variant_output_image)
            crop_box_dest = (0,
                             0,
                             self.global_constants.sprites_max_x_extent,
                             graphics_constants.spriterow_height)
            self.units.append(AppendToSpritesheet(variant_spritesheet, crop_box_dest))

        # provide an empty spritesheet (or skip compositing) if container is 'empty'
        # but what about offsetting containers to end or middle? e.g. 40ft container on 60ft wagon
        # - always default to offset centered if < total length
        # - offsetting to end is achieved by including 'empty' containers
        # == #
        # each template will need to provide a row of black pixels to use between containers
        # - no mask for singles
        # - don't insert the mask if empty
        # - this means 20-20-empty is not going to be possible, probably fine
        # - add a guard against 20-20-empty and empty-20-20

    def render(self, intermodal_container_gestalt, global_constants):
        self.units = []
        self.intermodal_container_gestalt = intermodal_container_gestalt
        self.global_constants = global_constants

        self.add_container_spriterows()

        # for this pipeline, input_image is just blank white 10px high image, to which the vehicle sprites are then appended
        input_image = Image.new("P", (graphics_constants.spritesheet_width, 10), 255)
        input_image.putpalette(DOS_PALETTE)
        self.render_common(input_image, self.units, output_base_name=intermodal_container_gestalt.id)


class CheckBuyMenuOnlyPipeline(Pipeline):
    """
    Opens the input image, inserts a custom buy menu if required, then saves with no other changes.
    """
    def __init__(self):
        # this should be sparse, don't store any consist info in Pipelines, pass at render time
        super().__init__()

    def render(self, consist, global_constants):
        self.units = []
        self.consist = consist

        if self.consist.buy_menu_x_loc == 360:
            # !! this currently will cause the vehicle spritesheet buy menu sprites to be copied to the pans spritesheet,
            # !! it needs pixels from the pans spritesheet, but automated buy menu sprites need providing first
            self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        input_image = Image.open(self.vehicle_source_input_path)
        self.render_common(input_image, self.units)


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

        # the gestalt can optionally tell us how many spriterows are needed, but if it doesn't, fallback to the unique spriterows
        # we do it this way because the gestalt doesn't have easy access to the consist, so easier to do the fallback here
        num_pantograph_rows = getattr(self.consist.gestalt_graphics, 'num_pantograph_rows', len(self.consist.unique_spriterow_nums))

        pantograph_input_images = {'diamond-single': 'diamond.png', 'diamond-double': 'diamond.png',
                                   'diamond-single-with-base': 'diamond-with-base.png',
                                   'z-shaped-single': 'z-shaped.png', 'z-shaped-double': 'z-shaped.png',
                                   'z-shaped-single-with-base': 'z-shaped-with-base.png'}
        pantograph_input_path = os.path.join(currentdir, 'src', 'graphics', 'pantographs', pantograph_input_images[self.consist.pantograph_type])
        pantograph_input_image = Image.open(pantograph_input_path)

        bboxes = []
        # only a 3 tuple in global constants bounding box definitions (no y position), we need a 4 tuple inc. y position
        # also the format of bounding boxes needs converted to PIL crop box format
        for yoffset in (10, 40):
            for bbox in self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed:
                bboxes.append([bbox[0], yoffset, bbox[0] + bbox[1], yoffset + bbox[2]])

        pantograph_sprites = self.get_arbitrary_angles(pantograph_input_image, bboxes)
        # needs to slice out A down, A up, B down, B up, depending on type
        # but B is probably just A reversed
        # so two spriterows is enough: down, up
        # two colours of loc pixel, for A and B positions
        spriterow_pantograph_state_maps = {'diamond-single': {'down': ['a'], 'up': ['A']},
                                           'diamond-double': {'down': ['a', 'a'], 'up': ['A', 'A']}, # A and B functionally identical here, so just use A
                                           'diamond-single-with-base': {'down': ['a'], 'up': ['A']},
                                           'z-shaped-single': {'down': ['a'], 'up': ['A']},
                                           'z-shaped-double': {'down': ['a', 'b'], 'up': ['A', 'b']},  # aB was tried and removed, TMWFTLB, instead just use Ab and respect depot flip
                                           'z-shaped-single-with-base': {'down': ['a'], 'up': ['A']}}
        pantograph_state_sprite_map = {'a': [pantograph_sprites[0], pantograph_sprites[1], pantograph_sprites[2], pantograph_sprites[3],
                                             pantograph_sprites[4], pantograph_sprites[5], pantograph_sprites[6], pantograph_sprites[7]],
                                       'A': [pantograph_sprites[8], pantograph_sprites[9], pantograph_sprites[10], pantograph_sprites[11],
                                             pantograph_sprites[12], pantograph_sprites[13], pantograph_sprites[14], pantograph_sprites[15]],
                                       'b': [pantograph_sprites[4], pantograph_sprites[5], pantograph_sprites[6], pantograph_sprites[7],
                                             pantograph_sprites[0], pantograph_sprites[1], pantograph_sprites[2], pantograph_sprites[3]],
                                       'B': [pantograph_sprites[12], pantograph_sprites[13], pantograph_sprites[14], pantograph_sprites[15],
                                             pantograph_sprites[8], pantograph_sprites[9], pantograph_sprites[10], pantograph_sprites[11]]}

        vehicle_input_image = Image.open(self.vehicle_source_input_path)
        # get the loc points
        loc_points = [(pixel[0], pixel[1], pixel[2]) for pixel in pixascan(vehicle_input_image) if pixel[2] == 226 or pixel[2] == 164]
        # loc points are in arbitrary row in source spritesheet but need to be moved up in output, so shift the y offset by the required amount
        loc_points = [(pixel[0], pixel[1] - (num_pantograph_rows * graphics_constants.spriterow_height), pixel[2]) for pixel in loc_points]
        # sort them in y order, this causes sprites to overlap correctly when there are multiple loc points for an angle
        loc_points = sorted(loc_points, key=lambda x: x[1])

        empty_spriterow_image = Image.open(os.path.join(currentdir, 'src', 'graphics', 'spriterow_template.png'))
        empty_spriterow_image = empty_spriterow_image.crop((0, 10, graphics_constants.spritesheet_width, 10 + graphics_constants.spriterow_height))
        #empty_spriterow_image.show()

        # create the empty spritesheet to paste into; in some cases this creates redundant spriterows, but it's fine
        pantograph_output_image = Image.new("P", (graphics_constants.spritesheet_width, (2 * num_pantograph_rows * graphics_constants.spriterow_height) + 10), 255)
        pantograph_output_image.putpalette(DOS_PALETTE)
        for i in range(num_pantograph_rows + 1):
            pantograph_output_image.paste(empty_spriterow_image, (0, 10 + (i * graphics_constants.spriterow_height)))

        state_map = spriterow_pantograph_state_maps[self.consist.pantograph_type][self.pantograph_state]
        for pixel in loc_points:
            angle_num = 0
            for counter, bbox in enumerate(self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed):
                if pixel[0] >= bbox[0]:
                    angle_num = counter
            pantograph_sprite_num = angle_num

            pantograph_width = pantograph_sprites[pantograph_sprite_num][0].size[0]
            pantograph_height = pantograph_sprites[pantograph_sprite_num][0].size[1]
            # the +1s for height adjust the crop box to include the loc point
            # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
            pantograph_bounding_box = (pixel[0],
                                       pixel[1] - pantograph_height + 1,
                                       pixel[0] + pantograph_width,
                                       pixel[1] + 1)
            if pixel[2] == 164:
                # it's b or B
                state_sprites = pantograph_state_sprite_map[state_map[1]]
            else:
                # it's a or A
                state_sprites = pantograph_state_sprite_map[state_map[0]]
            pantograph_output_image.paste(state_sprites[pantograph_sprite_num][0], pantograph_bounding_box, state_sprites[pantograph_sprite_num][1])

        # add debug sprites with vehicle-pantograph comp for ease of checking
        vehicle_debug_image = vehicle_input_image.copy().crop((0, 10, graphics_constants.spritesheet_width, 10 + graphics_constants.spriterow_height))
        pantograph_output_image.paste(vehicle_debug_image, (0, 10 + (num_pantograph_rows * graphics_constants.spriterow_height)))
        pantograph_debug_image = pantograph_output_image.copy().crop((0, 10, graphics_constants.spritesheet_width, 10 + graphics_constants.spriterow_height))
        pantograph_debug_mask = pantograph_debug_image.copy()
        pantograph_debug_mask = pantograph_debug_mask.point(lambda i: 0 if i == 255 or i == 0 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
        pantograph_output_image.paste(pantograph_debug_image, (0, 10 + (num_pantograph_rows * graphics_constants.spriterow_height)), pantograph_debug_mask)

        # make spritesheet
        pantograph_spritesheet = self.make_spritesheet_from_image(pantograph_output_image)
        crop_box_dest = (0,
                         10,
                         self.global_constants.sprites_max_x_extent,
                         10 + (2 * num_pantograph_rows * graphics_constants.spriterow_height))
        self.units.append(AppendToSpritesheet(pantograph_spritesheet, crop_box_dest))

    def render(self, consist, global_constants):
        self.units = []
        self.consist = consist
        self.global_constants = global_constants

        self.add_pantograph_spriterows()

        if self.consist.buy_menu_x_loc == 360:
            self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        # this will render a spritesheet with an additional suffix, separate from the vehicle spritesheet
        input_image = Image.open(self.vehicle_source_input_path).crop((0, 0, graphics_constants.spritesheet_width, 10))
        output_suffix = '_pantographs_' + self.pantograph_state
        self.render_common(input_image, self.units, output_suffix=output_suffix)


class GeneratePantographsUpSpritesheetPipeline(GeneratePantographsSpritesheetPipeline):
    """ Sparse subclass, solely to set pan 'up' state (simplest way to implement this). """
    pantograph_state = 'up' # lol, actually valid class vars

    def __init__(self):
        super().__init__()


class GeneratePantographsDownSpritesheetPipeline(GeneratePantographsSpritesheetPipeline):
    """ Sparse subclass, solely to set pan 'down' state (simplest way to implement this). """
    pantograph_state = 'down' # lol, actually valid class vars

    def __init__(self):
        super().__init__()


class ExtendSpriterowsForCompositedSpritesPipeline(Pipeline):
    """"
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

    def comp_chassis_and_body(self, body_image):
        crop_box_input_1 = (0,
                            10,
                            self.sprites_max_x_extent,
                            10 + graphics_constants.spriterow_height)
        chassis_image = Image.open(self.chassis_input_path).crop(crop_box_input_1)

        # roof is composited (N.B. gangways are not, just draw them in vehicle sprite, handling asymmetric railcar cases would be one step too far on automation)
        if self.vehicle_unit.roof is not None and not self.vehicle_unit.suppress_roof_sprite:
            crop_box_roof_dest = (0,
                                0,
                                self.sprites_max_x_extent,
                                graphics_constants.spriterow_height)
            roof_image = Image.open(self.roof_input_path).crop(crop_box_input_1)

            # the roof image has false colour pixels to aid drawing; remove these by converting to white, also convert any blue to white
            roof_image = roof_image.point(lambda i: 255 if i == 226 else i)

            # create a mask so that we paste only the roof pixels over the chassis (no blue pixels)
            roof_mask = roof_image.copy()
            roof_mask = roof_mask.point(lambda i: 0 if i == 255 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
            chassis_image.paste(roof_image, crop_box_roof_dest, roof_mask)

        # chassis and roofs are *always* symmetrical, with 4 angles drawn; for vehicles with asymmetric bodies, copy and paste to provide all 8 angles
        if self.vehicle_unit.symmetry_type == 'asymmetric':
            crop_box_input_2 = (self.global_constants.spritesheet_bounding_boxes_symmetric_unreversed[4][0],
                                0,
                                self.sprites_max_x_extent,
                                0 + graphics_constants.spriterow_height)
            chassis_image_2 = chassis_image.copy().crop(crop_box_input_2)

            crop_box_input_2_dest = (self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[0][0],
                                     0,
                                     self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[0][0] + chassis_image_2.size[0],
                                     0 + graphics_constants.spriterow_height)
            chassis_image.paste(chassis_image_2, crop_box_input_2_dest)

        # the body image has false colour pixels for the chassis, to aid drawing; remove these by converting to white, also convert any blue to white
        body_image = body_image.point(lambda i: 255 if (i in range(178, 192) or i == 0) else i)
        #body_image.show()

        # create a mask so that we paste only the vehicle pixels over the chassis (no blue pixels)
        body_mask = body_image.copy()
        body_mask = body_mask.point(lambda i: 0 if i == 255 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato

        #body_mask.show()
        crop_box_chassis_body_comp = (0,
                                 0,
                                 self.sprites_max_x_extent,
                                 0 + graphics_constants.spriterow_height)
        chassis_image.paste(body_image, crop_box_chassis_body_comp, body_mask)

        #chassis_image.show()
        return chassis_image

    def add_generic_spriterow(self):
        crop_box_source = (0,
                           self.base_yoffs,
                           self.sprites_max_x_extent,
                           self.base_yoffs + graphics_constants.spriterow_height)
        vehicle_generic_spriterow_input_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_source))

        # vehicle_generic_spriterow_input_image.show() # comment in to see the image when debugging
        vehicle_generic_spriterow_input_as_spritesheet = self.make_spritesheet_from_image(vehicle_generic_spriterow_input_image)

        crop_box_dest = (0,
                         0,
                         self.sprites_max_x_extent,
                         graphics_constants.spriterow_height)
        self.units.append(AppendToSpritesheet(vehicle_generic_spriterow_input_as_spritesheet, crop_box_dest))
        self.units.append(AddCargoLabel(label='EMPTY',
                                        x_offset=self.sprites_max_x_extent + 5,
                                        y_offset= -1 * graphics_constants.spriterow_height))

    def add_livery_spriterow(self):
        # one spriterow, no loading / loaded states, intended for tankers etc
        crop_box_source = (0,
                           self.base_yoffs,
                           self.sprites_max_x_extent,
                           self.base_yoffs + graphics_constants.spriterow_height)
        vehicle_livery_spriterow_input_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_source))

        # vehicle_generic_spriterow_input_image.show() # comment in to see the image when debugging
        vehicle_livery_spriterow_input_as_spritesheet = self.make_spritesheet_from_image(vehicle_livery_spriterow_input_image)

        for label, recolour_map in self.consist.gestalt_graphics.recolour_maps:
            crop_box_dest = (0,
                             0,
                             self.sprites_max_x_extent,
                             graphics_constants.spriterow_height)

            self.units.append(AppendToSpritesheet(vehicle_livery_spriterow_input_as_spritesheet, crop_box_dest))
            self.units.append(SimpleRecolour(recolour_map))
            self.units.append(AddCargoLabel(label=label,
                                            x_offset=self.sprites_max_x_extent + 5,
                                            y_offset= -1 * graphics_constants.spriterow_height))

    def add_pax_mail_car_with_opening_doors_spriterows(self, row_count):
        for row_num in range(int(row_count / 2)):
            # this is complex necessarily
            # 'first' and 'last' vehicles tend to be asymmetric, but only one direction is drawn for each
            # for the alternative direction, we swap the sprites for 'first' and 'last' by picking a different input row num
            # then we copy them into the first column of the spritesheet which is for the -> orientation
            # 'default' and 'special' vehicles are assumed to be symmetric, or near enough that it's not important to swap the sprites
            input_row_nums = [row_num]
            input_row_nums.append(self.consist.gestalt_graphics.get_asymmetric_source_row(row_num))

            # guard against the unexpected eh, although this should never be reached, it will help debugging in future if it is triggered
            assert(len(input_row_nums) == 2), "must be exactly 2 entries in input_row_nums list for %s; %s" % (self.consist.id, input_row_nums)

            # this loop builds the spriterow and comps doors etc
            # we repeat it twice per output row to create asymmetrical output from symmetrical input (see notes above)
            pax_mail_car_rows_image = Image.new("P", (graphics_constants.spritesheet_width, 2 * graphics_constants.spriterow_height), 255)
            pax_mail_car_rows_image.putpalette(DOS_PALETTE)

            # get doors
            doors_bboxes = self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed
            crop_box_doors_source = (doors_bboxes[1][0],
                                     self.base_yoffs + (row_num * graphics_constants.spriterow_height),
                                     doors_bboxes[3][0] + doors_bboxes[3][1],
                                     self.base_yoffs + (row_num * graphics_constants.spriterow_height) + graphics_constants.spriterow_height)
            doors_image = self.vehicle_source_image.copy().crop(crop_box_doors_source)

            # the doors image has false colour pixels for the body, to aid drawing; remove these by converting to white, also convert any blue to white
            doors_image = doors_image.point(lambda i: 255 if (i in range(178, 192) or i == 0) else i)
            #if self.consist.id == 'mail_car_pony_gen_4C':
                #doors_image.show()

            # create a mask so that we paste only the door pixels over the body (no blue pixels)
            doors_mask = doors_image.copy()
            doors_mask = doors_mask.point(lambda i: 0 if i == 255 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
            #doors_mask.show()

            for col_count, row_offset in enumerate([row_num * graphics_constants.spriterow_height for row_num in input_row_nums]):
                crop_box_source = (0,
                                   self.base_yoffs + row_offset,
                                   self.sprites_max_x_extent,
                                   self.base_yoffs + row_offset + graphics_constants.spriterow_height)
                pax_mail_car_spriterow_input_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_source))

                crop_box_comped_body_and_chassis = (self.second_col_start_x,
                                                    0,
                                                    self.second_col_start_x + self.col_image_width,
                                                    graphics_constants.spriterow_height)

                pax_mail_car_spriterow_input_image = pax_mail_car_spriterow_input_image.crop(crop_box_comped_body_and_chassis)

                #empty/loaded state and loading state will need pasting once each, so two crop boxes needed
                crop_box_comp_col_dest_1 = (0,
                                            0,
                                            self.col_image_width,
                                            graphics_constants.spriterow_height)
                crop_box_comp_col_dest_2 = (0,
                                            graphics_constants.spriterow_height,
                                            self.col_image_width,
                                            2 * graphics_constants.spriterow_height)
                crop_box_comp_col_dest_doors = (doors_bboxes[1][0] - doors_bboxes[0][0],
                                                graphics_constants.spriterow_height,
                                                doors_bboxes[1][0] - doors_bboxes[0][0] + doors_image.size[0],
                                                2 * graphics_constants.spriterow_height)

                pax_mail_car_col_image = Image.new("P", (self.col_image_width, 2 * graphics_constants.spriterow_height))
                pax_mail_car_col_image.putpalette(DOS_PALETTE)
                pax_mail_car_col_image.paste(pax_mail_car_spriterow_input_image, crop_box_comp_col_dest_1)
                pax_mail_car_col_image.paste(pax_mail_car_spriterow_input_image, crop_box_comp_col_dest_2)
                # add doors
                pax_mail_car_col_image.paste(doors_image, crop_box_comp_col_dest_doors, doors_mask)
                #if self.consist.id == 'luxury_passenger_car_pony_gen_6A':
                     #pax_mail_car_col_image.show()

                row_dest_start_x = [self.second_col_start_x, self.first_col_start_x][col_count]
                crop_box_comp_row_dest = (row_dest_start_x,
                                          0,
                                          row_dest_start_x + self.col_image_width,
                                          2 * graphics_constants.spriterow_height)
                pax_mail_car_rows_image.paste(pax_mail_car_col_image, crop_box_comp_row_dest)
            #if self.consist.id == 'luxury_passenger_car_pony_gen_6A':
                 #pax_mail_car_rows_image.show()

            crop_box_dest = (0,
                             0,
                             self.sprites_max_x_extent,
                             2 * graphics_constants.spriterow_height)
            pax_mail_car_rows_image_as_spritesheet = self.make_spritesheet_from_image(pax_mail_car_rows_image)

            self.units.append(AppendToSpritesheet(pax_mail_car_rows_image_as_spritesheet, crop_box_dest))

    def add_box_car_with_opening_doors_spriterows(self):
        # all wagons using this gestalt repaint the relevant base sprite for the wagon's generation and subtype
        id_base = self.consist.gestalt_graphics.id_base
        if self.consist.base_track_type == 'NG':
            id_base = id_base + '_ng'
        box_car_id = self.consist.get_wagon_id(id_base=id_base, roster=self.consist.roster.id, gen=self.consist.gen, subtype=self.consist.subtype + '.png')
        box_car_input_path = os.path.join(currentdir, 'src', 'graphics', self.consist.roster_id, box_car_id)

        # two spriterows, closed doors and open doors
        crop_box_source_1 = (0,
                             self.base_yoffs,
                             self.sprites_max_x_extent,
                             self.base_yoffs + graphics_constants.spriterow_height)
        crop_box_source_2 = (0,
                             self.base_yoffs + graphics_constants.spriterow_height,
                             self.sprites_max_x_extent,
                             self.base_yoffs + 2 * graphics_constants.spriterow_height)
        box_car_input_image_1 = self.comp_chassis_and_body(Image.open(box_car_input_path).crop(crop_box_source_1))
        box_car_input_image_2 = self.comp_chassis_and_body(Image.open(box_car_input_path).crop(crop_box_source_2))
        #box_car_input_image_1.show() # comment in to see the image when debugging

        # empty/loaded state and loading state will need pasting once each, so two crop boxes needed
        # open doors are shown, but no cargo, TMWFTLB, see notes in GestaltGraphicsBoxCarOpeningDoors
        crop_box_comp_dest_1 = (0,
                                0,
                                self.sprites_max_x_extent,
                                graphics_constants.spriterow_height)
        crop_box_comp_dest_2 = (0,
                                graphics_constants.spriterow_height,
                                self.sprites_max_x_extent,
                                2 * graphics_constants.spriterow_height)
        box_car_rows_image = Image.new("P", (graphics_constants.spritesheet_width, 2 * graphics_constants.spriterow_height))
        box_car_rows_image.putpalette(DOS_PALETTE)

        box_car_rows_image.paste(box_car_input_image_1, crop_box_comp_dest_1)
        box_car_rows_image.paste(box_car_input_image_2, crop_box_comp_dest_2)

        crop_box_dest = (0,
                         0,
                         self.sprites_max_x_extent,
                         2 * graphics_constants.spriterow_height)

        box_car_rows_image_as_spritesheet = self.make_spritesheet_from_image(box_car_rows_image)

        self.units.append(AppendToSpritesheet(box_car_rows_image_as_spritesheet, crop_box_dest))
        self.units.append(SimpleRecolour(self.consist.gestalt_graphics.recolour_map))

    def add_caboose_spriterows(self, row_count):
        for row_num in range(int(row_count/2)):
            row_offset = row_num * graphics_constants.spriterow_height

            crop_box_source = (0,
                               self.base_yoffs + row_offset,
                               self.sprites_max_x_extent,
                               self.base_yoffs + row_offset + graphics_constants.spriterow_height)
            caboose_car_spriterow_input_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_source))

            crop_box_comp_dest = (0,
                                  0,
                                  self.sprites_max_x_extent,
                                  graphics_constants.spriterow_height)
            caboose_car_rows_image = Image.new("P", (graphics_constants.spritesheet_width, graphics_constants.spriterow_height))
            caboose_car_rows_image.putpalette(DOS_PALETTE)

            caboose_car_rows_image.paste(caboose_car_spriterow_input_image, crop_box_comp_dest)
            #caboose_car_rows_image.show()

            crop_box_dest = (0,
                             0,
                             self.sprites_max_x_extent,
                             graphics_constants.spriterow_height)

            caboose_car_rows_image_as_spritesheet = self.make_spritesheet_from_image(caboose_car_rows_image)

            self.units.append(AppendToSpritesheet(caboose_car_rows_image_as_spritesheet, crop_box_dest))
            self.units.append(SimpleRecolour(self.consist.gestalt_graphics.recolour_map_1))
            self.units.append(AppendToSpritesheet(caboose_car_rows_image_as_spritesheet, crop_box_dest))
            self.units.append(SimpleRecolour(self.consist.gestalt_graphics.recolour_map_2))

    def add_bulk_cargo_spriterows(self):
        cargo_group_row_height = 2 * graphics_constants.spriterow_height

        crop_box_cargo = (self.second_col_start_x,
                          self.base_yoffs,
                          self.second_col_start_x + self.col_image_width,
                          self.base_yoffs + (2 * graphics_constants.spriterow_height))
        cargo_base_image = self.vehicle_source_image.copy().crop(crop_box_cargo)
        # the loading/loaded image has false colour pixels for the cargo; keep only these, removing everything else
        cargo_base_image = cargo_base_image.point(lambda i: 255 if (i not in range(170, 177)) else i)
        #if self.consist.id == "dump_car_pony_gen_3A":
            #cargo_base_image.show()

        # create a mask so that we paste only the cargo pixels over the body (no blue pixels)
        cargo_base_mask = cargo_base_image.copy()
        cargo_base_mask = cargo_base_mask.point(lambda i: 0 if i == 255 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
        #if self.consist.id == "dump_car_pony_gen_3A":
            #cargo_base_mask.show()

        #loading and loaded state will need pasting once each, so two crop boxes needed
        crop_box_comp_dest_1 = (0,
                                0,
                                self.sprites_max_x_extent,
                                graphics_constants.spriterow_height)
        crop_box_comp_dest_2 = (0,
                                graphics_constants.spriterow_height,
                                self.sprites_max_x_extent,
                                2 * graphics_constants.spriterow_height)
        crop_box_comp_dest_3 = (self.second_col_start_x,
                                0,
                                self.second_col_start_x + self.col_image_width,
                                2 * graphics_constants.spriterow_height)

        # 2 sets of rows iff there's a second livery, otherwise 1
        for livery_counter in range(self.consist.gestalt_graphics.num_visible_cargo_liveries):
            empty_row_livery_offset = livery_counter * graphics_constants.spriterow_height
            crop_box_vehicle_body = (0,
                                     self.cur_vehicle_empty_row_yoffs + empty_row_livery_offset,
                                     self.sprites_max_x_extent,
                                     self.cur_vehicle_empty_row_yoffs + empty_row_livery_offset + graphics_constants.spriterow_height)

            vehicle_base_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_vehicle_body))
            #vehicle_base_image.show()

            bulk_cargo_rows_image = Image.new("P", (graphics_constants.spritesheet_width, cargo_group_row_height), 255)
            bulk_cargo_rows_image.putpalette(DOS_PALETTE)

            # paste the empty state into two rows, then paste the cargo over those rows
            bulk_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_1)
            bulk_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_2)
            bulk_cargo_rows_image.paste(cargo_base_image, crop_box_comp_dest_3, cargo_base_mask)
            #if self.consist.id == "dump_car_pony_gen_3A":
                #bulk_cargo_rows_image.show()

            crop_box_dest = (0,
                             0,
                             self.sprites_max_x_extent,
                             cargo_group_row_height)
            bulk_cargo_rows_image_as_spritesheet = self.make_spritesheet_from_image(bulk_cargo_rows_image)

            for label, recolour_map in polar_fox.constants.bulk_cargo_recolour_maps:
                self.units.append(AppendToSpritesheet(bulk_cargo_rows_image_as_spritesheet, crop_box_dest))
                self.units.append(SimpleRecolour(recolour_map))
                self.units.append(AddCargoLabel(label=label,
                                                x_offset=self.sprites_max_x_extent + 5,
                                                y_offset=  -1 * cargo_group_row_height))

    def add_heavy_items_cargo_spriterows(self):
        # indivisible cargos, generation-specific sprites, asymmetric, pre-positioned to suit the vehicle
        # used for supply cars, others if needed
        crop_box_source = (0,
                           10,
                           self.sprites_max_x_extent,
                           10 + graphics_constants.spriterow_height)
        vehicle_spriterow_input_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_source))

        # n.b. keys have to be sorted as order needs to be consistent everywhere
        for cargo_filename in sorted(self.consist.gestalt_graphics.heavy_items_sprites_to_cargo_labels_maps.keys()):
            cargo_filename = cargo_filename + '_' +  str(4 * self.vehicle_unit.vehicle_length) + 'px'
            cargo_sprites_input_path = os.path.join(currentdir, 'src', 'graphics', 'heavy_items_cargo', cargo_filename + '.png')
            # !! temp, needs defined per cargo graphic type
            cargo_spriterow_offset = {1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0}[self.consist.gen]

            crop_box_cargo_source = (0,
                                     10 + (cargo_spriterow_offset * graphics_constants.spriterow_height),
                                     self.sprites_max_x_extent,
                                     10 + ((cargo_spriterow_offset + 1) * graphics_constants.spriterow_height))

            cargo_image = Image.open(cargo_sprites_input_path).crop(crop_box_cargo_source)
            #if cargo_filename == 'trucks_1_32px':
                #cargo_image.show()

            # the cargo image has false colour pixels for the chassis, to aid drawing; remove these by converting to white, also convert any blue to white
            cargo_image = cargo_image.point(lambda i: 255 if (i in range(178, 192) or i == 0) else i)

            # create a mask so that we paste only the cargo pixels over the body (no blue pixels)
            cargo_mask = cargo_image.copy()
            cargo_mask = cargo_image.point(lambda i: 0 if i == 255 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
            # cargo_mask.show()

            crop_box_cargo_dest = (0,
                                   0,
                                   self.sprites_max_x_extent,
                                   graphics_constants.spriterow_height)

            vehicle_comped_image = vehicle_spriterow_input_image.copy()
            vehicle_comped_image.paste(cargo_image, crop_box_cargo_dest, cargo_mask)
            # vehicle_comped_image_as_spritesheet.show()

            crop_box_comp_dest = (0,
                                  0,
                                  self.sprites_max_x_extent,
                                  graphics_constants.spriterow_height)

            vehicle_comped_image_as_spritesheet = self.make_spritesheet_from_image(vehicle_comped_image)

            # loaded and loading states are same for these vehicles, but template expects spriterows for both, so add result twice
            self.units.append(AppendToSpritesheet(vehicle_comped_image_as_spritesheet, crop_box_comp_dest))
            self.units.append(AppendToSpritesheet(vehicle_comped_image_as_spritesheet, crop_box_comp_dest))
            self.units.append(AddCargoLabel(label=cargo_filename,
                                            x_offset=self.sprites_max_x_extent + 5,
                                            y_offset= -1 * graphics_constants.spriterow_height))

    def add_piece_cargo_spriterows(self):
        # !! this could possibly be optimised by slicing all the cargos once, globally, instead of per-unit
        cargo_group_output_row_height = 2 * graphics_constants.spriterow_height

        # Cargo spritesheets provide multiple lengths, using a specific format of rows
        # given a base set, find the bounding boxes for the rows per length
        cargo_spritesheet_bounding_boxes = {}
        for counter, length in enumerate([3, 4, 5, 6, 7, 8]):
            bb_result = []
            for y_offset in [0, 30]:
                bb_y_offset = (counter * 60) + y_offset
                bb_result.extend(tuple([(i[0], i[1] + bb_y_offset, i[2], i[3] + bb_y_offset) for i in polar_fox.constants.cargo_spritesheet_bounding_boxes_base]))
            cargo_spritesheet_bounding_boxes[length] = bb_result

        # Overview
        # 2 spriterows for the vehicle loading / loaded states, with pink loc points for cargo
        # a mask row for the vehicle, with pink mask area, which is converted to black and white mask image
        # an overlay for the vehicle, created from the vehicle empty state spriterow, and comped with the mask after each cargo has been placed
        # - there is a case not handled, where long cargo sprites will overlap cabbed vehicles in / direction with cab at N end, hard to solve
        # - this has no awareness of vehicle symmetry_type property, so will needlessly scan too many pixels for symmetric vehicles
        #   that's TMWFTLB to fix right now, as it will require relative offsets of all the loc points for probably very little performance gain
        crop_box_vehicle_cargo_loc_row = (self.second_col_start_x,
                                          self.base_yoffs,
                                          self.second_col_start_x + self.col_image_width,
                                          self.base_yoffs + graphics_constants.spriterow_height)
        vehicle_cargo_loc_image = self.vehicle_source_image.copy().crop(crop_box_vehicle_cargo_loc_row)
        # get the loc points
        loc_points = [(pixel[0] + self.second_col_start_x, pixel[1], pixel[2]) for pixel in pixascan(vehicle_cargo_loc_image) if pixel[2] == 226]
        # two cargo rows needed, so extend the loc points list
        loc_points.extend([(pixel[0], pixel[1] + 30, pixel[2]) for pixel in loc_points])
        # sort them in y order, this causes sprites to overlap correctly when there are multiple loc points for an angle
        loc_points = sorted(loc_points, key=lambda x: x[1])

        crop_box_vehicle_body = (0,
                                 self.cur_vehicle_empty_row_yoffs,
                                 self.sprites_max_x_extent,
                                 self.cur_vehicle_empty_row_yoffs + graphics_constants.spriterow_height)
        vehicle_base_image = self.comp_chassis_and_body(self.vehicle_source_image.copy().crop(crop_box_vehicle_body))

        crop_box_mask_source = (self.second_col_start_x,
                                self.base_yoffs + graphics_constants.spriterow_height,
                                self.second_col_start_x + self.col_image_width,
                                self.base_yoffs + (2 * graphics_constants.spriterow_height))
        crop_box_mask_dest = (self.second_col_start_x,
                              0,
                              self.second_col_start_x + self.col_image_width,
                              graphics_constants.spriterow_height)
        vehicle_mask_source = self.vehicle_source_image.copy().crop(crop_box_mask_source).point(lambda i: 255 if i == 226 else 0).convert("1")
        vehicle_mask = Image.new("1", (self.sprites_max_x_extent, graphics_constants.spriterow_height), 0)
        vehicle_mask.paste(vehicle_mask_source, crop_box_mask_dest)
        #if self.consist.id == "open_car_pony_gen_1A":
            #vehicle_mask.show()

        #mask and empty state will need pasting once for each of two cargo rows, so two crop boxes needed
        crop_box_comp_dest_1 = (0,
                                0,
                                self.sprites_max_x_extent,
                                graphics_constants.spriterow_height)
        crop_box_comp_dest_2 = (0,
                                graphics_constants.spriterow_height,
                                self.sprites_max_x_extent,
                                2 * graphics_constants.spriterow_height)

        piece_cargo_rows_image = Image.new("P", (graphics_constants.spritesheet_width, cargo_group_output_row_height))
        piece_cargo_rows_image.putpalette(DOS_PALETTE)
        # paste empty states in for the cargo rows (base image = empty state)
        piece_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_1)
        piece_cargo_rows_image.paste(vehicle_base_image, crop_box_comp_dest_2)
        #if self.consist.id == "open_car_pony_gen_1A":
            #piece_cargo_rows_image.show()
        crop_box_dest = (0,
                         0,
                         self.sprites_max_x_extent,
                         cargo_group_output_row_height)

        for cargo_filename in polar_fox.constants.piece_vehicle_type_to_sprites_maps[self.consist.gestalt_graphics.piece_type]:
            # get a list, with a two-tuple (cargo_sprite, mask) for each of 4 angles
            # cargo sprites are assumed to be symmetrical, only 4 angles are needed
            # cargos with 8 angles (e.g. bulldozers) aren't handled here, assume heavy_items_cargo should handle those (might need extended)
            # loading states are first 4 sprites, loaded are second 4, all in one list, just pick them out as needed
            cargo_sprites_input_path = os.path.join(currentdir, 'src', 'polar_fox', 'cargo_graphics', cargo_filename + '.png')
            cargo_sprites_input_image = Image.open(cargo_sprites_input_path)
            # n.b. Iron Horse assumes cargo length is always equivalent from vehicle length (probably fine)
            cargo_sprites = self.get_arbitrary_angles(cargo_sprites_input_image, cargo_spritesheet_bounding_boxes[self.vehicle_unit.vehicle_length])

            vehicle_comped_image = piece_cargo_rows_image.copy()

            for pixel in loc_points:
                angle_num = 0
                for counter, bbox in enumerate(self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed):
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
                cargo_bounding_box = (pixel[0],
                                      pixel[1] - cargo_height + 1,
                                      pixel[0] + cargo_width,
                                      pixel[1] + 1)
                vehicle_comped_image.paste(cargo_sprites[cargo_sprite_num][0], cargo_bounding_box, cargo_sprites[cargo_sprite_num][1])

            # vehicle overlay with mask - overlays any areas where cargo shouldn't show
            vehicle_comped_image.paste(vehicle_base_image, crop_box_comp_dest_1, vehicle_mask)
            vehicle_comped_image.paste(vehicle_base_image, crop_box_comp_dest_2, vehicle_mask)
            #if self.consist.id == "open_car_pony_gen_1A":
                #vehicle_comped_image.show()

            vehicle_comped_image_as_spritesheet = self.make_spritesheet_from_image(vehicle_comped_image)

            self.units.append(AppendToSpritesheet(vehicle_comped_image_as_spritesheet, crop_box_dest))
            self.units.append(AddCargoLabel(label=cargo_filename,
                                            x_offset=self.sprites_max_x_extent + 5,
                                            y_offset= -1 * cargo_group_output_row_height))

    def render(self, consist, global_constants):
        self.units = [] # graphics units not same as consist units ! confusing overlap of terminology :(
        self.consist = consist
        self.global_constants = global_constants
        self.sprites_max_x_extent = self.global_constants.sprites_max_x_extent
        self.first_col_start_x = self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[0][0]
        self.second_col_start_x = self.global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[4][0]
        self.col_image_width = self.sprites_max_x_extent - self.second_col_start_x

        self.vehicle_source_image = Image.open(self.vehicle_source_input_path)

        # the cumulative_input_spriterow_count updates per processed group of spriterows, and is key to making this work
        # !! input_spriterow_count looks a bit weird though; I tried moving it to gestalts, but didn't really work
        cumulative_input_spriterow_count = 0
        for vehicle_counter, vehicle_rows in enumerate(self.consist.get_spriterows_for_consist_or_subpart(self.consist.unique_units)):
            # 'vehicle_unit' not 'unit' to avoid conflating with graphics processor 'unit'
            self.vehicle_unit = self.consist.unique_units[vehicle_counter] # !!  this is ugly hax, I didn't want to refactor the iterator above to contain the vehicle
            self.cur_vehicle_empty_row_yoffs = 10 + cumulative_input_spriterow_count * graphics_constants.spriterow_height
            for spriterow_type in vehicle_rows:
                self.base_yoffs = 10 + (graphics_constants.spriterow_height * cumulative_input_spriterow_count)
                if spriterow_type == 'always_use_same_spriterow' or spriterow_type == 'empty':
                    input_spriterow_count = 1
                    self.add_generic_spriterow()
                elif spriterow_type == 'livery_spriterow':
                    input_spriterow_count = 1
                    self.add_livery_spriterow()
                elif spriterow_type == 'box_car_with_opening_doors_spriterows':
                    input_spriterow_count = 2
                    self.add_box_car_with_opening_doors_spriterows()
                elif spriterow_type == 'caboose_spriterows':
                    input_spriterow_count = 2 * self.consist.gestalt_graphics.num_generations
                    self.add_caboose_spriterows(input_spriterow_count)
                elif spriterow_type == 'pax_mail_cars_with_doors':
                    # 2 liveries with 2 rows each: empty & loaded (doors closed), loading (doors open)
                    input_spriterow_count = 4 * self.consist.gestalt_graphics.num_cargo_sprite_variants
                    self.add_pax_mail_car_with_opening_doors_spriterows(input_spriterow_count)
                elif spriterow_type == 'bulk_cargo':
                    input_spriterow_count = 2
                    self.add_bulk_cargo_spriterows()
                elif spriterow_type == 'heavy_items_cargo':
                    input_spriterow_count = 1
                    self.add_heavy_items_cargo_spriterows()
                elif spriterow_type == 'piece_cargo':
                    input_spriterow_count = 2
                    self.add_piece_cargo_spriterows()
                cumulative_input_spriterow_count += input_spriterow_count
            # self.vehicle_unit is hax, and is only valid inside this loop, so clear it to prevent incorrectly relying on it outside the loop in future :P
            self.vehicle_unit = None

        if self.consist.buy_menu_x_loc == 360:
            self.units.append(AddBuyMenuSprite(self.process_buy_menu_sprite))

        # for this pipeline, input_image is just blank white 10px high image, to which the vehicle sprites are then appended
        input_image = Image.new("P", (graphics_constants.spritesheet_width, 10), 255)
        input_image.putpalette(DOS_PALETTE)
        self.render_common(input_image, self.units)


def get_pipelines(pipeline_names):
    # return a pipeline by name;
    # add pipelines here when creating new ones
    # this is a bit hokey, there's probably a simpler way to do this but eh
    # looks like it could be replaced by a simple dict lookup directly from gestalt_graphics, but eh, I tried, it's faff
    pipelines = {"pass_through_pipeline": PassThroughPipeline,
                 "check_buy_menu_only": CheckBuyMenuOnlyPipeline,
                 "extend_spriterows_for_composited_sprites_pipeline": ExtendSpriterowsForCompositedSpritesPipeline,
                 "generate_pantographs_up_spritesheet": GeneratePantographsUpSpritesheetPipeline,
                 "generate_pantographs_down_spritesheet": GeneratePantographsDownSpritesheetPipeline}
    return [pipelines[pipeline_name]() for pipeline_name in pipeline_names]

def main():
    print("yeah, pipelines.main() does nothing")

if __name__ == '__main__':
    main()
