import global_constants
from train import SiloConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SiloConsist(roster='pony',
                          base_numeric_id=2950,
                          gen=4,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = SiloConsist(roster='pony',
                          base_numeric_id=2980,
                          gen=5,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = SiloConsist(roster='pony',
                          base_numeric_id=2960,
                          gen=5,
                          subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
