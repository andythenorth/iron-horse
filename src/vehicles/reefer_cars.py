import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

options = {'template': 'reefer_car_brit_gen_2_template.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)

options = {'template': 'reefer_car_brit_gen_2_template.png'}
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)


type_config = TypeConfig(base_id = 'reefer_car',
                template = 'train.pynml',
                fixed_run_cost_factor = 3.5,
                class_refit_groups = ['refrigerated_freight'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'FOOD',
                default_capacity_type = 'capacity_freight',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Reefer [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1895,
                    buy_cost = 22,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 25,
                        weight = 14,
                        vehicle_length = 5,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

# no gen 2 reefer - straight to gen 3

consist = WagonConsist(type_config = type_config,
                    title = 'Reefer [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1964,
                    buy_cost = 22,
                    vehicle_life = 40,
                    speedy = True,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 40,
                        weight = 30,
                        vehicle_length = 8,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)
