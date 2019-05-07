from train import CoilCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=1990,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_sparse_24px')


    consist = CoilCarConsist(roster='pony',
                             base_numeric_id=2000,
                             gen=6,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_sparse_32px')
