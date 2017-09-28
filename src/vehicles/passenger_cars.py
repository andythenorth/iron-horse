import global_constants
from train import PassengerConsist, PassengerCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerConsist(roster='pony',
                               base_numeric_id=740,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='pony',
                               base_numeric_id=750,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=55,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='pony',
                               base_numeric_id=760,
                               gen=3,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=75,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = PassengerConsist(roster='pony',
                               base_numeric_id=980,
                               gen=6,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=25,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='pony',
                               base_numeric_id=770,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=PassengerCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    #--------------- llama ----------------------------------------------------------------------
    consist = PassengerConsist(roster='llama',
                               base_numeric_id=780,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='llama',
                               base_numeric_id=790,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=50,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='llama',
                               base_numeric_id=800,
                               gen=3,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=60,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='llama',
                               base_numeric_id=810,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=PassengerCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='llama',
                               base_numeric_id=1350,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=PassengerCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='llama',
                               base_numeric_id=1370,
                               gen=3,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=PassengerCar,
                     capacity=50,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    #--------------- antelope ----------------------------------------------------------------------
    consist = PassengerConsist(roster='antelope',
                               base_numeric_id=1580,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=55,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='antelope',
                               base_numeric_id=1560,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=PassengerCar,
                     capacity=80,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='antelope',
                               base_numeric_id=2130,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=PassengerCar,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = PassengerConsist(roster='antelope',
                               base_numeric_id=1940,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=PassengerCar,
                     capacity=30,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)
