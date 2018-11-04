from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='turtle',
                        base_numeric_id=3150,
                        name='Turtle',
                        role='express_1',
                        power=3450,
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=DieselEngineUnit,
                 weight=95,
                 vehicle_length=8,
                 spriterow_num=0)
