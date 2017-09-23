import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'badger',
              base_numeric_id = 450,
              title = 'Flying Badger [Electric]',
              power = 6400,
              speed = 125,
              type_base_buy_cost_points = 71, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1990)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 105,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
