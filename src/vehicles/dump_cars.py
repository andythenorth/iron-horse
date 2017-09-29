import global_constants
from train import DumpConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpConsist(roster='pony',
                          base_numeric_id=1340,
                          gen=3,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = DumpConsist(roster='pony',
                          base_numeric_id=1810,
                          gen=4,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
