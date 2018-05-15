from train import MailEngineConsist, MetroUnit

consist = MailEngineConsist(id='tideway',
                            base_numeric_id=2200,
                            name='Tideway',
                            role='mail_metro',
                            track_type='METRO',
                            power=1100,
                            type_base_buy_cost_points=36,  # dibble buy cost for game balance
                            gen=5,
                            intro_date_offset=10)  # introduce later than gen epoch by design

consist.add_unit(type=MetroUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=0)

consist.add_unit(type=MetroUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=1)
