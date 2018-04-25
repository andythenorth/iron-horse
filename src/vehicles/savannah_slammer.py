from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='savannah_slammer',
                        base_numeric_id=1540,
                        name='Savannah Slammer',
                        power=500,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=1980)

consist.add_unit(type=DieselEngineUnit,
                 weight=65,
                 vehicle_length=8,
                 capacity=65,
                 spriterow_num=0)

