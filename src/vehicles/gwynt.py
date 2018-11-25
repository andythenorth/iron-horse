from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='gwynt',
                        base_numeric_id=1330,
                        name='2-8-2 Gwynt',
                        role='branch_freight',
                        power=1000,
                        random_reverse=True,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)
