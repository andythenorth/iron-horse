from train import CoalHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 hoppers in Pony eh
    # also just type A for gen 2 and 3

    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=2030,
                               gen=2,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=2040,
                               gen=3,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=2320,
                               gen=4,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=1380,
                               gen=4,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=1090,
                               gen=5,
                               subtype='B',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=2780,
                               gen=5,
                               subtype='C',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_32px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=3010,
                               gen=6,
                               subtype='B',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')


    consist = CoalHopperCarConsist(roster='pony',
                               base_numeric_id=3020,
                               gen=6,
                               subtype='C',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_32px')
