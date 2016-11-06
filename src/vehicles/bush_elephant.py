import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'bush_elephant',
              base_numeric_id = 2000,
              title = '2-6-6-2 Bush Elephant [Steam]',
              replacement_id = '-none',
              power = 2200,
              track_type = 'NG',
              speed = 45,
              type_base_buy_cost_points = 35, # dibble buy cost for game balance
              type_base_running_cost_points = 35, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1915)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 128,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 52,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
