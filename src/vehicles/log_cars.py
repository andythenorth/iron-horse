import global_constants
from train import LogConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = LogConsist(roster='pony',
                         base_numeric_id=1710,
                         gen=4,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = LogConsist(roster='pony',
                         base_numeric_id=930,
                         gen=5,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])  # --------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------
