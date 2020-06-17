from train import BulkheadFlatCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    """
    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=1170,
                             gen=1,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=1130,
                             gen=3,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=1370,
                             gen=4,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')
    """
    #--------------- pony ----------------------------------------------------------------------

    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4700,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4710,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4720,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4730,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4740,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4750,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4760,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4770,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4780,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_24px')


    consist = BulkheadFlatCarConsist(roster_id='pony',
                             base_numeric_id=4790,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
