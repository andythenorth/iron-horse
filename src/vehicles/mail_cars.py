import global_constants
from train import MailConsist, MailCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = MailConsist(roster='pony',
                          base_numeric_id=2280,
                          gen=1,
                          subtype='A',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=15,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='pony',
                          base_numeric_id=2220,
                          gen=1,
                          subtype='B',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=15,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(
        roster='pony',
        base_numeric_id=2290,
        gen=2,
        subtype='A',
        speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=25,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='pony',
                          base_numeric_id=920,
                          gen=2,
                          subtype='B',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='pony',
                          base_numeric_id=2300,
                          gen=3,
                          subtype='A',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='pony',
                          base_numeric_id=940,
                          gen=3,
                          subtype='B',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='pony',
                          base_numeric_id=950,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=MailCar,
                     capacity=24,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    """
    #--------------- llama ----------------------------------------------------------------------
    consist = MailConsist(roster = 'llama',
                          base_numeric_id = 960,
                          gen = 1,
                                    subtype='A',
                          speedy = True)

    consist.add_unit(type = MailCar,
                            capacity = 30,
                            vehicle_length = 7)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = MailConsist(roster = 'llama',
                          base_numeric_id = 970,
                          gen = 2,
                                    subtype='A',
                          speedy = True)

    consist.add_unit(type = MailCar,
                            capacity = 45,
                            vehicle_length = 7)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = MailConsist(roster = 'llama',
                          base_numeric_id = 980,
                          gen = 3,
                                    subtype='A',
                          speedy = True)

    consist.add_unit(type = MailCar,
                            capacity = 60,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = MailConsist(roster = 'llama',
                          base_numeric_id = 990,
                          gen = 1,
                                    subtype='A',
                          speedy = True,
                          track_type = 'NG')

    consist.add_unit(type = MailCar,
                            capacity = 30,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = MailConsist(roster = 'llama',
                          base_numeric_id = 1380,
                          gen = 2,
                                    subtype='A',
                          speedy = True,
                          track_type = 'NG')

    consist.add_unit(type = MailCar,
                            capacity = 40,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = MailConsist(roster = 'llama',
                          base_numeric_id = 1450,
                          gen = 3,
                                    subtype='A',
                          speedy = True,
                          track_type = 'NG')

    consist.add_unit(type = MailCar,
                            capacity = 50,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)

    """
    #--------------- antelope ----------------------------------------------------------------------
    consist = MailConsist(roster='antelope',
                          base_numeric_id=1730,
                          gen=1,
                          subtype='A',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='antelope',
                          base_numeric_id=2120,
                          gen=1,
                          subtype='A',
                          track_type='NG',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailConsist(roster='antelope',
                          base_numeric_id=1950,
                          gen=2,
                          subtype='A',
                          track_type='NG',
                          speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=30,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)
