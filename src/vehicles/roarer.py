import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'roarer',
              base_numeric_id = 2230,
              title = 'Roarer [Electric]',
              power = 3200,
              tractive_effort_coefficient = 0.32,
              speed = 110,
              type_base_buy_cost_points = 30, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1965)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 80,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
