from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='thunderbird',
                        base_numeric_id=3090,
                        name='Thunderbird',
                        role='express_1',
                        power=2750,
                        random_reverse=True,
                        gen=5,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=90,
                 vehicle_length=8,
                 spriterow_num=0)
