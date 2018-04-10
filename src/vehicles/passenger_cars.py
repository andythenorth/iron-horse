from train import PassengerCarConsist, TrainCar


def main():
    #--------------- pony NG----------------------------------------------------------------------
    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=770,
                                  gen=1,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=TrainCar,
                     capacity=25,
                     vehicle_length=6)

        #--------------- pony ----------------------------------------------------------------------

    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=740,
                                  gen=1,
                                  subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=25,
                     vehicle_length=6)


    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=750,
                                  gen=2,
                                  subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=40,
                     vehicle_length=6)


    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=760,
                                  gen=3,
                                  subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=40,
                     vehicle_length=6)


    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=3110,
                                  gen=4,
                                  subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=50,
                     vehicle_length=6)


    consist = PassengerCarConsist(roster='pony',
                                  base_numeric_id=3100,
                                  gen=5,
                                  subtype='A')

    consist.add_unit(type=TrainCar,
                     capacity=50,
                     vehicle_length=6)

    # no gen 6 for brit roster, max speed reached for engines

