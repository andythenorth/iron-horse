import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'chinook',
              base_numeric_id = 1080,
              title = 'Chinook [Diesel]',
              replacement_id = '-none',
              power = 2000,
              speed = 75,
              buy_cost = 80,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1955,
              graphics_status = '',
              use_legacy_spritesheet = True)
              
consist.add_unit(DieselLoco(consist = consist,
                        weight = 73,
                        vehicle_length = 7,
                        spriterow_num = 0))              

consist.add_unit(DieselLoco(consist = consist,
                        weight = 73,
                        vehicle_length = 7,
                        spriterow_num = 1))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
