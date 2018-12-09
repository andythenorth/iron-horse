from train import ExpressCarConsist, ExpressCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------

    # no NG express cars in pony, use mail car

    #--------------- pony ----------------------------------------------------------------------

    consist = ExpressCarConsist(roster='pony',
                             base_numeric_id=1050,
                             gen=1,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')


    consist = ExpressCarConsist(roster='pony',
                             base_numeric_id=1060,
                             gen=2,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')


    consist = ExpressCarConsist(roster='pony',
                             base_numeric_id=1100,
                             gen=2,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = ExpressCarConsist(roster='pony',
                             base_numeric_id=1110,
                             gen=3,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')


    consist = ExpressCarConsist(roster='pony',
                             base_numeric_id=1120,
                             gen=3,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

