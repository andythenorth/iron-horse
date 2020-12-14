from train import BolsterCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5280,
                                  gen=1,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    # no gen 2A, gen 1A continues in pony

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5290,
                                  gen=2,
                                  subtype='B',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5300,
                                  gen=3,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5310,
                                  gen=3,
                                  subtype='B',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5320,
                                  gen=3,
                                  subtype='C',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5330,
                                  gen=4,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5340,
                                  gen=4,
                                  subtype='B',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5350,
                                  gen=4,
                                  subtype='C',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5360,
                                  gen=5,
                                  subtype='B',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5250,
                                  gen=5,
                                  subtype='C',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5260,
                                  gen=6,
                                  subtype='B',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')

    consist = BolsterCarConsist(roster_id='pony',
                                  base_numeric_id=5270,
                                  gen=6,
                                  subtype='C',
                                  sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
