from train import AggregateHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = AggregateHopperCarConsist(roster='pony',
                               base_numeric_id=1610,
                               gen=5,
                               subtype='A',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = AggregateHopperCarConsist(roster='pony',
                               base_numeric_id=1600,
                               gen=5,
                               subtype='B',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')
