from train import ExpressCarConsist, ExpressCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------

    # no NG express cars in pony, use mail car

    #--------------- pony ----------------------------------------------------------------------

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1050,
                                gen=1,
                                subtype='A',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1060,
                                gen=2,
                                subtype='A',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1100,
                                gen=2,
                                subtype='B',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1110,
                                gen=3,
                                subtype='A',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='3_axle_solid_express_16px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1120,
                                gen=3,
                                subtype='B',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1390,
                                gen=4,
                                subtype='A',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1400,
                                gen=4,
                                subtype='B',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=3220,
                                gen=4,
                                subtype='C',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    # !! should there be no 4/8 car for gen 5-6? (but add 8/8 car instead starting gen 4)

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1410,
                                gen=5,
                                subtype='A',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1420,
                                gen=5,
                                subtype='B',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=3240,
                                gen=5,
                                subtype='C',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    # no gen 6A 4/8 express car, removed Feb 2019, excessive number of express cars

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=1510,
                                gen=6,
                                subtype='B',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = ExpressCarConsist(roster='pony',
                                base_numeric_id=3230,
                                gen=6,
                                subtype='C',
                                sprites_complete=True)

    consist.add_unit(type=ExpressCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')
