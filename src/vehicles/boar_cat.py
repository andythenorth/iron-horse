from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='boar_cat',
                        base_numeric_id=1320,
                        name='Boar Cat',
                        role='universal',
                        power=800,
                        random_reverse=True,
                        base_track_type='NG',
                        gen=4,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=20,
                 vehicle_length=4,
                 spriterow_num=0)
