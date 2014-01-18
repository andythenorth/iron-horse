from graphics_processor import registered_pipelines

def register_pipeline(pipeline):
    print "Registering pipeline ", pipeline.name 
    registered_pipelines[pipeline.name] = pipeline
    print registered_pipelines

class TestPipeline(object):
    def __init__(self):
        self.name = "test_pipeline"
        print "I am a pipeline"
        register_pipeline(self)

TestPipeline()
