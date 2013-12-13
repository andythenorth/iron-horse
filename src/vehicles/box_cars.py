import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'box_car',
                template = 'train.pynml',
                class_refit_groups = ['packaged_freight'],
                label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 20,
                        weight = 12,
                        vehicle_length = 5,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1930,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 40,
                        weight = 24,
                        vehicle_length = 8,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


type_config = TypeConfig(base_id = 'box_car_ng',
                template = 'train.pynml',
                class_refit_groups = ['packaged_freight'],
                label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight',
                track_type = 'NG',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Narrow Gauge Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1870,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 12,
                        weight = 6,
                        vehicle_length = 5,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
