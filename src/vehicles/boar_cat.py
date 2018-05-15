from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='boar_cat',
                        base_numeric_id=1320,
                        name='Boar Cat',
                        role='universal',
                        power=800,
                        track_type='NG',
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1990)

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=0)
