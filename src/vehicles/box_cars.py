import global_constants
from train import TypeConfig, WagonConsist, BoxCar, GraphicsProcessorFactory

box_car_label_refits_allowed = ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR']
cargo_graphics_mappings = {} # template needs this, but box car has zero cargo-specific graphics, all generic

type_config_normal = TypeConfig(base_id = 'box_car',
                    template = 'car_with_open_doors_during_loading.pynml',
                    num_cargo_rows = 1, # template needs this, but box car has zero cargo-specific graphics, all generic
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    class_refit_groups = ['packaged_freight'],
                    label_refits_allowed = box_car_label_refits_allowed,
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases'],
                    autorefit = True,
                    default_cargo = 'GOOD',
                    default_capacity_type = 'capacity_freight')

type_config_narrow_gauge = TypeConfig(base_id = 'box_car_ng',
                    template = 'car_with_open_doors_during_loading.pynml',
                    num_cargo_rows = 1, # template needs this, but box car has zero cargo-specific graphics, all generic
                    class_refit_groups = ['packaged_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = box_car_label_refits_allowed,
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases'],
                    autorefit = True,
                    default_cargo = 'GOOD',
                    default_capacity_type = 'capacity_freight',
                    track_type = 'NG')

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Box Car]',
                        roster = 'pony',
                        base_numeric_id = 550,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 30,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'box_car_pony_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Box Car]',
                        roster = 'pony',
                        base_numeric_id = 560,
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1950,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            capacity_mail = 45,
                            weight = 18,
                            vehicle_length = 6))

    options = {'template': 'box_car_pony_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Box Car]',
                        roster = 'pony',
                        base_numeric_id = 570,
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1995,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            capacity_mail = 65,
                            weight = 25,
                            vehicle_length = 10))

    options = {'template': 'box_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Box Car]',
                        roster = 'pony',
                        base_numeric_id = 580,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 12,
                            capacity_mail = 20,
                            weight = 5,
                            vehicle_length = 4))

    options = {'template': 'box_car_ng_pony_gen_1_template.png'}

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
                        title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 590,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 25,
                            capacity_mail = 35,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'box_car_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 600,
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1920,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 45,
                            capacity_mail = 55,
                            weight = 20,
                            vehicle_length = 6))

    options = {'template': 'box_car_llama_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 610,
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1980,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 65,
                            capacity_mail = 75,
                            weight = 30,
                            vehicle_length = 7))

    options = {'template': 'box_car_llama_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 620,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 20,
                            weight = 10,
                            vehicle_length = 6))

    options = {'template': 'box_car_ng_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 1310,
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1920,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            capacity_mail = 35,
                            weight = 15,
                            vehicle_length = 6))

    options = {'template': 'box_car_ng_llama_gen_2_template.png'}

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
                        title = '[Box Car]',
                        roster = 'antelope',
                        base_numeric_id = 1740,
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1981,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 70,
                            capacity_mail = 100,
                            weight = 32,
                            vehicle_length = 8))

    options = {'template': 'box_car_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


