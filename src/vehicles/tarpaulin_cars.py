from train import TarpaulinCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = TarpaulinCarConsist(roster_id='pony',
                            base_numeric_id=340,
                            gen=5,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = TarpaulinCarConsist(roster_id='pony',
                            base_numeric_id=350,
                            gen=5,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = TarpaulinCarConsist(roster_id='pony',
                            base_numeric_id=370,
                            gen=6,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_24px')


    consist = TarpaulinCarConsist(roster_id='pony',
                            base_numeric_id=400,
                            gen=6,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
