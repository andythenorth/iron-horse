import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'livestock_car',
                    template = 'train.pynml',
                    class_refit_groups = [],
                    label_refits_allowed = ['LVST'],
                    label_refits_disallowed = [],
                    autorefit = True,
                    default_cargo = 'LVST',
                    default_capacity_type = 'capacity_freight',
                    cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD)

consist = WagonConsist(type_config = type_config,
                    title = '[Livestock Car]',
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
                        loading_speed = 5))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = '[Livestock Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1950,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 35,
                        weight = 25,
                        vehicle_length = 8,
                        loading_speed = 5))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


type_config = TypeConfig(base_id = 'livestock_car_ng',
                template = 'train.pynml',
                class_refit_groups = [],
                label_refits_allowed = ['LVST'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'LVST',
                default_capacity_type = 'capacity_freight',
                track_type = 'NG')

consist = WagonConsist(type_config = type_config,
                    title = '[Livestock Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 12,
                        weight = 5,
                        vehicle_length = 4,
                        loading_speed = 5))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
