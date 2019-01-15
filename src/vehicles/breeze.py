from train import PassengerEngineRailcarConsist, ElectricRailcarUnit

consist = PassengerEngineRailcarConsist(id='breeze',
                                        base_numeric_id=3200,
                                        name='Breeze',
                                        role='pax_railcar',
                                        power=650, # RL EMU HP is much lower, but eh
                                        pantograph_type='z-shaped-single',
                                        easter_egg_haulage_speed_bonus=True,
                                        gen=5,
                                        sprites_complete=False,
                                        intro_date_offset=-3)  # introduce early by design

consist.add_unit(type=ElectricRailcarUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar')
