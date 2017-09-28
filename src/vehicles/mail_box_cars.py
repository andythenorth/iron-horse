import global_constants
from train import MailBoxConsist, MailCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = MailBoxConsist(title = '[Mail Box Car]',
                               roster = 'pony',
                               base_numeric_id = 2280,
                               wagon_generation = 1,
                               intro_date = 1860,
                               vehicle_life = 40,
                               speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 15,
                             vehicle_length = 4))

    consist.add_model_variant(intro_date = 0,
                              end_date=global_constants.max_game_date)


    consist = MailBoxConsist(title = '[Mail Box Car]',
                              roster = 'pony',
                              base_numeric_id = 2290,
                              wagon_generation = 2,
                              intro_date = 1900,
                              vehicle_life = 40,
                              speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 25,
                             vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailBoxConsist(title = '[Mail Box Car]',
                              roster = 'pony',
                              base_numeric_id = 2300,
                              wagon_generation = 3,
                              intro_date = 1960,
                              vehicle_life = 40,
                              speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 40,
                             vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
