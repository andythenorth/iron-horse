from train import DumpCarScrapMetalConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4180,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4190,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')


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


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4220,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4230,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4240,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4250,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4260,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarScrapMetalConsist(roster_id='pony',
                             base_numeric_id=4270,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
