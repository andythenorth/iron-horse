from train import DumpCarScrapMetalConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    # gen 2 start eh?
    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=5090,
                                       gen=2,
                                       subtype='U',
                                       base_track_type='NG',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=5100,
                                       gen=3,
                                       subtype='U',
                                       base_track_type='NG',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=5110,
                                       gen=4,
                                       subtype='U',
                                       base_track_type='NG',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4180,
                                       gen=3,
                                       subtype='A',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4190,
                                       gen=3,
                                       subtype='B',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4200,
                                       gen=4,
                                       subtype='A',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4210,
                                       gen=4,
                                       subtype='B',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')

    # no gen 5A or 6A

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4230,
                                       gen=5,
                                       subtype='B',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_24px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4240,
                                       gen=5,
                                       subtype='C',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_greebled_32px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4260,
                                       gen=6,
                                       subtype='B',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_24px')

    consist = DumpCarScrapMetalConsist(roster_id='pony',
                                       base_numeric_id=4270,
                                       gen=6,
                                       subtype='C',
                                       sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_greebled_32px')
