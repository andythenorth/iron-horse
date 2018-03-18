from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='oribi',
                        base_numeric_id=1980,
                        title='Oribi [Diesel]',
                        power=450,
                        track_type='NG',
                        speed=65,
                        type_base_running_cost_points=-28,  # dibble running costs for game balance
                        intro_date=1960)

consist.add_unit(type=DieselEngineUnit,
                 weight=65,
                 vehicle_length=8,
                 capacity=30,
                 spriterow_num=0)

