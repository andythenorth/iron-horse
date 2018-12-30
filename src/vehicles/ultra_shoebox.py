from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='ultra_shoebox',
                        base_numeric_id=2170,
                        name='Ultra Shoebox',
                        role='branch_express',
                        power=1550,
                        power_by_railtype={'RAIL': 1550, 'ELRL': 2600},
                        random_reverse=True,
                        pantograph_type='z-shaped-single',
                        gen=6,
                        sprites_complete=True)

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=67,
                 vehicle_length=6,
                 spriterow_num=0)
