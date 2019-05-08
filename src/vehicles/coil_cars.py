from train import CoilCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2030,
                             gen=4,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2040,
                             gen=4,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2010,
                             gen=5,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2020,
                             gen=5,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=1990,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2000,
                             gen=6,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
