from train import SlidingWallCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # gen 4 start, only B and C lengths

    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=410,
                            gen=5,
                            subtype='B',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')

    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=440,
                            gen=5,
                            subtype='C',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=330,
                            gen=6,
                            subtype='B',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=320,
                            gen=6,
                            subtype='C',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
