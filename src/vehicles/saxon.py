from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='saxon',
                        base_numeric_id=1330,
                        name='0-8-0 Saxon',
                        role='branch_freight',
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        power=1000,
                        # dibble TE for game balance, assume magic or sand or something
                        tractive_effort_coefficient=0.35,
                        random_reverse=True,
                        gen=3,
                        intro_date_offset=-8)  # introduce earlier than gen epoch by design

consist.add_unit(type=SteamEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)
