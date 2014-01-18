from graphics_processor import registered_pipelines

def register_pipeline(pipeline):
    print "Registering pipeline ", pipeline.name 
    registered_pipelines[pipeline.name] = pipeline
    print registered_pipelines

class Pipeline(object):
    def render_common(self, variant, consist):
        result = variant.get_spritesheet_name(consist) 
        result = result + str(variant.spritesheet_suffix)
        return result

class TestPipeline(Pipeline):
    def __init__(self):
        self.name = "test_pipeline"
        print "I am a pipeline"
        register_pipeline(self)
        
    def render(self, variant, consist):
        print 'render'
        result = self.render_common(variant, consist)
        return 25
        
TestPipeline()
