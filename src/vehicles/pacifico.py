from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='pacifico',
                        base_numeric_id=310,
                        title='4-6-2 Pacifico [Steam]',
                        power=1800,
                        speed=65,
                        intro_date=1910)

consist.add_unit(type=SteamEngineUnit,
                 weight=90,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=5,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
