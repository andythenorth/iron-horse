import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'drakensberg',
              # !! This vehicle needs more than one id range due to length
              base_numeric_id = 1800,
              title = '4-8-2+2-8-4 Drakensberg [Steam]',
              tractive_effort_coefficient = 0.25,
              power = 3000,
              track_type = 'NG',
              speed = 45,
              type_base_buy_cost_points = 5, # dibble buy cost for game balance
              type_base_running_cost_points = 12, # dibble running costs for game balance
              intro_date = 1945)

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 65,
                        vehicle_length = 4,
                        spriterow_num = 0))

consist.add_unit(SteamLoco(consist = consist,
                        weight = 80,
                        vehicle_length = 6,
                        spriterow_num = 1))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 65,
                        vehicle_length = 4,
                        spriterow_num = 2))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 45,
                        vehicle_length = 6,
                        spriterow_num = 3))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date,
                       visual_effect_offset = -3)

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date,
                       visual_effect_offset = -3)
