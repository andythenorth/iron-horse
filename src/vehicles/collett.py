from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='collett',
                        base_numeric_id=1880,
                        title='2-8-2 Collett [Steam]',
                        power=1400,
                        speed=60,
                        type_base_buy_cost_points=12,  # dibble buy cost for game balance
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)

