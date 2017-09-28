import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'argentina',
              base_numeric_id = 40,
              title = '4-8-0 Argentina [Steam]',
              power = 1800,
              speed = 50,
              vehicle_life = 40,
              intro_date = 1910)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 100,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
