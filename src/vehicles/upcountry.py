from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='upcountry',
                        base_numeric_id=230,
                        name='4-6-0 Upcountry',
                        role='heavy_express_1',
                        power=1450,
                        tractive_effort_coefficient=0.18,
                        buy_cost=47,
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=90,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=35,
                 vehicle_length=4,
                 spriterow_num=1)
