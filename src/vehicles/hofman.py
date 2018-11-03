from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='hofman',
                        base_numeric_id=1840,
                        name='2-6-2+2-6-2 Hofman',
                        tractive_effort_coefficient=0.27,  # dibble for game balance
                        power=750,
                        base_track_type='NG',
                        type_base_buy_cost_points=-5,  # dibble buy cost for game balance
                        intro_date=1940)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=15,
                 vehicle_length=3,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineUnit,
                 weight=30,
                 vehicle_length=4,
                 spriterow_num=1,
                 visual_effect_offset=-3)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=15,
                 vehicle_length=3,
                 spriterow_num=2)
