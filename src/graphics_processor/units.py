class ProcessingUnit(object):
    def __init__(self):
        pass


class PassThrough(ProcessingUnit):
    def __init__(self):
        super(ProcessingUnit, self).__init__()
        
    def render(self, spritesheet):
        print 'PassThrough'
        return spritesheet
