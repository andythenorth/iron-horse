import global_constants
from train import EngineConsist, DieselLoco
# GE Shovelnose - meter gauge ish
consist = EngineConsist(id = 'cooper',
              base_numeric_id = 1440,
              title = 'Cooper [Diesel]',
              power = 1000,
              track_type = 'NG',
              speed = 55,
              vehicle_life = 30,
              intro_date = 1949)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 85,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
