from train import HopperCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------

    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=3590,
                               gen=1,
                               subtype='U',
                               base_track_type='NG',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=3600,
                               gen=3,
                               subtype='U',
                               base_track_type='NG',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=3610,
                               gen=4,
                               subtype='U',
                               base_track_type='NG',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')


    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 hoppers in Pony eh
    # also just type A for gen 2 and 3

    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=2030,
                               gen=2,
                               subtype='A',
                               intro_date_offset=-10,  # let's be earlier for this one
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=2040,
                               gen=3,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=2320,
                               gen=4,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=1380,
                               gen=4,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=1090,
                               gen=5,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=2780,
                               gen=5,
                               subtype='C',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=3010,
                               gen=6,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = HopperCarConsist(roster_id='pony',
                               base_numeric_id=3020,
                               gen=6,
                               subtype='C',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')
