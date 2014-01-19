import os.path
currentdir = os.curdir
import codecs

from pixa import PixaColour, PixaSequence, PixaSequenceCollection, PixaShiftColour, PixaShiftDY, PixaMaskColour, Spritesheet, PixaImageLoader
from pixa import make_cheatsheet as make_cheatsheet
from PIL import Image

from graphics_processor import registered_pipelines

DOS_PALETTE = Image.open('palette_key.png').palette

def register_pipeline(pipeline):
    print "Registering pipeline ", pipeline.name 
    registered_pipelines[pipeline.name] = pipeline
    print registered_pipelines

class Pipeline(object):
    def __init__(self):
        print "I am a pipeline"
        register_pipeline(self)

    def render_common(self, variant, consist, options):
        input_path = os.path.join(currentdir, 'src', 'graphics', options['template'])
        output_path = os.path.join(currentdir, 'generated', 'graphics', variant.get_spritesheet_name(consist))
        input_image = Image.open(input_path)
        spritesheet = Spritesheet(width=input_image.size[0], height=input_image.size[1] , palette=DOS_PALETTE)
        spritesheet.sprites.paste(input_image)
        spritesheet.save(output_path)

class TestPipeline(Pipeline):
    def __init__(self):
        self.name = "test_pipeline"
        super(TestPipeline, self).__init__()
                
    def render(self, variant, consist):
        print 'render'
        options = variant.graphics_processor.options
        print options
        result = self.render_common(variant, consist, options)
        return result
        
TestPipeline()
