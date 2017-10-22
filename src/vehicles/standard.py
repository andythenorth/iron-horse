from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='standard',
                        base_numeric_id=480,
                        title='4-2-2 Standard [Steam]',
                        power=950,
                        tractive_effort_coefficient=0.07,
                        speed=65,
                        type_base_buy_cost_points=18,  # dibble buy cost for game balance
                        gen=1)

consist.add_unit(type=SteamLoco,
                 weight=62,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
