import global_constants
from train import Train, DieselLoco

vehicle = DieselLoco(id = 'growler',
            numeric_id = 190,
            title = 'Growler [Freighter]',
            capacity_cargo_holds = 20,
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1900,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            gross_tonnage = 360,
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
