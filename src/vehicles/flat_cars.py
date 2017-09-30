import global_constants
from train import FlatConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = FlatConsist(roster='pony',
                          base_numeric_id=1140,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     cargo_length=3,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=1150,
                          gen=2,
                          subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=1160,
                          gen=3,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=2550,
                          gen=3,
                          subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=2540,
                          gen=4,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=2530,
                          gen=4,
                          subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=2520,
                          gen=5,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=2510,
                          gen=5,
                          subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='pony',
                          base_numeric_id=1170,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=12,
                     cargo_length=3,
                     vehicle_length=3)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- llama ----------------------------------------------------------------------
    consist = FlatConsist(roster='llama',
                          base_numeric_id=1180,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='llama',
                          base_numeric_id=1510,
                          gen=2,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='llama',
                          base_numeric_id=520,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='llama',
                          base_numeric_id=1500,
                          gen=2,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=35,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------
    consist = FlatConsist(roster='antelope',
                          base_numeric_id=1640,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=55,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='antelope',
                          base_numeric_id=1650,
                          gen=2,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=70,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='antelope',
                          base_numeric_id=2110,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FlatConsist(roster='antelope',
                          base_numeric_id=1930,
                          gen=2,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
