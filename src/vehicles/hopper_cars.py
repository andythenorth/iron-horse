import global_constants
from train import HopperConsistShort, HopperConsistLong, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HopperConsistShort(title = '[Hopper Car]',
                                 roster = 'pony',
                                 base_numeric_id = 1070,
                                 vehicle_generation = 3,
                                 vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistLong(title = '[Hopper Car]',
                                 roster = 'pony',
                                 base_numeric_id = 2330,
                                 vehicle_generation = 3,
                                 vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1080,
                            vehicle_generation = 4,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistLong(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1090,
                            vehicle_generation = 4,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'llama',
                            base_numeric_id = 1100,
                            vehicle_generation = 2,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'llama',
                            base_numeric_id = 1110,
                            vehicle_generation = 3,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'llama',
                            base_numeric_id = 1120,
                            vehicle_generation = 2,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 45,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'llama',
                            base_numeric_id = 1130,
                            vehicle_generation = 3,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 65,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'antelope',
                            base_numeric_id = 1630,
                            vehicle_generation = 1,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 60,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'antelope',
                            base_numeric_id = 1660,
                            vehicle_generation = 2,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 1 NG hopper in Antelope, straight to gen 2
    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'antelope',
                            base_numeric_id = 1890,
                            vehicle_generation = 2,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 35,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


