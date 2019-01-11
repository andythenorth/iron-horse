from train import PassengerEngineRailcarConsist, ElectricRailcarUnit

consist = PassengerEngineRailcarConsist(id='geronimo',
                                        base_numeric_id=2140,
                                        name='Geronimo',
                                        role='pax_railcar',
                                        power=1500, # RL EMU HP is much lower, but eh
                                        pantograph_type='z-shaped-single',
                                        gen=4,
                                        sprites_complete=False,
                                        intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=ElectricRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar',
                 repeat=3)
