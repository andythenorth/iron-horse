from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='ultra_shoebox',
                        base_numeric_id=2170,
                        name='Ultra Shoebox',
                        role='branch_express',
                        power=1450,  # a bit higher than progression would require, to support higher speed
                        power_by_railtype={'RAIL': 1450, 'ELRL': 2600},
                        random_reverse=True,
                        pantograph_type='z-shaped-single',
                        gen=6)

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=67,
                 vehicle_length=6,
                 spriterow_num=0)
