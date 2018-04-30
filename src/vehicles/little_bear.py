from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='little_bear',
                        base_numeric_id=1730,
                        name='Little Bear',
                        role='freight_2',
                        power=1200,
                        random_reverse=True,
                        joker=True,
                        gen=5,
                        intro_date_offset=-16)

consist.add_unit(type=DieselEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

