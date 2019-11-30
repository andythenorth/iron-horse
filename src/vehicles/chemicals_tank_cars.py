from train import ChemicalsTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=2860,
                             gen=2,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3360,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='3_axle_filled_16px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3370,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3460,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3380,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3390,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3400,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3410,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3420,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3430,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    # gen 6A not included - could add?

    """
    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=180,
                             gen=6,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')
    """

    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3440,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = ChemicalsTankCarConsist(roster_id='pony',
                             base_numeric_id=3450,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')

