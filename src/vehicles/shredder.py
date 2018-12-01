from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='shredder',
                        base_numeric_id=900,
                        name='Shredder',
                        role='express_1',
                        power=1300,
                        # nerf TE for game balance, assume magic or sand or something
                        tractive_effort_coefficient=0.27,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        random_reverse=True,
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=72,
                 vehicle_length=6,
                 spriterow_num=0)
