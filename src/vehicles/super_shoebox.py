from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='super_shoebox',
                        base_numeric_id=880,
                        name='Super Shoebox',
                        role='branch_express',
                        power=1250,  # double the previous progression, to support higher speed and offer replacement for Shredder
                        power_by_railtype={'RAIL': 1250, 'ELRL': 2200},
                        random_reverse=True,
                        pantograph_type='z-shaped-single',
                        gen=5,
                        sprites_complete=True)

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=66,
                 vehicle_length=6,
                 spriterow_num=0)
