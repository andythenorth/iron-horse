import global_constants
from train import EngineConsist, DieselLoco
# for rest of stats, look up GE Export models U5B-U8B
consist = EngineConsist(id = 'universal',
              base_numeric_id = 540,
              title = 'Universal [Diesel]',
              replacement_id = '-none',
              power = 800,
              speed = 60,
              vehicle_life = 30,
              intro_date = 1958)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 65,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
