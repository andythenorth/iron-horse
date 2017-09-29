import global_constants
from train import HopperConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HopperConsist(roster='pony',
                            base_numeric_id=1070,
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

    consist = HopperConsist(roster='pony',
                            base_numeric_id=2330,
                            gen=3,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = HopperConsist(roster='pony',
                            base_numeric_id=1080,
                            gen=4,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = HopperConsist(roster='pony',
                            base_numeric_id=1090,
                            gen=4,
                            subtype='B')

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
    consist = HopperConsist(roster='llama',
                            base_numeric_id=1100,
                            gen=2,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=55,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = HopperConsist(roster='llama',
                            base_numeric_id=1110,
                            gen=3,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=75,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = HopperConsist(roster='llama',
                            base_numeric_id=1120,
                            gen=2,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = HopperConsist(roster='llama',
                            base_numeric_id=1130,
                            gen=3,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=65,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------
    consist = HopperConsist(roster='antelope',
                            base_numeric_id=1630,
                            gen=1,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=60,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = HopperConsist(roster='antelope',
                            base_numeric_id=1660,
                            gen=2,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=75,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 1 NG hopper in Antelope, straight to gen 2
    consist = HopperConsist(roster='antelope',
                            base_numeric_id=1890,
                            gen=2,
                            subtype='A',
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=35,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])
