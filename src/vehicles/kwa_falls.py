from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='kwa_falls',
                        base_numeric_id=1970,
                        title='2-8-2 Kwa Falls',
                        power=1800,
                        tractive_effort_coefficient=0.19,
                        track_type='NG',
                        speed=75,
                        intro_date=1945)

consist.add_unit(type=SteamEngineUnit,
                 weight=100,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=5,
                 spriterow_num=1)

