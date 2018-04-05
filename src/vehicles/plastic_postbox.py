from train import MailEngineRailcarConsist, DieselRailcarUnit

consist = MailEngineRailcarConsist(id='plastic_postbox',
                            base_numeric_id=3080,
                            name='Plastic Postbox',
                            role='mail_railcar',
                            power=720,
                            speed=90,
                            type_base_running_cost_points=-32,  # dibble running costs for game balance
                            intro_date=1985)  # explicit intro date by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=3)

