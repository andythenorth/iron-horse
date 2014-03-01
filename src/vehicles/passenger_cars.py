import global_constants
from train import TypeConfig, WagonConsist, Wagon

#self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]

type_config = TypeConfig(base_id = 'passenger_car',
                template = 'train.pynml',
                fixed_run_cost_factor = 3.5,
                class_refit_groups = ['pax'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'PASS',
                default_capacity_type = 'capacity_pax',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Passenger [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    buy_cost = 22,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_pax = 40,
                        weight = 30,
                        vehicle_length = 9,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Passenger [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1925,
                    buy_cost = 22,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_pax = 55,
                        weight = 33,
                        vehicle_length = 9,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Passenger [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1985,
                    buy_cost = 22,
                    vehicle_life = 40,
                    graphics_status = '')

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_pax = 75,
                        weight = 36,
                        vehicle_length = 10,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


type_config = TypeConfig(base_id = 'passenger_car_ng',
                template = 'train.pynml',
                fixed_run_cost_factor = 3.5,
                class_refit_groups = ['pax'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'PASS',
                default_capacity_type = 'capacity_pax',
                track_type = 'NG',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Narrow Gauge Passenger [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1870,
                    buy_cost = 22,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_pax = 25,
                        weight = 12,
                        vehicle_length = 6,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
