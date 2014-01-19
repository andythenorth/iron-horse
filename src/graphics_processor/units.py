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
    # just an example unit that does nothing
    def __init__(self):
        super(PassThrough, self).__init__()

    def render(self, spritesheet):
        print 'PassThrough'
        return spritesheet


class SimpleRecolour(ProcessingUnit):
    def __init__(self, recolour_map):
        self.recolour_map = recolour_map
        super(SimpleRecolour, self).__init__()
        
    def render(self, spritesheet):
        print 'SimpleRecolour'
        self.selective_recolour(spritesheet, self.recolour_map)
        return spritesheet
