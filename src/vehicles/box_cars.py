from train import BoxCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=580,
                            gen=1,
                            subtype='U',
                            base_track_type='NG',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=1180,
                            gen=3,
                            subtype='U',
                            base_track_type='NG',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=810,
                            gen=4,
                            subtype='U',
                            base_track_type='NG',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=1780,
                            gen=1,
                            subtype='A',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=550,
                            gen=2,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=560,
                            gen=3,
                            subtype='A',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2340,
                            gen=3,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=570,
                            gen=4,
                            subtype='A',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2500,
                            gen=4,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_24px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2480,
                            gen=5,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_24px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=2490,
                            gen=5,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=1670,
                            gen=6,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_24px')

    consist = BoxCarConsist(roster='pony',
                            base_numeric_id=1680,
                            gen=6,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
