import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='americano',
                        base_numeric_id=20,
                        title='4-4-0 Americano [Steam]',
                        power=1000,
                        speed=65,
                        intro_date=1850)

consist.add_unit(type=SteamLoco,
                 weight=52,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=30,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
