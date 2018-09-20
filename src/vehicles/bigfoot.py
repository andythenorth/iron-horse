from train import EngineConsist, DieselEngineUnit
# roughly an SAR 91-000 class
consist = EngineConsist(id='bigfoot',
                        base_numeric_id=1620,
                        name='Bigfoot',
                        power=900,
                        base_track_type='NG',
                        type_base_buy_cost_points=-5,  # dibble buy cost for game balance
                        type_base_running_cost_points=-10,  # dibble running costs for game balance
                        intro_date=1970)

consist.add_unit(type=DieselEngineUnit,
                 weight=50,
                 vehicle_length=5,
                 spriterow_num=0)
