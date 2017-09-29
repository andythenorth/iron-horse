import global_constants
from train import OpenConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = OpenConsist(roster='pony',
                          base_numeric_id=820,
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

    consist = OpenConsist(roster='pony',
                          base_numeric_id=830,
                          gen=2,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=35,
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

    consist = OpenConsist(roster='pony',
                          base_numeric_id=840,
                          gen=3,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=55,
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

    consist = OpenConsist(roster='pony',
                          base_numeric_id=1450,
                          gen=4,
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

    consist = OpenConsist(roster='pony',
                          base_numeric_id=850,
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
    consist = OpenConsist(roster='llama',
                          base_numeric_id=860,
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

    consist = OpenConsist(roster='llama',
                          base_numeric_id=1330,
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

    consist = OpenConsist(roster='llama',
                          base_numeric_id=870,
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

    consist = OpenConsist(roster='llama',
                          base_numeric_id=1320,
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
    consist = OpenConsist(roster='antelope',
                          base_numeric_id=1760,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=55,
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

    consist = OpenConsist(roster='antelope',
                          base_numeric_id=1770,
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

    consist = OpenConsist(roster='antelope',
                          base_numeric_id=2090,
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

    consist = OpenConsist(roster='antelope',
                          base_numeric_id=1830,
                          gen=2,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=30,
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

    consist = OpenConsist(roster='antelope',
                          base_numeric_id=1820,
                          gen=3,
                          subtype='A',
                          track_type='NG')

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
