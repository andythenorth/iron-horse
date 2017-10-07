import global_constants
from train import FruitVegConsist, FreightCar


def main():
    #--------------- pony --------------------------------------------------------------------------
    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2640,
                              gen=2,
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

    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2630,
                              gen=3,
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

    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2620,
                              gen=3,
                              subtype='B')

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

    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2600,
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

    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2610,
                              gen=4,
                              subtype='B')

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

    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2650,
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

    consist = FruitVegConsist(roster='pony',
                              base_numeric_id=2660,
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

    #--------------- antelope ----------------------------------------------------------------------
    consist = FruitVegConsist(roster='antelope',
                              base_numeric_id=2140,
                              gen=1,
                              subtype='A',
                              track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FruitVegConsist(roster='antelope',
                              base_numeric_id=2170,
                              gen=2,
                              subtype='A',
                              track_type='NG')

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

    consist = FruitVegConsist(roster='antelope',
                              base_numeric_id=2180,
                              gen=3,
                              subtype='A',
                              track_type='NG')

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
