from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='goliath',
                        base_numeric_id=780,
                        name='Goliath',
                        role='branch_freight',
                        power=1450,
                        random_reverse=True,
                        joker=True,
                        gen=6,
                        intro_date_offset=+5,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=74,
                 vehicle_length=6,
                 spriterow_num=0)
