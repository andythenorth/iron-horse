from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='faun',
                        base_numeric_id=1720,
                        name='Faun',
                        role='branch_freight',
                        power=1300,
                        # dibble TE up for game balance, assume low gearing or something
                        tractive_effort_coefficient=0.375,
                        random_reverse=True,
                        joker=True,
                        gen=5,
                        intro_date_offset=-5,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=71,
                 vehicle_length=6,
                 spriterow_num=0)
