import global_constants
from train import EngineConsist, DieselLoco
# for rest of stats, look up EMD G22CW
consist = EngineConsist(id = 'astarsa',
              base_numeric_id = 50,
              title = 'Astarsa [Diesel]',
              power = 1600,
              speed = 65,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              intro_date = 1969)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
