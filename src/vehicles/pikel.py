from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='pikel',
                        base_numeric_id=430,
                        name='Pikel',
                        role='universal',
                        power=650,
                        random_reverse=True,
                        base_track_type='NG',
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        gen=3)

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=0)
