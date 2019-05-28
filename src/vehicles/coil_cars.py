from train import CoilCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # start gen 4, B and C lengths only

    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2950,
                             gen=4,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=3250,
                             gen=4,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=3320,
                             gen=5,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=3330,
                             gen=5,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=3340,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=3350,
                             gen=6,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
