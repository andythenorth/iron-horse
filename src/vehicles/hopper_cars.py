import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'hopper_car',
                template = 'train.pynml',
                class_refit_groups = ['hopper_freight'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'COAL',
                default_capacity_type = 'capacity_freight',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Hopper [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1910,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 30,
                        weight = 100,
                        vehicle_length = 5,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Hopper [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1950,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 55,
                        weight = 100,
                        vehicle_length = 8,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
