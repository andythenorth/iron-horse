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
    """
    def make_spritesheet(floorplan, row_count):
        return Spritesheet(width=floorplan.size[0], height=SPRITEROW_HEIGHT * row_count, palette=DOS_PALETTE)
        floorplan = Image.open(os.path.join(currentdir, 'input', floorplan_filename))
        # slice out the floorplan needed for this gestalt
        return floorplan.crop((0, gv.floorplan_start_y, floorplan.size[0], gv.floorplan_start_y + SPRITEROW_HEIGHT))
    """
        
    def render_common(self, variant, consist):
        #result = variant.get_spritesheet_name(consist) 
        #result = result + str(variant.spritesheet_suffix)
        loader = PixaImageLoader(mask=(0,255))
        image_path = os.path.join(currentdir, 'src', 'graphics', variant.get_spritesheet_name(consist))
        #points = loader.make_points(image_path, origin=(0,0))
        output_path = os.path.join(currentdir, 'generated', 'graphics', variant.get_spritesheet_name(consist))
        spritesheet = Spritesheet(width=400, height=440 , palette=DOS_PALETTE)
        spritesheet.sprites.paste(Image.open(output_path))
        spritesheet.save(output_path)        
        #return points

class TestPipeline(Pipeline):
    def __init__(self):
        self.name = "test_pipeline"
        print "I am a pipeline"
        register_pipeline(self)
        
    def render(self, variant, consist):
        print 'render'
        result = self.render_common(variant, consist)
        return result
        
TestPipeline()
