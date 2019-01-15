from train import MailEngineRailcarConsist, ElectricRailcarUnit

consist = MailEngineRailcarConsist(id='ares',
                                   base_numeric_id=2130,
                                   name='Ares',
                                   role='mail_railcar',
                                   power=550,
                                   pantograph_type='diamond-single',
                                   easter_egg_haulage_speed_bonus=True,
                                   gen=3,
                                   sprites_complete=False,
                                   intro_date_offset=-3)  # introduce early by design

consist.add_unit(type=ElectricRailcarUnit,
                 weight=43,
                 vehicle_length=8,
                 # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                 capacity=20,
                 chassis='railcar')
