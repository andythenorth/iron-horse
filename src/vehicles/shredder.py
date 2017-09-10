import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'shredder',
              base_numeric_id = 2240,
              title = 'Shredder [Diesel]',
              power = 1550,
              speed = 85,
              vehicle_life = 40,
              intro_date = 1960)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 85,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
