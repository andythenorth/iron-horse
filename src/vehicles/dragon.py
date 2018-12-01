from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='dragon',
                        base_numeric_id=420,
                        name='Dragon',
                        role='express_1',
                        power=2050, # one-off huge jump in HP compared to steam engine of same era
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        random_reverse=True,
                        gen=4,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=85,
                 vehicle_length=8,
                 spriterow_num=0)
