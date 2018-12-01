from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='little_bear',
                        base_numeric_id=1730,
                        name='Little Bear',
                        role='branch_freight',
                        power=1200,
                        random_reverse=True,
                        joker=True,
                        gen=4,
                        intro_date_offset=-6,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=68,
                 vehicle_length=6,
                 spriterow_num=0)
