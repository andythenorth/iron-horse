from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='high_flyer',
                        base_numeric_id=230,
                        title='4-4-2 High Flyer [Steam]',
                        power=1300,
                        tractive_effort_coefficient=0.10,
                        speed=80,
                        buy_cost=47,
                        gen=2)

consist.add_unit(type=SteamLoco,
                 weight=90,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
