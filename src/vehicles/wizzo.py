import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'wizzo',
              base_numeric_id = 420,
              title = 'Wizzo [Diesel]',
              power = 2200,
              speed = 100,
              type_base_buy_cost_points = 30, # dibble buy cost for game balance
              type_base_running_cost_points = 30, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1960)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 80,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
