import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'cyclops',
              base_numeric_id = 130,
              title = 'Cyclops [Diesel]',
              power = 3200,
              speed = 125,
              buy_cost = 135,
              vehicle_life = 40,
              intro_date = 1999,
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 95,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
