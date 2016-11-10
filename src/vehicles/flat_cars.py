import global_constants
from train import FlatConsist, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1140,
                           wagon_generation = 1,
                           replacement_id = '-none',
                           intro_date = 1860,
                           vehicle_life = 40,
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           weight = 6,
                           vehicle_length = 5))

    options = {'template': 'flat_car_pony_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1150,
                           wagon_generation = 2,
                           replacement_id = '-none',
                           intro_date = 1950,
                           vehicle_life = 40,
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 35,
                           weight = 12,
                           vehicle_length = 8))

    options = {'template': 'flat_car_pony_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1160,
                           wagon_generation = 3,
                           replacement_id = '-none',
                           intro_date = 1990,
                           vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           weight = 25,
                           vehicle_length = 10))

    options = {'template': 'flat_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1170,
                           wagon_generation = 1,
                           replacement_id = '-none',
                           intro_date = 1860,
                           vehicle_life = 40,
                           track_type = 'NG',
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 12,
                           weight = 3,
                           vehicle_length = 3))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)


    #--------------- llama ----------------------------------------------------------------------
    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 1180,
                           wagon_generation = 1,
                           replacement_id = '-none',
                           intro_date = 1860,
                           vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 25,
                           weight = 6,
                           vehicle_length = 5))

    options = {'template': 'flat_car_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 1510,
                           wagon_generation = 2,
                           replacement_id = '-none',
                           intro_date = 1920,
                           vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 45,
                           weight = 6,
                           vehicle_length = 5))

    options = {'template': 'flat_car_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 520,
                           wagon_generation = 1,
                           replacement_id = '-none',
                           intro_date = 1860,
                           vehicle_life = 40,
                           track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           weight = 6,
                           vehicle_length = 5))

    options = {'template': 'flat_car_ng_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 1500,
                           wagon_generation = 2,
                           replacement_id = '-none',
                           intro_date = 1920,
                           vehicle_life = 40,
                           track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 35,
                           weight = 6,
                           vehicle_length = 5))

    options = {'template': 'flat_car_ng_llama_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- antelope ----------------------------------------------------------------------
    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 1640,
                           wagon_generation = 1,
                           replacement_id = '-none',
                           intro_date = 1950,
                           vehicle_life = 40,
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           weight = 15,
                           vehicle_length = 8))

    options = {'template': 'flat_car_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 1650,
                           wagon_generation = 2,
                           replacement_id = '-none',
                           intro_date = 1978,
                           vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 70,
                           weight = 22,
                           vehicle_length = 10))

    options = {'template': 'flat_car_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 2110,
                           wagon_generation = 1,
                           replacement_id = '-none',
                           intro_date = 1860,
                           vehicle_life = 40,
                           track_type = 'NG',
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           weight = 9,
                           vehicle_length = 8))

    options = {'template': 'flat_car_ng_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 1930,
                           wagon_generation = 2,
                           replacement_id = '-none',
                           intro_date = 1915,
                           vehicle_life = 40,
                           track_type = 'NG',
                           use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           weight = 14,
                           vehicle_length = 8))

    options = {'template': 'flat_car_ng_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
