import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'gridiron',
              title = 'Gridiron [Diesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 3300,
              speed = 80,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1980,
              graphics_status = '')
              
consist.add_unit(DieselLoco(consist = consist,
                        weight = 125,
                        vehicle_length = 8,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
