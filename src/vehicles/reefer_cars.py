import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

cargo_graphics_mappings = {} # template needs this, but reefer car has zero cargo-specific graphics, all generic

type_config_normal = TypeConfig(base_id = 'reefer_car',
                        template = 'car_with_open_doors_during_loading.pynml',
                        num_cargo_rows = 1, # template needs this, but box car has zero cargo-specific graphics, all generic
                        cargo_graphics_mappings = cargo_graphics_mappings,
                        class_refit_groups = ['refrigerated_freight'],
                        label_refits_allowed = [],
                        label_refits_disallowed = [],
                        autorefit = True,
                        default_cargo = 'FOOD',
                        default_capacity_type = 'capacity_freight',
                        cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD)

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'pony',
                        base_numeric_id = 730,
                        wagon_generation = 1,
                        replacement_id = '-none',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'pony',
                        base_numeric_id = 720,
                        wagon_generation = 3,
                        replacement_id = '-none',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'llama',
                        base_numeric_id = 1390,
                        wagon_generation = 1,
                        replacement_id = '-none',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'llama',
                        base_numeric_id = 1400,
                        wagon_generation = 3,
                        replacement_id = '-none',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'llama',
                        base_numeric_id = 1410,
                        wagon_generation = 1,
                        replacement_id = '-none',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'llama',
                        base_numeric_id = 1420,
                        wagon_generation = 3,
                        replacement_id = '-none',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'antelope',
                        base_numeric_id = 1570,
                        wagon_generation = 1,
                        replacement_id = '-none',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Reefer Car]',
                        roster = 'antelope',
                        base_numeric_id = 1900,
                        wagon_generation = 1,
                        replacement_id = '-none',
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
