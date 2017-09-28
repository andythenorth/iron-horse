import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'kwa_falls',
              base_numeric_id = 1970,
              title = '2-8-2 Kwa Falls [Steam]',
              power = 1800,
              tractive_effort_coefficient = 0.19,
              track_type = 'NG',
              speed = 75,
              vehicle_life = 40,
              intro_date = 1945)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 100,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
