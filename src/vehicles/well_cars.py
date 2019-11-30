from train import WellCarConsist, WellCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=710,
                             gen=2,
                             subtype='A')

    consist.add_unit(type=WellCar,
                     chassis='2_axle_filled_16px')

    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=700,
                             gen=3,
                             subtype='A')

    consist.add_unit(type=WellCar,
                     chassis='2_axle_filled_16px')

    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=2850,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=WellCar,
                     chassis='4_axle_filled_24px')

    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=2860,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=WellCar,
                     chassis='4_axle_filled_24px')

    """
    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=2870,
                             gen=4,
                             subtype='C')

    consist.add_unit(type=WellCar,
                     vehicle_length=8)
    """

    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=2880,
                             gen=5,
                             subtype='A')

    consist.add_unit(type=WellCar,
                     chassis='2_axle_filled_16px')

    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=2890,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=WellCar,
                     chassis='4_axle_filled_greebled_24px')

    """
    consist = WellCarConsist(roster_id='pony',
                             base_numeric_id=2690,
                             gen=5,
                             subtype='C')

    consist.add_unit(type=WellCar,
                     vehicle_length=8)
    """
    # no gen 6 supplies cars, cap to gen 5 in Pony

    #--------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------
