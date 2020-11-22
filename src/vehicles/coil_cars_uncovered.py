from train import CoilCarUncoveredConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # start gen 4

    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5000,
                                      gen=4,
                                      subtype='A',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5010,
                                      gen=4,
                                      subtype='B',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5020,
                                      gen=4,
                                      subtype='C',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')

    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5030,
                                      gen=5,
                                      subtype='B',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')

    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5040,
                                      gen=5,
                                      subtype='C',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')

    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5050,
                                      gen=6,
                                      subtype='B',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_24px')

    consist = CoilCarUncoveredConsist(roster_id='pony',
                                      base_numeric_id=5060,
                                      gen=6,
                                      subtype='C',
                                      sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
