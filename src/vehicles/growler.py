from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='growler',
                        base_numeric_id=2240,
                        title='Growler [Diesel]',
                        power=1550,
                        speed=75,
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=100,
                 vehicle_length=8,
                 spriterow_num=0)

