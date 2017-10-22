from train import EngineConsist, SteamLoco

consist = EngineConsist(id='pequeno',
                        base_numeric_id=350,
                        title='0-4-0 Pequeno [Steam]',
                        power=350,
                        track_type='NG',
                        speed=35,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1865)

consist.add_unit(type=SteamLoco,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
