import global_constants
from train import TypeConfig, WagonConsist, Wagon

#self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]

type_config = TypeConfig(base_id = 'mail_car',
                template = 'train.pynml',
                class_refit_groups = ['mail', 'express_freight'],
                label_refits_allowed = [],
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
                    graphics_status = '')

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_mail = 30,
                        weight = 100,
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
                    graphics_status = '')

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_mail = 45,
                        weight = 100,
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
                    graphics_status = '')

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_mail = 60,
                        weight = 100,
                        vehicle_length = 7,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
