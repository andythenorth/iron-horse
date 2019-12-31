from train import SulphurTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4870,
                             gen=2,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4880,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4890,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4910,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4920,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4930,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')

    # no gen 5A or 6A

    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4950,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4960,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4970,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = SulphurTankCarConsist(roster_id='pony',
                             base_numeric_id=4980,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
