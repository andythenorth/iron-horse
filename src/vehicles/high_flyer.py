from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='high_flyer',
                        base_numeric_id=230,
                        name='4-4-2 High Flyer',
                        role='express_1',
                        power=1300,
                        tractive_effort_coefficient=0.25,
                        speed=80,
                        buy_cost=47,
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=80,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)

