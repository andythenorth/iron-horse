import graphics_processor.graphics_constants as graphics_constants
from graphics_processor import pipelines
import utils

class GestaltGraphics(object):
    """
        Simple stub class, which is extended in sub-classes to configure:
         - base vehicle recolour (if any)
         - cargo graphics (if any)
    """
    def __init__(self):
        # no graphics processing by default
        self.pipeline = None

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        return 'vehicle_default.pynml'

    @property
    def num_cargo_sprite_variants(self, cargo_type=None):
        # rows can be reused across multiple cargo labels, so find uniques (assumes row nums are identical when reused across labels)
        unique_row_nums = []
        for row_nums in self.cargo_row_map.values():
            if row_nums not in unique_row_nums:
                unique_row_nums.append(row_nums)
        return sum([len(i) for i in unique_row_nums])

    def get_output_row_counts_by_type(self):
        # stub, for template compatibility reasons
        return []


class GestaltGraphicsVisibleCargo(GestaltGraphics):
    """
        Used for vehicle with visible cargos
        Supports *only* pixa-generated cargos; mixing with custom cargo rows isn't handled, TMWFTLB
    """
    def __init__(self, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipeline = pipelines.get_pipeline('extend_spriterows_for_composited_cargos_pipeline')
        # default body recolour to CC1, pass param to over-ride as needed
        self.body_recolour_map = kwargs.get('body_recolour_map', graphics_constants.body_recolour_CC1)
        # cargo flags
        self.has_bulk = kwargs.get('bulk', False)
        self.has_piece = kwargs.get('piece', None) is not None
        if self.has_piece:
            self.piece_type = kwargs.get('piece')
        # required if piece is set, cargo sprites are available in multiple lengths, set the most appropriate
        self.cargo_length = kwargs.get('cargo_length', None)

    @property
    def generic_rows(self):
        # map unknown cargos to sprites for some other label
        # assume that piece > input_spriterow_count, it's acceptable to show something like tarps for bulk, but not gravel for piece
        if self.has_piece:
            return self.cargo_row_map['DFLT']
        elif self.has_bulk:
            return self.cargo_row_map['GRVL']
        else:
            # shouldn't reach here, but eh,
            utils.echo_message('generic_rows hit an unknown result in GestaltGraphics')
            return [0]

    @property
    def nml_template(self):
        return 'vehicle_with_visible_cargo.pynml'

    @property
    def piece_cargo_maps(self):
        # I cleaned up how piece cargo maps are *defined* in March 2018
        # however the pre-existing pipelines and templates expect a specific data structure
        # it's more effective right now to simply remap the new data structure onto the old
        # the templates and pipelines can be refactored later, and this can then be simpler
        result = []
        sprite_names = graphics_constants.piece_vehicle_type_to_sprites_maps[self.piece_type]
        for sprite_name in sprite_names:
            cargo_labels = graphics_constants.piece_sprites_to_cargo_labels_maps[sprite_name]
            map = (cargo_labels, [sprite_name])
            result.append(map)
        return result

    def get_output_row_counts_by_type(self):
        # private method because I want to reuse it in subclasses which over-ride the public method
        # provide the number of output rows per cargo group, total row count for the group is calculated later as needed
        # uses a list of 2-tuples, not a dict as order must be preserved
        result = []
        # assume an empty state spriterow - there was an optional bool flag for this per consist but it was unused so I removed it
        result.append(('empty', 1))
        if self.has_bulk:
            result.append(('bulk_cargo', 2 * len(graphics_constants.bulk_cargo_recolour_maps)))
        if self.has_piece:
            result.append(('piece_cargo', 2 * sum([len(cargo_map[1]) for cargo_map in self.piece_cargo_maps])))
        return result

    @property
    def cargo_row_map(self):
        result = {}
        counter = 0
        if self.has_bulk:
            for cargo_map in graphics_constants.bulk_cargo_recolour_maps:
                result[cargo_map[0]] = [counter] # list because multiple spriterows can map to a cargo label
                counter += 1
        if self.has_piece:
            for cargo_labels, cargo_filenames in self.piece_cargo_maps:
                num_variants = len(cargo_filenames)
                spriterow_nums = [counter + i for i in range(num_variants)]
                for cargo_label in cargo_labels:
                    result[cargo_label] = spriterow_nums
                counter += num_variants
        return result


class GestaltGraphicsLiveryOnly(GestaltGraphics):
    """
        Used to handle the specific case of cargos shown only by vehicle livery.
        This can also be used for recolouring vehicles with just a *single* livery which isn't cargo-specific.
    """
    def __init__(self, recolour_maps, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipeline = pipelines.get_pipeline('extend_spriterows_for_composited_cargos_pipeline')
        # recolour_maps map cargo labels to liveries, use 'DFLT' as the labe in the case of just one livery
        self.recolour_maps = recolour_maps

    @property
    def generic_rows(self):
        utils.echo_message ('generic_rows not implemented in GestaltGraphicsLiveryOnly')
        return None

    @property
    def nml_template(self):
        return 'vehicle_with_cargo_specific_liveries.pynml'

    def get_output_row_counts_by_type(self):
        # the template for visible livery requires the count of _all_ the liveries, *no calculating later*
        # 3 rows per livery (empty, 50% load, 100% load)
        return [('livery_only', 3 * self.num_cargo_sprite_variants)]

    @property
    def cargo_row_map(self):
        # !! this works more by accident than design
        # !! the order of cargo types here must be kept in sync with the order in the cargo graphics processor
        result = {}
        counter = 0
        for cargo_map in self.recolour_maps:
            result[cargo_map[0]] = [counter] # list because multiple spriterows can map to a cargo label
            counter += 1
        return result


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
        self.pipeline = pipelines.get_pipeline('pass_through_pipeline')
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

    def get_output_row_counts_by_type(self):
        # assume we want whatever the base class count of rows is (handles empty state etc)
        # ^ that might not be viable as it ties 'custom' to same template assumptions as base class - change if needed eh?
        result = []
        # assume two output rows (loading, loaded) - extend this if it's not viable
        result.append(('custom_cargo', 2))
        return result

    @property
    def cargo_row_map(self):
        return self._cargo_row_map
