from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='standard',
                        base_numeric_id=480,
                        name='4-2-2 Standard',
                        role='express_1',
                        power=950,
                        tractive_effort_coefficient=0.07,
                        speed=65,
                        type_base_buy_cost_points=18,  # dibble buy cost for game balance
                        gen=1)

consist.add_unit(type=SteamEngineUnit,
                 weight=62,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)

