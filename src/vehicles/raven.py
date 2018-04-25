from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='raven',
                        base_numeric_id=390,
                        name='Raven',
                        role='express_2',
                        power=1800,
                        tractive_effort_coefficient=0.25,
                        speed=75,
                        buy_cost=77,
                        intro_date=1905)  # explicit intro date by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=90,
                 vehicle_length=8,
                 spriterow_num=0)

