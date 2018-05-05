from train import PassengerLuxuryCarConsist, PaxMailCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerLuxuryCarConsist(roster='pony',
                                        base_numeric_id=2250,
                                        gen=1,
                                        subtype='A')

    consist.add_unit(type=PaxMailCar,
                     capacity=25,
                     vehicle_length=8,
                     chassis='6_axle_solid_express_32px')


    consist = PassengerLuxuryCarConsist(roster='pony',
                                        base_numeric_id=2260,
                                        gen=2,
                                        subtype='A')

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=8,
                     chassis='6_axle_solid_express_32px')


    consist = PassengerLuxuryCarConsist(roster='pony',
                                        base_numeric_id=2270,
                                        gen=3,
                                        subtype='A')

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=8,
                     chassis='6_axle_solid_express_32px')


    consist = PassengerLuxuryCarConsist(roster='pony',
                                        base_numeric_id=3120,
                                        gen=4,
                                        subtype='A',
                                        sprites_complete=True)

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')


    consist = PassengerLuxuryCarConsist(roster='pony',
                                        base_numeric_id=3130,
                                        gen=5,
                                        subtype='A',
                                        sprites_complete=True)

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerLuxuryCarConsist(roster='pony',
                                        base_numeric_id=1860,
                                        gen=6,
                                        subtype='A')

    consist.add_unit(type=PaxMailCar,
                     capacity=40,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
