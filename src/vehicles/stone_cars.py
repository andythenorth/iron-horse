from train import DumpCarStoneConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4280,
                             gen=3,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4290,
                             gen=3,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4300,
                             gen=4,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4310,
                             gen=4,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4320,
                             gen=5,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4330,
                             gen=5,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_24px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4340,
                             gen=5,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_greebled_32px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4350,
                             gen=6,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4360,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_24px')


    consist = DumpCarStoneConsist(roster_id='pony',
                             base_numeric_id=4370,
                             gen=6,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_greebled_32px')
