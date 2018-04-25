from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='growler',
                        base_numeric_id=2240,
                        name='Growler',
                        role='freight',
                        power=1550,
                        random_reverse=True,
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=100,
                 vehicle_length=8,
                 spriterow_num=0)

