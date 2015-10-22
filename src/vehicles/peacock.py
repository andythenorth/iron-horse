import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'peacock',
              base_numeric_id = 340,
              title = '2-6-0 Peacock [Steam]',
              replacement_id = '-none',
              power = 1200,
              tractive_effort_coefficient = 0.32,
              speed = 50,
              vehicle_life = 40,
              intro_date = 1885)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 65,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 45,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
