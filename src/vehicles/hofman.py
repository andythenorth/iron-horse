from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='hofman',
                        base_numeric_id=1840,
                        title='2-6-2+2-6-2 Hofman',
                        tractive_effort_coefficient=0.27,  # dibble for game balance
                        power=750,
                        track_type='NG',
                        speed=60,
                        type_base_buy_cost_points=-5,  # dibble buy cost for game balance
                        type_base_running_cost_points=-10,  # dibble running costs for game balance
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

