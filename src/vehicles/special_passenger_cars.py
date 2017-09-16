import global_constants
from train import SpecialPassengerConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SpecialPassengerConsist(title = '[Special Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 2250,
                               wagon_generation = 1,
                               intro_date = 1860,
                               vehicle_life = 40,
                               speedy = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_pax = 25,
                           weight = 30,
                           vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = SpecialPassengerConsist(title = '[Special Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 2260,
                               wagon_generation = 2,
                               intro_date = 1900,
                               vehicle_life = 40,
                               speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 55,
                            weight = 33,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = SpecialPassengerConsist(title = '[Special Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 2270,
                               wagon_generation = 3,
                               intro_date = 1960,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_pax = 75,
                           weight = 36,
                           vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
