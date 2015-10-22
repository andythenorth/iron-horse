import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'cooke',
              base_numeric_id = 150,
              title = '4-6-0 Cooke [Steam]',
              replacement_id = '-none',
              power = 1500,
              speed = 65,
              vehicle_life = 40,
              intro_date = 1885)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 75,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
