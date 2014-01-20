import os.path
currentdir = os.curdir
import codecs

from pixa import PixaColour, PixaSequence, PixaSequenceCollection, PixaShiftColour, PixaShiftDY, PixaMaskColour, Spritesheet, PixaImageLoader
from pixa import make_cheatsheet as make_cheatsheet
from PIL import Image

from graphics_processor import registered_pipelines, graphics_constants
from graphics_processor.units import PassThrough, SimpleRecolour, SwapCompanyColours, AppendToSpritesheet

DOS_PALETTE = Image.open('palette_key.png').palette

"""
Pipelines can be dedicated to a single task such as SimpleRecolourPipeline
Or they can compose units for more complicated tasks, such as colouring and loading a specific vehicle type  
"""


class Pipeline(object):
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        print "I am a pipeline"
        print "Registering pipeline ", self.name 
        registered_pipelines[self.name] = self
        print registered_pipelines

    def render_common(self, variant, consist, input_image, units, options):
        # expects to be passed a PIL Image object
        # options is a dict and can be used abitrarily to pass options wherever needed in the pipeline
        # units is a list of objects, with their config data already baked in (don't have to anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        print 'Rendering ' + variant.get_spritesheet_name(consist)  
        output_path = os.path.join(currentdir, 'generated', 'graphics', variant.get_spritesheet_name(consist))
        spritesheet = Spritesheet(width=input_image.size[0], height=input_image.size[1] , palette=DOS_PALETTE)
        spritesheet.sprites.paste(input_image)
        
        for unit in units:
            spritesheet = unit.render(spritesheet)        
        spritesheet.save(output_path)


class PassThroughPipeline(Pipeline):
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        self.name = "pass_through_pipeline"
        super(PassThroughPipeline, self).__init__()
                
    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = []
        result = self.render_common(variant, consist, input_image, units, options)
        return result
        
PassThroughPipeline()


class SimpleRecolourPipeline(Pipeline):
    """ Swaps colours using the recolour map (dict {colour index: replacement colour}) """
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        self.name = "simple_recolour_pipeline"
        super(SimpleRecolourPipeline, self).__init__()
                
    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = [SimpleRecolour(options['recolour_map'])]
        result = self.render_common(variant, consist, input_image, units, options)
        return result
        
SimpleRecolourPipeline()


class SwapCompanyColoursPipeline(Pipeline):
    """ Swaps 1CC and 2CC colours """
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        self.name = "swap_company_colours_pipeline"
        super(SwapCompanyColoursPipeline, self).__init__()
                
    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = [SwapCompanyColours()]
        result = self.render_common(variant, consist, input_image, units, options)
        return result
        
SwapCompanyColoursPipeline()


class ContainerCarrierPipeline(Pipeline):
    """" Extends a container carrier spritesheet with variations on container colours """
    def __init__(self):
        # this should be sparse, don't store any consist or variant info in Pipelines, pass them at render time
        self.name = "container_carrier_pipeline"
        super(ContainerCarrierPipeline, self).__init__()

    def render(self, variant, consist):
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = [AppendToSpritesheet(input_image)]
        result = self.render_common(variant, consist, input_image, units, options)
        return result

ContainerCarrierPipeline()
