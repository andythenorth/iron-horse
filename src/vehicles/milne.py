from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='milne',
                        base_numeric_id=2050,
                        name='4-8-2 Milne',
                        power=600,
                        track_type='NG',
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        random_reverse=True,
                        intro_date=1910)

consist.add_unit(type=SteamEngineUnit,
                 weight=50,
                 vehicle_length=7,
                 spriterow_num=0)
