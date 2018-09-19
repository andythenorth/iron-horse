from train import MailEngineMetroConsist, MetroUnit

consist = MailEngineMetroConsist(id='longwater',
                                 base_numeric_id=290,
                                 name='Longwater',
                                 role='mail_metro',
                                 power=600,
                                 type_base_buy_cost_points=36,  # dibble buy cost for game balance
                                 gen=1,
                                 sprites_complete=True)

consist.add_unit(type=MetroUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 chassis='railcar',
                 repeat=2)
