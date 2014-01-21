import graphics_constants
from PIL import Image

DOS_PALETTE = Image.open('palette_key.png').palette

class ProcessingUnit(object):
    def __init__(self):
        pass
        
    def make_recolour_table(self, recolour_map):
        table = []
        for i in range(256):
            if i in recolour_map.keys():
                table.append(recolour_map[i])
            else:
                table.append(i)
        return table
        
    def selective_recolour(self, spritesheet, recolour_map):
        table = self.make_recolour_table(recolour_map)
        result = spritesheet.sprites.point(table)
        spritesheet.sprites.paste(result)
        # doesn't need to return, the spritesheet object is already modified


class PassThrough(ProcessingUnit):
    """ PassThrough """
    # just an example unit that does nothing
    def __init__(self):
        super(PassThrough, self).__init__()

    def render(self, spritesheet):
        return spritesheet


class SimpleRecolour(ProcessingUnit):
    """ SimpleRecolour """
    def __init__(self, recolour_map):
        self.recolour_map = recolour_map
        super(SimpleRecolour, self).__init__()
        
    def render(self, spritesheet):
        self.selective_recolour(spritesheet, self.recolour_map)
        return spritesheet


class SwapCompanyColours(ProcessingUnit):
    """ SwapCompanyColours """
    def __init__(self):
        self.recolour_map = graphics_constants.CC1_CC2_SWAP_MAP
        super(SwapCompanyColours, self).__init__()
        
    def render(self, spritesheet):
        self.selective_recolour(spritesheet, self.recolour_map)
        return spritesheet


class AppendToSpritesheet(ProcessingUnit):
    """ AppendToSpritesheet """
    def __init__(self, source_spritesheet, crop_box=None, insertion_point=(0, 0)):
        self.source_spritesheet = source_spritesheet
        # 4 tuple for box size (left, upper, right, lower)
        self.crop_box = crop_box
        if self.crop_box is None:
            self.crop_box = (0, 0, source_spritesheet.sprites.size[0], source_spritesheet.sprites.size[1])
        # 2 tuple for insertion_point into target image (x, y) from top left
        self.insertion_point = insertion_point
        super(AppendToSpritesheet, self).__init__()
        
    def render(self, spritesheet):
        image_to_paste = self.source_spritesheet.sprites.copy().crop((0, 0, self.crop_box[0], self.crop_box[1]))
        width = 400
        height = 1200
        temp = Image.new('P', (width, height), 255)
        temp.putpalette(DOS_PALETTE)
        previous = spritesheet.sprites
        temp.paste(previous, (0, 0, previous.size[0], previous.size[1]))
        spritesheet.sprites = temp
        box = (self.insertion_point[0], self.insertion_point[1], self.insertion_point[0] + self.crop_box[0], self.insertion_point[1] + self.crop_box[1])
        spritesheet.sprites.paste(image_to_paste, box)
        return spritesheet

