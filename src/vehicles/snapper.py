from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='snapper',
                                        base_numeric_id=590,
                                        name='Snapper',
                                        role='pax_railcar',
                                        base_track_type='NG',
                                        power=350,
                                        type_base_buy_cost_points=-18,  # dibble buy cost for game balance
                                        type_base_running_cost_points=-30,  # dibble running costs for game balance
                                        gen=4,
                                        sprites_complete=True)

consist.add_unit(type=DieselRailcarUnit,
                 weight=20,
                 vehicle_length=6,
                 capacity=30,
                 chassis='railcar_ng')
