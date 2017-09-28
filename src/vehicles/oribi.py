import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'oribi',
              base_numeric_id = 1980,
              title = 'Oribi [Diesel]',
              power = 450,
              track_type = 'NG',
              speed = 65,
              type_base_running_cost_points = -28, # dibble running costs for game balance
              intro_date = 1960)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_pax = 30,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
