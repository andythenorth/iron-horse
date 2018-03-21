from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='peacock',
                        base_numeric_id=340,
                        title='2-6-0 Peacock',
                        power=1200,
                        tractive_effort_coefficient=0.32,
                        speed=50,
                        intro_date=1885)

consist.add_unit(type=SteamEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=45,
                 vehicle_length=4,
                 spriterow_num=1)

