from train import EngineConsist, SteamEngineUnit

# basically a Q1, which is why it's 0-6-0 even though it replaces a 2-6-0

consist = EngineConsist(id='collett',
                        base_numeric_id=1880,
                        name='0-6-0 Haar',
                        role='freight',
                        power=1450,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)
