from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='walker',
                        base_numeric_id=430,
                        title='Walker [Diesel]',
                        power=900,
                        track_type='NG',
                        speed=55,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1955)

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=6,
                 spriterow_num=0)

