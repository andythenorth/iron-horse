import global_constants
from train import MailBoxConsist, MailCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = MailBoxConsist(roster='pony',
                             base_numeric_id=2280,
                             vehicle_generation=1,
                             speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=15,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailBoxConsist(title='[Mail Box Car]',
                             roster='pony',
                             base_numeric_id=2290,
                             vehicle_generation=2,
                             speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=25,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    consist = MailBoxConsist(title='[Mail Box Car]',
                             roster='pony',
                             base_numeric_id=2300,
                             vehicle_generation=3,
                             speedy=True)

    consist.add_unit(type=MailCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
