import global_constants
from train import Train, MailCar

vehicle = MailCar(id = 'mail_car',
            numeric_id = 10020,
            title = 'Mail [Car]',
            capacity_mail = 20,
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            weight = 100,
            offsets = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            vehicle_length = 7,
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1900,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            vehicle_generation = 'gen_1',
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
