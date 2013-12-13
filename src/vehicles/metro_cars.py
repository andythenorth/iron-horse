import global_constants
from train import TypeConfig, WagonConsist, Wagon

#self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]

type_config = TypeConfig(base_id = 'metro_car',
                template = 'train.pynml',
                class_refit_groups = ['pax', 'express_freight'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                track_type = 'METRO',
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Metro [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1900,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_mail = 40,
                        capacity_freight = 15,
                        weight = 20,
                        vehicle_length = 8,
                        loading_speed = 10))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
