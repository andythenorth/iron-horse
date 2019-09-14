from train import DumpCarHighSideConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3860,
                             gen=3,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3870,
                             gen=3,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3780,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3790,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3800,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3810,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3820,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3830,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3840,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarHighSideConsist(roster='pony',
                             base_numeric_id=3850,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
