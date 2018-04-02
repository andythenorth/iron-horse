from train import FlatCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1170,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=3)


    #--------------- pony ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1140,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    # no gen 2A, gen 1A continues in pony

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1150,
                             gen=2,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')


    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1160,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')


    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2550,
                             gen=3,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     vehicle_length=8,
                     chassis='4_axle_gapped_32px')


    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2540,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6)


    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2530,
                             gen=4,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     vehicle_length=8)


    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2520,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6)


    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2510,
                             gen=5,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     vehicle_length=8)


    # no gen 6 flat cars, cap to gen 5 in Pony
