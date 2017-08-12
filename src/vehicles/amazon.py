import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'amazon',
              base_numeric_id = 10,
              title = 'Amazon [Diesel]',
              power = 300,
              speed = 75,
              type_base_running_cost_points = -32, # dibble running costs for game balance
              intro_date = 1930,
              vehicle_life = 40)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_pax = 55,
                        capacity_mail = 30,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
