from train import CoilCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # start gen 4, B and C lengths only

    consist = CoilCarConsist(roster_id='pony',
                             base_numeric_id=3510,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = CoilCarConsist(roster_id='pony',
                             base_numeric_id=3520,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = CoilCarConsist(roster_id='pony',
                             base_numeric_id=3530,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = CoilCarConsist(roster_id='pony',
                             base_numeric_id=3540,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = CoilCarConsist(roster_id='pony',
                             base_numeric_id=3550,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_2cc_filled_24px')


    consist = CoilCarConsist(roster_id='pony',
                             base_numeric_id=3560,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_2cc_filled_32px')
