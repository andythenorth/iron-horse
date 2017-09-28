import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'screamer',
              base_numeric_id = 130,
              title = 'Screamer [Diesel]',
              power = 4500,
              speed = 125,
              buy_cost = 135,
              intro_date = 1985, # explicit intro date by design
              dual_headed = True)

consist.add_unit(type = DieselLoco,
                 weight = 95,
                 vehicle_length = 8,
                 spriterow_num = 0)

consist.add_model_variant(start_date = 0,
                          end_date = global_constants.max_game_date)
