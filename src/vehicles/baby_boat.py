import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'baby_boat',
              base_numeric_id = 1590,
              title = 'Baby Boat [Diesel]',
              power = 1800,
              speed = 75,
              intro_date = 1978)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 120,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
