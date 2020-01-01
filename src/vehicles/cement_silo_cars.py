from train import SiloCarCementConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=1230,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=1240,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=1260,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=1270,
                             gen=5,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_greebled_16px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=1340,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_24px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=1940,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=2060,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=2070,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_24px')


    consist = SiloCarCementConsist(roster_id='pony',
                             base_numeric_id=2700,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')
