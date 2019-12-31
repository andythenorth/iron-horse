from train import GravityCoveredHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4500,
                                      gen=2,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4510,
                                      gen=3,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4520,
                                      gen=4,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4530,
                                      gen=4,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_24px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4540,
                                      gen=5,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4550,
                                      gen=5,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4560,
                                      gen=5,
                                      subtype='C',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4570,
                                      gen=6,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4580,
                                      gen=6,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = GravityCoveredHopperCarConsist(roster_id='pony',
                                      base_numeric_id=4590,
                                      gen=6,
                                      subtype='C',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    #--------------- llama ----------------------------------------------------------------------
