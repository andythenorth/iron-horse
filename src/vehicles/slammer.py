from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='slammer',
                                 base_numeric_id=470,
                                 name='Slammer',
                                 role='pax_railcar',
                                 power=300,
                                 type_base_running_cost_points=-32,  # dibble running costs for game balance
                                 gen=4,
                                 intro_date_offset=-5) # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar')

