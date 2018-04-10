from train import ReeferCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 reefer - straight to gen 2

    consist = ReeferCarConsist(roster='pony',
                               base_numeric_id=730,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')


    consist = ReeferCarConsist(roster='pony',
                               base_numeric_id=720,
                               gen=3,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)


    consist = ReeferCarConsist(roster='pony',
                               base_numeric_id=2560,
                               gen=4,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)


    consist = ReeferCarConsist(roster='pony',
                               base_numeric_id=2590,
                               gen=4,
                               subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = ReeferCarConsist(roster='pony',
                               base_numeric_id=2570,
                               gen=5,
                               subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = ReeferCarConsist(roster='pony',
                               base_numeric_id=2580,
                               gen=5,
                               subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_cc_filled_32px')
