from graphics_processor import registered_pipelines

def register_pipeline(pipeline):
    print "Registering pipeline ", pipeline.name 
    registered_pipelines[pipeline.name] = pipeline
    print registered_pipelines

class Pipeline(object):
    def render_common(self, variant, consist, src_spritesheet):
        result = src_spritesheet 
        result = result + str(variant.spritesheet_suffix)
        return result

class TestPipeline(Pipeline):
    def __init__(self):
        self.name = "test_pipeline"
        print "I am a pipeline"
        register_pipeline(self)
        
    def render(self, variant, consist, src_spritesheet):
        print 'render'
        result = self.render_common(variant, consist, src_spritesheet)
        return 25
        
TestPipeline()
