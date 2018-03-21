from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='hyena',
                        base_numeric_id=2080,
                        title='4-6-2 Hyena',
                        power=1400,
                        tractive_effort_coefficient=0.19,
                        track_type='NG',
                        speed=65,
                        type_base_buy_cost_points=25,  # dibble buy cost for game balance
                        type_base_running_cost_points=35,  # dibble running costs for game balance
                        intro_date=1915)

consist.add_unit(type=SteamEngineUnit,
                 weight=68,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=37,
                 vehicle_length=5,
                 spriterow_num=1)

