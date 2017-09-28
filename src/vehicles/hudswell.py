import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'hudswell',
              base_numeric_id = 240,
              title = '2-6-4 Hudswell [Steam]',
              track_type = 'NG',
              power = 650,
              tractive_effort_coefficient = 0.2,
              speed = 50,
              type_base_buy_cost_points = -11, # dibble buy cost for game balance
              type_base_running_cost_points = 0, # dibble running costs for game balance
              intro_date = 1910)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 45,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
