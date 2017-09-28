import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'pangolin',
              base_numeric_id = 2060,
              title = '2-6-0 Pangolin [Steam]',
              power = 1200,
              track_type = 'NG',
              speed = 45,
              type_base_buy_cost_points = 0, # dibble buy cost for game balance
              type_base_running_cost_points = 5, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1860)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 27,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
