import global_constants
from train import TypeConfig, WagonConsist, CombineCar

type_config = TypeConfig(base_id = 'combine_car',
                template = 'train.pynml',
                class_refit_groups = ['mail', 'express_freight'],
                label_refits_allowed = [],
                label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases'],
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail')

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Combine Car]',
                        roster = 'pony',
                        base_numeric_id = 1000,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(CombineCar(consist = consist,
                            capacity_mail = 20,
                            capacity_freight = 12,
                            capacity_pax = 30,
                            weight = 34,
                            vehicle_length = 9))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    #--------------- llama ----------------------------------------------------------------------
