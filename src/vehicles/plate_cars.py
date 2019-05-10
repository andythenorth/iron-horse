from train import PlateCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1480,
                             gen=1,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    # no gen 2A, gen 1A continues in pony

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1490,
                             gen=2,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='4_axle_gapped_24px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1500,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1540,
                             gen=3,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='4_axle_gapped_24px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1590,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_gapped_32px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1550,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     chassis='2_axle_filled_16px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1470,
                             gen=4,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1840,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_gapped_32px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1800,
                             gen=5,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1870,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_filled_32px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1960,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     chassis='2_axle_filled_24px')

    consist = PlateCarConsist(roster='pony',
                             base_numeric_id=1970,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     cargo_length=8,
                     chassis='4_axle_1cc_filled_32px')

