from train import HopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2310,
                               gen=2,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1070,
                               gen=3,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2330,
                               gen=3,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1080,
                               gen=4,
                               subtype='A',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2000,
                               gen=4,
                               subtype='B',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2010,
                               gen=4,
                               subtype='C',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1610,
                               gen=5,
                               subtype='A',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1600,
                               gen=5,
                               subtype='B',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1620,
                               gen=5,
                               subtype='C',
                               intro_date_offset=5,  # let's be a little bit later for this one
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2020,
                               gen=6,
                               subtype='B',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1990,
                               gen=6,
                               subtype='C',
                               sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
