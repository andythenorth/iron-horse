from train import MailCarConsist, TrainCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = MailCarConsist(roster='pony',
                             base_numeric_id=950,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=4)

    #--------------- pony ----------------------------------------------------------------------

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2280,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=10,
                     vehicle_length=4)


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2220,
                             gen=1,
                             subtype='B')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2290,
                             gen=2,
                             subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=10,
                     vehicle_length=4)


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=920,
                             gen=2,
                             subtype='B')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=1830,
                             gen=3,
                             subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=10,
                     vehicle_length=4)


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=2300,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=940,
                             gen=3,
                             subtype='C')

    consist.add_unit(type=TrainCar,
                     capacity=15,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=1430,
                             gen=4,
                             subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=4,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=3160,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=3170,
                             gen=4,
                             subtype='C')

    consist.add_unit(type=TrainCar,
                     capacity=15,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=970,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=3140,
                             gen=5,
                             subtype='C')

    consist.add_unit(type=TrainCar,
                     capacity=15,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')


    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = MailCarConsist(roster='pony',
                             base_numeric_id=1950,
                             gen=6,
                             subtype='B')

    consist.add_unit(type=TrainCar,
                     capacity=12,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = MailCarConsist(roster='pony',
                             base_numeric_id=10,
                             gen=6,
                             subtype='C')

    consist.add_unit(type=TrainCar,
                     capacity=15,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')