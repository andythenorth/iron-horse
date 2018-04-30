from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='hudswell',
                        base_numeric_id=240,
                        name='2-6-4 Hudswell',
                        role='branch_express',
                        track_type='NG',
                        power=650,
                        tractive_effort_coefficient=0.2,
                        type_base_buy_cost_points=-11,  # dibble buy cost for game balance
                        type_base_running_cost_points=0,  # dibble running costs for game balance
                        intro_date=1910)

consist.add_unit(type=SteamEngineUnit,
                 weight=45,
                 vehicle_length=7,
                 spriterow_num=0)
