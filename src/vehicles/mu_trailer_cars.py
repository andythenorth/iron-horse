from train import PassengerMUTrailerCarConsist, PaxCar


def main():

    #--------------- pony ----------------------------------------------------------------------

    consist = PassengerMUTrailerCarConsist(roster='pony',
                                  base_numeric_id=700,
                                  gen=4,
                                  subtype='U',
                                  sprites_complete=False)

    consist.add_unit(type=PaxCar,
                     capacity=40,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')

    """
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

    """
