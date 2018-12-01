from train import EngineConsist, DieselEngineUnit

# Shredder replces Pegasus, so is 2 * 6/8
# a single 6/8 conflates with the branch engines, that's not useful

consist = EngineConsist(id='shredder',
                        base_numeric_id=900,
                        name='Shredder',
                        role='heavy_express_1', # Shredder is last of the heavy_express_1 type in Brit roster
                        power=2750,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        random_reverse=True,
                        intro_date_offset=2, # let's not have everything turn up in 1960
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=72,
                 vehicle_length=6,
                 spriterow_num=0,
                 repeat=2)
