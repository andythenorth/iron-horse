import global_constants
from train import EdiblesTankConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = EdiblesTankConsist(roster='pony',
                                 base_numeric_id=1190,
                                 gen=1,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(roster='pony',
                                 base_numeric_id=1200,
                                 gen=3,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- llama ----------------------------------------------------------------------
    consist = EdiblesTankConsist(roster='llama',
                                 base_numeric_id=1210,
                                 gen=1,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(roster='llama',
                                 base_numeric_id=1220,
                                 gen=3,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=55,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------
    consist = EdiblesTankConsist(roster='antelope',
                                 base_numeric_id=1690,
                                 gen=1,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = EdiblesTankConsist(roster='antelope',
                                 base_numeric_id=1700,
                                 gen=2,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=60,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])
