from train import EngineConsist, DieselEngineUnit
# for rest of stats, look up EMD G22CW
consist = EngineConsist(id='astarsa',
                        base_numeric_id=50,
                        title='Astarsa',
                        power=1600,
                        speed=65,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1969)

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=0)

