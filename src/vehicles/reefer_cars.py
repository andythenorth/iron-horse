import global_constants
from train import ReeferConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = ReeferConsist(roster='pony',
                            base_numeric_id=730,
                            gen=1,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 reefer - straight to gen 3
    consist = ReeferConsist(roster='pony',
                            base_numeric_id=720,
                            gen=3,
                            subtype='A',
                            speedy=True)

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
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1390,
                            gen=1,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1400,
                            gen=3,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1410,
                            gen=1,
                            subtype='A',
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1420,
                            gen=3,
                            subtype='A',
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------
    consist = ReeferConsist(roster='antelope',
                            base_numeric_id=1570,
                            gen=1,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='antelope',
                            base_numeric_id=1900,
                            gen=1,
                            subtype='A',
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])
