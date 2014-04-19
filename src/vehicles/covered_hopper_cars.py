import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'covered_hopper_car',
                template = 'train.pynml',
                class_refit_groups = ['covered_hopper_freight'],
                label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ', 'FOOD', 'SUGR', 'FMSP', 'RFPR', 'CLAY'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GRAI',
                default_capacity_type = 'capacity_freight',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Covered Hopper [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1922,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 30,
                        weight = 14,
                        vehicle_length = 5,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

# no gen 2 for covered hopper - straight to gen 3

consist = WagonConsist(type_config = type_config,
                    title = 'Covered Hopper [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1960,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 55,
                        weight = 30,
                        vehicle_length = 8,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
