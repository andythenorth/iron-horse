import global_constants
from train import Train, SteamTankLoco

vehicle = SteamTankLoco(id = 'suburban',
            numeric_id = 1280,
            title = 'Suburban [Steam]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 70,
            power = 650,
            weight = 57,
            tractive_effort_coefficient = 0.2,
            vehicle_length = 7,
            loading_speed = 20,
            intro_date = 1930,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
