from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='tin_rocket',
                                 base_numeric_id=530,
                                 name='Tin Rocket',
                                 role='pax_railcar',
                                 power=600,
                                 type_base_running_cost_points=-36,  # dibble running costs for game balance
                                 intro_date=1985)  # explicit intro date by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 chassis='railcar')

