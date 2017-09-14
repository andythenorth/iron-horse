import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'chinook',
              base_numeric_id = 120,
              title = 'Chinook [Diesel]',
              power = 3000,
              speed = 85,
              type_base_buy_cost_points = 30, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1960)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 80,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_unit(DieselLoco(consist = consist,
                        weight = 80,
                        vehicle_length = 6,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
