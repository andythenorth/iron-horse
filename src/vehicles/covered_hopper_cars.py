from train import CoveredHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4500,
                                      gen=2,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4510,
                                      gen=3,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4520,
                                      gen=4,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4530,
                                      gen=4,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_24px')

    # no gen 5A or 6A

    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4550,
                                      gen=5,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_greebled_24px')


    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4560,
                                      gen=5,
                                      subtype='C',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4580,
                                      gen=6,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_greebled_24px')


    consist = CoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4590,
                                      gen=6,
                                      subtype='C',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    #--------------- llama ----------------------------------------------------------------------
