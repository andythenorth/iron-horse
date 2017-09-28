import global_constants
from train import PassengerLuxuryConsist, PassengerCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerLuxuryConsist(roster = 'pony',
                               base_numeric_id = 2250,
                               vehicle_generation = 1,
                               intro_date = 1860,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                           capacity = 25,
                           weight = 30,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    consist = PassengerLuxuryConsist(roster = 'pony',
                               base_numeric_id = 2260,
                               vehicle_generation = 2,
                               intro_date = 1900,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 55,
                            weight = 33,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    consist = PassengerLuxuryConsist(roster = 'pony',
                               base_numeric_id = 2270,
                               vehicle_generation = 3,
                               intro_date = 1960,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                           capacity = 75,
                           weight = 36,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
