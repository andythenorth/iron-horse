from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='chaplin',
                        base_numeric_id=110,
                        title='2-4-0 Chaplin [Steam]',
                        power=500,
                        tractive_effort_coefficient=0.2,
                        speed=65,
                        type_base_buy_cost_points=-3,  # dibble buy cost for game balance
                        reversible=True,
                        gen=1)

consist.add_unit(type=SteamEngineUnit,
                 weight=35,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)