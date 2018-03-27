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
        # colour defaults
        CC1 = 198
        CC2 = 80
        self.recolour_map = {}
        for i in range(8):
            self.recolour_map[CC1 + i] = CC2 + i
            self.recolour_map[CC2 + i] = CC1 + i
        super(SwapCompanyColours, self).__init__()

    def render(self, spritesheet):
        self.selective_recolour(spritesheet, self.recolour_map)
        return spritesheet


class AppendToSpritesheet(ProcessingUnit):
    """ AppendToSpritesheet """
    """ Always appends at the end vertically.  Insertions and horizontal appending are not supported. """
    def __init__(self, spritesheet_to_paste, crop_box=None):
        self.spritesheet_to_paste = spritesheet_to_paste
        # 4 tuple for box size (left, upper, right, lower)
        self.crop_box = crop_box
        if self.crop_box is None:
            self.crop_box = (0, 0, spritesheet_to_paste.sprites.size[0], spritesheet_to_paste.sprites.size[1])
        super(AppendToSpritesheet, self).__init__()

    def render(self, spritesheet):
        image_to_paste = self.spritesheet_to_paste.sprites.copy()
        image_to_paste = image_to_paste.crop((self.crop_box[0], self.crop_box[1], self.crop_box[2], self.crop_box[3]))
        previous = spritesheet.sprites
        width = previous.size[0]
        height = previous.size[1] + image_to_paste.size[1]
        temp = Image.new('P', (width, height), 255)
        temp.putpalette(DOS_PALETTE)
        temp.paste(previous, (0, 0, previous.size[0], previous.size[1]))
        spritesheet.sprites = temp
        box = (0, previous.size[1], image_to_paste.size[0], previous.size[1] + image_to_paste.size[1])
        spritesheet.sprites.paste(image_to_paste, box)
        return spritesheet

