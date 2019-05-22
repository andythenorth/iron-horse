from train import AggregateHopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = AggregateHopperCarConsist(roster='pony',
                               base_numeric_id=1610,
                               gen=5,
                               subtype='A',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = AggregateHopperCarConsist(roster='pony',
                               base_numeric_id=1600,
                               gen=5,
                               subtype='B',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = AggregateHopperCarConsist(roster='pony',
                               base_numeric_id=1620,
                               gen=5,
                               subtype='C',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')
