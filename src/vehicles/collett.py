from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

# basically a Q1, which is why it's 0-6-0 even though it replaces a 2-6-0

consist = EngineConsist(id='collett',
                        base_numeric_id=1880,
                        name='0-8-0 Haar',
                        role='freight',
                        power=1450,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=70,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=30,
                 vehicle_length=3,
                 spriterow_num=1)
