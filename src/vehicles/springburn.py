from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='springburn',
                        base_numeric_id=1790,
                        title='Springburn',
                        power=1200,
                        type_base_running_cost_points=-20,  # dibble run cost for game balance
                        speed=55,
                        intro_date=1950)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=0)

