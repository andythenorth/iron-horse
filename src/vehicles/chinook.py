from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='chinook',
                        base_numeric_id=120,
                        name='Chinook',
                        role='heavy_freight_1',
                        power=3000,
                        gen=4,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=1)
