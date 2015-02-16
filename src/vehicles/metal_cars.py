import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'metal_car',
                template = 'train.pynml',
                class_refit_groups = [],
                label_refits_allowed = ['STEL'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'STEL',
                default_capacity_type = 'capacity_freight',
                loading_speed_multiplier = 2)

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Metal Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1910,
                        vehicle_life = 40,
                        speed = 45,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 10,
                            vehicle_length = 3,
                            spriterow_num = 0))

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            weight = 30,
                            vehicle_length = 5,
                            spriterow_num = 1))

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 10,
                            vehicle_length = 3,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)
