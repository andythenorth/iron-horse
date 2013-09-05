import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'sunk_rock_ferry',
            numeric_id = 10,
            title = 'Sunk Rock [Ferry]',
            capacity_pax = 100,
            capacity_cargo_holds = 25,
            capacity_mail = 80,
            replacement_id = '-none',
            buy_cost = 27,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 40,
            loading_speed = 30,
            intro_date = 1870,
            buy_menu_bb_xy = [669, 21],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 40,
            gross_tonnage = 60,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
