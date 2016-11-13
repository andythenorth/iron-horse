import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'donegal',
              base_numeric_id = 140,
              title = 'Donnegal [Diesel]',
              track_type = 'NG',
              power = 250,
              speed = 55,
              type_base_buy_cost_points = -18, # dibble buy cost for game balance
              type_base_running_cost_points = -30, # dibble running costs for game balance
              intro_date = 1954,
              vehicle_life = 40)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 20,
                        vehicle_length = 7,
                        capacity_pax = 35,
                        capacity_mail = 12,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
