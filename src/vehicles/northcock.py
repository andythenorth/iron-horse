import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'northcock',
              base_numeric_id = 300,
              title = '2-8-2 Northcock [Steam]',
              power = 1750,
              tractive_effort_coefficient = 0.2,
              speed = 95,
              buy_cost = 81,
              vehicle_life = 40,
              intro_date = 1930)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 120,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 50,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
