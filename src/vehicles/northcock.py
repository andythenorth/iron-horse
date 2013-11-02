import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'northcock',
              base_numeric_id = 1070,
              title = 'Northcock [Steam]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 1750,
              tractive_effort_coefficient = 0.2,
              speed = 100,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1935,
              graphics_status = '')
              
consist.add_unit(SteamLoco(consist = consist,
                        weight = 120,
                        vehicle_length = 7,
                        spriterow_num = 0))              

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 50,
                        vehicle_length = 4,
                        spriterow_num = 1))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
