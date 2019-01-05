from train import PassengerVeryHighSpeedMiddleEngineConsist, ElectricPaxUnit

consist = PassengerVeryHighSpeedMiddleEngineConsist(id='brenner_middle',
                                                    base_numeric_id=2880,
                                                    name='Brenner - Middle',
                                                    role='pax_high_speed',
                                                    power=0, # set power 0, when attached to correct cab, cab power will be increased
                                                    gen=6) # no intro date offset for this unit

# 4 units (2-tiles) because building these is annoying if the units are too small?
# or 2 units (1-tile) to make any integer length?

consist.add_unit(type=ElectricPaxUnit,
                 weight=55,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0,
                 chassis='4_axle_solid_express_articulated_32px',
                 repeat=2)

