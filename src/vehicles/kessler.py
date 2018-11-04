from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='kessler',
                        base_numeric_id=1990,
                        name='0-4-2 Kessler',
                        power=450,
                        base_track_type='NG',
                        random_reverse=True,
                        intro_date=1860)

consist.add_unit(type=SteamEngineUnit,
                 weight=25,
                 vehicle_length=5,
                 spriterow_num=0)
