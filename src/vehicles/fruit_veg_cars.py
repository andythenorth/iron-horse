from train import FruitVegCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=1310,
                                 gen=1,
                                 subtype='U',
                                 base_track_type='NG',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=1360,
                                 gen=3,
                                 subtype='U',
                                 base_track_type='NG',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=1520,
                                 gen=4,
                                 subtype='U',
                                 base_track_type='NG',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony --------------------------------------------------------------------------
    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2640,
                                 gen=2,
                                 subtype='A',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2630,
                                 gen=3,
                                 subtype='A',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2620,
                                 gen=3,
                                 subtype='B',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_filled_24px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2600,
                                 gen=4,
                                 subtype='A',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2610,
                                 gen=4,
                                 subtype='B',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='2_axle_filled_24px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2650,
                                 gen=5,
                                 subtype='B',
                                 sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='2_axle_filled_24px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2660,
                                 gen=5,
                                 subtype='C',
                                 sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_filled_32px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=1890,
                                 gen=6,
                                 subtype='B',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='2_axle_filled_24px')

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=1900,
                                 gen=6,
                                 subtype='C',
                                 sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_2cc_filled_32px')

