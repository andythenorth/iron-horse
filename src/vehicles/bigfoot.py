import global_constants
from train import EngineConsist, DieselLoco
# roughly an SAR 91-000 class
consist = EngineConsist(id = 'bigfoot',
              base_numeric_id = 1620,
              title = 'Bigfoot [Diesel]',
              replacement_id = '-none',
              power = 750,
              track_type = 'NG',
              speed = 70,
              vehicle_life = 40,
              intro_date = 1970)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 50,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
