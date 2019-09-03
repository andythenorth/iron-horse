from train import SiloCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3680,
                             gen=4,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3690,
                             gen=4,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3700,
                             gen=4,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3620,
                             gen=5,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3630,
                             gen=5,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3640,
                             gen=5,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3650,
                             gen=6,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3660,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=3670,
                             gen=6,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
