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
              vehicle_life = 40,
              intro_date = 1887,
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 75,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 35,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
