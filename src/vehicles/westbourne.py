import global_constants
from train import EngineConsist, MetroPaxUnit

consist = EngineConsist(id = 'westbourne',
              base_numeric_id = 360,
              title = 'Westbourne [Metro Train]',
              track_type = 'METRO',
              power = 900,
              speed = 55,
              type_base_buy_cost_points = 60, # dibble buy cost for game balance
              intro_date = 1950)

consist.add_unit(type = MetroPaxUnit,
                 weight = 40,
                 vehicle_length = 8,
                 capacity_pax = 160,
                 spriterow_num = 0)

consist.add_unit(type = MetroPaxUnit,
                 weight = 40,
                 vehicle_length = 8,
                 capacity_pax = 160,
                 spriterow_num = 1)

consist.add_model_variant(start_date = 0,
                          end_date = global_constants.max_game_date)
