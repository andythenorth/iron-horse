import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'aberdare',
              base_numeric_id = 0,
              title = '2-6-0 Aberdare [Steam]',
              power = 1250,
              tractive_effort_coefficient = 0.22,
              speed = 45,
              type_base_buy_cost_points = 12, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1900)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 67,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 3,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
