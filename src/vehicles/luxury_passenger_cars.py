import global_constants
from train import PassengerLuxuryConsist, PassengerCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=2250,
                                     gen=1,
                                     subtype='A',
                                     intro_date=1860)

    consist.add_unit(type=PassengerCar,
                     capacity=25,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=2260,
                                     gen=2,
                                     subtype='A',
                                     intro_date=1900)

    consist.add_unit(type=PassengerCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=2270,
                                     gen=3,
                                     subtype='A',
                                     intro_date=1930)

    consist.add_unit(type=PassengerCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
