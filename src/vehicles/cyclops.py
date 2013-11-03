import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'cyclops',
              base_numeric_id = 1140,
              title = 'Cyclops [Diesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 3200,
              speed = 125,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1999,
              graphics_status = '',
              use_legacy_spritesheet = True)
              
consist.add_unit(DieselLoco(consist = consist,
                        weight = 95,
                        vehicle_length = 7,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
