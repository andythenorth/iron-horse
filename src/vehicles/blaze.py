from train import EngineConsist, DieselEngineUnit

# no wagon attach cb should be used, let them eat cake etc.

consist = EngineConsist(id='blaze',
                        base_numeric_id=2860,
                        name='Blaze',
                        role='heavy_express_1',
                        power=5350,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        dual_headed=True,
                        intro_date_offset=-2, # let's be a little bit earlier for this one
                        gen=6,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=70,
                 vehicle_length=8,
                 spriterow_num=0)
