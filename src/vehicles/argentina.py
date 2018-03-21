from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='argentina',
                        base_numeric_id=40,
                        title='4-8-0 Argentina',
                        power=1800,
                        speed=50,
                        intro_date=1910)

consist.add_unit(type=SteamEngineUnit,
                 weight=100,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=5,
                 spriterow_num=1)

