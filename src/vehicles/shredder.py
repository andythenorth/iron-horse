from train import EngineConsist, DieselEngineUnit

# as of Dec 2018 there is no replacement for Shredder in the tech tree

consist = EngineConsist(id='shredder',
                        base_numeric_id=900,
                        name='Shredder',
                        role='express_1',
                        power=1450,
                        random_reverse=True,
                        intro_date_offset=-2, # let's not have everything turn up in 1960
                        gen=4,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=72,
                 vehicle_length=6,
                 spriterow_num=0)
