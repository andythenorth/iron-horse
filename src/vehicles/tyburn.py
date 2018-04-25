from train import MailEngineConsist, MetroUnit

consist = MailEngineConsist(id='tyburn',
                            base_numeric_id=2190,
                            name='Tyburn',
                            role='mail_metro',
                            track_type='METRO',
                            power=900,
                            type_base_buy_cost_points=56,  # dibble buy cost for game balance
                            intro_date=1950)

consist.add_unit(type=MetroUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=0)

consist.add_unit(type=MetroUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=1)

