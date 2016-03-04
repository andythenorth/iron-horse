import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'okapi',
              base_numeric_id = 1960,
              title = 'Okapi [Diesel]',
              replacement_id = '-none',
              power = 2000,
              track_type = 'NG',
              speed = 60,
              vehicle_life = 40,
              intro_date = 1955,
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 100,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
