import global_constants
from train import CoveredHopperConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1270,
                                   gen=1,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1230,
                                   gen=2,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1240,
                                   gen=3,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=60,
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
    consist = CoveredHopperConsist(roster='llama',
                                   base_numeric_id=1250,
                                   gen=2,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=7)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = CoveredHopperConsist(roster='llama',
                                   base_numeric_id=1260,
                                   gen=3,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=65,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
