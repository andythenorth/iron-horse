from train import MailEngineMetroConsist, MetroUnit

consist = MailEngineMetroConsist(id='tideway',
                                 base_numeric_id=2200,
                                 name='Tideway',
                                 role='mail_metro',
                                 power=1100,
                                 type_base_buy_cost_points=36,  # dibble buy cost for game balance
                                 gen=3,
                                 sprites_complete=True)

consist.add_unit(type=MetroUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=60,
                 chassis='railcar',
                 repeat=2)
