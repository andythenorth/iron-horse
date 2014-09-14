import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

cargo_graphics_mappings = {'STEL': [1, 2, 3], 'WOOD': [4], 'WDPR': [5], 'ENSP': [6], 'FMSP': [6], 'MNSP': [6]}

options = {'template': 'flat_car_brit_gen_1_template.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)

type_config = TypeConfig(base_id = 'flat_car',
                template = 'car_with_visible_cargo.pynml',
                num_cargo_rows = 7,
                class_refit_groups = ['flatcar_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys(),
                label_refits_disallowed = ['FOOD'],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight')

consist = WagonConsist(type_config = type_config,
                    title = 'Flat [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 20,
                        weight = 6,
                        vehicle_length = 5,
                        loading_speed = 10))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)


options = {'template': 'flat_car_brit_gen_2_template.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)

consist = WagonConsist(type_config = type_config,
                    title = 'Flat [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1945,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 35,
                        weight = 12,
                        vehicle_length = 8,
                        loading_speed = 10))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)


cargo_graphics_mappings = {}

type_config = TypeConfig(base_id = 'flat_car_ng',
                template = 'car_with_visible_cargo.pynml',
                num_cargo_rows = 1,
                class_refit_groups = ['flatcar_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys(),
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight',
                track_type = 'NG')

consist = WagonConsist(type_config = type_config,
                    title = 'Narrow Gauge Flat [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1870,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 12,
                        weight = 3,
                        vehicle_length = 3,
                        loading_speed = 10))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
