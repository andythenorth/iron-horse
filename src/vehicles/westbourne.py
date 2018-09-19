from train import PassengerEngineMetroConsist, MetroUnit

consist = PassengerEngineMetroConsist(id='westbourne',
                                      base_numeric_id=360,
                                      name='Westbourne',
                                      role='pax_metro',
                                      power=900,
                                      type_base_buy_cost_points=60,  # dibble buy cost for game balance
                                      gen=2,
                                      sprites_complete=True)

consist.add_unit(type=MetroUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=160,
                 chassis='railcar',
                 repeat=2)
