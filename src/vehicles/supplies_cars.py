import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings = {'ENSP': [0, 1, 2, 3, 4], 'FMSP': [0, 1, 2, 3, 4], 'BDMT': [0, 1]}

# Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
# not strictly right, but eh, means it got done :)
options = {'template': 'supplies_car_brit_gen_1_template_0.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
options = {'template': 'supplies_car_brit_gen_1_template_1.png'}
graphics_processor_3 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_4 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)

type_config = TypeConfig(base_id = 'supplies_car',
                template = 'car_with_visible_cargo.pynml',
                num_cargo_rows = 5,
                class_refit_groups = [],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys(),
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'ENSP',
                default_capacity_type = 'capacity_freight')

consist = WagonConsist(type_config = type_config,
                    title = '[Supplies Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    vehicle_life = 40,
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 30,
                        weight = 6,
                        vehicle_length = 7,
                        loading_speed = 10))

consist.add_model_variant(intro_date=0,
                       end_date=1910,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=1910,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)

consist.add_model_variant(intro_date=1910,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=2,
                       graphics_processor=graphics_processor_3)

consist.add_model_variant(intro_date=1910,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=3,
                       graphics_processor=graphics_processor_4)

options = {'template': 'supplies_car_brit_gen_2_template_0.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
options = {'template': 'supplies_car_brit_gen_2_template_1.png'}
graphics_processor_3 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_4 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)

consist = WagonConsist(type_config = type_config,
                    title = '[Supplies Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1960,
                    vehicle_life = 40,)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 45,
                        weight = 12,
                        vehicle_length = 10,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=2010,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=2010,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)

consist.add_model_variant(intro_date=2010,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=2,
                       graphics_processor=graphics_processor_3)

consist.add_model_variant(intro_date=2010,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=3,
                       graphics_processor=graphics_processor_4)
