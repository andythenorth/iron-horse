import global_constants
from train import TypeConfig, WagonConsist, Wagon

type_config = TypeConfig(base_id = 'box_car',
                template = 'train.pynml',
                class_refit_groups = ['packaged_freight'],
                label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_cargo_capacities = 'capacities_freight',
                str_type_info = 'DOGTRACK')

print "BoxCars are pretty unfinished, not sure what needs to be on consist, and what on vehicle class"

consist = WagonConsist(type_config = type_config,
                    title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '')

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 20,
                        weight = 100,
                        vehicle_length = 7,
                        loading_speed = 20))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

"""vehicles=[BoxCar(
                capacity_freight = 20,
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                visible_part_lengths = [5],
                loading_speed = 20,
                vehicle_life = 40,
                graphics_status = '',)]"""
"""
consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)

vehicle = BoxCar(title = 'Box [Car]',
                vehicle_set = 'brit',
                wagon_generation = 2,
                capacity_freight = 40,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                visible_part_lengths = [8],
                loading_speed = 20,
                intro_date = 1930,
                vehicle_life = 40,
                graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
"""
