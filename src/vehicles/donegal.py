from train import EngineConsist, DieselRailcarUnit

consist = EngineConsist(id='donegal',
                        base_numeric_id=140,
                        name='Donnegal',
                        role='pax_railcar',
                        track_type='NG',
                        power=250,
                        type_base_buy_cost_points=-18,  # dibble buy cost for game balance
                        type_base_running_cost_points=-30,  # dibble running costs for game balance
                        gen=3)

consist.add_unit(type=DieselRailcarUnit,
                 weight=20,
                 vehicle_length=7,
                 capacity=35,
                 spriterow_num=0)
