from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='mumble',
                                        base_numeric_id=140,
                                        name='Mumble',
                                        role='pax_railcar',
                                        base_track_type='NG',
                                        power=250,
                                        type_base_buy_cost_points=-18,  # dibble buy cost for game balance
                                        gen=3,
                                        sprites_complete=True)

consist.add_unit(type=DieselRailcarUnit,
                 weight=20,
                 vehicle_length=6,
                 capacity=30,
                 chassis='railcar_ng')
