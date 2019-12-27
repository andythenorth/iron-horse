from train import PetrolTankCarConsist, FreightCar


def main():

    #--------------- pony ----------------------------------------------------------------------

    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4730,
                             gen=1,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4740,
                             gen=2,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4750,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4760,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4770,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4780,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4790,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4800,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4810,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4820,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4830,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4840,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4850,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = PetrolTankCarConsist(roster_id='pony',
                             base_numeric_id=4860,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
