from train import TankCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = TankCarConsist(roster='pony',
                             base_numeric_id=650,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    #--------------- pony ----------------------------------------------------------------------
    consist = TankCarConsist(roster='pony',
                             base_numeric_id=1200,
                             gen=2,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=3180,
                             gen=2,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=630,
                             gen=3,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2430,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2900,
                             gen=3,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_gapped_32px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=640,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=960,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=1250,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2410,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2420,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2930,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2920,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2970,
                             gen=6,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = TankCarConsist(roster='pony',
                             base_numeric_id=2790,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')
