import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'smokey_mountain',
              base_numeric_id = 1610,
              title = 'Smokey Mountain [Diesel]',
              power = 3200,
              type_base_buy_cost_points = 24, # dibble buy cost for game balance
              type_base_running_cost_points = 20, # dibble run cost for game balance
              speed = 55,
              vehicle_life = 40,
              intro_date = 1950)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 112,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(DieselLoco(consist = consist,
                        weight = 112,
                        vehicle_length = 8,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
