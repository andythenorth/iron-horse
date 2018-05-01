from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='collett',
                        base_numeric_id=1880,
                        name='0-6-0 Haar',
                        role='freight',
                        power=1450,
                        type_base_buy_cost_points=12,  # dibble buy cost for game balance
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)

