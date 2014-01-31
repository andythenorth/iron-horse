import global_constants
import graphics_processor.utils as graphics_utils
from train import EngineConsist, CargoSprinter, GraphicsProcessorFactory

recolour_maps = graphics_utils.get_container_recolour_maps() 
graphics_options = {'template': 'cargo_sprinter_template.png',
           'recolour_maps': (recolour_maps),
           'copy_block_top_offset': 0,
           'num_rows_per_unit': 3,
           'num_unit_types': 3}
graphics_processor_1 = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options)
                
consist = EngineConsist(id = 'cargo_sprinter',
              base_numeric_id = 1100,
              title = 'Cargo Sprinter [Diesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 1520,
              speed = 75,
              buy_cost = 69,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1999,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(CargoSprinter(consist = consist,
                        weight = 82,
                        vehicle_length = 8,
                        capacity_freight = 30,
                        num_random_cargo_variants = len(graphics_options['recolour_maps'])),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0,
                       graphics_processor = graphics_processor_1)
