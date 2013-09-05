import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'patos_island_vehicle_ferry',
            numeric_id = 50,
            title = 'Patos Island [Ferry]',
            capacity_pax = 450,
            capacity_cargo_holds = 280,
            capacity_mail = 360,
            replacement_id = '-none',
            buy_cost = 27,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 22.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -54], [-61, -28], [-36, -29], [-10, -28], [-14, -54], [-55, -26], [-36, -29], [0, -24]],
            buy_menu_width = 89,
            loading_speed = 35,
            intro_date = 1953,
            buy_menu_bb_xy = [622, 28],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 60,
            gross_tonnage = 500,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
