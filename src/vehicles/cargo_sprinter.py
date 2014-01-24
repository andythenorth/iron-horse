import global_constants
from train import EngineConsist, CargoSprinter, GraphicsProcessorFactory

options = {'template': 'cargo_sprinter_template.png',
           'recolour_maps': ({170: 186, 171: 187, 172: 188, 173: 189},
                             {170: 220, 171: 221, 172: 222, 173: 223},
                             {170: 110, 171: 111, 172: 112, 173: 113}),                             
           'num_rows_per_unit': 3,
           'num_unit_types': 3}
graphics_processor_1 = GraphicsProcessorFactory('container_carrier_pipeline', options)
                
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
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0,
                       graphics_processor = graphics_processor_1)
