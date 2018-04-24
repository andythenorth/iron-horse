from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='sparkycat',
                        base_numeric_id=160,
                        name='Slug Renewal',
                        role='freight',
                        power=1850,
                        speed=110,
                        type_base_buy_cost_points=60,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=DieselEngineUnit,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)

