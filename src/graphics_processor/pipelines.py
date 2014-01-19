import os.path
currentdir = os.curdir
import codecs

from pixa import PixaColour, PixaSequence, PixaSequenceCollection, PixaShiftColour, PixaShiftDY, PixaMaskColour, Spritesheet, PixaImageLoader
from pixa import make_cheatsheet as make_cheatsheet
from PIL import Image

from graphics_processor import registered_pipelines
from graphics_processor.units import PassThrough

DOS_PALETTE = Image.open('palette_key.png').palette

def register_pipeline(pipeline):
    print "Registering pipeline ", pipeline.name 
    registered_pipelines[pipeline.name] = pipeline
    print registered_pipelines

class Pipeline(object):
    def __init__(self):
        print "I am a pipeline"
        register_pipeline(self)

    def render_common(self, variant, consist, input_image, units, options):
        # expects to be passed a PIL Image object
        # options is a dict and can be used abitrarily to pass options wherever needed in the pipeline
        # units is a list of objects, with their config data already baked in (don't have to anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        output_path = os.path.join(currentdir, 'generated', 'graphics', variant.get_spritesheet_name(consist))
        spritesheet = Spritesheet(width=input_image.size[0], height=input_image.size[1] , palette=DOS_PALETTE)
        spritesheet.sprites.paste(input_image)
        
        for unit in units:
            spritesheet = unit.render(spritesheet)
        
        spritesheet.save(output_path)

class TestPipeline(Pipeline):
    def __init__(self):
        self.name = "test_pipeline"
        super(TestPipeline, self).__init__()
                
    def render(self, variant, consist):
        print 'render'
        options = variant.graphics_processor.options
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        input_image = Image.open(input_path)
        units = [PassThrough()]
        result = self.render_common(variant, consist, input_image, units, options)
        return result
        
TestPipeline()
