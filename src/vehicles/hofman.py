import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'hofman',
              base_numeric_id = 1840,
              title = '2-6-2+2-6-2 Hofman [Steam]',
              tractive_effort_coefficient = 0.27, # dibble for game balance
              power = 750,
              track_type = 'NG',
              speed = 60,
              type_base_buy_cost_points = -5, # dibble buy cost for game balance
              type_base_running_cost_points = -10, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1940)

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 15,
                        vehicle_length = 3,
                        spriterow_num = 0))

consist.add_unit(SteamLoco(consist = consist,
                        weight = 30,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 15,
                        vehicle_length = 3,
                        spriterow_num = 2))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date,
                       visual_effect_offset = -3)
