import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'springburn',
              base_numeric_id = 1790,
              title = '2-8-2 Springburn [Steam]',
              replacement_id = '-none',
              power = 900,
              speed = 55,
              vehicle_life = 40,
              intro_date = 1950,
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 95,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
"""
consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
"""
