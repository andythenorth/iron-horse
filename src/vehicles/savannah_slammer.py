import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'savannah_slammer',
              base_numeric_id = 1540,
              title = 'Savannah Slammer [Diesel]',
              power = 500,
              speed = 75,
              type_base_running_cost_points = -32, # dibble running costs for game balance
              intro_date = 1980)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_pax = 65,
                        capacity_mail = 40,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
