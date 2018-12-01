from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='trojan',
                        base_numeric_id=780,
                        name='Trojan',
                        role='branch_freight',
                        power=1600,
                        random_reverse=True,
                        joker=True,
                        gen=6,
                        intro_date_offset=+5,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=74,
                 vehicle_length=6,
                 spriterow_num=0)
