from train import OpenCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=850,
                             gen=1,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2160,
                             gen=3,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='4_axle_ng_16px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=910,
                             gen=4,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=820,
                             gen=1,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    # no new type A for gen 2, gen 1 type A continues

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=830,
                             gen=2,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='4_axle_gapped_24px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=840,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2440,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='4_axle_gapped_24px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=1450,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2450,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2460,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2470,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_1cc_filled_32px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=1650,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=1660,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_1cc_filled_32px')
