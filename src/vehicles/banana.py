from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='banana',
                                        base_numeric_id=1770,
                                        name='Deasil',
                                        role='pax_railcar',
                                        power=200,
                                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                                        gen=3,
                                        intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=30,
                 chassis='railcar')
