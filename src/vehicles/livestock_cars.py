from train import LivestockCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1030,
                                  gen=1,
                                  subtype='A',
                                  base_track_type='NG',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1010,
                                  gen=1,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    # no gen 2 needed

    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2680,
                                  gen=3,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1020,
                                  gen=4,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2720,
                                  gen=5,
                                  subtype='C',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_2cc_filled_32px')

    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2710,
                                  gen=6,
                                  subtype='C',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_2cc_filled_32px')
