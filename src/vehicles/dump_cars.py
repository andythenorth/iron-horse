from train import DumpCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=30,
                             gen=3,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=40,
                             gen=4,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------
    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2350,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2360,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2370,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2380,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=1340,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=1810,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2110,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=1940,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2400,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2390,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
