from train import EngineConsist, DieselEngineUnit
# for rest of stats, look up Chinese CKD8G
consist = EngineConsist(id='roca',
                        base_numeric_id=400,
                        title='Roca [Diesel]',
                        power=3000,
                        speed=100,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1990)

consist.add_unit(type=DieselEngineUnit,
                 weight=30,
                 vehicle_length=8,
                 spriterow_num=0)

