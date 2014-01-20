import graphics_constants

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
    def __init__(self, image_to_paste):
        self.image_to_paste = image_to_paste.copy() # avoid unwanted lazy copies which cause sadness
        super(AppendToSpritesheet, self).__init__()
        
    def render(self, spritesheet):
        image_to_paste = self.image_to_paste.crop((0, 0, 100, 100))
        spritesheet.sprites.paste(image_to_paste, (0, 0, 100, 100))
        return spritesheet

