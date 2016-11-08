import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings = {'STEL': [1, 2, 3], 'WOOD': [4], 'WDPR': [5], 'ENSP': [6], 'FMSP': [6], 'MNSP': [6], 'GOOD': [0, 6]}

type_config_normal = TypeConfig(base_id = 'flat_car',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 7,
                    class_refit_groups = ['flatcar_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = list(cargo_graphics_mappings.keys()),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight'],
                    autorefit = True,
                    default_cargo = 'STEL',
                    default_capacity_type = 'capacity_freight')

type_config_narrow_gauge = TypeConfig(base_id = 'flat_car_ng',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 7,
                    class_refit_groups = ['flatcar_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = list(cargo_graphics_mappings.keys()),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight'],
                    autorefit = True,
                    default_cargo = 'STEL',
                    default_capacity_type = 'capacity_freight')

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Flat Car]',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Flat Car]',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Flat Car]',
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


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Flat Car]',
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
