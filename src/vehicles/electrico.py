import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'electrico',
              base_numeric_id = 180,
              title = 'Electrico 2-B+B-2 [Electric]',
              power = 2400,
              speed = 75,
              type_base_buy_cost_points = 35, # dibble buy cost for game balance
              type_base_running_cost_points = -10, # dibble running costs for game balance
              vehicle_life = 60,
              intro_date = 1920)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 140,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
