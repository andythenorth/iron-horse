import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'vulcan',
              base_numeric_id = 420,
              title = 'Vulcan [Diesel]',
              power = 2300,
              speed = 100,
              type_base_buy_cost_points = 25, # dibble buy cost for game balance
              type_base_running_cost_points = 25, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1960)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 105,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
