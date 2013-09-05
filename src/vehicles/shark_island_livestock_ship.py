import global_constants
from ship import Ship, LivestockCarrier

ship = LivestockCarrier(id = 'shark_island_livestock_ship',
            numeric_id = 290,
            title = 'Shark Island [Livestock Ship]',
            capacities_refittable = [200, 400, 600],
            replacement_id = '-none',
            buy_cost = 58,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -42], [-82, -19], [-66, -29], [-28, -19], [-14, -42], [-80, -20], [-66, -29], [-26, -18]],
            buy_menu_width = 96,
            loading_speed = 20,
            intro_date = 1960,
            buy_menu_bb_xy = [640, 28],
            str_type_info = 'LIVESTOCK_SHIP',
            vehicle_life = 35,
            gross_tonnage = 650,
            graphics_status = 'Work in Progress - DanMacK',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
