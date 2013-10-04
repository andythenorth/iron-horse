import global_constants
from train import Train, MailCar

vehicle = MailCar(title = 'Mail [Car]',
                vehicle_set = 'brit',
                wagon_generation = 1,
                capacity_mail = 30,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                vehicle_length = 7,
                loading_speed = 20,
                intro_date = 1860,
                str_type_info = 'COASTER',
                vehicle_life = 40,
                graphics_status = '')

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

vehicle = MailCar(title = 'Mail [Car]',
                vehicle_set = 'brit',
                wagon_generation = 2,
                capacity_mail = 45,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                vehicle_length = 7,
                loading_speed = 20,
                intro_date = 1925,
                str_type_info = 'COASTER',
                vehicle_life = 40,
                graphics_status = '')

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

vehicle = MailCar(title = 'Mail [Car]',
                vehicle_set = 'brit',
                wagon_generation = 3,
                capacity_mail = 60,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 100,
                vehicle_length = 7,
                loading_speed = 20,
                intro_date = 1985,
                str_type_info = 'COASTER',
                vehicle_life = 40,
                graphics_status = '')

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
