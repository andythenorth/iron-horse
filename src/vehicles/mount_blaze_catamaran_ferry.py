import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'mount_blaze_catamaran_ferry',
            numeric_id = 100,
            title = 'Mount Blaze [Fast Ferry]',
            capacity_pax = 1600,
            capacity_cargo_holds = 450,
            capacity_mail = 630,
            replacement_id = '-none',
            buy_cost = 63,
            fixed_run_cost_factor = 16.0,
            fuel_run_cost_factor = 1.0,
            speed = 40.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-67, -25], [-59, -29], [-15, -26], [-14, -45], [-67, -26], [-59, -29], [-15, -25]],
            buy_menu_width = 117,
            loading_speed = 20,
            intro_date = 2002,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'CATAMARAN_FAST_FERRY',
            vehicle_life = 30,
            gross_tonnage = 1800,
            graphics_status = 'Unstarted',)

ship.add_model_variant(intro_date=0, 
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)