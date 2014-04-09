import global_constants
from train import TypeConfig, WagonConsist, Wagon

cargo_graphics_mappings = {'FMSP': [1], 'MILK': [2], 'RFPR': [1]}

# tank cars are unrealistically autorefittable, and at no cost
# Pikka: if people complain that it's unrealistic, tell them "don't do it then"

type_config = TypeConfig(base_id = 'tank_car',
                template = 'tank_car.pynml',
                fixed_run_cost_factor = 3.5,
                num_cargo_rows = 3,
                class_refit_groups = ['liquids'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys() ,
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'OIL_',
                default_capacity_type = 'capacity_freight',
                str_type_info = 'DOGTRACK')

        # mappings are to rows in the spritesheet, 0-based (0 is also default)
        # also get the allowed label refits from the graphics mapping - use row 0 if there's no specific graphics for the label

consist = WagonConsist(type_config = type_config,
                    title = 'Tank [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
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
                    title = 'Tank [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1925,
                          vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 35,
                        weight = 24,
                        vehicle_length = 5,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Tank [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1964,
                          vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 55,
                        weight = 40,
                        vehicle_length = 8,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

type_config = TypeConfig(base_id = 'tank_car_ng',
                template = 'tank_car.pynml',
                fixed_run_cost_factor = 3.5,
                num_cargo_rows = 3,
                class_refit_groups = ['liquids'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys() ,
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'OIL_',
                default_capacity_type = 'capacity_freight',
                track_type = 'NG',
                str_type_info = 'DOGTRACK')


consist = WagonConsist(type_config = type_config,
                    title = 'Narrow Gauge Tank [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1870,
                          vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 12,
                        weight = 5,
                        vehicle_length = 4,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
