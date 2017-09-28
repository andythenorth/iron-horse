import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id='chaplin',
                        base_numeric_id=110,
                        title='2-4-0 Chaplin [Steam]',
                        power=450,
                        tractive_effort_coefficient=0.2,
                        speed=65,
                        type_base_buy_cost_points=-3,  # dibble buy cost for game balance
                        gen=1)

consist.add_unit(type=SteamLoco,
                 weight=35,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          visual_effect_offset='AUTOFLIP')
