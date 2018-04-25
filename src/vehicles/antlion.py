from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='antlion',
                        base_numeric_id=1550,
                        name='Antlion',
                        power=350,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=1950)

consist.add_unit(type=DieselEngineUnit,
                 weight=75,
                 vehicle_length=8,
                 capacity=45,
                 spriterow_num=0)

