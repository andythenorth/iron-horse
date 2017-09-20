import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'express_tank',
              base_numeric_id = 1300,
              title = '2-6-2 Express Tank [Steam]',
              power = 800,
              tractive_effort_coefficient = 0.2,
              speed = 90,
              type_base_buy_cost_points = -2, # dibble buy cost for game balance
              type_base_running_cost_points = -6, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1900)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 57,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       visual_effect_offset='AUTOFLIP')

