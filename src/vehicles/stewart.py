from train import EngineConsist, SteamLoco

consist = EngineConsist(id='stewart',
                        base_numeric_id=490,
                        title='4-4-0 Stewart [Steam]',
                        track_type='NG',
                        power=350,
                        tractive_effort_coefficient=0.2,
                        speed=40,
                        type_base_buy_cost_points=-5,  # dibble buy cost for game balance
                        type_base_running_cost_points=0,  # dibble running costs for game balance
                        intro_date=1860)

consist.add_unit(type=SteamLoco,
                 weight=30,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)

consist.add_model_variant(spritesheet_suffix=1)
