from train import PassengerCarConsist, PaxMailCar


def main():
    #--------------- pony NG----------------------------------------------------------------------
    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=770,
                                  gen=1,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=PaxMailCar,
                     capacity=25,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')

    #--------------- pony ----------------------------------------------------------------------

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=740,
                                  gen=1,
                                  subtype='A')

    consist.add_unit(type=PaxMailCar,
                     capacity=25,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=750,
                                  gen=2,
                                  subtype='A')

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=760,
                                  gen=3,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=3110,
                                  gen=4,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=PaxMailCar,
                     capacity=50,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=3100,
                                  gen=5,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=PaxMailCar,
                     capacity=50,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=1580,
                                  gen=6,
                                  subtype='A',
                                  sprites_complete=True)

    consist.add_unit(type=PaxMailCar,
                     capacity=50,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    # no gen 6 for brit roster, max speed reached for engines
