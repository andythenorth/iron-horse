import global_constants
from train import BoxCarConsist, Wagon

consist = BoxCarConsist(title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    buy_cost = 22,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    vehicle_life = 40,
                    graphics_status = '')

consist.add_unit(Wagon(consist = consist,
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
