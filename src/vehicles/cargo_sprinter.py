import global_constants
import graphics_processor.utils as graphics_utils
from graphics_processor import graphics_constants
from train import EngineConsist, CargoSprinter, GraphicsProcessorFactory

CC1 = graphics_constants.CC1
CC2 = graphics_constants.CC2
graphics_options = {'template': 'cargo_sprinter_template.png',
           'recolour_maps': (graphics_utils.make_colour_map(170, CC1, 8),
                             graphics_utils.make_colour_map(170, CC2, 8),
                             graphics_utils.make_colour_map(170, 8, 8)),                             
           'num_rows_per_unit': 3,
           'num_unit_types': 3}
graphics_processor_1 = GraphicsProcessorFactory('container_carrier_pipeline', graphics_options)
                
consist = EngineConsist(id = 'cargo_sprinter',
              base_numeric_id = 1100,
              title = 'Cargo Sprinter [Diesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 1520,
              speed = 75,
              buy_cost = 22,
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
