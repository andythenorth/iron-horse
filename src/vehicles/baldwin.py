from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='baldwin',
                        base_numeric_id=60,
                        title='2-8-2 Baldwin [Steam]',
                        power=1600,
                        track_type='NG',
                        speed=45,
                        intro_date=1920)

consist.add_unit(type=SteamLoco,
                 weight=70,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=25,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
