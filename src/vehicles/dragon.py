from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='dragon',
                        base_numeric_id=420,
                        name='Dragon',
                        role='express_1',
                        power=2200,
                        random_reverse=True,
                        gen=4,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)
