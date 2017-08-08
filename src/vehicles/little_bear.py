import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'little_bear',
              base_numeric_id = 280,
              title = 'Little Bear [Diesel]',
              power = 850,
              speed = 85,
              type_base_buy_cost_points = 0, # dibble buy cost for game balance
              type_base_running_cost_points = -28, # dibble run cost for game balance
              vehicle_life = 40,
              intro_date = 1964)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 54,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
