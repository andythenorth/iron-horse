from train import StakeCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=2740,
                              gen=2,
                              subtype='A',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=2730,
                              gen=3,
                              subtype='A',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=2750,
                              gen=3,
                              subtype='B',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     cargo_length=6,
                     chassis='4_axle_filled_24px')

    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=1710,
                              gen=4,
                              subtype='A',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=2760,
                              gen=4,
                              subtype='B',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     cargo_length=6,
                     chassis='4_axle_filled_24px')

    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=930,
                              gen=5,
                              subtype='A',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = StakeCarConsist(roster='pony',
                              base_numeric_id=2770,
                              gen=5,
                              subtype='B',
                              sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    # no gen 6 stake cars, cap to gen 5 in Pony

    # --------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------
