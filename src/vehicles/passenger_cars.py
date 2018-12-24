from train import PassengerCarConsist, PaxCar


def main():
    #--------------- pony NG----------------------------------------------------------------------
    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=770,
                                  gen=1,
                                  subtype='U',
                                  base_track_type='NG',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=22,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=800,
                                  gen=3,
                                  subtype='U',
                                  base_track_type='NG',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=30,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=860,
                                  gen=4,
                                  subtype='U',
                                  base_track_type='NG',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=30,
                     vehicle_length=4,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=740,
                                  gen=1,
                                  subtype='U',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=30,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=750,
                                  gen=2,
                                  subtype='U',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=30,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=760,
                                  gen=3,
                                  subtype='U',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=36,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=3110,
                                  gen=4,
                                  subtype='U',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=40,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=3100,
                                  gen=5,
                                  subtype='U',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=40,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=1580,
                                  gen=6,
                                  subtype='U',
                                  sprites_complete=True)

    consist.add_unit(type=PaxCar,
                     capacity=40,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')

    # no gen 6 for brit roster, max speed reached for engines
