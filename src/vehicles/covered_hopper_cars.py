from train import CoveredHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1270,
                                      gen=2,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1260,
                                      gen=3,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2940,
                                      gen=4,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1230,
                                      gen=4,
                                      subtype='B',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_24px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2070,
                                      gen=5,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=1240,
                                      gen=5,
                                      subtype='B',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2700,
                                      gen=5,
                                      subtype='C',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2060,
                                      gen=6,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=3040,
                                      gen=6,
                                      subtype='B',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = CoveredHopperCarConsist(roster='pony',
                                      base_numeric_id=2910,
                                      gen=6,
                                      subtype='C',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    #--------------- llama ----------------------------------------------------------------------
