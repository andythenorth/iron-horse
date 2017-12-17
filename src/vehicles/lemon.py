from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='lemon',
                        base_numeric_id=270,
                        title='4-8-0 Lemon [Steam]',
                        power=2400,
                        tractive_effort_coefficient=0.29,
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        speed=60,
                        buy_cost=114,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=115,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=50,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
