from train import PassengerEngineRailcarConsist, ElectricRailcarUnit

consist = PassengerEngineRailcarConsist(id='athena',
                                        base_numeric_id=2150,
                                        name='Athena',
                                        role='pax_railcar',
                                        power=350, # RL EMU HP is much lower, but eh
                                        pantograph_type='diamond-single',
                                        gen=3,
                                        sprites_complete=False,
                                        intro_date_offset=-3)  # introduce early by design

consist.add_unit(type=ElectricRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=36,
                 chassis='railcar')
