import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config_normal = TypeConfig(base_id = 'livestock_car',
                            template = 'train.pynml',
                            class_refit_groups = [],
                            label_refits_allowed = ['LVST'],
                            label_refits_disallowed = [],
                            autorefit = True,
                            default_cargo = 'LVST',
                            default_capacity_type = 'capacity_freight',
                            cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD)

type_config_narrow_gauge = TypeConfig(base_id = 'livestock_car_ng',
                            template = 'train.pynml',
                            class_refit_groups = [],
                            label_refits_allowed = ['LVST'],
                            label_refits_disallowed = [],
                            autorefit = True,
                            default_cargo = 'LVST',
                            default_capacity_type = 'capacity_freight',
                            track_type = 'NG')

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Livestock Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Livestock Car]',
                        roster = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1950,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 25,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Livestock Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 5,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    #--------------- soam ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Livestock Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Livestock Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 5,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)
