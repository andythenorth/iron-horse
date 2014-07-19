import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'caboose_car',
                template = 'train.pynml',
                class_refit_groups = ['all_freight'], # refit anything to allow auto-replace
                label_refits_allowed = [],
                label_refits_disallowed = [],
                default_cargo = 'DEFAULT_CARGO_FIRST_REFITTABLE',
                default_capacity_type = 'capacity_freight',
                str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Caboose [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 0,
                        weight = 20,
                        vehicle_length = 5,
                        loading_speed = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
