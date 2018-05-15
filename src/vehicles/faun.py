from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='faun',
                        base_numeric_id=1720,
                        name='Faun',
                        role='branch_freight',
                        power=1400,
                        random_reverse=True,
                        joker=True,
                        gen=5,
                        intro_date_offset=-5)

consist.add_unit(type=DieselEngineUnit,
                 weight=70,
                 vehicle_length=6,
                 spriterow_num=0)
