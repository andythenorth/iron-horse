from train import EngineConsist, SteamLoco

consist = EngineConsist(id='oubangui',
                        base_numeric_id=2010,
                        title='2-6-6-2 Oubangui [Steam]',
                        power=1500,
                        track_type='NG',
                        speed=55,
                        intro_date=1920)

consist.add_unit(type=SteamLoco,
                 weight=90,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
