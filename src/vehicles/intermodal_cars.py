from train import IntermodalCarConsist, IntermodalCar


def main():
    #--------------- pony ng ----------------------------------------------------------------------
    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3960,
                                   gen=4,
                                   subtype='U',
                                   base_track_type='NG',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_ng_16px')


    #--------------- pony ----------------------------------------------------------------------
    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3880,
                                   gen=4,
                                   subtype='A',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='2_axle_filled_16px')


    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3890,
                                   gen=4,
                                   subtype='B',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_gapped_24px')


    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3710,
                                   gen=4,
                                   subtype='C',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_gapped_32px')


    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3720,
                                   gen=5,
                                   subtype='A',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='2_axle_1cc_filled_16px')


    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3730,
                                   gen=5,
                                   subtype='B',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_1cc_filled_24px')


    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3740,
                                   gen=5,
                                   subtype='C',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_1cc_filled_32px')

    # no gen 6A

    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3750,
                                   gen=6,
                                   subtype='B',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_1cc_filled_24px')


    consist = IntermodalCarConsist(roster_id='pony',
                                   base_numeric_id=3760,
                                   gen=6,
                                   subtype='C',
                                   sprites_complete=True)

    consist.add_unit(type=IntermodalCar,
                     chassis='4_axle_1cc_filled_32px')
