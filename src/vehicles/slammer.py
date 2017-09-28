import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'slammer',
              base_numeric_id = 470,
              title = 'Slammer [Diesel]',
              power = 300,
              speed = 75,
              type_base_running_cost_points = -32, # dibble running costs for game balance
              intro_date = 1955) # explicit intro date by design

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 37,
                        vehicle_length = 8,
                        capacity_pax = 55,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
