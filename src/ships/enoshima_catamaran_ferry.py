import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'enoshima_catamaran_ferry',
            numeric_id = 90,
            title = 'Enoshima [Fast Ferry]',
            capacity_pax = 300,
            capacity_cargo_holds = 175,
            capacity_mail = 224,
            replacement_id = '-none',
            buy_cost = 63,
            fixed_run_cost_factor = 16.0,
            fuel_run_cost_factor = 1.0,
            speed = 50.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -54], [-57, -26], [-35, -29], [-19, -32], [-14, -54], [-58, -32], [-42, -29], [-1, -26]],
            buy_menu_width = 67,
            loading_speed = 20,
            intro_date = 1997,
            buy_menu_bb_xy = [624, 28],
            str_type_info = 'CATAMARAN_FAST_FERRY',
            vehicle_life = 25,
            gross_tonnage = 350,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
