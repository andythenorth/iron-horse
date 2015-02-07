import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'thing_7',
              base_numeric_id = 2070,
              title = 'Boxcab Thing 7 [Electric]',
              replacement_id = '-none',
              power = 900,
              speed = 55,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1955)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
