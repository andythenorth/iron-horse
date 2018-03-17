from train import MailEngineConsist, MetroUnit

consist = MailEngineConsist(id='longwater',
                            base_numeric_id=290,
                            title='Longwater [Metro Train]',
                            track_type='METRO',
                            power=600,
                            speed=40,
                            type_base_buy_cost_points=36,  # dibble buy cost for game balance
                            intro_date=1900)

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

consist.add_model_variant(spritesheet_suffix=0)
