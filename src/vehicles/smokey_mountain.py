import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'smokey_mountain',
              base_numeric_id = 1610,
              title = 'Baby Boat [Diesel]',
              replacement_id = '-none',
              power = 3200,
              speed = 55,
              vehicle_life = 40,
              intro_date = 1950)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 112,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(DieselLoco(consist = consist,
                        weight = 112,
                        vehicle_length = 8,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

"""
consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
"""
