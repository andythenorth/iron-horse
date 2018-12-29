from train import PassengerVeryHighSpeedMiddleEngineConsist, ElectricPaxUnit

consist = PassengerVeryHighSpeedMiddleEngineConsist(id='landlash_middle',
                                                    base_numeric_id=2870,
                                                    name='Landlash - Middle',
                                                    role='pax_high_speed',
                                                    power=0, # set power 0, when attached to correct cab, cab power will be increased
                                                    gen=5,
                                                    intro_date_offset=10)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricPaxUnit,
                 weight=41,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0,
                 chassis='4_axle_solid_express_32px',
                 repeat=2)

