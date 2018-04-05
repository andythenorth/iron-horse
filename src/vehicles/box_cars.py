from train import BoxCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=580,
                            gen=1,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)


    #--------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=1780,
                            gen=1,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')


    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=550,
                            gen=2,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')


    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=560,
                            gen=3,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)


    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2340,
                            gen=3,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=570,
                            gen=4,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)


    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2500,
                            gen=4,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2480,
                            gen=5,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2490,
                            gen=5,
                            subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)


    # no gen 6 box cars, cap to gen 5 in Pony

    #--------------- llama ----------------------------------------------------------------------
    consist = BoxCarConsist(roster='llama',
                            base_numeric_id=590,
                            gen=1,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=5)


    consist = BoxCarConsist(roster='llama',
                            base_numeric_id=600,
                            gen=2,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='llama',
                            base_numeric_id=610,
                            gen=3,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=7)


    consist = BoxCarConsist(roster='llama',
                            base_numeric_id=620,
                            gen=1,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='llama',
                            base_numeric_id=1310,
                            gen=2,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    #--------------- antelope ----------------------------------------------------------------------
    consist = BoxCarConsist(roster='antelope',
                            base_numeric_id=1750,
                            gen=1,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='antelope',
                            base_numeric_id=1740,
                            gen=2,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)


    consist = BoxCarConsist(roster='antelope',
                            base_numeric_id=2100,
                            gen=1,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=5)


    consist = BoxCarConsist(roster='antelope',
                            base_numeric_id=1850,
                            gen=2,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = BoxCarConsist(roster='antelope',
                            base_numeric_id=1860,
                            gen=3,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

