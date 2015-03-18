import global_constants
from train import TypeConfig, WagonConsist, Wagon

cargo_graphics_mappings = {}

type_config = TypeConfig(base_id = 'metal_car',
                template = 'car_with_visible_cargo.pynml',
                num_cargo_rows = 1,
                generic_cargo_rows = [0],
                cargo_graphics_mappings = cargo_graphics_mappings,
                class_refit_groups = [],
                label_refits_allowed = ['STEL', 'COPR'],
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
                        intro_date = 1860,
                        vehicle_life = 50,
                        speed = 35)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 30,
                            vehicle_length = 5,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config,
                        title = '[Metal Car]',
                        roster = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1910,
                        vehicle_life = 50,
                        speed = 45)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            weight = 60,
                            vehicle_length = 9,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config,
                        title = '[Metal Car]',
                        roster = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1960,
                        vehicle_life = 50,
                        speed = 65)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 90,
                            weight = 90,
                            vehicle_length = 10,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)
