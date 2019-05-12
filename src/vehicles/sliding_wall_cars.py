from train import SlidingWallCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # starts with gen 4C only, then gen 5 and 6, B and C lengths

    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=1790,
                            gen=4,
                            subtype='C',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=410,
                            gen=5,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=440,
                            gen=5,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=330,
                            gen=6,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingWallCarConsist(roster='pony',
                            base_numeric_id=320,
                            gen=6,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
