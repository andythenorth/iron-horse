from train import AutomatedHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = AutomatedHopperCarConsist(roster='pony',
                               base_numeric_id=1610,
                               gen=4,
                               subtype='A',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = AutomatedHopperCarConsist(roster='pony',
                               base_numeric_id=1600,
                               gen=4,
                               subtype='B',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')
