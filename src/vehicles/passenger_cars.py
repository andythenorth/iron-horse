import global_constants
from train import PassengerConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 740,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40,
                               speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 40,
                            weight = 30,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 750,
                               wagon_generation = 2,
                                                intro_date = 1925,
                               vehicle_life = 40,
                               speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 55,
                            weight = 33,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 760,
                               wagon_generation = 3,
                                                intro_date = 1985,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 75,
                            weight = 36,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 770,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 25,
                            weight = 12,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'llama',
                               base_numeric_id = 780,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 40,
                            weight = 30,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'llama',
                               base_numeric_id = 790,
                               wagon_generation = 2,
                                                intro_date = 1920,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 50,
                            weight = 30,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'llama',
                               base_numeric_id = 800,
                               wagon_generation = 3,
                                                intro_date = 1980,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 60,
                            weight = 30,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'llama',
                               base_numeric_id = 810,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               speedy = True,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 30,
                            weight = 12,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'llama',
                               base_numeric_id = 1350,
                               wagon_generation = 2,
                                                intro_date = 1920,
                               speedy = True,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 40,
                            weight = 16,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)



    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'llama',
                               base_numeric_id = 1370,
                               wagon_generation = 3,
                                                intro_date = 1980,
                               speedy = True,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 50,
                            weight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'antelope',
                               base_numeric_id = 1580,
                               wagon_generation = 1,
                               intro_date = 1950,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 55,
                            weight = 32,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'antelope',
                               base_numeric_id = 1560,
                               wagon_generation = 2,
                               intro_date = 1985,
                               speedy = True,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 80,
                            weight = 40,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'antelope',
                               base_numeric_id = 2130,
                               wagon_generation = 1,
                               intro_date = 1860,
                               speedy = True,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 20,
                            weight = 16,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = PassengerConsist(title = '[Passenger Car]',
                               roster = 'antelope',
                               base_numeric_id = 1940,
                               wagon_generation = 2,
                               intro_date = 1910,
                               speedy = True,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 30,
                            weight = 24,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)
