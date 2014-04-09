import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'gridiron',
              base_numeric_id = 1120,
              title = 'Gridiron [Diesel]',
              replacement_id = '-none',
              power = 3700,
              speed = 85,
              buy_cost = 186,
              vehicle_life = 40,
              intro_date = 1980,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 125,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
