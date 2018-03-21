from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='amazon',
                        base_numeric_id=10,
                        title='Amazon',
                        power=300,
                        speed=75,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=1930)

consist.add_unit(type=DieselEngineUnit,
                 weight=65,
                 vehicle_length=8,
                 capacity=55,
                 spriterow_num=0)

