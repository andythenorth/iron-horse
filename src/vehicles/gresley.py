import global_constants
from train import Train, SteamTenderLoco

vehicle = SteamTenderLoco(id = 'gresley',
            numeric_id = 1260,
            title = 'Gresley [Steam]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 110,
            power = 1750,
            weight = 151,
            tractive_effort_coefficient = 0.18,
            vehicle_length = 8,
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1860,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            trailing_part_lengths = [5],
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
