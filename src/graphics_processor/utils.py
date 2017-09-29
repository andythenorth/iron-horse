from graphics_processor import graphics_constants
from graphics_processor import pipelines


class GraphicsProcessor(object):
    # simple class which wraps a graphics processing pipeline along with some options
    # pipeline objects may get reused across consists,
    # so we don't store consist info in the pipeline, it's passed to pipeline.render() method when needed
    def __init__(self, pipeline_name, options):
        self.pipeline_name = pipeline_name
        self.options = options
        self.pipeline = pipelines.get_pipeline(pipeline_name)


def get_composited_cargo_processors(template):
    # returns two cargo-compositing graphics processors, one of which flips company colours
    # also provides optional 2CC recolor
    graphics_options_1 = {'template': template, 'swap_company_colours': False}
    graphics_options_2 = {'template': template, 'swap_company_colours': True}
    graphics_processor_1 = GraphicsProcessor('extend_spriterows_for_composited_cargos_pipeline', graphics_options_1)
    graphics_processor_2 = GraphicsProcessor('extend_spriterows_for_composited_cargos_pipeline', graphics_options_2)
    return (graphics_processor_1, graphics_processor_2)
