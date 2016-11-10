import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'ge289a',
              base_numeric_id = 1460,
              title = 'GE 289a Boxcab [Electric]',
              power = 1200,
              track_type = 'NG',
              speed = 45,
              type_base_buy_cost_points = 35, # dibble buy cost for game balance
              type_base_running_cost_points = -10, # dibble running costs for game balance
              vehicle_life = 80,
              intro_date = 1922)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 64,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
