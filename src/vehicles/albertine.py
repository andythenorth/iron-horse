from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='albertine',
                        base_numeric_id=2040,
                        name='4-4-2 Albertine',
                        power=1200,
                        tractive_effort_coefficient=0.19,
                        base_track_type='NG',
                        type_base_buy_cost_points=25,  # dibble buy cost for game balance
                        type_base_running_cost_points=35,  # dibble running costs for game balance
                        intro_date=1885)

consist.add_unit(type=SteamEngineUnit,
                 weight=45,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=30,
                 vehicle_length=4,
                 spriterow_num=1)
