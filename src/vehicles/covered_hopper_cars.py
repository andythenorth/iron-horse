from train import CoveredHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1270,
                                      gen=2,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1260,
                                      gen=3,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2940,
                                      gen=4,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_gapped_16px')

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1230,
                                      gen=4,
                                      subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='2_axle_gapped_24px')

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1240,
                                      gen=5,
                                      subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2700,
                                      gen=5,
                                      subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=3040,
                                      gen=6,
                                      subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2910,
                                      gen=6,
                                      subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    # no gen 6 covered hopper cars, cap to gen 5 in Pony

    #--------------- llama ----------------------------------------------------------------------
