import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'metro_car',
                template = 'train.pynml',
                class_refit_groups = ['mail', 'express_freight'],
                label_refits_allowed = [],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail',
                track_type = 'METRO')

def main():
    consist = WagonConsist(type_config = type_config,
                        title = 'Mail [Metro Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1900,
                        vehicle_life = 40,
                              use_legacy_spritesheet = True)

    consist.add_unit(Wagon(type_config = type_config,
                            consist = consist,
                            capacity_mail = 40,
                            capacity_freight = 15,
                            weight = 20,
                            vehicle_length = 8,
                            loading_speed = 40))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)
