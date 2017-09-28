import global_constants
from train import HopperConsistShort, HopperConsistLong, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HopperConsistShort(roster = 'pony',
                                 base_numeric_id = 1070,
                                 vehicle_generation = 3)

    consist.add_unit(type = FreightCar,
                           capacity = 20,
                           vehicle_length = 4)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistLong(roster = 'pony',
                                 base_numeric_id = 2330,
                                 vehicle_generation = 3)

    consist.add_unit(type = FreightCar,
                           capacity = 30,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(roster = 'pony',
                            base_numeric_id = 1080,
                            vehicle_generation = 4)

    consist.add_unit(type = FreightCar,
                           capacity = 30,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistLong(roster = 'pony',
                            base_numeric_id = 1090,
                            vehicle_generation = 4)

    consist.add_unit(type = FreightCar,
                           capacity = 40,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = HopperConsistShort(roster = 'llama',
                            base_numeric_id = 1100,
                            vehicle_generation = 2)

    consist.add_unit(type = FreightCar,
                           capacity = 55,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(roster = 'llama',
                            base_numeric_id = 1110,
                            vehicle_generation = 3)

    consist.add_unit(type = FreightCar,
                           capacity = 75,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(roster = 'llama',
                            base_numeric_id = 1120,
                            vehicle_generation = 2,
                            track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 45,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(roster = 'llama',
                            base_numeric_id = 1130,
                            vehicle_generation = 3,
                            track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 65,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = HopperConsistShort(roster = 'antelope',
                            base_numeric_id = 1630,
                            vehicle_generation = 1)

    consist.add_unit(type = FreightCar,
                           capacity = 60,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(roster = 'antelope',
                            base_numeric_id = 1660,
                            vehicle_generation = 2)

    consist.add_unit(type = FreightCar,
                           capacity = 75,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 1 NG hopper in Antelope, straight to gen 2
    consist = HopperConsistShort(roster = 'antelope',
                            base_numeric_id = 1890,
                            vehicle_generation = 2,
                            track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 35,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


