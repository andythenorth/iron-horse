import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'burro',
              base_numeric_id = 90,
              title = '0-4-2 Burro [Steam]',
              power = 650,
              speed = 55,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              intro_date = 1850)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
