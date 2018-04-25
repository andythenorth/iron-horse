from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='happy_train',
                                 base_numeric_id=100,
                                 name='Happy Train',
                                 role='pax_railcar',
                                 power=750,
                                 type_base_running_cost_points=-36,  # dibble running costs for game balance
                                 intro_date=2015)  # explicit intro date by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 chassis='railcar')

