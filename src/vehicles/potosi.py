import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'potosi',
              base_numeric_id = 370,
              title = '4-8-2+2-8-4 Potosi [Steam]',
              replacement_id = '-none',
              power = 2500,
              speed = 55,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1927)

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_unit(SteamLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        spriterow_num = 1))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 2))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       visual_effect_offset = -3,
                       spritesheet_suffix=0)
