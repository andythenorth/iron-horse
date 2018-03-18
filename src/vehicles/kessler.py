from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='kessler',
                        base_numeric_id=1990,
                        title='0-4-2 Kessler [Steam]',
                        power=450,
                        track_type='NG',
                        speed=45,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-7,  # dibble running costs for game balance
                        reversible=True,
                        intro_date=1860)

consist.add_unit(type=SteamEngineUnit,
                 weight=25,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)