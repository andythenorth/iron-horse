from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='pequeno',
                        base_numeric_id=350,
                        name='0-4-0 Pequeno',
                        power=350,
                        base_track_type='NG',
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        intro_date=1865)

consist.add_unit(type=SteamEngineUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=0)
