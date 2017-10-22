from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='potosi',
                        base_numeric_id=370,
                        title='4-8-2+2-8-4 Potosi [Steam]',
                        power=4500,
                        speed=60,
                        type_base_buy_cost_points=5,  # dibble buy cost for game balance
                        type_base_running_cost_points=5,  # dibble running costs for game balance
                        intro_date=1935)

consist.add_unit(type=SteamLocoTender,
                 weight=65,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamLoco,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=1)

consist.add_unit(type=SteamLocoTender,
                 weight=65,
                 vehicle_length=5,
                 spriterow_num=2)

consist.add_model_variant(visual_effect_offset=-3,
                          spritesheet_suffix=0)
