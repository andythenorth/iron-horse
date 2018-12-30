from train import EngineConsist, DieselEngineUnit

# as of Dec 2018 there is no replacement for Shredder 2 in the tech tree
# the assumption is that the Ultra Shoebox can replace it eh?
# this might cause a monoculture of Ultra Shoeboxes, which might be boring?

consist = EngineConsist(id='griffon',
                        base_numeric_id=2840,
                        name='Griffon',
                        role='express_1',
                        power=1650,
                        random_reverse=True,
                        gen=5,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=72,
                 vehicle_length=6,
                 spriterow_num=0)
