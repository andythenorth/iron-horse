import global_constants
from train import EngineConsist, DieselLoco
# for rest of stats, look up GE Shovelnose
consist = EngineConsist(id = 'pala',
              base_numeric_id = 2150,
              title = 'Pala [Diesel]',
              replacement_id = '-none',
              power = 1000,
              speed = 65,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              vehicle_life = 30,
              intro_date = 1953)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 30,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
