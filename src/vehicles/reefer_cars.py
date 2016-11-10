import global_constants
from train import ReeferConsist, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'pony',
                            base_numeric_id = 730,
                            wagon_generation = 1,
                                          intro_date = 1915,
                            vehicle_life = 40,
                            speedy = True,
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 14,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_pony_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    # no gen 2 reefer - straight to gen 3
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'pony',
                            base_numeric_id = 720,
                            wagon_generation = 3,
                                          intro_date = 1964,
                            vehicle_life = 40,
                            speedy = True,
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'reefer_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- llama ----------------------------------------------------------------------
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1390,
                            wagon_generation = 1,
                                          intro_date = 1905,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 14,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1400,
                            wagon_generation = 3,
                                          intro_date = 1980,
                            vehicle_life = 40,
                            speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 50,
                            weight = 25,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_llama_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1410,
                            wagon_generation = 1,
                                          intro_date = 1905,
                            vehicle_life = 40,
                            speedy = True,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 14,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_ng_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'llama',
                            base_numeric_id = 1420,
                            wagon_generation = 3,
                                          intro_date = 1980,
                            vehicle_life = 40,
                            speedy = True,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 20,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_ng_llama_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- antelope ----------------------------------------------------------------------
    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'antelope',
                            base_numeric_id = 1570,
                            wagon_generation = 1,
                                          intro_date = 1950,
                            vehicle_life = 40,
                            speedy = True,
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'reefer_car_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = ReeferConsist(title = '[Reefer Car]',
                            roster = 'antelope',
                            base_numeric_id = 1900,
                            wagon_generation = 1,
                                          intro_date = 1905,
                            vehicle_life = 40,
                            speedy = True,
                            track_type = 'NG',
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 22,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_ng_antelope_gen_1_template.png'}


    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
