from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='suburban',
                        base_numeric_id=500,
                        title='2-6-2 Suburban [Steam]',
                        power=650,
                        tractive_effort_coefficient=0.2,
                        speed=80,
                        type_base_buy_cost_points=-2,  # dibble buy cost for game balance
                        type_base_running_cost_points=-6,  # dibble running costs for game balance
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=57,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)

consist.add_model_variant(spritesheet_suffix=1,
                          visual_effect_offset='AUTOFLIP')
