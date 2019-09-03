from train import EdiblesTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 or 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=3030,
                                    gen=2,
                                    subtype='A',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1190,
                                    gen=3,
                                    subtype='A',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='3_axle_filled_16px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=2990,
                                    gen=4,
                                    subtype='A',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='3_axle_filled_16px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1690,
                                    gen=4,
                                    subtype='B',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1220,
                                    gen=4,
                                    subtype='C',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1210,
                                    gen=5,
                                    subtype='A',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='3_axle_filled_16px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1700,
                                    gen=5,
                                    subtype='B',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=3050,
                                    gen=5,
                                    subtype='C',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')

    # gen 6A not included - could add?

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=2100,
                                    gen=6,
                                    subtype='B',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=2090,
                                    gen=6,
                                    subtype='C',
                                    sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
