import global_constants
from train import EdiblesTankConsist, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'pony',
                                 base_numeric_id = 1190,
                                 wagon_generation = 1,
                                 replacement_id = '-none',
                                 intro_date = 1905,
                                 vehicle_life = 40,
                                 speedy = True,
                                 use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'edibles_tank_car_pony_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'pony',
                                 base_numeric_id = 1200,
                                 wagon_generation = 3,
                                 replacement_id = '-none',
                                 intro_date = 1988,
                                 vehicle_life = 40,
                                 speedy = True,
                                 use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'edibles_tank_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- llama ----------------------------------------------------------------------
    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'llama',
                                 base_numeric_id = 1210,
                                 wagon_generation = 1,
                                 replacement_id = '-none',
                                 intro_date = 1905,
                                 vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 6))

    options = {'template': 'edibles_tank_car_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'llama',
                                 base_numeric_id = 1220,
                                 wagon_generation = 3,
                                 replacement_id = '-none',
                                 intro_date = 1988,
                                 vehicle_life = 40,
                                 speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'edibles_tank_car_llama_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- antelope ----------------------------------------------------------------------
    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                        roster = 'antelope',
                        base_numeric_id = 1690,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1950,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            weight = 15,
                            vehicle_length = 6))

    options = {'template': 'edibles_tank_car_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'antelope',
                                 base_numeric_id = 1700,
                                 wagon_generation = 2,
                                 replacement_id = '-none',
                                 intro_date = 1981,
                                 vehicle_life = 40,
                                 speedy = True,
                                 use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'edibles_tank_car_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


