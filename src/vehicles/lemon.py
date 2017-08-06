import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'lemon',
              base_numeric_id = 270,
              title = '4-8-0 Lemon [Steam]',
              power = 2400,
              tractive_effort_coefficient = 0.29,
              type_base_running_cost_points = 30, # dibble running costs for game balance
              speed = 65,
              buy_cost = 114,
              vehicle_life = 40,
              intro_date = 1935)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 97,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 52,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
