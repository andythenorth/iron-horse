import global_constants
from ship import Ship, LogTug

ship = LogTug(id = 'pine_island_log_tug',
            numeric_id = 250,
            title = 'Pine Island [Log Tug]',
            capacities_refittable = [80, 240, 400],
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 12.0,
            speed_factor_unladen = 1.7,
            inland_capable = True,
            sea_capable = True,
            offsets = [[0, 0]],
            buy_menu_width = 24,
            loading_speed = 20,
            intro_date = 1900,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LOG_TUG',
            vehicle_life = 25,
            gross_tonnage = 26,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
