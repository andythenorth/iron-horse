from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='tencendur',
                        base_numeric_id=890,
                        name='4-4-0 Tencendur',
                        role='express_1',
                        power=1450,
                        tractive_effort_coefficient=0.16,
                        buy_cost=47,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=80,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)
