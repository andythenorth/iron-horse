from train import EngineConsist, DieselEngineUnit

# as of Dec 2018 - is there any replacement for Shredder in the tech tree?
# the assumption was that the Shoebox can replace it eh?
# this might cause a monoculture of Shoeboxes, which might be boring?

consist = EngineConsist(id='kelpie',
                        base_numeric_id=900,
                        name='Kelpie',
                        role='express_1',
                        power=1450,
                        random_reverse=True,
                        intro_date_offset=-2,  # let's not have everything turn up in 1960
                        gen=4,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=72,
                 vehicle_length=6,
                 spriterow_num=0)
