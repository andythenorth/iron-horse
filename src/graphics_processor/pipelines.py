import os.path
currentdir = os.curdir
import codecs

from pixa import PixaColour, PixaSequence, PixaSequenceCollection, PixaShiftColour, PixaShiftDY, PixaMaskColour, Spritesheet, PixaImageLoader
from pixa import make_cheatsheet as make_cheatsheet
from PIL import Image

from graphics_processor import registered_pipelines, graphics_constants
from graphics_processor.units import PassThrough, SimpleRecolour, SwapCompanyColours, AppendToSpritesheet

DOS_PALETTE = Image.open('palette_key.png').palette

def register(pipeline):
    registered_pipelines[pipeline.name] = pipeline

"""
Pipelines can be dedicated to a single task such as SimpleRecolourPipeline
Or they can compose units for more complicated tasks, such as colouring and loading a specific vehicle type
"""


class Pipeline(object):
    def __init__(self, name):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        self.name = name

    def make_spritesheet_from_image(self, input_image):
        spritesheet = Spritesheet(width=input_image.size[0], height=input_image.size[1] , palette=DOS_PALETTE)
        spritesheet.sprites.paste(input_image)
        return spritesheet

    def render_common(self, variant, consist, input_image, units, options):
        # expects to be passed a PIL Image object
        # options is a dict and can be used abitrarily to pass options wherever needed in the pipeline
        # units is a list of objects, with their config data already baked in (don't have to anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        output_path = os.path.join(currentdir, 'generated', 'graphics', variant.get_spritesheet_name(consist))
        spritesheet = self.make_spritesheet_from_image(input_image)

        for unit in units:
            spritesheet = unit.render(spritesheet)
        spritesheet.save(output_path)

    def render(self, variant, consist):
        raise NotImplementedError("Implement me in %s" % repr(self))

class PassThroughPipeline(Pipeline):
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        super(PassThroughPipeline, self).__init__("pass_through_pipeline")

    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = []
        result = self.render_common(variant, consist, input_image, units, options)
        return result

register(PassThroughPipeline())


class SimpleRecolourPipeline(Pipeline):
    """ Swaps colours using the recolour map (dict {colour index: replacement colour}) """
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        super(SimpleRecolourPipeline, self).__init__("simple_recolour_pipeline")

    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = [SimpleRecolour(options['recolour_map'])]
        result = self.render_common(variant, consist, input_image, units, options)
        return result

register(SimpleRecolourPipeline())


class SwapCompanyColoursPipeline(Pipeline):
    """ Swaps 1CC and 2CC colours """
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        super(SwapCompanyColoursPipeline, self).__init__("swap_company_colours_pipeline")

    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        #input_image.show()
        units = [SwapCompanyColours()]
        result = self.render_common(variant, consist, input_image, units, options)
        return result

register(SwapCompanyColoursPipeline())


class ExtendSpriterowsForRecolouredCargosPipeline(Pipeline):
    """" Extends a cargo carrier spritesheet with variations on cargo colours """
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        super(ExtendSpriterowsForRecolouredCargosPipeline, self).__init__("extend_spriterows_for_recoloured_cargos_pipeline")

    def render(self, variant, consist):
        # there are various options for controlling the crop box, I haven't documented them - read example uses to figure them out
        options = variant.graphics_processor.options
        unit_row_cluster_height = options['num_rows_per_unit'] * graphics_constants.spriterow_height * options['num_unit_types']
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        crop_box = (0, 0, graphics_constants.spritesheet_width, graphics_constants.spritesheet_top_margin + unit_row_cluster_height + options['copy_block_top_offset'])
        input_image = Image.open(input_path).crop(crop_box)
        #if options['template'] == 'hopper_car_brit_gen_1_template.png':
            #make_cheatsheet(Image.open(os.path.join(currentdir,'src','graphics','hopper_car_brit_gen_1_template.png')), os.path.join(currentdir,'foo.png'))
        source_spritesheet = self.make_spritesheet_from_image(input_image)
        crop_box = (0,
                    graphics_constants.spritesheet_top_margin + options['copy_block_top_offset'],
                    graphics_constants.spritesheet_width,
                    graphics_constants.spritesheet_top_margin + options['copy_block_top_offset'] + unit_row_cluster_height)
        units = [SimpleRecolour(options['recolour_maps'][0])]
        print options
        for recolour_map_index in range(len(options['recolour_maps'])-1):
            units.append(AppendToSpritesheet(source_spritesheet, crop_box))
            units.append(SimpleRecolour(options['recolour_maps'][recolour_map_index+1]))
        result = self.render_common(variant, consist, input_image, units, options)
        return result

register(ExtendSpriterowsForRecolouredCargosPipeline())
