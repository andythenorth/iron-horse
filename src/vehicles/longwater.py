from train import MailEngineMetroConsist, MetroUnit

consist = MailEngineMetroConsist(id='longwater',
                                 base_numeric_id=290,
                                 name='Longwater',
                                 role='mail_metro',
                                 track_type='METRO',
                                 power=600,
                                 type_base_buy_cost_points=36,  # dibble buy cost for game balance
                                 gen=2)  # no intro_date_offset for this unit by design

consist.add_unit(type=MetroUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 chassis='railcar',
                 repeat=2)
