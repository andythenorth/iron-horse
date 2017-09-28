import global_constants
from train import MailConsist, MailCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = MailConsist(title = '[Mail Car]',
                               roster = 'pony',
                               base_numeric_id = 2220,
                               vehicle_generation = 1,
                               speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 15,
                             vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                              roster = 'pony',
                              base_numeric_id = 920,
                              vehicle_generation = 2,
                                              speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 25,
                             vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                              roster = 'pony',
                              base_numeric_id = 940,
                              vehicle_generation = 3,
                                              speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 40,
                             vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                              roster = 'pony',
                              base_numeric_id = 950,
                              vehicle_generation = 1,
                                              track_type = 'NG')

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 24,
                             vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    """
    #--------------- llama ----------------------------------------------------------------------
    consist = MailConsist(title = '[Mail Car]',
                          roster = 'llama',
                          base_numeric_id = 960,
                          vehicle_generation = 1,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            vehicle_length = 7))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'llama',
                          base_numeric_id = 970,
                          vehicle_generation = 2,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 45,
                            vehicle_length = 7))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'llama',
                          base_numeric_id = 980,
                          vehicle_generation = 3,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 60,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'llama',
                          base_numeric_id = 990,
                          vehicle_generation = 1,
                          speedy = True,
                          track_type = 'NG')

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'llama',
                          base_numeric_id = 1380,
                          vehicle_generation = 2,
                          speedy = True,
                          track_type = 'NG')

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 40,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'llama',
                          base_numeric_id = 1450,
                          vehicle_generation = 3,
                          speedy = True,
                          track_type = 'NG')

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 50,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)

    """
    #--------------- antelope ----------------------------------------------------------------------
    consist = MailConsist(title = '[Mail Car]',
                          roster = 'antelope',
                          base_numeric_id = 1730,
                          vehicle_generation = 1,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 40,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'antelope',
                          base_numeric_id = 2120,
                          vehicle_generation = 1,
                          track_type = 'NG',
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 20,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsist(title = '[Mail Car]',
                          roster = 'antelope',
                          base_numeric_id = 1950,
                          vehicle_generation = 2,
                          track_type = 'NG',
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)
