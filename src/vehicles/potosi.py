from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='potosi',
                        base_numeric_id=370,
                        name='4-8-2+2-8-4 Potosi',
                        power=4500,
                        type_base_buy_cost_points=5,  # dibble buy cost for game balance
                        intro_date=1935)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=65,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=1,
                 visual_effect_offset=-3)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=65,
                 vehicle_length=5,
                 spriterow_num=2)
