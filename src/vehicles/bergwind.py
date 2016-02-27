import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'bergwind',
              base_numeric_id = 1870,
              title = 'Bergwind [Diesel]',
              replacement_id = '-none',
              power = 3600,
              track_type = 'NG',
              speed = 65,
              vehicle_life = 40,
              intro_date = 1975)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 113,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(DieselLoco(consist = consist,
                        weight = 113,
                        vehicle_length = 8,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
