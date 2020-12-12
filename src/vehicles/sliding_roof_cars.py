from train import SlidingRoofCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = SlidingRoofCarConsist(roster_id='pony',
                            base_numeric_id=5230,
                            gen=5,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingRoofCarConsist(roster_id='pony',
                            base_numeric_id=5240,
                            gen=5,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingRoofCarConsist(roster_id='pony',
                            base_numeric_id=5220,
                            gen=6,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingRoofCarConsist(roster_id='pony',
                            base_numeric_id=5210,
                            gen=6,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
