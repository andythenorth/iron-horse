from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='northcock',
                        base_numeric_id=300,
                        title='2-8-2 Northcock [Steam]',
                        power=1750,
                        tractive_effort_coefficient=0.2,
                        speed=95,
                        buy_cost=81,
                        gen=3)

consist.add_unit(type=SteamLoco,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=50,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
