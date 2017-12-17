from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='aberdare',
                        base_numeric_id=0,
                        title='2-6-0 Aberdare [Steam]',
                        power=1250,
                        tractive_effort_coefficient=0.22,
                        speed=45,
                        type_base_buy_cost_points=12,  # dibble buy cost for game balance
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=67,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=3,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
