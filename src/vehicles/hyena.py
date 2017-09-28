import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'hyena',
              base_numeric_id = 2080,
              title = '4-6-2 Hyena [Steam]',
              power = 1400,
              tractive_effort_coefficient = 0.19,
              track_type = 'NG',
              speed = 65,
              type_base_buy_cost_points = 25, # dibble buy cost for game balance
              type_base_running_cost_points = 35, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1915)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 68,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 37,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
