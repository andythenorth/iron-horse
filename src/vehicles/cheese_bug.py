from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='cheese_bug',
                        base_numeric_id=490,
                        name='0-6-2 Cheese Bug',
                        role='universal',
                        base_track_type='NG',
                        power=350,
                        tractive_effort_coefficient=0.2,
                        gen=1)


consist.add_unit(type=SteamEngineUnit,
                 weight=16,
                 vehicle_length=4,
                 spriterow_num=0)
