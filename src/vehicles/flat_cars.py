from train import FlatCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1170,
                             gen=1,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1130,
                             gen=3,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1370,
                             gen=4,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1140,
                             gen=1,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    # no gen 2A, gen 1A continues in pony

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1150,
                             gen=2,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1350,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1160,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2550,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     vehicle_length=8,
                     chassis='4_axle_gapped_32px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2540,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='2_axle_filled_24px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2530,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     vehicle_length=8,
                     chassis='4_axle_gapped_32px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2520,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='2_axle_filled_24px')

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2510,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     vehicle_length=8,
                     chassis='4_axle_1cc_filled_32px')
