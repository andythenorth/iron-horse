import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'pacifico',
              base_numeric_id = 310,
              title = '4-6-2 Pacifico [Steam]',
              power = 1800,
              speed = 65,
              vehicle_life = 40,
              intro_date = 1910)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 90,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
