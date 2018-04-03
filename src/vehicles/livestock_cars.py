from train import LivestockCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1030,
                                  gen=1,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)


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
                                  subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)


    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2710,
                                  gen=6,
                                  subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)
