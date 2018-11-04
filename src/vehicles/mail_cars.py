from train import MailCarConsist, MailCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = MailCarConsist(roster='pony',
                             base_numeric_id=950,
                             gen=1,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=610,
                             gen=3,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=670,
                             gen=4,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2280,
                             gen=1,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2220,
                             gen=1,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2290,
                             gen=2,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=920,
                             gen=2,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=1830,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2300,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=940,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=1430,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=3160,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=3170,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=520,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=970,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=3140,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=870,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=1950,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=10,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=MailCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')
