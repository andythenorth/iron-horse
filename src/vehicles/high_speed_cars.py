import global_constants
from train import MailHighSpeedConsist, HighSpeedPassengerConsist, Wagon

# for consistency, should be split to high_speed_mail_cars and high_speed_passenger_cars eh?

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HighSpeedPassengerConsist(title = '[High Speed Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 980,
                               vehicle_generation = 5)

    consist.add_unit(Wagon(consist = consist,
                           capacity_pax = 25,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailHighSpeedConsist(title = '[High Speed Mail Car]',
                               roster = 'pony',
                               base_numeric_id = 970,
                               vehicle_generation = 5)

    consist.add_unit(Wagon(consist = consist,
                            capacity_mail = 55,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

    #--------------- llama ----------------------------------------------------------------------


    #--------------- antelope ----------------------------------------------------------------------
