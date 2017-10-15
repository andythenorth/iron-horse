import global_constants
from train import OpenConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = OpenConsist(roster='pony',
                          base_numeric_id=850,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=FreightCar,
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
    #--------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = OpenConsist(roster='pony',
                          base_numeric_id=820,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
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

    # no new type A for gen 2, gen 1 type A continues

    consist = OpenConsist(roster='pony',
                          base_numeric_id=830,
                          gen=2,
                          subtype='B')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=840,
                          gen=3,
                          subtype='A')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=2440,
                          gen=3,
                          subtype='B')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=2450,
                          gen=4,
                          subtype='B')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=2460,
                          gen=5,
                          subtype='A')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=2470,
                          gen=5,
                          subtype='B')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=3260,
                          gen=6,
                          subtype='A')

    consist.add_unit(type=FreightCar,
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
                          base_numeric_id=3250,
                          gen=6,
                          subtype='B')

    consist.add_unit(type=FreightCar,
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
    #--------------- llama ----------------------------------------------------------------------
    consist = OpenConsist(roster='llama',
                          base_numeric_id=860,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=FreightCar,
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
