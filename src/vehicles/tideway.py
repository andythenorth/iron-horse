from train import MailEngineConsist, MetroUnit

consist = MailEngineConsist(id='tideway',
                            base_numeric_id=2200,
                            title='Tideway',
                            track_type='METRO',
                            power=1100,
                            speed=65,
                            type_base_buy_cost_points=36,  # dibble buy cost for game balance
                            intro_date=2000)

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

