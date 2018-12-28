from train import EngineConsist, DieselEngineUnit

# Scorcher changes the game from previous generations by going dual-headed
# ¿¿ but should it use wagon attach cb to restrict to pax and express vehicles only ??

consist = EngineConsist(id='scorcher',
                        base_numeric_id=2950,
                        name='Scorcher',
                        role='heavy_express_1',
                        power=4500,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        dual_headed=True,
                        intro_date_offset=-2, # let's be a little bit earlier for this one
                        gen=5,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=70,
                 vehicle_length=8,
                 spriterow_num=0)
