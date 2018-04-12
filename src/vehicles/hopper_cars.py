from train import HopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 hoppers in Pony eh
    # also just type A for gen 1

    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2310,
                               gen=2,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1070,
                               gen=3,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2330,
                               gen=3,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2320,
                               gen=4,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1380,
                               gen=4,
                               subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1080,
                               gen=5,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1090,
                               gen=5,
                               subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2780,
                               gen=5,
                               subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=3010,
                               gen=6,
                               subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=3020,
                               gen=6,
                               subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)


    #--------------- llama ----------------------------------------------------------------------
    consist = HopperCarConsist(roster='llama',
                               base_numeric_id=1100,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='llama',
                               base_numeric_id=1110,
                               gen=3,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='llama',
                               base_numeric_id=1120,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='llama',
                               base_numeric_id=1130,
                               gen=3,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    #--------------- antelope ----------------------------------------------------------------------
    consist = HopperCarConsist(roster='antelope',
                               base_numeric_id=1630,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = HopperCarConsist(roster='antelope',
                               base_numeric_id=1660,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    # no gen 1 NG hopper in Antelope, straight to gen 2
    consist = HopperCarConsist(roster='antelope',
                               base_numeric_id=1890,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

