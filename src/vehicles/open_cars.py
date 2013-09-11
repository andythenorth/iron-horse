import global_constants
from train import Train, OpenCar

vehicle = OpenCar(numeric_id = 10080,
                vehicle_set = 'nagn',
                vehicle_generation = 'gen_1',
                title = 'Open [Car]',
                capacity_freight = 20,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                vehicle_length = 6,
                buy_menu_width = 32,
                loading_speed = 20,
                intro_date = 1900,
                str_type_info = 'COASTER',
                vehicle_life = 40,
                graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

vehicle = OpenCar(numeric_id = 10070,
                vehicle_set = 'univ',
                vehicle_generation = 'gen_2',
                title = 'Open [Car]',
                capacity_freight = 20,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                vehicle_length = 8,
                buy_menu_width = 32,
                loading_speed = 20,
                intro_date = 1900,
                str_type_info = 'COASTER',
                vehicle_life = 40,
                graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

