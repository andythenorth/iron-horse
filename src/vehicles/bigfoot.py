import global_constants
from train import EngineConsist, DieselLoco
# roughly an SAR 91-000 class
consist = EngineConsist(id = 'bigfoot',
              base_numeric_id = 1620,
              title = 'Bigfoot [Diesel]',
              power = 900,
              track_type = 'NG',
              speed = 70,
              type_base_buy_cost_points = -5, # dibble buy cost for game balance
              type_base_running_cost_points = -10, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1970)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 50,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
