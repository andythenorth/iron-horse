from train import PassengerVeryHighSpeedCabEngineConsist, ElectricPaxUnit

consist = PassengerVeryHighSpeedCabEngineConsist(id='pendolino_thing_cab',
                                                 base_numeric_id=980,
                                                 name='Blaze - Cab',
                                                 role='pax_high_speed',
                                                 dual_headed=True,
                                                 power=1900,
                                                 gen=5,
                                                 intro_date_offset=10)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricPaxUnit,
                 weight=41,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0,
                 chassis='4_axle_solid_express_32px',
                 repeat=2)
