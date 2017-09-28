import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'ndemi',
              base_numeric_id = 2070,
              title = '4-8-0 Ndemi [Steam]',
              power = 1700,
              track_type = 'NG',
              speed = 35,
              type_base_buy_cost_points = 35, # dibble buy cost for game balance
              type_base_running_cost_points = 35, # dibble running costs for game balance
              intro_date = 1887)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 75,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 35,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
