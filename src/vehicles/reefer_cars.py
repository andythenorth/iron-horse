import global_constants
from train import ReeferConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'pony',
                            base_numeric_id = 730,
                            wagon_generation = 1,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 reefer - straight to gen 3
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'pony',
                            base_numeric_id = 720,
                            wagon_generation = 3,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1390,
                            wagon_generation = 1,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1400,
                            wagon_generation = 3,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 50,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1410,
                            wagon_generation = 1,
                            vehicle_life = 40,
                            speedy = True,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1420,
                            wagon_generation = 3,
                            vehicle_life = 40,
                            speedy = True,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'antelope',
                            base_numeric_id = 1570,
                            wagon_generation = 1,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'antelope',
                            base_numeric_id = 1900,
                            wagon_generation = 1,
                            vehicle_life = 40,
                            speedy = True,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
