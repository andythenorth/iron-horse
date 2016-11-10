import global_constants
import graphics_processor.utils as graphics_utils
from train import IntermodalConsist, Wagon, GraphicsProcessorFactory

recolour_maps = graphics_utils.get_container_recolour_maps()
graphics_options = {'template': '',
                    'recolour_maps': (recolour_maps),
                    'copy_block_top_offset': 30,
                    'num_rows_per_unit': 2,
                    'num_unit_types': 1}

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = IntermodalConsist(title = '[Intermodal Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1060,
                           wagon_generation = 3,
                                        intro_date = 1960,
                           vehicle_life = 40,
                           speedy = True,
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 48, # matched to RH and Squid containers
                            weight = 20,
                            vehicle_length = 8))

    graphics_options['template'] = 'intermodal_flat_car_pony_gen_3_template_0.png'

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options))


    #--------------- llama ----------------------------------------------------------------------
