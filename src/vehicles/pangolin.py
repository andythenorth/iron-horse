from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='pangolin',
                        base_numeric_id=2060,
                        title='2-6-0 Pangolin [Steam]',
                        power=1200,
                        track_type='NG',
                        speed=45,
                        type_base_buy_cost_points=0,  # dibble buy cost for game balance
                        type_base_running_cost_points=5,  # dibble running costs for game balance
                        intro_date=1860)

consist.add_unit(type=SteamLoco,
                 weight=40,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=27,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
