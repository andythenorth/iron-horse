import global_constants
from train import ReeferConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = ReeferConsist(roster='pony',
                            base_numeric_id=730,
                            vehicle_generation=1,
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    # no gen 2 reefer - straight to gen 3
    consist = ReeferConsist(roster='pony',
                            base_numeric_id=720,
                            vehicle_generation=3,
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    #--------------- llama ----------------------------------------------------------------------
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1390,
                            vehicle_generation=1,
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1400,
                            vehicle_generation=3,
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=50,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1410,
                            vehicle_generation=1,
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1420,
                            vehicle_generation=3,
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    #--------------- antelope ----------------------------------------------------------------------
    consist = ReeferConsist(roster='antelope',
                            base_numeric_id=1570,
                            vehicle_generation=1,
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    consist = ReeferConsist(roster='antelope',
                            base_numeric_id=1900,
                            vehicle_generation=1,
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])
