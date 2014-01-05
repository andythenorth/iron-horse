import global_constants
from train import TypeConfig, WagonConsist, MailCar

#self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]

cargo_graphics_mappings = {} # template needs this, but mail car has zero cargo-specific graphics, all generic

type_config = TypeConfig(base_id = 'mail_car',
                template = 'car_with_visible_cargo.pynml',
                num_cargo_rows = 1, # template needs this, but mail car has zero cargo-specific graphics, all generic
                class_refit_groups = ['mail', 'express_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys() ,
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Mail [Car]',
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

consist.add_unit(MailCar(type_config = type_config,
                        consist = consist,
                        capacity_mail = 30,
                        weight = 29,
                        vehicle_length = 7,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Mail [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1925,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(MailCar(type_config = type_config,
                        consist = consist,
                        capacity_mail = 45,
                        weight = 30,
                        vehicle_length = 7,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Mail [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1985,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(MailCar(type_config = type_config,
                        consist = consist,
                        capacity_mail = 60,
                        weight = 31,
                        vehicle_length = 8,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
