from train import PassengerVeryHighSpeedCabEngineConsist, ElectricPaxUnit

consist = PassengerVeryHighSpeedCabEngineConsist(id='brenner_cab',
                                                 base_numeric_id=130,
                                                 name='Brenner - Cab',
                                                 role='pax_high_speed',
                                                 dual_headed=True,
                                                 power=2600,
                                                 gen=6)  # no intro date offset for this unit

# 4 units (2-tiles) because building these is annoying if the units are too small?
# or 2 units (1-tile) to make any integer length?

consist.add_unit(type=ElectricPaxUnit,
                 weight=55,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0,
                 chassis='4_axle_solid_express_32px')
