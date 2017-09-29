import global_constants
from train import TankConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = TankConsist(roster='pony',
                          base_numeric_id=630,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='pony',
                          base_numeric_id=640,
                          gen=3,
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

    consist = TankConsist(roster='pony',
                          base_numeric_id=960,
                          gen=4,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='pony',
                          base_numeric_id=650,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=12,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- llama ----------------------------------------------------------------------
    consist = TankConsist(roster='llama',
                          base_numeric_id=660,
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

    consist = TankConsist(roster='llama',
                          base_numeric_id=670,
                          gen=2,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='llama',
                          base_numeric_id=680,
                          gen=3,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=75,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='llama',
                          base_numeric_id=690,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='llama',
                          base_numeric_id=1360,
                          gen=2,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------
    consist = TankConsist(roster='antelope',
                          base_numeric_id=1670,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=55,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='antelope',
                          base_numeric_id=1680,
                          gen=2,
                          subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=70,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = TankConsist(roster='antelope',
                          base_numeric_id=1910,
                          gen=1,
                          subtype='A',
                          track_type='NG')

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

    consist = TankConsist(roster='antelope',
                          base_numeric_id=1920,
                          gen=2,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=35,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])


# gen 3 at 1980 or so
