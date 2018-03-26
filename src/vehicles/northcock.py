from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='northcock',
                        base_numeric_id=300,
                        name='2-8-2 Northcock',
                        role='express_1',
                        power=1750,
                        tractive_effort_coefficient=0.25,
                        speed=95,
                        buy_cost=81,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=110,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=1)

