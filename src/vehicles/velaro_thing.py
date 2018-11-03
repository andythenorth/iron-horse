from train import PassengerEngineVeryHighSpeedConsist, ElectricPaxUnit

consist = PassengerEngineVeryHighSpeedConsist(id='velaro_thing',
                                              base_numeric_id=130,
                                              name='Brenner',
                                              role='pax_high_speed',
                                              power=2600,
                                              gen=6)  # no intro date offset for this unit

# 4 units (2-tiles) because building these is annoying if the units are too small?
# or 2 units (1-tile) to make any integer length?

consist.add_unit(type=ElectricPaxUnit,
                 weight=55,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0,
                 chassis='4_axle_solid_express_32px',
                 repeat=2)
