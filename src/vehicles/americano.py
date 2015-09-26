import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'americano',
              base_numeric_id = 1310,
              title = '4-4-0 Americano [Steam]',
              replacement_id = '-none',
              power = 1000,
              speed = 65,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1860)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
