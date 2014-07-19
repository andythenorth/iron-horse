import global_constants
from train import TypeConfig, WagonConsist, CombineCar

#self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]

type_config = TypeConfig(base_id = 'combine_car',
                template = 'train.pynml',
                class_refit_groups = ['mail', 'express_freight'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail')

consist = WagonConsist(type_config = type_config,
                    title = 'Combine [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    vehicle_life = 40,
                    graphics_status = '')

consist.add_unit(CombineCar(type_config = type_config,
                        consist = consist,
                        capacity_mail = 20,
                        capacity_freight = 12,
                        capacity_pax = 30,
                        weight = 34,
                        vehicle_length = 9,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
