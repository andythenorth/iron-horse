from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='ndemi',
                        base_numeric_id=2070,
                        title='4-8-0 Ndemi [Steam]',
                        power=1700,
                        track_type='NG',
                        speed=35,
                        type_base_buy_cost_points=35,  # dibble buy cost for game balance
                        type_base_running_cost_points=35,  # dibble running costs for game balance
                        intro_date=1887)

consist.add_unit(type=SteamLoco,
                 weight=75,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=35,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
