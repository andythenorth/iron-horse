from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='ge289a',
                        base_numeric_id=1460,
                        title='GE 289a Boxcab',
                        power=1200,
                        track_type='NG',
                        speed=45,
                        type_base_buy_cost_points=35,  # dibble buy cost for game balance
                        type_base_running_cost_points=-10,  # dibble running costs for game balance
                        intro_date=1922)

consist.add_unit(type=ElectricEngineUnit,
                 weight=64,
                 vehicle_length=6,
                 spriterow_num=0)

