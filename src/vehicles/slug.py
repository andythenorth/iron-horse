import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'slug',
              base_numeric_id = 1000,
              title = 'Slug [Diesel]',
              power = 1700,
              speed = 90,
              vehicle_life = 40,
              intro_date = 1990)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 110,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
