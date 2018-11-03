from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='happy_train',
                                        base_numeric_id=100,
                                        name='Happy Train',
                                        role='pax_railcar',
                                        power=500,
                                        gen=6,
                                        sprites_complete=True,
                                        intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 chassis='railcar')
