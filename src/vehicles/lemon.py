import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='lemon',
                        base_numeric_id=270,
                        title='4-8-0 Lemon [Steam]',
                        power=2400,
                        tractive_effort_coefficient=0.29,
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        speed=60,
                        buy_cost=114,
                        vehicle_generation=3)

consist.add_unit(type=SteamLoco,
                 weight=97,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=52,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
