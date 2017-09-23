import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'tin_rocket',
              base_numeric_id = 530,
              title = 'Tin Rocket [Diesel]',
              power = 600,
              speed = 90,
              type_base_running_cost_points = -36, # dibble running costs for game balance
              intro_date = 1985,
              vehicle_life = 40)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 75,
                        capacity_mail = 40,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
