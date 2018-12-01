from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='carrack',
                        base_numeric_id=1040,
                        name='4-4-0 Carrack',
                        role='express_1',
                        power=1050,
                        tractive_effort_coefficient=0.18,
                        buy_cost=47,
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=60,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)
