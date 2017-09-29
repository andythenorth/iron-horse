import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='ramsbottom',
                        base_numeric_id=380,
                        title='0-6-0 Ramsbottom [Steam]',
                        power=1100,
                        tractive_effort_coefficient=0.22,
                        speed=45,
                        type_base_buy_cost_points=12,  # dibble buy cost for game balance
                        gen=1)

consist.add_unit(type=SteamLoco,
                 weight=59,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
