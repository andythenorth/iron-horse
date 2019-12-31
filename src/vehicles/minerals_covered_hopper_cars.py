from train import GravityCoveredHopperCarMineralsConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4600,
                                      gen=2,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4610,
                                      gen=3,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4620,
                                      gen=4,
                                      subtype='A',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4630,
                                      gen=4,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_24px')

    # no gen 5A or 6A

    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4650,
                                      gen=5,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4660,
                                      gen=5,
                                      subtype='C',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4680,
                                      gen=6,
                                      subtype='B',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = GravityCoveredHopperCarMineralsConsist(roster_id='pony',
                                      base_numeric_id=4690,
                                      gen=6,
                                      subtype='C',
                                      sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    #--------------- llama ----------------------------------------------------------------------
