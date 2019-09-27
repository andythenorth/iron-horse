import polar_fox
import gestalt_graphics.graphics_constants as graphics_constants
from gestalt_graphics import pipelines
import utils

class GestaltGraphics(object):
    """
        Simple class, which is extended in sub-classes to configure:
         - base vehicle recolour (if any)
         - cargo graphics (if any)
         - pantographs (if any)
         - other processing as required
    """
    def __init__(self):
        # by default, check for buy menu only
        self.pipelines = pipelines.get_pipelines(['check_buy_menu_only'])

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        return 'vehicle_default.pynml'

    @property
    def num_cargo_sprite_variants(self):
        # this tends to be common across multiple templates, so provide it in the base class
        # rows can be reused across multiple cargo labels, so find uniques (assumes row nums are identical when reused across labels)
        # !! fails if the subclass doesn't have cargo_row_map
        row_nums_seen = []
        for row_nums in self.cargo_row_map.values():
            for row_num in row_nums:
                row_nums_seen.append(row_num)
        return len(set(row_nums_seen))

    def get_output_row_types(self):
        # stub, for compatibility reasons
        return ['single_row']


class GestaltGraphicsOnlyAddPantographs(GestaltGraphics):
    """
        Simple Gestalt specifically for engines that have absolutely no other graphics processing except pantograph generation.
        Any Gestalt can also add pantographs as needed (it's a method on Pipeline base class).
    """
    def __init__(self):
        # no graphics processing by default
        self.pipelines = pipelines.get_pipelines(['check_buy_menu_only', 'generate_pantographs_up_spritesheet', 'generate_pantographs_down_spritesheet'])


class GestaltGraphicsVisibleCargo(GestaltGraphics):
    """
        Used for vehicle with visible cargos
        Supports *only* pixa-generated cargos; mixing with custom cargo rows isn't handled, TMWFTLB
        Should not be used with 'random_reverse' property, composited cargos are symmetric, so cargo template doesn't handle random_reverse.
    """
    def __init__(self, **kwargs):
        super().__init__()
        self.pipelines = pipelines.get_pipelines(['extend_spriterows_for_composited_sprites_pipeline'])
        # default body recolour to CC1, pass param to over-ride as needed
        self.body_recolour_map = kwargs.get('body_recolour_map', graphics_constants.body_recolour_CC1)
        # option for alternative livery, will be selected by player flip on depot, default to 1 if not set
        self.num_visible_cargo_liveries = 2 if kwargs.get('has_alt_livery', False) else 1
        # cargo flags
        self.has_bulk = kwargs.get('bulk', False)
        self.has_heavy_items = kwargs.get('heavy_items', None) is not None
        self.has_piece = kwargs.get('piece', None) is not None
        if self.has_piece:
            self.piece_type = kwargs.get('piece')

    @property
    def generic_rows(self):
        # map unknown cargos to sprites for some other label
        # assume that piece > input_spriterow_count, it's acceptable to show something like tarps for bulk, but not gravel for piece
        if self.has_piece or self.has_heavy_items:
            return self.cargo_row_map['DFLT']
        elif self.has_bulk:
            return self.cargo_row_map['GRVL']
        else:
            # shouldn't reach here, but eh,
            utils.echo_message('generic_rows hit an unknown result in GestaltGraphics')
            return ['FAIL']

    @property
    def nml_template(self):
        return 'vehicle_with_visible_cargo.pynml'

    def get_output_row_types(self):
        result = []
        # assume an empty state spriterow per livery
        for i in range(self.num_visible_cargo_liveries):
            result.append('empty')

        if self.has_bulk:
            result.append('bulk_cargo')
        if self.has_heavy_items:
            result.append('heavy_items_cargo')
        if self.has_piece:
            result.append('piece_cargo')
        return result

    @property
    def cargo_row_map(self):
        result = {}
        counter = 0
        if self.has_bulk:
            for cargo_map in polar_fox.constants.bulk_cargo_recolour_maps:
                result[cargo_map[0]] = [counter] # list because multiple spriterows can map to a cargo label
                counter += 1
        if self.has_heavy_items:
            # n.b. keys have to be sorted as order needs to be consistent everywhere
            for cargo_filename, cargo_labels in sorted(self.heavy_items_sprites_to_cargo_labels_maps.items(), key = lambda x: x[0]):
                for cargo_label in cargo_labels:
                    result.setdefault(cargo_label, []).append(counter)
                counter += 1
        if self.has_piece:
            # handle that piece cargos are defined in dicts as {filename:[labels]}, where most cargo sprite stuff uses ((label, values), (label, values)) pairs format
            for cargo_filename in polar_fox.constants.piece_vehicle_type_to_sprites_maps[self.piece_type]:
                for cargo_label in polar_fox.constants.piece_sprites_to_cargo_labels_maps[cargo_filename]:
                    result.setdefault(cargo_label, []).append(counter)
                counter += 1
        return result

    @property
    def unique_spritesets(self):
        # the template for this gestalt was getting complex with loops and logic where logic shouldn't be
        # so instead we delegate that logic here and simplify the loop
        # this builds heavily on the row numbers already in cargo_row_map, reformatting that data to make it easy to render in the template
        row_nums_seen = []
        result = []
        for row_nums in self.cargo_row_map.values():
            for row_num in row_nums:
                row_nums_seen.append(row_num)
        unique_cargo_rows = set(row_nums_seen)

        row_height = graphics_constants.spriterow_height
        start_y = graphics_constants.spritesheet_top_margin
        empty_state_offset = 0

        for flipped in ['unflipped', 'flipped']:
            # there are _always_ two liveries (flipped and unflipped)
            # but some vehicles have custom realsprites for the second livery, not just a recolor
            # so add another empty row and do some offset admin
            if self.num_visible_cargo_liveries == 2:
                if flipped == 'unflipped':
                    # cargo rows need an offset for 2 empty rows
                    cargo_rows_base_y_offset = start_y + (2 * row_height)
                else:
                    # empty state needs an offset to the flipped empty state
                    empty_state_offset = row_height
                    # cargo rows need an offset for 2 empty rows, plus the previous livery
                    cargo_rows_base_y_offset = start_y + (2 * row_height) + (len(unique_cargo_rows) * 2 * row_height)
            else:
                # cargo rows need an offset for just 1 empty row
                cargo_rows_base_y_offset = start_y + row_height

            # add a row for empty sprite
            result.append(['empty', flipped, start_y + empty_state_offset])

            # !! not sure unique_cargo_rows order will always reliably match to what's needed, but if it doesn't, explicitly sort it eh
            for row_num in unique_cargo_rows:
                row_y_offset = cargo_rows_base_y_offset + (row_num * 2 * row_height)
                result.append(['loading_' + str(row_num), flipped, row_y_offset])
                result.append(['loaded_' + str(row_num), flipped, row_y_offset + 30])
        return result


    # !! possibly move this to polar fox later, currently heavy item cargos are restricted to Iron Horse, but will be needed in Road Hog at least
    # cargo labels can be repeated for different sprites, they'll be used selectively by vehicle types and/or randomised as appropriate
    # keep alphabetised for general quality-of-life
    # DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
    heavy_items_sprites_to_cargo_labels_maps = {'tarps_2cc_1': ['DFLT'], # see note on use of DFLT above
                                                'tractors_1': ['FMSP'],
                                                'trucks_2': ['ENSP', 'FMSP', 'VEHI'],
                                                'trucks_3': ['ENSP', 'FMSP', 'VEHI'],
                                                'trucks_4': ['ENSP', 'FMSP', 'VEHI'],
                                                'trucks_5': ['ENSP', 'FMSP', 'VEHI']}


class GestaltGraphicsBoxCarOpeningDoors(GestaltGraphics):
    """
        Used to handle the specific case of box-type freight cars
        - base boxcar template for generation is recoloured to make refrigerated car, fruit & veg car etc
        - doors open during loading
        - no cargo is shown by design (TMWFTLB: piece sprites could be generated in, but setting up masks etc for all vehicles is unwanted complexity)
    """
    def __init__(self, recolour_maps, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipelines = pipelines.get_pipelines(['extend_spriterows_for_composited_sprites_pipeline'])
        # common format for recolour_maps provides multiple remaps
        # but just one livery remap is supported for this gestalt, and should be the first in the remap list
        self.recolour_map = recolour_maps[0][1]
        self.id_base = kwargs.get('id_base')

    @property
    def generic_rows(self):
        utils.echo_message ('generic_rows not implemented in GestaltGraphicsBoxCarOpeningDoorsGestaltGraphics (by design)')
        return None

    @property
    def nml_template(self):
        return 'vehicle_box_car_with_opening_doors.pynml'

    def get_output_row_types(self):
        return ['box_car_with_opening_doors_spriterows']

    @property
    def cargo_row_map(self):
        utils.echo_message ('cargo_row_map not implemented in GestaltGraphicsBoxCarOpeningDoorsGestaltGraphics (by design)')
        return None


class GestaltGraphicsCaboose(GestaltGraphics):
    """
        Used to handle specific rules for caboose cars
        - colour remap
        - specific livery variants (pixels, not just colour remap) for specific engine IDs
    """
    def __init__(self, num_generations, recolour_maps, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipelines = pipelines.get_pipelines(['extend_spriterows_for_composited_sprites_pipeline'])
        self.num_generations = num_generations
        # common format for recolour_maps provides multiple remaps
        # but just one livery remap is supported for this gestalt, and should be the first in the remap list
        self.recolour_map_1 = recolour_maps[0][1]
        self.recolour_map_2 = recolour_maps[1][1]

    @property
    def generic_rows(self):
        utils.echo_message ('generic_rows not implemented in GestaltGraphicsCaboose (by design)')
        return None

    @property
    def nml_template(self):
        return 'vehicle_caboose.pynml'

    def get_output_row_types(self):
        return ['caboose_spriterows']

    @property
    def cargo_row_map(self):
        utils.echo_message ('cargo_row_map not implemented in GestaltGraphicsCaboose (by design)')
        return None


class GestaltGraphicsIntermodal(GestaltGraphics):
    """
        Used to handle specific rules for intermodal cars
        - specific template to handle containers which are in separate layer
    """

    def __init__(self, **kwargs):
        # we use the composited sprites pipeline so we can make use of chassis compositing
        self.pipelines = pipelines.get_pipelines(['extend_spriterows_for_composited_sprites_pipeline'])
        self.consist_ruleset = kwargs.get('consist_ruleset', None)
        # intermodal cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        # two liveries
        self.asymmetric_row_map = {1: 1, 2: 2, # default: default
                                   3: 5, 4: 6, # first: last
                                   5: 3, 6: 4, # last: first
                                   7: 7, 8: 8} # middle: middle

    def get_output_row_types(self):
        # 2 liveries * 4 variants so 8 empty rows, we're only using the composited sprites pipeline for chassis compositing, containers are provided on separate layer
        # note to self, remarkably adding multiple empty rows appears to just work here :o
        return ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']

    @property
    def cargo_label_mapping(self):
        # tuple because type order is relied on for increasing specificity of cargo:type mapping
        # e.g. cryo tank > chemical tank > tank
        container_cargo_maps = (('box', ([], [])),
                                ('bulk', ([], polar_fox.constants.bulk_cargo_recolour_maps)),
                                #('flat', ([], [])),
                                ('livestock', (['LVST'], [])),
                                ('tank', ([], polar_fox.constants.tanker_livery_recolour_maps)),
                                ('edibles_tank', (polar_fox.constants.allowed_refits_by_label['edible_liquids'], [])),
                                ('chemicals_tank', (polar_fox.constants.allowed_refits_by_label['chemicals'],
                                                    polar_fox.constants.chemicals_tanker_livery_recolour_maps)),
                                ('cryo_tank', (polar_fox.constants.allowed_refits_by_label['cryo_gases'],
                                               polar_fox.constants.cryo_tanker_livery_recolour_maps)))

        result = {}
        for container_type, cargo_maps in container_cargo_maps:
            # first handle the cargos as explicitly refittable
            # lists of explicitly refittable cargos are by no means *all* the cargos refittable to for a type
            # nor does explicitly refittable cargos have 1:1 mapping with cargo-specific graphics
            # these will all map cargo_label: container_type_DFLT
            for cargo_label in cargo_maps[0]:
                if cargo_label in result and cargo_label not in ['DFLT']:
                   print('GestaltGraphicsIntermodal.cargo_label_mapping: cargo_label', cargo_label, 'already exists, being over-written by', container_type, 'label')
                result[cargo_label] = container_type + '_DFLT'

            # then insert or over-ride entries with cargo_label: container_type_[CARGO_LABEL] where there are explicit graphics for a cargo
            for cargo_label, recolour_map in cargo_maps[1]:
                if cargo_label in result and cargo_label not in ['DFLT']:
                   print('GestaltGraphicsIntermodal.cargo_label_mapping: cargo_label', cargo_label, 'already exists, being over-written by', container_type, 'label')
                result[cargo_label] = container_type + '_' + cargo_label
        return result

    @property
    def position_variants(self):
        # used in spriteset templating
        # 2 unit articulated sets only need 3 variants, > 2 units also need
        return ['default', 'first', 'last'] if self.consist_ruleset == '2_unit_sets' else ['default', 'first', 'last', 'middle']

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        return 'vehicle_intermodal.pynml'


class GestaltGraphicsCargoSpecificLivery(GestaltGraphics):
    """
        Used to handle the specific case of cargos shown only by vehicle livery.
        This can also be used with vehicles with just a *single* livery which isn't cargo-specific for
            - adding automated chassis
            - recolouring from false body colour (easier than using paint bucket on individual sprites)
    """
    def __init__(self, recolour_maps, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipelines = pipelines.get_pipelines(['extend_spriterows_for_composited_sprites_pipeline'])
        # recolour_maps map cargo labels to liveries, use 'DFLT' as the labe in the case of just one livery
        self.recolour_maps = recolour_maps

    @property
    def generic_rows(self):
        utils.echo_message ('generic_rows not implemented in GestaltGraphicsCargoSpecificLivery (by design)')
        return None

    @property
    def nml_template(self):
        return 'vehicle_with_cargo_specific_liveries.pynml'

    def get_output_row_types(self):
        return ['livery_spriterow']

    @property
    def cargo_row_map(self):
        # !! this works more by accident than design
        # !! the order of cargo types here must be kept in sync with the order in the cargo graphics processor
        result = {}
        counter = 0
        for cargo_map in self.recolour_maps:
            result[cargo_map[0]] = [counter] # list because multiple spriterows can map to a cargo label
            # !! ^ but this should be appending 'counter' to the list, not just replacing the entire list
            # !! ^^ no real consequence as long as only one livery per cargo label is used, but will need fixed if multiple liveries per label are ever needed
            counter += 1
        return result


class GestaltGraphicsConsistSpecificLivery(GestaltGraphics):
    """
        Used when the vehicle changes livery to match
        - the engine (based on engine 'role')
        - major cargo refit in the consist (mail vs. freight)
        - position in consist (pax restaurant cars etc)
        Intended for pax and mail cars
         - multiple engine roles might map to one livery
         - livery shown is specific to the engine role and/or the major cargo in the consist
         - player can toggle engine-livery or solid CC by flipping vehicle
         - intended for closed vehicles with doors, 'loaded' sprites are same as 'empty'
         - option to show cargo loading sprites (open doors) via 1 or 2 'loading' rows
       - vehicles can be configured to optionally show 1 of 4 different sprites depending on position in consist
            - 'default'
            - 'first'
            - 'last'
            - 'special'
        - 'positions' are flexible, and hax can safely be used within reason to get worthwhile results / save time
            - positions are controlled by consist_rulesets, defined per Consist type as needed
            - the positions are just keywords, mapped onto spriterow nums, and can be remapped fairly freely
        - the limit of 4 is arbitrary, and self-imposed to prevent combinatorial explosion (and consequent need to draw sprites)
    """
    def __init__(self, spriterow_group_mappings, **kwargs):
        # no graphics processing for this gestalt
        super().__init__()
        # spriterow_group_mappings provided by subclass calling gestalt_graphics:
        # (1) consist-cargo types for which specific liveries are provided
        # (2) spriterow numbers for named positions in consist
        # spriterow numbers are zero-indexed *relative* to the start of the consist-cargo block, to reduce shuffling them all if new rows are inserted in future
        # *all* of the values in consist_positions_ordered must be provided in the mapping, set them to 0 if unused
        self.spriterow_group_mappings = spriterow_group_mappings
        # rulesets are used to define for different types of vehicle how sprites change depending on consist position
        self.consist_ruleset = kwargs.get('consist_ruleset', None)
        # it's nice to use a dict for the consist position->row mapping, but order matters for the spritesheet, so have an ordered set of keys
        # also, although rulesets allow fine-grained control, there are deliberately only 4 configuration options
        # this stops rules getting out of control and simplifies other methods
        self.consist_positions_ordered = ['default', 'first', 'last', 'special']

        self.pipelines = pipelines.get_pipelines(['extend_spriterows_for_composited_sprites_pipeline'])
        if kwargs.get('pantograph_type', None) is not None:
            self.pipelines.extend(pipelines.get_pipelines(['generate_pantographs_up_spritesheet', 'generate_pantographs_down_spritesheet']))
            # this relies on DFLT mapping being safe to take
            # *and* assumes no gaps in the spriterows, so take the max spriterow num
            # *and* assumes 2 liveries are in use
            # note the +1 because livery rows are zero indexed
            self.num_pantograph_rows = 2 * (max([int(i) + 1 for i in self.cargo_row_map['DFLT']]))

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        return 'vehicle_with_consist_specific_liveries.pynml'

    def get_output_row_types(self):
        return ['pax_mail_cars_with_doors']

    def get_variants_with_position_keys(self, cargo_row_map):
        # just formatting for human-readable access to positions in templates where mapping[0][n] was fiddly
        # the cargo_row_map structure can't use a dict for compatibility reasons, so handle it here
        result = {}
        for i, name in enumerate(self.consist_positions_ordered):
            result[name] = cargo_row_map[1][i]
        return result

    @property
    def cargo_row_map(self):
        # This is tied completely to the spritesheet format, which as of April 2018 was:
        # - pax consist liveries (n vehicle variants x 2 liveries x 2 rows: empty & loaded, loading)
        # - mail consist liveries (n vehicle variants x 2 liveries x 2 rows: empty & loaded, loading)
        # these are mapped by the subclass using spriterow_group_mappings to consist positions that
        #   the template expects for e.g. restaurant cars, brake coaches etc
        result = {}
        counter = 0
        # this doesn't account for cargos like TOUR, but could be extended so cargo labels are a list, TMWFTLB as of April 2018 though
        # not a dict because order matters
        for livery_type, cargo_label in (('pax', 'PASS'), ('mail', 'MAIL')):
            if livery_type in self.spriterow_group_mappings:
                # we have to rebuild the row_nums in a predictable order (they're stored in a dict for convenience when configuring)
                relative_row_nums = [self.spriterow_group_mappings[livery_type][position] for position in self.consist_positions_ordered]
                result[cargo_label] = [counter + row_num for row_num in relative_row_nums] # we make relative row_nums absolute here
                counter += len(set(relative_row_nums))
        # we rely on DFLT here to explicitly catch the case for 'freight' (which has no label we can check)
        if 'DFLT' not in result.keys():
            # this will error if neither pax nor mail are defined
            # default to mail if available (to handle mail cars in freight consists)
            if 'MAIL' in result.keys():
                result['DFLT'] = result['MAIL']
            else:
                # fallback to pax if nothing else
                result['DFLT'] = result['PASS']
        return result

    @property
    def asymmetric_row_map(self):
        # used in graphics processor to figure out how to make correct asymmetric sprites for 'first' and 'last'
        # pax / mail cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        result = {}
        for variant in range(self.num_cargo_sprite_variants):
            # !! this is very hokey and assumes (by excluding mail) that only pax needs asymmetric, and will always need to flip row groups 1 and 2
            # !! if that fails in future, the actual 'first' and 'last' numbers can be looked up self.spriterow_group_mappings
            # !! just applying JFDI for now
            if variant == 1 and 'mail' not in self.spriterow_group_mappings:
                source_row_num = 2
            elif variant == 2 and 'mail' not in self.spriterow_group_mappings:
                source_row_num = 1
            else:
                source_row_num = variant
            # group of 4 rows - two liveries * two loaded/loading states (opening doors)
            for i in range(1, 5):
                result[(4 * variant) + i] = (4 * source_row_num) + i
        return(result)


class GestaltGraphicsCustom(GestaltGraphics):
    """
        Used to handle (rare) cases with hand-drawn cargo (no pixa-generated cargos).
        There is currently no graphics processing for this:
        - just a simple pass-through, and an interface to the nml templates
        - this could get support for body recolouring if needed
        - this should not get support for compositing custom rows, TMWFTLB, just draw them in the vehicle spritesheet
    """
    def __init__(self, _cargo_row_map, _nml_template, generic_rows):
        super().__init__()
        self.pipelines = pipelines.get_pipelines(['pass_through_pipeline'])
        # options
        self._nml_template = _nml_template
        self._cargo_row_map = _cargo_row_map
        self._generic_rows = generic_rows

    @property
    def generic_rows(self):
        # generic rows is normally automated, but for custom, get it from a manully specified property
        return self._generic_rows

    @property
    def nml_template(self):
        return self._nml_template

    def get_output_row_types(self):
        return ['custom_cargo']

    @property
    def cargo_row_map(self):
        return self._cargo_row_map
